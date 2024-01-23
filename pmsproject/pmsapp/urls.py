from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('registration',views.registration,name="registration"),
    path('login',views.login,name="login"),
    path('checkemplogin',views.checkemplogin,name="checkemplogin"),
    path('home',views.home,name="home"),
    path('viewprofile',views.viewprofile,name="viewprofile"),
    path('changepassword',views.changepassword,name="changepassword"),
    path('empupdatepwd', views.empupdatepwd, name="empupdatepwd"),
    path("vieweproducts",views.vieweproducts,name="vieweproducts"),
    path("displayeproducts",views.displayeproducts,name="displayeproducts"),
    path('emplogout',views.emplogout,name='emplogout'),

    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('checkadminlogin',views.checkadminlogin,name="checkadminlogin"),
    path('adminhome',views.adminhome,name="adminhome"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("viewaproducts",views.viewaproducts,name="viewaproducts"),
    path('viewusers',views.viewusers,name="viewusers"),
    path("deleteemp/<int:eid>",views.deleteemp,name="deleteemp"),
    path('adminlogout', views.adminlogout, name='adminlogout'),
    path('furniture', views.furniture, name="furniture"),
    path('about', views.about, name="about"),
    path('booknow', views.booknow, name="booknow"),

    path("setcookies", views.setcookies, name="setcookies"),
    path("getcookies", views.getcookies, name="getcookies"),


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

