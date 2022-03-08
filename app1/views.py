
import os
from django.shortcuts import redirect, render
from .models import userlogin

# Create your views here.


#load edit page
def edit(request,pk):
    products=userlogin.objects.get(id=pk)
    return render(request,'edit.html', {'products':products})


#index for form
def form(request):
    return render(request,'form.html')
    

def signup_details(request):
    if request.method == "POST":
        nm=request.POST['name']
        uname=request.POST['username']
        upass=request.POST['password']
        repas=request.POST['repassword']
        if request.FILES.get('file') is not None:
            image=request.FILES['file']
        else:
            image = "static/image/icon.png"
        eum=request.POST['email']

        result=userlogin(
            name=nm,
            username=uname,
            password=upass,
            repassword=repas,
            image=image,
            email=eum,
                            
            )
        result.save()
        return redirect('view')

        #show products
def view(request):
    products=userlogin.objects.all()
    return render(request,'view.html', {'products':products})


#editing page
def edit_details(request,pk):
    if request.method=='POST':
        products = userlogin.objects.get(id=pk)
        products.name=request.POST.get('name')
        products.username=request.POST.get('username')
        products.password=request.POST.get('password')
        products.repassword=request.POST.get('repassword')
        products.email=request.POST.get('email')
        # if len(products.image)>0:
        #     os.remove(products.image.path)
        if request.FILES.get('file') is not None:
            print('hai')
            if not products.image =="static/image/icon.png":
                os.remove(products.image.path)
                products.image = request.FILES['file']
            else:
                products.image = request.FILES['file']
        else:
            os.remove(products.image.path)
            products.image ="static/image/icon.png"
        
        products.save()
        return redirect('view')
    return render(request, 'edit.html')


#deleting products

def delete_product(request,pk):
    products=userlogin.objects.get(id=pk)
    if not products.image =="static/image/icon.png":
                os.remove(products.image.path)
    else:
        pass
    products.delete()
    return redirect('view')