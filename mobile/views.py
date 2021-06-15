from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mobile/index.html')


#list all mobiles
def listmobiles(request):
    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobileadmin/adminpage.html",context)

