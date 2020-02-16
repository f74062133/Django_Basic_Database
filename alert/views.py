from django.shortcuts import render
from alert import models
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.
def hello_view(request):
    return render(request, 'hello_django.html', {
        'data': 'hello django',
    })

def blogs(request):
    #num = {'id_get':[]}
    #num = num.cleaned_data['id_get']
    # return HttpResponse(“Hello world ! “)
    # article = models.Blog.objects.get(pk=’41078855')
    # return render(request, ‘blog/index.html’, {“article”: articles})
    articles = models.Admissions.objects.all()
    paginator = Paginator(articles, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

#    if 'id' in request.GET:
#        num = models.Student.objects.get(id=request.GET['id'])
#    if request.method == 'GET':
#        num = (request.GET.get('id'))
        #if id_get is not None and type(id_get)==int:
        #    num['id_get'] = int(id_get)
    #返回至前端渲染
    return render(request, "index.html",{'contacts': contacts}) #必须用这个return

def child(request, num):
    articles = models.Patients.objects.filter(subject=num)
    paginator = Paginator(articles, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "child.html",context) #必须用这个return

