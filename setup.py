from orders.models import *

tops = ['Pepperoni', 'Sausage','Mushrooms','Onions','Ham','Canadian Bacon','Pineapple','Eggplant','Tomato & Basil','Green Peppers','Hamburger','Spinach','Artichoke','Buffalo Chicken','Barbecue Chicken','Anchovies','Black Olives','Fresh Garlic','Zucchini']

for top in tops:
    new = Topping(name = top)
    new.save()


subs = ['Cheese','Italian','Ham + Cheese','Meatball','Tuna','Turkey','Chicken Parmigiana','Eggplant Parmigiana','Steak','Steak + Cheese','Sausage, Peppers & Onions','Hamburger','Cheeseburger','Fried Chicken','Veggie']
small = [6.5,6.5,6.5,6.5,6.5,7.5,7.5,6.5,6.5,6.95,0,4.6,5.1,6.95,6.95]
large = [7.95,7.95,7.95,7.95,7.95,8.5,8.5,7.95,7.95,8.5,8.5,6.95,7.45,8.5,8.5]

for i in range(len(subs)):
    new_s = Food(name = subs[i], type= 'Sub',size='S', price=small[i])
    new_s.save()
    new_l = Food(name = subs[i], type= 'Sub',size='L', price=large[i])
    new_l.save()

dinner = ['Garden Salad','Greek Salad','Antipasto','Baked Ziti','Meatball Parm','Chicken Parm']
small = [35,45,45,35,45,45]
large = [60,70,70,60,70,80]

for i in range(len(dinner)):
    new_s = Food(name = dinner[i], type= 'Dinner',size='S', price=small[i])
    new_s.save()
    new_l = Food(name = dinner[i], type= 'Dinner',size='L', price=large[i])
    new_l.save()
