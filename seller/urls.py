from django.urls import path
from seller import views
urlpatterns=[
    path('home', views.SellerHome.as_view(),name='seller_home'),
    path('bikes/add',views.AddBike.as_view(),name='add_bike'),
    path('bikes/all_bikes',views.BikeList.as_view(),name='listbikes'),
    path('bikes/bike_details/<int:id>',views.BikeDetail.as_view(),name='bikeview'),
    path('bikes/edit_bike/<int:id>',views.EditBike.as_view(),name='edit_bike'),
    path('bikes/deletebike/<int:id>',views.DeleteBike.as_view(),name='remove_bike'),
    path('user/account/register',views.SignUp.as_view(),name='signup'),
    path('user/account/signin',views.SigninView.as_view(),name='signin'),
    path('user/account/signout',views.signout_view,name='signout'),
    path('user/account/verify_password',views.ChangePassword.as_view(),name='pwdchange'),
    path('user/account/create_new_password',views.PasswordReset.as_view(),name='resetpwd')

]
