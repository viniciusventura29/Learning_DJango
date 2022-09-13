from home.models import Prod
from django.shortcuts import render, redirect


def home_index(request):
    infoData_sql =Prod.objects.all
    context ={
        'Produtos':infoData_sql
    }

    return render(request,'home/index.html',context)

def cadastrar_prod(request):
    if str(request.method) != 'POST':
        return render(request, 'home/cadastrar.html')
    else:
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        product = request.POST.get('product')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        photo = request.FILES.get('photo')

    data_to_save = Prod.objects.create(
        name=name,
        brand=brand,
        product=product,
        price=price,
        quantity=quantity,
        photo=photo,
    )

    data_to_save.save()

    return redirect('homeindex')

def details(request,name):
    name = Prod.objects.get(name=name)
    return render(request,'home/details.html',{'name': name})