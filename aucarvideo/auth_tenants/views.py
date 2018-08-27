from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


class RegisterView(TemplateView):
    def get(self, request,*args,**kwargs):
        user_form = UserCreationForm()
        template_name = 'auth_tenants/register_form.html'
        context = {
            'user_form': user_form
        }
        return render(request,template_name,context)

    def post(self, request,*args,**kwargs):
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('auth_tenants:login')
            
        else:
            template_name = 'auth_tenants/register_form.html'
            context = {
                'user_form': user_form,
            }

            return render(request,template_name,context)



class LoginView(TemplateView):
    def get(self, request, *args, **kwargs):
        login_form = AuthenticationForm()
        template_name = 'auth_tenants/login.html'
        context = {
            'login_form': login_form
        }
        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        login_form = AuthenticationForm(request=request, data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('contests:list_admin')
        else:
            template_name = 'auth_tenants/login.html'
            context = {
                'login_form': login_form
            }
            return render(request, template_name, context)

