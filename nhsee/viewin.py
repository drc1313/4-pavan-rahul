

from django.shortcuts import render,get_object_or_404

def login(request):
    email=request.GET.get("email")
    password=request.GET.get("password")
    repassword=request.GET.get("repassword")
    if password == repassword:
        insertusers=superusers(username=email,password=password)
        insertusers.save()
        return render(request,'signup.html')


    print(email)
    print(password)
    return render(request,'signup.html')

def home(request):
    return render(request,"home.html")
