from .models import *
import json
def cookieCart(request):
    try:
        cart=json.loads(request.COOKIES['cart']) 
    except:
        cart={}
    print('cart:', cart)
    items = []
    order = {'get_cart_items':0, 'get_cart_total':0}
    cartItems=order['get_cart_items']
    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            item = s_and_t.objects.get(id=i)
            total= (item.price*cart[i]['quantity'])
            order['get_cart_total'] += total
            order['get_cart_items']+=cart[i]['quantity']
            itemz= {
                'product':{
                    'id':item.id,
                    'name': item.title,
                    'price':item.price,
                    'imageUrl': item.thumbnail,
                },
                'quantity':cart[i]['quantity'],
                'get_total':total
            }
            items.append(itemz)
        except:
            pass
    return{'cartItems':cartItems, 'order':order, 'items':items}