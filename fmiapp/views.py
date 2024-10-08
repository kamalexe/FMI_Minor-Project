from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import FarmerInfo, MerchantInfo, LoginInfo, Enquiry
from adminapp.models import News


# Create your views here.
def index(request):
    ns = News.objects.all()

    # Initialize session variables
    merchantsession = None
    farmersession = None

    # Check if 'merchant' and 'farmer' keys exist in session
    if 'merchant' in request.session:
        merchantsession = request.session['merchant']
    if 'farmer' in request.session:
        farmersession = request.session['farmer']

    return render(request, 'index.html', {'ns': ns, 'merchantsession': merchantsession, 'farmersession': farmersession})


def about(request):
    return render(request, 'about.html')


def farmerreg(request):
    return render(request, 'farmerreg.html')


def merchentreg(request):
    return render(request, 'merchentreg.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


def freg(request):
    name = request.POST['name']
    gender = request.POST['gender']
    address = request.POST['address']
    contactno = request.POST['contactno']
    aadharno = request.POST['aadharno']
    userid = request.POST['userid']
    password = request.POST['password']
    # regdate = datetime.datetime.today()
    fi = FarmerInfo(name=name, gender=gender, address=address, contactno=contactno, aadharno=aadharno, userid=userid,
                    password=password)
    fi.save()
    msg = 'You have registered successfully'
    return render(request, 'farmerreg.html', {'msg': msg})


def mreg(request):
    name = request.POST['name']
    gender = request.POST['gender']
    firmname = request.POST['firmname']
    firmaddress = request.POST['firmaddress']
    contactno = request.POST['contactno']
    userid = request.POST['userid']
    aadharno = request.POST['aadharno']
    panno = request.POST['panno']
    gstno = request.POST['gstno']
    password = request.POST['password']
    # regdate = datetime.datetime.today()
    mi = MerchantInfo(name=name, gender=gender, firmname=firmname, firmaddress=firmaddress, contactno=contactno,
                      userid=userid, aadharno=aadharno, panno=panno, gstno=gstno, password=password)
    mi.save()
    msg = 'You have registered successfully'
    return render(request, 'merchentreg.html', {'msg': msg})


def validate(request):
    userid = request.POST['userid']
    password = request.POST['password']
    usertype = request.POST['usertype']
    try:
        if usertype == 'farmer':
            obj = FarmerInfo.objects.get(userid=userid, password=password, usertype='farmer')
            if obj.usertype == usertype:
                request.session['farmer'] = userid
                return redirect(reverse('farmerapp:farmerhome'))
            else:
                return HttpResponse("farmer Not Login")
        elif usertype == 'admin':
            obj = LoginInfo.objects.get(userid=userid, password=password)
            if obj.usertype == 'admin':
                request.session['admin'] = userid
                return redirect(reverse('adminapp:adminhome'))
            else:
                return HttpResponse("admin not Login")

        if usertype == 'merchant':
            obj = MerchantInfo.objects.get(userid=userid, password=password)
            if obj.usertype == 'merchant':
                request.session['merchant'] = userid
                return redirect(reverse('merchantapp:merchanthome'))
            else:
                msg = 'Invalid User'
                return render(request, 'login.html', {'msg': msg})
        obj = LoginInfo.objects.get(userid=userid, password=password)
        msg = 'Valid User'
    except:
        msg = 'Invalid User'
    return render(request, 'login.html', {'msg': msg})


def saveenq(request):
    name = request.POST['name']
    gender = request.POST['gender']
    address = request.POST['address']
    contactno = request.POST['contactno']
    emailaddress = request.POST['emailaddress']
    enquirytext = request.POST['enquirytext']
    se = Enquiry(name=name, gender=gender, address=address, contactno=contactno, emailaddress=emailaddress,
                 enquirytext=enquirytext)
    se.save()
    msg = 'Your enquiry is submitted! '
    return render(request, 'contact.html', {'msg': msg})

