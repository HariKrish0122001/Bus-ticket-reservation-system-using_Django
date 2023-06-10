from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import UserProfile
from datetime import date
from app.models import Bus_details,Book
from datetime import date

# Create your views here.
#admin loginpage

def admin_login(request):
    if request.method=="GET":
        print("Admin page")
        return render(request,'admin_login.html')
    else:
        mailid=request.POST.get('mail')
        password=request.POST.get('pass')
        username = User.objects.get(email=mailid).username
        print(username)
        user_obj=User.objects.filter(username=username)
        print(user_obj)
        print("SAY HELLO")
        if not user_obj.exists():
            messages.error(request,"Account not found")
            return redirect('admin_login')
        print("HELLO")
        user = authenticate(request, username=username, password=password)
        print(user,"After authentication")
        try:
            if user.is_superuser:
                print("sueruser")
                login(request, user)
                messages.success(request, "Login Success")
                print("LOGIN SUCCESS")
                return redirect('dashboard')
        except:
            print("not a super user")
            messages.error(request, "Invalid Login credentials")
            print("LOGIN FAILED")
            return redirect('admin_login')

def admin_signin(request):
    if request.method=="GET":
        return render(request, 'admin_sign_up.html')

    else:
        User = get_user_model()
        username=request.POST.get("name")
        mail=request.POST.get('email')
        password=request.POST.get('pass')
        repassword=request.POST.get('repass')
        if User.objects.filter(is_superuser=True,email=mail).exists():
            print("Check",User.objects.filter(is_superuser=True,email=mail).exists())
            messages.error(request, 'Mail id already exists')
            return redirect('sign_in')
        else:
            try:
                user=User.objects.create_superuser(username,mail,password)
                print("SIGN SUCCESS")
                messages.success(request, "Admin created successfully")
                return redirect("admin_login")
            except IntegrityError:
                messages.error(request, "Organisation already exists.")
                return redirect('sign_in')
            except ValidationError as e:
                messages.error(request, e)
                print("Name already exists")
                return redirect('sign_in')

#dashboard
@login_required(login_url='/')
def dashboard(request):
    return render(request,"dashboard.html")

#bus details
@login_required(login_url='/')
def busdetails(request):
    if request.method=='GET':
        today=date.today()
        admin_id=request.user.id
        bus=Bus_details.objects.filter(admin_id=admin_id)
        for i in bus:
            if i.date == today:
                i.bus_status = "Running"
                i.save()
            elif i.date < today:
                i.bus_status = "Completed"
                i.save()
        print("dbkjbggls",bus)
        return render(request,'busdetails.html',{'data':bus})

#userdetails
@login_required(login_url='/')
def customerdetails(request):
    if request.method=='GET':
        travels=request.user.username
        print(travels)
        cust=Book.objects.filter(travels_name=travels)
        for i in cust:
            if not Bus_details.objects.filter(id=i.bus_id).exists():
                Book.objects.filter(bus_id=i.bus_id).update(status="Bus cancelled,amount will be refunded",seat_number=0)
        return render(request,"userdetails.html",{'data':cust})

#addbus
@login_required(login_url='/')
def addbus(request):
    if request.method=="GET":
        return render(request,"addbus.html")
    else:
        id__=request.user.id
        travels_name=request.user.username
        print("User_id",id__)
        busname=request.POST.get('busname')
        if busname=='1':
            bus_type="AC -Sleeper"
        elif busname=='2':
            bus_type="Deluxe"
        elif busname == '3':
            bus_type = "NON - AC Sleeper"
        #elif busname == '4':
          #  bus_type = "AC Sleeper"
        elif busname == '5':
            bus_type = "NON - AC"
        from_=request.POST.get('from')
        to_=request.POST.get('to')
        #total_seats=request.POST.get("total_seats")
       # remain=request.POST.get("remain")
        cost=request.POST.get('cost')
        date=request.POST.get('date')
        time=request.POST.get('time')
        bus=Bus_details.objects.create(bus_type=bus_type,start_location=from_,travels_name=travels_name,admin_id=id__,destination=to_,price=cost,date=date,time=time)
        print("Bus ID",bus.id)
        messages.success(request,"Bus Created Successfully")
        return redirect('dashboard')

@login_required(login_url='/')
def cancelbus(request):
    if request.method=="GET":
        ad_id=request.user.id
        today=date.today()
        bus=Bus_details.objects.filter(admin_id=ad_id)

        return render(request,'cancelbus.html',{'data':bus})
    else:
        ids = request.POST.getlist('ids[]')
        print(ids)
        try:
            for bus_id in ids:
                bus_id=int(bus_id)
                print("bus_id",bus_id)
                obj = Bus_details.objects.get(id=bus_id)
                print(obj)
                obj.delete()
            else:
                messages.success(request,"Bus Cancelled Successfully")
                return redirect('cancelbus')
        except:
            messages.error(request,"Bus can't be cancelled")
            return redirect('cancelbus')


def log_out(request):
    print("Logout phase ")
    logout(request)
    print("LOGOUT success")
    return redirect('/')
























