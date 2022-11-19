from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import FarmerInfo, MerchantInfo, LoginInfo, Enquiry
from adminapp.models import News


# Create your views here.
def index(request):
    ns = News.objects.all()
    return render(request, 'index.html', {'ns': ns})


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
    fi = FarmerInfo(name=name, gender=gender, address=address, contactno=contactno, aadharno=aadharno,userid= userid,password = password)
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
                      userid=userid, aadharno=aadharno, panno=panno, gstno=gstno,password=password)
    mi.save()
    msg = 'You have registered successfully'
    return render(request, 'merchentreg.html', {'msg': msg})


def validate(request):
    userid = request.POST['userid']
    password = request.POST['password']
    usertype = request.POST['usertype']
    print(usertype)
    try:
        if usertype == 'farmer':
            obj = FarmerInfo.objects.get(userid=userid, password=password,usertype ='farmer')
            print("farmer Login")
            print(obj)
            if obj.usertype == usertype:
                request.session['farmer'] = userid
                return redirect(reverse('farmerapp:farmerhome'))
            else:
                print('Not Farmer')
                return HttpResponse("farmer Not Login")
        elif usertype == 'admin':
                print("admin Login")
                obj = LoginInfo.objects.get(userid=userid, password=password)
                if obj.usertype == 'admin':
                    request.session['admin'] = userid
                    return redirect(reverse('adminapp:adminhome'))
                    # return HttpResponse("admin Login")
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
                return HttpResponse("M no Login")


        obj = LoginInfo.objects.get(userid=userid, password=password)
        msg = 'Valid User'
        print(obj+" Login")
    except:
        print(" Except")
        msg = 'Invalid User'
    return render(request, 'login.html', {'msg': msg})


def saveenq(request):
    name = request.POST['name']
    gender = request.POST['gender']
    address = request.POST['address']
    contactno = request.POST['contactno']
    emailaddress = request.POST['emailaddress']
    enquirytext = request.POST['enquirytext']
    # enquirydate = datetime.datetime.now()
    se = Enquiry(name=name, gender=gender, address=address, contactno=contactno, emailaddress=emailaddress,
                 enquirytext=enquirytext)
    se.save()
    msg = 'Your enquiry is submitted! '
    return render(request, 'contact.html', {'msg': msg})

def socialpage(request):
    return redirect(reverse('irrigreatapp:bloghome'))
