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

def patients(request):
    #num = {'id_get':[]}
    #num = num.cleaned_data['id_get']
    # return HttpResponse(“Hello world ! “)
    # article = models.Blog.objects.get(pk=’41078855')
    # return render(request, ‘blog/index.html’, {“article”: articles})
    articles = models.Patients.objects.all()
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

def admissions(request, num):
    articles = models.Admissions.objects.filter(subject=num)
    paginator = Paginator(articles, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "child.html",context) #必须用这个return

def callout(request, num):
    articles = models.Callout.objects.filter(subject=num)
    paginator = Paginator(articles, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "callout.html",context) #必须用这个return

def cptevents(request, num):
    articles = models.Cptevents.objects.filter(subject=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "cptevents.html",context) #必须用这个return
def datetimeevents(request, num):
    articles = models.Datetimeevents.objects.filter(subject=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "datetimeevents.html",context) #必须用这个return
def diagnoses_icd(request, num):
    articles = models.DiagnosesIcd.objects.filter(subject=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "diagnoses_icd.html",context) #必须用这个return

def drgcodes(request, num):
    articles = models.Drgcodes.objects.filter(subject=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "drgcodes.html",context) #必须用这个return

def icustays(request, num):
    articles = models.Icustays.objects.filter(subject=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "icustays.html",context) #必须用这个return
def inputevents_cv(request, num):
    articles = models.InputeventsCv.objects.filter(subject=num)
    paginator = Paginator(articles, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "inputevents_cv.html",context) #必须用这个return
def inputevents_mv(request, num):
    articles = models.InputeventsMv.objects.filter(subject=num)
    paginator = Paginator(articles, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "inputevents_mv.html",context) #必须用这个return
def labevents(request, num):
    articles = models.Labevents.objects.filter(subject=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "labevents.html",context) #必须用这个return

def microbiologyevents(request, num):
    articles = models.Microbiologyevents.objects.filter(subject=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "microbiologyevents.html",context) #必须用这个return
def noteevents(request, num):
    articles = models.Noteevents.objects.filter(subject=num)
    paginator = Paginator(articles, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "noteevents.html",context) #必须用这个return
def outputevents(request, num):
    articles = models.Outputevents.objects.filter(subject=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "outputevents.html",context) #必须用这个return
def prescriptions(request, num):
    articles = models.Prescriptions.objects.filter(subject=num)
    paginator = Paginator(articles, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "prescriptions.html",context) #必须用这个return
def procedureevents_mv(request, num):
    articles = models.ProcedureeventsMv.objects.filter(subject=num)
    paginator = Paginator(articles, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "procedureevents_mv.html",context) #必须用这个return
def procedures_icd(request, num):
    articles = models.ProceduresIcd.objects.filter(subject=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "procedures_icd.html",context) #必须用这个return
def services(request, num):
    articles = models.Services.objects.filter(subject=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "services.html",context) #必须用这个return
def transfers(request, num):
    articles = models.Transfers.objects.filter(subject=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "transfers.html",context) #必须用这个return
def chartevents(request, num):
    articles = models.Chartevents.objects.filter(subject=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "chartevents.html",context) #必须用这个return
def d_icd_diagnoses(request, num):
    articles = models.DIcdDiagnoses.objects.filter(icd9_code=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "d_icd_diagnoses.html",context) #必须用这个return
def d_icd_procedures(request, num):
    articles = models.DIcdProcedures.objects.filter(icd9_code=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "d_icd_procedures.html",context) #必须用这个return
def d_items(request, num):
    articles = models.DItems.objects.filter(itemid=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "d_items.html",context) #必须用这个return
def d_labitems(request, num):
    articles = models.DLabitems.objects.filter(itemid=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "d_labitems.html",context) #必须用这个return
def find_icustays(request, num):
    articles = models.Icustays.objects.filter(icustay_id=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "find_icustays.html",context) #必须用这个return
def find_hadmid(request, num):
    articles = models.Admissions.objects.filter(hadm_id=num)
    paginator = Paginator(articles, 20)  # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}
    return render(request, "find_hadmid.html", context) #必须用这个return