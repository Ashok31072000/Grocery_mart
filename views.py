from django.shortcuts import render
from webapp.models import user

# Create your views here.
def main(request):
    return render(request, 'main.html')
def home(request):
    return render(request,'home.html')
def features(request):
    return render(request,'features.html')
def products(request):
    return render(request,'products.html')
def categories(request):
    return render(request,'categories.html')
def reviews(request):
    return render(request,'reviews.html')
def blogs(request):
    return render(request,'blogs.html')
def signup(request):
    msg=""
    if (request.method == "POST"):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        psw = request.POST.get("psw")
        phonenum = request.POST.get("phonenum")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        h_no = request.POST.get("h_no")
        street = request.POST.get("street")
        pincode = request.POST.get("pincode")
        district = request.POST.get("district")
        state = request.POST.get("state")
        country = request.POST.get("country")
        data=user.objects.all()
        print ("Create New User")
        flag=True
        for x in data:
            if(x.email==email or x.psw==psw):
                msg="email/password already exists"
                flag=False
                break
        if (flag and email!="Admin123@Gmail.Com") :
            obj = user(fname=fname, lname=lname, email=email, psw=psw, phonenum=phonenum,
                              dob=dob,gender=gender,h_no=h_no,street=street,pincode=pincode,district=district,
                                state=state,country=country)
            obj.save()
            msg="User Registered Success"
        else:
            msg="Username already exists"

        print("Message : ", msg)
    return render(request, 'signup.html', {'msg':msg})



        # ORM => Object Relational Mapping
    #     obj = user(fname=fname,lname=lname,email=email,psw=psw,phonenum=phonenum,
    #                dob=dob,gender=gender,h_no=h_no,street=street,pincode=pincode,district=district,
    #                state=state,country=country)
    #     # Save the changes in the table
    #     obj.save()

def login(request):
    msg=''
    data=[]
    if(request.method=="POST"):
        email=request.POST.get('email')
        psw=request.POST.get('psw')
        if(email=="Admin123@Gmail.Com" and psw=="Admin"):
            data = user.objects.all()
            return render(request,"admin.html",{'msg':msg,'data':data})
        else:
            data=user.objects.all()
            flag=False
            for x in data:
                if(x.email==email and x.psw==psw):
                    request.session['userid']=x.id
                    flag=True
                    break
            if(flag):
                if (flag):
                        return render(request, "home.html")
                else:
                         msg="invalid email and password"
    return render(request, "login.html", {'msg': msg})

        # data=user.objects.all()
        # flag=False
        # for x in data:
        #     if x.email == email and x.psw ==pwd:
        #         request.session['userid'] = x.id
        #         flag=True
        #         break
        #
        # if(flag):
        #     return render(request, "home.html")
        # else:
        #     msg="invalid email and password"
    # return render(request,"login.html",{'msg':msg})
def display(request):
    data=user.objects.all()
    print("Data : ",data)
    return render(request,"admin.html",{'data':data})