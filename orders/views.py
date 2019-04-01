from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from orders.forms import *
from orders.models import *
import json, decimal, requests

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
          return render(request, "orders/login.html", {"message": None})
    toppings = Topping.objects.all()
    pizza_prices = (PizzaPrice.objects.get(large=False, sicilian=False, toppings_count=0).price, PizzaPrice.objects.get(large=False, sicilian=True, toppings_count=0).price)
    dinner = Food.objects.filter(type='Dinner').order_by('name')
    dinner_options = [i for i in dinner.values_list('name',flat=True).distinct()]
    dinner_mapping = {option:(dinner.filter(name=option, size='S').first(),dinner.filter(name=option, size='L').first()) for option in dinner_options}
    sub = Food.objects.filter(type='Sub')
    sub_options = [i for i in sub.values_list('name',flat=True).distinct()]
    sub_mapping = {option:(sub.filter(name=option, size='S').first(),sub.filter(name=option, size='L').first()) for option in sub_options}
    pasta = Food.objects.filter(type='Pasta')
    salad = Food.objects.filter(type='Salad')
    food_type_data = {'dinner':dinner_mapping, 'sub': sub_mapping, 'pasta': pasta, 'salad': salad}
    context = {"user": request.user, "toppings":toppings, "pizza_prices":pizza_prices, "data":food_type_data}
    return render(request, "orders/menu.html", context)

def login_view(request):
    if request.method == 'GET':
        return render(request, "orders/login.html")
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        context = {"user": user}
        return redirect('index')
    else:
        # Return an 'invalid login' error message.
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def cart(request):
    cart = request.session.get('cart', {'items':[]})
    if request.method == 'POST':
        item = request.POST
        type = item.get('type')
        sub_type = item.get('sub_type')
        size = item.get('size')
        name = item.get('name')
        price = item.get('price')
        if type == 'pizza':
            toppings = item.getlist('toppings')
            sicilian = item.get('sicilian')
            price = PizzaPrice.objects.get(large=(size=='large'),sicilian=(sicilian=='sicilian'), toppings_count=len(toppings)).price
        addition = {'type':type, 'sub_type':sub_type, 'size':size, 'toppings':toppings, 'price': str(price), 'name': name}
        addition['id']= get_food_id(addition)
        cart['items'].append(addition)
        cart['subtotal'] = get_cart_total(cart)
        request.session['cart'] = cart
    return JsonResponse(cart, safe="False")

def add_to_cart(request):
    cart = request.session.get('cart', {'items':[]})
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        item = json.loads(body_unicode)
        cart['items'].append(item)
        cart['subtotal'] = get_cart_total(cart)
        request.session['cart'] = cart
        return JsonResponse({'success':True}, safe="False")

def checkout_view(request):
    cart = request.session.get('cart', {'items':[]})
    if cart['items'] == []:
        return redirect('/')
    checkout_items = [Food.objects.get(id=item.get('id')) for item in cart.get('items')]
    if request.method == 'GET':
        return render(request, 'orders/checkout.html', {'cart':checkout_items, 'subtotal':cart['subtotal']})
    else:
        order = Order(user=request.user, total= cart.get('subtotal'))
        order.save()
        for item in checkout_items:
            line = OrderLine(order_id=order, food=item)
            line.save()
        msg = {'status': 'success', 'total':cart['subtotal'], 'id':order.id }
        return JsonResponse(msg)

def get_cart_total(cart):
    total = 0
    for item in cart['items']:
        total += decimal.Decimal(item['price'])
    return str(total)

def get_food_id(item):
    if item['type'] == 'pizza':
        size = 'L' if item.get('size') == 'large' else 'S'
        sub_type = item.get('sub_type').capitalize()
        toppings = item.get('toppings')
        try:
            return Food.objects.get(type='Pizza', sub_type=sub_type, size=size,toppings__name__in= toppings).id
        except Food.MultipleObjectsReturned:
            return Food.objects.filter(type='Pizza', sub_type=sub_type, size=size,toppings__name__in= toppings).first().id
        except:
            obj = Food(type='Pizza', sub_type=sub_type, size=size)
            obj.save()
            for topping in toppings:
                top = Topping.objects.get(name=topping)
                obj.toppings.add(top)
                obj.save()
            return obj.id

def register_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, "orders/register.html", {'form':form})
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('index')
    else:
        form = UserCreationForm()
        return render(request, "orders/register.html", {'form': form, 'message': 'Invalid Form'})

def logout_view(request):
    logout(request)
    return redirect('index')

def get_pizza_price(request):
    item = request.POST
    size = item.get('size') == 'large'
    sicilian = item.get('sub_type') == 'sicilian'
    toppings = item.getlist('toppings')
    price = PizzaPrice.objects.get(large=size, sicilian=sicilian, toppings_count=len(toppings)).price
    return JsonResponse({'price':price}, safe=False)

def get_toppings(request):
    return Topping.objects.all()

def clear_cart(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        num = int(body.get('num'))
        cart = request.session.get('cart', {'items':[]})
        if num == -1:
            cart['items'] = []
        else:
            cart['items'].pop(num)
        cart['subtotal'] = get_cart_total(cart)
        request.session['cart'] = cart
        return JsonResponse({'status':'success', 'num': num}, safe=False)
    if request.method == 'GET':
            return JsonResponse({'status':'fail'}, safe=False)

def get_item_details(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id = int(body.get('id'))
        food = Food.objects.get(id=id)
        size = food.get_size_display()
        item = {'name':food.name, 'type':food.type,'sub_type':food.sub_type,
         'size':size, 'price': str(food.price), 'id':id}
        return JsonResponse(item, safe=False)
    if request.method == 'GET':
            return JsonResponse({'status':'fail'}, safe=False)
