from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signUpView(request):
    form = UserCreationForm()
    template_name = 'AUTH_APP/register.html'
    context = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,template_name,context)


def loginView(request):
    form = UserCreationForm()
    template_name = 'AUTH_APP/login_temp.html'
    context = {}
    if request.method=='POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')
        #print(f'username:{u}-------------- PASSWORD:{p}')

        User = authenticate(username=u, password=p)
        #print(user)
        if User is not None:
            login(request, User)
            return redirect('showorder_url')
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('showorder_url')