from django.shortcuts import render,redirect
from order.models import Order
from order.forms import OrderForm
from authenticate import Authentication
# Create your views here.
#@Authentication.valid_user
def index(request):
    print(request.method)
    if(request.method=="POST"):
        page=int(request.POST['page'])

        if('prev' in request.POST):
            page=page-1

        if('next' in request.POST):
            page=page+1

        tempOffSet=page-1
        offset=tempOffSet*4
        print(offset)

    else:
        offset=0
        page=1

    order=Order.objects.raw("select * from order limit 4 offset %s",[offset])
    pageItem=len(order)
    return render(request,"order/index.html",{'order':order,'page':page,'pageItem':pageItem})

#Authentication.valid_user
def search(request):
    print(request.POST['search'])
    order=Order.objects.get(email=request.POST['search'])
    return render(request,"order/search.html",{'order':order})

#@Authentication.valid_user
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=OrderForm(request.POST)
        form.save()
        return redirect("/order")
    else:
        form=OrderForm()
    return render(request,"order/create.html",{'form':form})

#@Authentication.valid_user_where_id
def update(request,id):
    order=Order.objects.get(order_id=id)
    if request.method=="POST":
        form=OrderForm(request.POST,instance=order)
        form.save()
        return redirect("/order")
    else:
        form=OrderForm(instance=order)
    return render(request,"order/edit.html",{'form':form})

#@Authentication.valid_user_where_id
def delete(request,id):
    order=Order.objects.get(order_id=id)
    order.delete()
    return redirect("/order")
