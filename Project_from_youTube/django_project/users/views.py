from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm



# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Been Created')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)

def profile(request):
    # context = {'username': user.username }
    return (request, 'users/profile.html',)
