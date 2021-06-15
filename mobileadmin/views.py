from django.shortcuts import render, redirect
from .models import Product,Orders
from .forms import CreateProductForm
from .forms import UserRegForm, UserLoginForm,OrderForm
from django.contrib.auth import authenticate, login, logout


# to get current user

# Create your views here.

def registeration(request):
    form = UserRegForm()
    context = {}
    context['form'] = form
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()  # calling clean method of usercreated form since inheriting
            return redirect(login)
        else:
            form = UserRegForm(request.POST)
            context['form'] = form
            return render(request, "mobileadmin/signup.html", context)

    return render(request, "mobileadmin/signup.html", context)


def login_form(request):
    form = UserLoginForm()
    context = {}
    context['form'] = form
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                login(request, user)
                if not user.is_superuser:
                    return redirect("alist")
                else:
                    return redirect("listall")
            else:
                print("Login failed")

    return render(request, "mobileadmin/login.html", context)


def signout(request):
    logout(request)
    return redirect("login")


def adminhome(request):
    return render(request, 'mobileadmin/adminhome.html')


# list all mobiles
def listall(request):
    mobiles = Product.objects.all()
    context = {}
    context["mobiles"] = mobiles
    return render(request, "mobileadmin/adminpage.html", context)


# add product
def add_product(request):
    form = CreateProductForm()  # get method ->to render the form to a htmlpage
    context = {}
    context['form'] = form
    if request.method == "POST":
        form = CreateProductForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listall")

    return render(request, "mobileadmin/addproduct.html", context)


def get_mobile_object(id):
    return Product.objects.get(id=id)


def detailview(request, id):
    mobile = get_mobile_object(id)
    context = {}
    context['mobile'] = mobile
    return render(request, "mobileadmin/detailview.html", context)


def deleteview(request, id):
    mobile = get_mobile_object(id)
    mobile.delete()
    return redirect("listall")


def update(request, id):
    mobile = get_mobile_object(id)
    form = CreateProductForm(instance=mobile)
    context = {}
    context['form'] = form
    if request.method == "POST":
        form = CreateProductForm(data=request.POST, instance=mobile)
        if form.is_valid():
            form.save()
            return redirect('listall')
    return render(request, "mobileadmin/update.html", context)


# wbsite
def index(request):
    return render(request, 'mobile/index.html')


# list all mobiles
def listmobiles(request):
    mobiles = Product.objects.all()
    context = {}
    context["mobiles"] = mobiles
    return render(request, "mobileadmin/listmobiles.html", context)


def mobileview(request,id):
    mobile = get_mobile_object(id)
    context = {}
    context['mobile'] = mobile
    return render(request, "mobileadmin/viewmobile.html", context)

#make orders
def orders(request,id):

    product = get_mobile_object(id)
    form = OrderForm(initial={'user': request.user, 'product': product})
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alist')
        else:
            context['form'] = form
            return render(request, 'mobileadmin/orders.html', context)
    return render(request, 'mobileadmin/orders.html', context)


#view orders details so far made

def vieworders(request):
    order=Orders.objects.filter(user=request.user)
    context={}
    context['order']=order
    return render(request,'mobileadmin/vieworders.html', context)

#to cancel order
def cancel_order(request,id):
    order=Orders.objects.get(id=id)
    order.status='Cancelled'
    order.save()
    return redirect('vieworders')