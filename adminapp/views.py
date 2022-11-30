from django.shortcuts import render, redirect, reverse
from fmiapp.models import Enquiry, LoginInfo, FarmerInfo, MerchantInfo
from .models import Booking, News
from merchantapp.models import orderDetail
from farmerapp.models import FarmerSellProduct
import datetime
from datetime import datetime
import pandas as pd


# Create your views here.
def adminhome(request):
    if not request.session['admin']:
        return render(request, 'login.html')
    try:
        if request.session['admin']:
            admin_name = LoginInfo.objects.get(userid=request.session['admin'])
            ns = News.objects.all()
            return render(request, 'adminhome.html', {'ns': ns, 'admin_name': admin_name})
    except:
        return render(request, 'login.html')


def enquiries(request):
    try:
        if request.session['admin']:
            enq = Enquiry.objects.all()
            return render(request, 'enquiries.html', {'enq': enq})
    except:
        return render(request, 'login.html')


def booking(request):
    try:
        if request.session['admin']:
            fi = FarmerInfo.objects.all()
            return render(request, 'booking.html', {'fi': fi})
    except:
        return render(request, 'login.html')


def purchase(request):
    try:
        if request.session['admin']:
            bk = Booking.objects.all()
            return render(request, 'purchase.html', {'bk': bk})
    except:
        return render(request, 'login.html')


def changepassword(request):
    try:
        if request.session['admin']:
            return render(request, 'changepassword.html')
    except:
        return render(request, 'login.html')


def logout(request):
    request.session['admin'] = None
    return render(request, 'login.html')


def book(request, ano):
    fi = FarmerInfo.objects.get(aadharno=ano)
    return render(request, 'book.html', {'fi': fi})


def pbook(request):
    name = request.POST['name']
    address = request.POST['address']
    aadharno = request.POST['aadharno']
    contactno = request.POST['contactno']
    noofpacket = int(request.POST['noofpacket'])
    duration = int(request.POST['duration'])
    rate = int(request.POST['rate'])
    advance = int(request.POST['advance'])
    totalamt = noofpacket * duration * rate
    restamt = totalamt - advance
    bookingdate = datetime.datetime.today()
    b = Booking(name=name, address=address, contactno=contactno, aadharno=aadharno, noofpacket=noofpacket,
                duration=duration, rate=rate, advance=advance, totalamt=totalamt, restamt=restamt,
                bookingdate=bookingdate)
    b.save()
    return redirect('adminapp:booking')


def viewbook(request, ano):
    res = Booking.objects.get(aadharno=ano)
    return render(request, 'viewbook.html', {'res': res})


def deleteenq(request, id):
    e = Enquiry.objects.get(id=id)
    e.delete()
    return redirect('adminapp:enquiries')


def addnews(request):
    newstext = request.POST['newstext']
    newsdate = datetime.datetime.today()
    ns = News(newstext=newstext, newsdate=newsdate)
    ns.save()
    return redirect('adminapp:adminhome')


def deletenews(request, id):
    ns = News.objects.get(id=id)
    ns.delete()
    return redirect('adminapp:adminhome')


def changepwd(request):
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    msg = 'Message ='
    if newpassword != confirmpassword:
        msg = msg + ' New password is not machted with confirm password!'
        return render(request, 'changepassword.html', {'msg': msg})
    admin = request.session['admin']
    try:
        obj = LoginInfo.objects.get(admin=admin, password=oldpassword)
        LoginInfo.objects.filter(admin=admin).update(password=newpassword)
        return redirect('adminapp:logout')
    except:
        msg = msg + ' Old Password is not match!'
    return render(request, 'changepassword.html', {'msg': msg})


def pay(request, ano):
    obj = Booking.objects.get(aadharno=ano)
    return render(request, 'pay.html', {'obj': obj})


def paid(request):
    aadharno = request.POST['aadharno']
    restamt = int(request.POST['restamt'])
    payamt = int(request.POST['payamt'])
    restamt = restamt - payamt
    Booking.objects.filter(aadharno=aadharno).update(restamt=restamt)
    return redirect('adminapp:purchase')


# First farmenr name in FarmerSellProduct and then show

def sellingitems(request):
    global productObj, soldobj
    try:
        soldobj = orderDetail.objects.all()
        productObj = FarmerSellProduct.objects.select_related('farmerName').all()
        farmerName = FarmerInfo.objects.filter(aadharno=productObj[0].farmerName)[0].name
    except:
        farmerName = ''
    context = {'soldobj': soldobj, 'productObj': productObj, 'farmerName': farmerName}
    return render(request, 'sellingitems.html', context)


def solditem(request):
    soldobj = orderDetail.objects.all()
    context = {'soldobj': soldobj}
    return render(request, 'solditem.html', context)


def downAllProdList(request):
    try:
        products = orderDetail.objects.all()
        productName = []
        qty = []
        price = []
        customer = []
        address = []
        panno = []
        gstno = []
        productid = []
        city = []
        state = []
        zip = []
        merchantName = []
        merchantId = []
        farmerName = []
        farmerId = []
        date = []
        for product in range(len(products)):
            productName.append(products[product].product)
            qty.append(products[product].qty)
            price.append(products[product].price)
            customer.append(products[product].customer)
            address.append(products[product].address)
            panno.append(products[product].panno)
            gstno.append(products[product].gstno)
            productid.append(products[product].productid)
            city.append(products[product].city)
            state.append(products[product].state)
            zip.append(products[product].zip)
            merchantName.append(products[product].merchantName)
            merchantId.append(products[product].merchantId)
            farmerName.append(products[product].farmerName)
            farmerId.append(products[product].farmerId)
            date.append(products[product].date)
        dict = {
            'Product Name': productName,
            'Qty': qty,
            'Price': price,
            'Customer': customer,
            'Address': address,
            'PAN No': panno,
            'GST No': gstno,
            'Product Id': productid,
            'City': city,
            'State': state,
            'Zip': zip,
            'Merchant Name': merchantName,
            'Merchant Id': merchantId,
            'FarmerName': farmerName,
            'Farmer Id': farmerId,
            'Date': date,
        }
        df = pd.DataFrame(dict)
        updateDate = str(datetime.now().strftime("%H_%M_%S"))
        path = r'C:/Users/Lenovo/Downloads/' + updateDate + '_product_List.csv'
        df.to_csv(path, index=False, header=True, index_label='Event_id')
        return redirect(reverse('adminapp:adminhome'))
    except Exception as e:
        # print(e)
        return redirect(reverse('adminapp:adminhome'))
