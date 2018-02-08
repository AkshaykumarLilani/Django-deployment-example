from django.shortcuts import render
from users_app.models import Users
from . import forms

# Create your views here.
def index(request):
    return render(request, 'users_app/index.html')

def users(request):
    users_list = Users.objects.order_by('first_name')
    users_dict = {'record':users_list}
    return render(request, 'users_app/users.html', context=users_dict)

def sign_up_view(request):
    form = forms.SignUpForm()

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Sorry")
    return render(request, 'users_app/sign-up.html', {'form':form})
