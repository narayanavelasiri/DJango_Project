from django.shortcuts import render
from main import models

def home(request):
    return render(request, "home.html")
def services(request):
    return render(request,"services.html")

def about(request):
    return render(request,"about.html")
def login(request):
    return render(request,"login.html")
def todo(request):
    if request.method=="POST":
        task = request.POST.get("task")
        c = models.todo(task=task)
        c.save()
        
    return render(request,"todo.html")

def ait(request):
    products = [
        {"id":1,"name":"product1","price":33,"url":"https://picsum.photos/id/870/200/300?grayscale&blur=2"},
        {"id":2,"name":"product2","price":39,"url":"https://picsum.photos/id/860/200/300?grayscale&blur=2"},
        {"id":3,"name":"product3","price":32,"url":"https://picsum.photos/id/770/200/300?grayscale&blur=2"}
    ]
    data = {'products':products}
    return render(request,'ait.html',data)

