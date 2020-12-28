from django.shortcuts import render,redirect
from shoe.models import Shoe
from customer.forms import CustomerForm
# Create your views here.
def index(request):
    shoe=Shoe.objects.all()
    return render(request,'home/index.html' ,{'shoe':shoe})

def register(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        result=form.save()
        request.session['customer_id']=result.customer_id
        return redirect("/")
    else:
        form=CustomerForm()
    return render(request,"home/register.html",{'form':form})

def login(request):

    if(request.method=='POST'):
       request.session['email']=request.POST['email']
       request.session['password']=request.POST['password']

       return redirect("/user")
    return render(request,"home/login.html")


def logout(request):
    request.session.clear()
    return redirect("/login")

def blog(request):
    shoe=Shoe.objects.all()
    return render(request,'home/blog.html' ,{'shoe':shoe})

def blog_details(request):
    shoe=Shoe.objects.all()
    return render(request,'home/blog-details.html' ,{'shoe':shoe})

def contact(request):
    shoe=Shoe.objects.all()
    return render(request,'home/contact.html' ,{'shoe':shoe})

def main(request):
    shoe=Shoe.objects.all()
    return render(request,'home/main.html' ,{'shoe':shoe})

def product(request):
    shoe=Shoe.objects.all()
    return render(request,'home/product.html' ,{'shoe':shoe})

def shop(request):
    shoe=Shoe.objects.all()
    return render(request,'home/shop.html' ,{'shoe':shoe})

