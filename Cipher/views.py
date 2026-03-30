from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Signup, Post, Theory


# Create your views here.

def home(request):
    return render(request, 'home.html')




def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Signup.objects.filter(email=email, password=password)

        if user:
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'Invalid email or password'})

    return render(request, 'signin.html')







def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        Signup.objects.create(
            username=username,
            email=email,
            password=password
        )

        return redirect('signin')

    return render(request, 'signup.html')



def blog(request):

    posts = Post.objects.all()

    return render(request, "blog.html", {"posts": posts})



def about(request):
    return render(request, 'about.html')




from django.shortcuts import render, redirect
from .models import Theory

def add_theory(request):

    if request.method == "POST":

        name = request.POST['name']
        theory = request.POST['theory']

        Theory.objects.create(
            name=name,
            theory=theory
        )

        return redirect('blog')

    return render(request, "add_theory.html")




def theories(request):

    theories = Theory.objects.all()

    return render(request, "theories.html", {"theories": theories})





def add_theory(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        Theory.objects.create(
            title=title,
            content=content,
            user=request.user
        )

        return redirect('theories')


    return render(request, 'add_theory.html')





def edit_theory(request, id):
    theory = get_object_or_404(Theory, id=id)

    # 🔥 owner check
    if theory.user != request.user:
        return redirect('theories')

    if request.method == "POST":
        theory.title = request.POST.get('title')
        theory.content = request.POST.get('content')
        theory.save()

        return redirect('theories')

    return render(request, 'edit_theory.html', {'theory': theory})




def delete_theory(request, id):
    theory = get_object_or_404(Theory, id=id)

    if theory.user != request.user:
        return redirect('theories')

    theory.delete()
    return redirect('theories')



