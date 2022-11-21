from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy


class SignUpView(generic.CreateView):
    template_name = 'pages/sign-up.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("signup")
    
    
class LoginView(generic.View):
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
              login(request, user)
              return redirect('/')
        else:
            return("please sign up")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, '/', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
 
 
 
 
 
 
 
 
