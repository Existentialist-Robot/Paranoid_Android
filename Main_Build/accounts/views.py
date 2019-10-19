from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # returns valid or invalue
        if form.is_valid():
            user = form.save()
            #log the user in
            login(request, user)
            return redirect('Search:list') # app name and then url
    else:
        form = UserCreationForm()
    return render(request,"accounts/signup.html",{'form':form}) # will run on initial page and if there is an invalid password/username

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) # have to specify data= because it is not the default of this function
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('search:home') # app name and then url

    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html",{'form':form})

# @login_required(login_url="/accounts/login/")
# def email_signup_view(request):
#     if request.method == 'POST':
#         form = forms.CreateBlog(request.POST,request.FILES) # validating the input data, images are on seperate FILES object
#         if form.is_valid():
#             instance = form.save(commit=False) # don't commit just yet
#             instance.author = request.user
#             instance.save()
#             form.save_m2m()
#             return redirect('blog:list')
#     else:
#         form = forms.CreateBlog()
#         return render(request, "blog/blog_create.html", {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('search:home')
