from django.shortcuts import render,HttpResponse,redirect,reverse
from fmiapp.models import MerchantInfo,FarmerInfo
from farmerapp.models import FarmerSellProduct,Tracker
from .models import orderDetail
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
MERCHANT_KEY = 'XW&JtZccG&mRxq0K'
# Create your views here.
def merchanthome(request):
    try:
        if not request.session['merchant']:
            return render(request, 'login.html')
        if request.session['merchant']:
            merchantName = MerchantInfo.objects.get(userid=request.session['merchant'])
            allProduct = FarmerSellProduct.objects.all()
            context = {'merchantName':merchantName,'allProduct':allProduct}
        return render(request,'merchanthome.html',context )
    except:
        return render(request, 'login.html')

def logout(request):
    request.session['merchant'] = None
    return render(request, 'login.html')


def viewProd(request,id):
    if not request.session['merchant']:
        return render(request, 'login.html')
    merchantName = MerchantInfo.objects.get(userid=request.session['merchant'])
    try:
        product = FarmerSellProduct.objects.get(id = id)
    except:
        return redirect('/merchantapp/')
    sellerobj= FarmerInfo.objects.get(aadharno = product.farmerName)
    print('----viewProd')
    print(sellerobj.name)
    total = int(product.qty) * int(product.price)

    # Like Unlike
    merchantid = merchantName.aadharno
    product = FarmerSellProduct.objects.get(id=id)
    liked = False
    likesymb = "fa-solid fa-thumbs-up"
    if product.likes.filter(aadharno=merchantid).exists():
        likesymb = "fa-solid fa-thumbs-up"
    else:
        likesymb = "fa-regular fa-thumbs-up"
        liked = True

    context = {'product':product,'total':total,'merchantName':merchantName,'sellerName':sellerobj.name,'likesymb':likesymb}
    return render(request ,'viewprod.html',context)

def placeorder(request,id):
    if not request.session['merchant']:
        return render(request, 'login.html')
    merchantName = MerchantInfo.objects.get(userid=request.session['merchant'])
    merchantid = merchantName.userid
    try:
        product = FarmerSellProduct.objects.get(id=id)
    except:
        return redirect('/merchantapp/')
    print(product.farmerName)
    total = int(product.qty) * int(product.price)
    context = {'product': product,'merchantName': merchantName,'total':total}

    return render(request,'placeorder.html',context)

def purchaseCustomerDetail(request):
    if not request.session['merchant']:
        return render(request, 'login.html')
    productid = request.POST['productid']
    request.session['productid2'] = productid
    print('111111111111111111111111111111111')
    print(productid)
    print(request.session['productid2'])
    print('111111111111111111111111111111111')
    soldProduct = FarmerSellProduct.objects.get(id=productid)
    sellerobj = FarmerInfo.objects.get(aadharno=soldProduct.farmerName)

    email = request.POST['email']
    customer = request.POST['customer']
    address = request.POST['address']
    panno = request.POST['panno']
    gstno = request.POST['gstno']
    product = request.POST['product']
    qty = request.POST['qty']
    price = request.POST['price']
    city = request.POST['city']
    state = request.POST['state']
    zip = request.POST['zip']
    merchantobj = MerchantInfo.objects.get(userid=request.session['merchant'])
    merchantId = merchantobj
    merchantName = merchantobj.name
    farmerName = sellerobj.name
    farmerId = sellerobj

    detail = orderDetail(email= email,customer=customer, address = address, panno=panno, gstno=gstno,productid=productid, product=product, qty=qty, price=price,city=city,state=state,zip=zip,merchantName=merchantName,merchantId=merchantId,farmerName=farmerName,farmerId=farmerId)
    detail.save()

    orderObj = orderDetail.objects.filter(merchantId=merchantId,productid=productid)
    updateTrack = Tracker(orderId = orderObj[0])
    updateTrack.save()
    # request paytm to transfer the amount to your account
    param_dict ={
        'MID': 'zNQCPg84186322693656',
        'ORDER_ID': str(orderObj[0].id),
        'TXN_AMOUNT': str(price),
        'CUST_ID': email,
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'WEBSTAGING',
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL':'http://127.0.0.1:8000/merchantapp/handlerequest',
    }
    param_dict['CHECKSUMHASH'] = Checksum.generateSignature(param_dict,MERCHANT_KEY)
    return render(request,'paytm.html', {'param_dict':param_dict} )

def purchasedprod(request):
    if request.session['merchant']:
        merchantobj = MerchantInfo.objects.get(userid=request.session['merchant'])
        merchantId = merchantobj.aadharno
        orderObj = orderDetail.objects.filter(merchantId = merchantId)

        context = {'orderObj':orderObj,'merchantName':merchantobj}
        return render(request,"purchasedprod.html",context)

def trackOrder(request):
    merchantobj = MerchantInfo.objects.get(userid=request.session['merchant'])
    merchantId = merchantobj.aadharno
    orderObj = orderDetail.objects.filter(merchantId=merchantId)
    orderId = request.POST['orderId']
    track = Tracker.objects.filter(orderId=orderId)
    notFound = ''
    if  track.count() ==0:
        track={'orderStatus':'Not Found'}
        print('@@@@@@@@@@@@@@@@@@@')
        notFound = "This is not available for to track"
        print('@@@@@@@@@@@@@@@@@@@')
    # print(track)
    context ={'track':track,'orderObj':orderObj,'notFound':notFound}
    # return HttpResponseRedirect(reverse('merchantapp:purchasedprod',args=(context,)))
    return render(request,"purchasedprod.html",context)

def LikeView(request,id):
    merchantName = MerchantInfo.objects.get(userid=request.session['merchant'])
    merchantid = merchantName.aadharno
    product = FarmerSellProduct.objects.get(id=id)
    liked = False
    if product.likes.filter(aadharno=merchantid).exists():
        product.likes.remove(merchantid)
        liked = False
    else:
        product.likes.add(merchantid)
        like = True
    return redirect(f'/merchantapp/viewProd/{id}')


@csrf_exempt
def handlerequest(request):
    # Paytm will send you a POST request
    form = request.POST
    response_dict = {}
    checksum = None  # Initialize checksum variable
    
    # Populate response_dict and find checksum from form data
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]  # Assign value to checksum if it exists

    # Define your key and iv
    key = "your_32_byte_key"  # Replace with your actual merchant key (32 bytes for AES-256)
    iv = "your_16_byte_iv"    # Replace with the initialization vector used for encryption (16 bytes)
    
    # If checksum is not present in form data, define a static demo checksum for debugging
    demo_checksum = "YOUR_STATIC_CHECKSUM_VALUE"  # Use a valid checksum for testing
    if checksum is None:
        checksum = demo_checksum

    # Verify the checksum
    verify_result = Checksum.verifySignature(response_dict, checksum, iv)
    
    if verify_result:
        if response_dict['RESPCODE'] == '01':
            print('Order successful')
            pro_id = response_dict['ORDERID']
            soldprdid = orderDetail.objects.get(id=pro_id)
            soldProduct = FarmerSellProduct.objects.get(id=soldprdid.productid)
            soldProduct.delete()
        else:
            print('Order was not successful: ' + response_dict['RESPMSG'])
    else:
        print('Checksum verification failed!')

    return render(request, 'paymentstatus.html', {'response': response_dict})
