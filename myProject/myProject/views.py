from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from myapp.models import *


def signupPage(request):

    if request.method == "POST":

        user_name= request.POST.get('username')
        displayname= request.POST.get('display_name')
        mail= request.POST.get('email')
        pass_word= request.POST.get('password')
        usertype= request.POST.get('user_type')
        user = Custom_User.objects.create_user(username=user_name,password=pass_word)
        user.display_name=displayname
        user.email=mail
        user.user_type=usertype
        user.save()
        return redirect("signinPage")

    return render(request,'signup.html')


def logoutPage(request):

    logout(request)

    return redirect('signinPage')

def signinPage(request):

    if request.method == "POST":

        user_name= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=user_name, password=password)

        print(user)

        if user:
            login(request,user)
            return redirect("dashboardPage")


    return render(request,'login.html')

@login_required
def dashboardPage(request):

    return render(request,"dashboard.html")

@login_required
def viewBlog(request):

    blog=BlogHub.objects.all()

    context={
        'blog':blog
    }
    return render(request,"view.html",context)

def addblog(request):

    user = request.user

    if request.method == 'POST':

        blogTitle=request.POST.get('blogTitle')
        bloggerName=request.POST.get('bloggerName')
        location=request.POST.get('location')
        description=request.POST.get('description')

        blog=BlogHub(
            blog_title=blogTitle,
            blogger_bio=bloggerName,
            location=location,
            description=description,
            blog_creator=user,
        )
        blog.save()

        return redirect("viewBlog")
    

    return render(request,'Viewers/Addblog.html')


def deleteBlog(request,myid):

    blog=BlogHub.objects.filter(id=myid)
    blog.delete()

    return redirect("viewBlog")

def editBlog(request,myid):

    blog=BlogHub.objects.filter(id=myid)

    return render(request,'Viewers/editblog.html',{'blog':blog})

def updateBlog(request):

    user = request.user
    if request.method == 'POST':

        blog_id=request.POST.get('blogid')
        jobTitle=request.POST.get('blogTitle')
        blogger_bio=request.POST.get('blogbio')
        location=request.POST.get('location')
        description=request.POST.get('description')
        blog=BlogHub(
            id=blog_id,
            blog_title=jobTitle,
            blogger_bio=blogger_bio,
            location=location,
            description=description,
            blog_creator=user,
        )
        blog.save()
        return redirect("viewBlog")
    

def createBlog(request,myid):

    blog=BlogHub.objects.filter(id=myid)
    

    return render(request,'Blogger/createblog.html')

def ProfilePage(request):

    return render(request,'profile.html')

def EditProfilePage(request):

    return render(request,'Editprofile.html')


