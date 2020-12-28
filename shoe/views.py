from django.shortcuts import render,redirect
from shoe.models import Shoe
from shoe.forms import ShoeForm
from authenticate import Authentication
# Create your views here.
@Authentication.valid_user
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

    shoe=Shoe.objects.raw("select * from shoe limit 4 offset %s",[offset])
    pageItem=len(shoe)
    return render(request,"shoe/index.html",{'shoe':shoe,'page':page,'pageItem':pageItem})

@Authentication.valid_user
def create(request):
    print(request.POST)
    if request.method=="POST":
        form=ShoeForm(request.POST,request.FILES)
        form.save()
        return redirect("/shoe")
    else:
        form=ShoeForm()
    return render(request,"shoe/create.html",{'form':form})

@Authentication.valid_user_where_id
def update(request,id):
    cshoe=Shoe.objects.get(shoe_id=id)
    if request.method=="POST":
        form=ShoeForm(request.POST,request.FILES,instance=shoe)
        form.save()
        return redirect("/shoe")
    else:
        form=ShoeForm(instance=shoe)
    return render(request,"shoe/edit.html",{'form':form})

@Authentication.valid_user_where_id
def delete(request,id):
    shoe=Shoe.objects.get(shoe_id=id)
    shoe.delete()
    return redirect("/shoe")