# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from eduskillprojectapp.models.models import Enquiryform, Enrollform
from django.contrib import messages


def home_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        place_of_study = request.POST.get('place_of_study')
        city_live = request.POST.get('city_live')
        course_interested = request.POST.get('course_interested')
        phone_code = request.POST.get('phone_code')
        hear = request.POST.get('hear')
        mode_training = request.POST.get('mode_training')
        other = request.POST.get('other')

        enquiry = Enquiryform(fname=fname, email=email, mobile_number=mobile_number, place_of_study=place_of_study,
                          city_live=city_live,course_interested=course_interested,phone_code=phone_code,hear=hear,
                            mode_training=mode_training,other=other)
        enquiry.register()
        return render(request, 'index.html')
        return HttpResponse("data inserted")
def about_page(request):
    return render(request,'about.html')
def software_page(request):
    return render(request,'software.html')
def multimedia_page(request):
    return render(request,'multimedia.html')
def contact_page(request):
    return render(request,'contact.html')
def hardware_page(request):
    return render(request,'hardware.html')
def dca_page(request):
    return render(request,'dca.html')
def more2019_page(request):
    return render(request,'more2019.html')
def pgdca_page(request):
    return render(request,'pgdca.html')
def dhne_page(request):
    return render(request,'dhne.html')
def dchm_page(request):
    return render(request,'dchm.html')
def san_page(request):
    return render(request,'san.html')
def aoc_page(request):
    return render(request,'aoc.html')
def dgda_page(request):
    return render(request,'dgda.html')
def twod_page(request):
    return render(request,'2d.html')
def threed_page(request):
    return render(request,'3d.html')
def cttc_page(request):
    return render(request,'cttc.html')
def dabd_page(request):
    return render(request,'dabd.html')
def dao_page(request):
    return render(request,'dao.html')
def dhne_page(request):
    return render(request,'dhne.html')
def dma_page(request):
    return render(request,'dma.html')
def mwd_page(request):
    return render(request,'mwd.html')
def dtp_page(request):
    return render(request,'dtp.html')
def wd_page(request):
    return render(request,'wd.html')

def pdcad_page(request):
    return render(request,'pdcad.html')
def pdcfa_page(request):
    return render(request,'pdcfa.html')
def oa_page(request):
    return render(request,'oa.html')
def enroll_page(request):
    if request.method == 'GET':
        return render(request, 'enroll.html')
    else:
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        place = request.POST.get('place')
        course = request.POST.get('course')
        
        enroll = Enrollform(name=name, mobile=mobile, place=place, course=course)
        enroll.register()
        messages.success(request, 'Form submitted successfully. Our educator will get in touch within 24hrs after registration.')
        return render(request,'enroll.html')
        return HttpResponse("data inserted")
    