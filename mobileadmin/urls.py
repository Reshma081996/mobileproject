"""mobilepro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import adminhome,listall,add_product,detailview,deleteview,update,registeration,login_form,signout,listmobiles,mobileview,orders,vieworders,cancel_order


urlpatterns = [
    path('adminhome/',adminhome,name='adminhome'),
    path('listall/',listall,name="listall"),
    path('add/',add_product,name="add"),
    path('detail/<int:id>',detailview,name='detail'),
    path('delete/<int:id>',deleteview,name='delete'),
    path('update/<int:id>',update,name='update'),
    path('register',registeration,name='register'),
    path('login',login_form,name='login'),
    path('signout',signout,name='signout'),

    path('list/',listmobiles,name='alist'),
    path('mobileview/<int:id>',mobileview,name='mobileview'),
    path('orders/<int:id>',orders,name='orders'),
    path('vieworders/',vieworders,name='vieworders'),
    path('cancelorder/<int:id>',cancel_order,name='cancelorder')

]
