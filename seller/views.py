from django.shortcuts import render, redirect
from django.views.generic import View,ListView,CreateView,DetailView,UpdateView,DeleteView,FormView,TemplateView
from seller.forms import BikeForm
from django.urls import reverse_lazy
from seller.models import Bikes
from seller.forms import SignUpForm,SigninForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


class SellerHome(View):
    def get(self, request):
        return render(request, 'seller_home.html')


#addbikes

class AddBike(CreateView):
    model=Bikes
    form_class=BikeForm
    template_name = 'add_bikes.html'
    success_url = reverse_lazy("listbikes")



#listbikes

class BikeList(ListView):
    model=Bikes
    context_object_name='bikes'
    template_name = 'seller_list_bikes.html'


#viewbike
class BikeDetail(DetailView):
    model=Bikes
    template_name = 'bike-details.html'
    context_object_name = 'bike'
    pk_url_kwarg = 'id'

#editbike
class EditBike(UpdateView):
    model=Bikes
    form_class = BikeForm
    template_name = 'edit_bike.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listbikes')

#delete
class DeleteBike(DeleteView):
    model=Bikes
    template_name = 'bikes_confirm_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listbikes')



class SignUp(CreateView):
    model=User
    form_class = SignUpForm
    template_name = 'usersignup.html'
    success_url = reverse_lazy('signin')




class SigninView(FormView):
    template_name = 'usersignin.html'
    form_class = SigninForm

    def post(self,request,*args,**kwargs):
        form=SigninForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pwd)
            # print(user)
            if user:
                login(request, user)
                return redirect('seller_home')
            else:
                return render(request,'usersignin.html',{'form':form})

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect('signin')


class ChangePassword(TemplateView):
    template_name = 'verify_password.html'

    def post(self,request):
        pwd=request.POST.get('pwd')
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect('resetpwd')
        else:

            return render(request,self.template_name,{'ermsg':'incorrect password'})




class PasswordReset(TemplateView):
    template_name = 'password_reset.html'


    def post(self,request,*args,**kwargs):
        new_password=request.POST.get('pwd1')
        confirmpwd=request.POST.get('pwd2')

        if new_password!=confirmpwd:
            return render(request,self.template_name,{'err_msg':'password mismatch'})
        else:
            usr=User.objects.get(username=request.user)
            usr.set_password(confirmpwd)
            usr.save()
            return render(request,self.template_name,{'success_msg':'Password Changed Successfully!'})





# class Getcountbike(View):
#     def get(self,request):
#         bik= Bikes.objects.filter(id=id).count()
#         return render(request,'base.html',{'countbikes':bik})











# Create your views here.
