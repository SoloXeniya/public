from django.shortcuts import render, redirect
from .models import Product
# Create your views here.

def index(request):

    products = Product.objects.all()  


    return render(request, "index.html", {"context_products": products})


def add_product(request):
    if request.method=="POST":
        html_image = request.FILES.get("image_product")
        html_title = request.POST.get("title_product")

        new_product = Product(image=html_image, title = html_title)
        new_product.save()

        return redirect("/")
    else:
        return render(request, "add_product.html")




