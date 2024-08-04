from django.shortcuts import render
from blog.models import Article
from .forms import InputForm

def home(request):
    list_articles = Article.objects.all()
    context={"liste_articles":list_articles}
    return render(request,"index.html",context)

def detail(request,id_article):
    article=Article.objects.get(id=id_article)
    category = article.category
    article_en_relations = Article.objects.filter(category=category)[:5]
    return render(request,'detail.html',{"article":article,"aer": article_en_relations})



def home_views(request):
    context = {}
    context['form'] = InputForm()
    return render(request,"home2.html",context)

def search(request):
    query=request.GET["article"]
    liste_article = Article.objects.filter(title__contains = query)
    return render (request,'search.html',{"liste_article":liste_article})
    
    
# Create your views here.
