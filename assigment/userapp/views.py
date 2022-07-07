from django.shortcuts import render, HttpResponse,HttpResponseRedirect, redirect
from .forms import SignUpForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignUpForm
from django.views.generic import CreateView,ListView
from .forms import SignUpForm, UserAuthentiationForm
from django.contrib.auth import authenticate, login,logout, get_user_model
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView,RedirectView



User = get_user_model()

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = '/users/signup/'


class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')
   

class Dashboard(TemplateView):
	template_name = 'dashboard.html'


class Signin(View):
    template_name = 'login.html'
    form_class = UserAuthentiationForm
    
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        if request.method=="POST":
            fm = UserAuthentiationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/users/dashboard/')
            else:

                fm = UserAuthentiationForm()
                message = "Invalid login credential"
            return render(request,self.template_name,{'form':fm,'msg':message})    
                        


# class SignUpView(TemplateView):
#     template_name = 'signup.html'

#     def get(self, request):
#         context = super().get_context_data(**kwargs)
#         fm = SignUpForm()
#         context['form'] = fm
#         return context

#     def post(self, request):
#         fm = SignUpForm(request.POST)
#         print(fm)
#         if fm.is_valid():
#             fm.save()
#         else:
#             print('not inserteds')
#             fm = SignUpForm()
#         return render(request, self.template_name, {'form': fm})


# def signup(request):
#     if request.method == "POST":
#         fm = SignUpForm(request.POST)
#         if fm.is_valid():
#             # messages.success(request, "Account Created Successfully !!")
#             fm.save()
#         else:
#             fm = SignUpForm()
#             return render(request, 'signup.html', {'form': fm})
#     return HttpResponse(request, 'signup.html', {})
# def clean(self):
#     form_data = self.cleaned_data
#     if form_data['password'] != form_data['password_repeat']:
#         self._errors["password"] = ["Password do not match"] # Will raise a error message
#         del form_data['password']
#     return form_data
