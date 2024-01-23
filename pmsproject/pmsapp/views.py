from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm,ProductForm,adminlogin,booknowForm
from .models import Customers,Admin,Product


def index(request):
    return render(request,"index.html")

def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        formdata = RegistrationForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg="Registered Successfully"
            return render(request, "registration.html", {"empform": form,"msg":msg})
        else:
            msg = "Failed to Register"
            return render(request, "registration.html", {"empform": form, "msg": msg})
    return render(request,"registration.html",{"empform":form})

def booknow(request):
    form = booknowForm()
    if request.method == "POST":
        formdata = booknowForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg="enquiry sent Successfully"
            return render(request, "booknow.html", {"booknowform": form,"msg":msg})
        else:
            msg = "Failed to send enquiry"
            return render(request, "booknow.html", {"booknowform": form, "msg": msg})
    return render(request,"booknow.html",{"booknowform":form})

def login(request):
    return render(request,"login.html")


def viewusers(request):
    return render(request,"viewusers.html")

def checkemplogin(request):
    uname = request.POST["eusername"]
    pwd = request.POST["epassword"]

    flag = Customers.objects.filter(Q(username=uname) & Q(password=pwd))

    print(flag)

    if flag:
        emp = Customers.objects.get(username=uname)
        print(emp)
        request.session["eid"] = emp.id
        request.session["ename"] = emp.fullname
        return render(request, "home.html", {"eid": emp.id, "ename": emp.fullname})
    else:
        msg = "Login Failed"
        return render(request, "login.html", {"msg": msg})

def home(request):
    eid=request.session["eid"]
    ename=request.session["ename"]

    return render(request,"home.html",{"eid":eid,"ename":ename})

def viewprofile(request):
    eid=request.session["eid"]
    ename=request.session["ename"]
    emp = Customers.objects.get(id=eid)
    return render(request,"viewprofile.html",{"eid":eid,"ename":ename,"emp":emp})

def changepassword(request):
    eid=request.session["eid"]
    ename=request.session["ename"]
    return render(request,"changepassword.html",{"eid":eid,"ename":ename})

def empupdatepwd(request):
    eid=request.session["eid"]
    ename=request.session["ename"]

    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]

    flag = Customers.objects.filter(Q(id=eid) & Q(password=opwd))

    if flag:
        Customers.objects.filter(id=eid).update(password=npwd)
        msg = "Password Updated Successfully"
        return render(request, "changepassword.html", {"eid": eid, "ename": ename,"msg":msg})
    else:
        msg = "Old Password is Incorrect"
        return render(request, "changepassword.html", {"eid": eid, "ename": ename,"msg":msg})

def vieweproducts(request):

    eid=request.session["eid"]
    ename=request.session["ename"]

    productlist = Product.objects.all()

    return render(request,"vieweproducts.html",{"eid": eid, "ename": ename,"productlist":productlist})

def displayeproducts(request):

    eid=request.session["eid"]
    ename=request.session["ename"]

    pname = request.POST["pname"]
    print(pname)

    productlist = Product.objects.filter(name__icontains=pname)

    return render(request,"displayeproducts.html",{"eid": eid, "ename": ename,"productlist":productlist})


def emplogout(request):
    return render(request,"login.html")

def adminlogin(request):
    return render(request,"adminlogin.html")

def checkadminlogin(request):
    uname = request.POST["ausername"]
    pwd = request.POST["apassword"]

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        request.session["auname"] = admin.username
        return render(request, "adminhome.html", {"auname": admin.username})
    else:
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})


def adminhome(request):
    auname=request.session["auname"]
    return render(request,"adminhome.html",{"auname":auname})





def addproduct(request):
    auname = request.session["auname"]
    form = ProductForm()
    if request.method == "POST":
        formdata = ProductForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Product Added Successfully"
            return render(request, "addproduct.html", {"auname":auname,"productform": form,"msg":msg})
        else:
            msg = "Failed to Add Product"
            return render(request, "addproduct.html", {"auname":auname,"productform": form, "msg": msg})
    return render(request,"addproduct.html",{"auname":auname,"productform":form})

def viewusers(request):
    auname=request.session["auname"]
    emplist = Customers.objects.all()
    count = Customers.objects.count()
    return render(request,"viewusers.html",{"auname":auname,"emplist":emplist,"count":count})



def viewaproducts(request):
    auname=request.session["auname"]
    productlist = Product.objects.all()
    count = Product.objects.count()
    return render(request,"viewaproducts.html",{"auname":auname,"productlist":productlist,"count":count})

def deleteemp(reequest,eid):
    Customers.objects.filter(id=eid).delete()
    return redirect("viewusers")

def adminlogout(request):
    return render(request,"adminlogin.html")

def about(request):
    return render(request,"about.html")


def furniture(request):
    return render(request,"furniture.html")

def setcookies(request):
    response=HttpResponse("COOKIES DEMO .. !!")
    response.set_cookie("username","exflor")
    response.set_cookie("location","india",max_age=10)
    return response

def getcookies(request):
    uname=request.COOKIES.get("username")
    loc = request.COOKIES.get("location")

    if uname is not None and loc is not None:
        response = uname+","+loc
    elif uname is not None and loc is None:
        response = uname
    elif uname is None and loc is not None:
        response = loc
    else:
        response = "COOKIES NOT FOUND"

    return HttpResponse(response)



