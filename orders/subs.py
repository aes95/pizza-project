subs = ['Cheese','Italian','Ham + Cheese','Meatball','Tuna','Turkey','Chicken Parmigiana','Eggplant Parmigiana','Steak','Sausage, Peppers & Onions','Hamburger','Cheeseburger','Fried Chicken','Veggie']
price_s = [6.5,6.5,6.5,6.5,6.5,7.5,7.5,6.5,6.5,0,4.6,5.1,6.95,6.95]
price_l = [7.95,7.95,7.95,7.95,7.95,8.5,8.5,7.95,7.95,8.5,6.95,7.45,8.5,8.5]


for i in range(len(subs)):
    s1 = Sub(name=subs[i], price=price_s[i])
    s1.save()
    s2 = Sub(name=subs[i], large=True, price=price_l[i])
    s2.save()
    s3 = Sub(name=subs[i], large=True, extra_cheese=True, price=(price_l[i]+0.50))
    s3.save()
    s4 = Sub(name=subs[i], large=False, extra_cheese=True, price=(price_s[i]+0.50))
    s4.save()
