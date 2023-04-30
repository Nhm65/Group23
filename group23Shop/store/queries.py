from datetime import datetime, timedelta, timezone

from django.db.models import Avg, Count, DurationField

from store.models import Order,Order_Details

def view_users_shopping_cart(request,id):
    customer_id=request.POST['customer_id']
    cart_details=Order_Details.filter(order_id=id).values()
def add_item_to_cart(request):
    order_id = request.POST['order_id']
    product_id = request.POST['product_id']
    quantity = request.POST['quantity']
    price = request.POST['price']
    orderdetails = Order_Details(order_id=order_id, product_id=product_id, quantity=quantity, price=price)
    orderdetails.save()
def remove_cart_item(request, id):
    orderdetails = Order_Details.objects.get(id=id)
    orderdetails.delete()
def get_customer_orders(request, customer_id):
    checkedout = request.POST['checkedout']
    order = Order.objects.get(customer_id=customer_id)
    order.objects.get
def checkout(request, id):
  checkedout = request.POST['checkedout']
  order = Order.objects.get(id=id)
  order.checkedout = 'Completed'
  order.save()
