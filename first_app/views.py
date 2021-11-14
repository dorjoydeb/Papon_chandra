from django.shortcuts import render
from django.http import HttpResponse
from . import models


def home(request):
    Project_data = models.Projects.objects.all()
    Cate_data = models.Proj_cate.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        sub = request.POST['subject']
        phone = request.POST['phone']
        mess = request.POST['message']
        Email_data = models.Email_info(Name=name, Email=email, Subject=sub, Phone=phone, Message=mess)
        Email_data.save()
        return render (request, 'index.html')
    dic = {
        'Proj': Project_data,
        'Cate': Cate_data
    }
    return render(request, 'index.html', context=dic)

# Create your views here.
