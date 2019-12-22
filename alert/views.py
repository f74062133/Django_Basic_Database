from django.shortcuts import render
from alert import models
from django.core.paginator import Paginator

# Create your views here.
def hello_view(request):
    return render(request, 'hello_django.html', {
        'data': "",
    })

def blogs(request):
    # return HttpResponse(“Hello world ! “)
    # article = models.Blog.objects.get(pk=’41078855')
    # return render(request, ‘blog/index.html’, {“article”: articles})
    articles = models.Student.objects.all()
    paginator = Paginator(articles, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    #返回至前端渲染
    return render(request, "index.html",context) #必须用这个return

