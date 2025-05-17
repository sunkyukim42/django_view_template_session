from django.shortcuts import render, redirect

from article.models import Article

def index(request):
    articles= Article.objects.all()

    return render(request, 'index.html',{'articles': articles})

def show(request, pk):
    article = Article.objects.get(pk=pk)

    return render(request, 'show.html', {'article' : article})

def new(request):
    return render(request, 'new.html')

def create(request):
    article = Article()
    article.author = request.user
    article.title = request.POST['title']
    article.content= request.POST['content']
    article.save()

    return redirect('article:show', pk=article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)

    return render(request, 'edit.html', {"article":article})

def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    if article.author != request.user:
        return redirect('article:show', pk=pk)
    
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()

    return redirect('article:show', pk=article.pk)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if article.author == request.user:
        article.delete()
    
    return redirect('article:index')

from article.models import Comment

def create_comment(request, pk):
    if request.method == 'POST':
        comment = Comment()
        comment.article = Article.objects.get(pk=pk)
        comment.author = request.user
        comment.content = request.POST['content']
        comment.save()

    return redirect('article:show', pk=pk)

def delete_comment(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()

    return redirect('article:show',pk=comment.article.pk)
