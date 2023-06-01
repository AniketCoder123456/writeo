from django.shortcuts import render, redirect
from .models import Article, User, Message
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, AddArticleForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    article = Article.objects.all()
    return render(request, "home.html", {"articles":article})



@csrf_exempt
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Check the fields")

    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect("home")
    

@csrf_exempt
def registerUser(request):
    form = RegisterForm()
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error ocurred during registration, username is taken or email")


    return render(request, "register.html", {"form":form})


def addarticle(request):
    
    if request.method=="POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        author = User.objects.get(username=request.user.username)
        
        article = Article(title=title, description=description, author=author)
        article.save()
        return redirect("home")



    return render(request, "add-article.html")


@login_required(login_url="login")
def singleArticle(request, pk):
    article = Article.objects.get(id=pk)

    comments = article.message_set.all().order_by("-created")

    if request.method=="POST":
        usermessage = Message.objects.create(
                user=request.user,
                article=article,
                body=request.POST.get("body")
        )
        return redirect("single-article", pk=article.id)
    context = {"article":article, "comments":comments}
    return render(request, "single-article.html", context)

@login_required(login_url="login")
def deleteMessage(request, pk):
    usermessage = Message.objects.get(id=pk)
    if request.method=="POST":
        usermessage.delete()
        return redirect("single-article", usermessage.article.id)
    return render(request, "delete-message.html", {"usermessage":usermessage})


@login_required(login_url="login")
def userArticles(request, pk):
    author = User.objects.get(id=pk)
    userkearticles = author.article_set.all()
    return render(request, "user-articles.html", {"userkearticles":userkearticles})


@login_required(login_url="login")
def deleteArticle(request, pk):
    article = Article.objects.get(id=pk)
    userid = article.id
    if request.method=="POST":
        article.delete()
        return redirect("home")
    return render(request, "delete-article.html", {"article":article})


@login_required(login_url="login")
def updateArticle(request, pk):
    article = Article.objects.get(id=pk)
    if request.method=="POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        article.title = title
        article.description = description
        article.save()
        return redirect("user-articles", article.author.id)

    return render(request, "add-article.html", {"page":"update","article_update":article})