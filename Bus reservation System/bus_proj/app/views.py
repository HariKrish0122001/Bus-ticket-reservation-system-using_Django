from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core import serializers
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Bus_details, User_Details, Book
from django.http import JsonResponse
from django.http import HttpResponse
import json
from datetime import date


# Create your views here.

##loginpage
def loginpage(request):
    if request.method=="POST":
        mail = request.POST.get('mail')
        password = request.POST.get('pass')
        print(mail)
        username = User.objects.get(email=mail).username
        user = authenticate(request, username=username, password=password)
        print(user)
        try:
            if not user.is_superuser:
                login(request, user)
                messages.success(request, "Login Success")
                print("LOGIN SUCCESS")
                return redirect('home')
        except:
            messages.error(request, "Invalid Login credentials")
            print("LOGIN FAILED")
            return redirect('/')
    else:
        return render(request, 'login.html')

#signinpage
def signin(request):
    if request.method =='POST':
        print("hell in a cell")
        name = request.POST.get('name')
        mail = request.POST.get('email')
        passwrd = request.POST.get('pass')
        repass = request.POST.get('repass')
        print("sign up here")
        if User.objects.filter(email=mail).exists():

            messages.error(request, 'Mail id already exists')
            return redirect('sign_up')
        elif passwrd!=repass:
            messages.error(request, "Password doesn't match")
            return redirect('sign_up')
        else:
            try:
                validate_password(passwrd)
                print("validated password",validate_password(passwrd))
                try:
                    user=User.objects.create_user(name,mail,passwrd)
                    print("SIGN SUCCESS")
                    return redirect("/")
                except IntegrityError:
                    messages.error(request, "Username already exists.")
                    return redirect('sign_up')
                except ValidationError as e:
                    messages.error(request, e)
                    print("Name already exists")
                    return redirect('sign_up')

            except ValidationError as e :
                messages.error(request, e)
                print("SIGN Fail")
                return redirect('sign_up')
    else:
        return render(request, 'sign_up.html')

#homepage
@login_required(login_url='/')
def home(request):
    if request.method=="GET":
        src = Bus_details.objects.values('start_location')
        dest = Bus_details.objects.values('destination')
        start = []
        for i in src:
            start.append(i['start_location'])
        destin = []
        for i in dest:
            destin.append(i['destination'])
        destin = set(destin)
        start = set(start)
        start = list(start)
        destin = list(destin)
        return render(request, 'home.html', {'source': start, 'dest': destin})



#bookingpage
@login_required(login_url='/')
def bookingpage(request):
    context={}

    if request.method =="POST":
        user_id=request.user.id
        print(user_id)
        src=request.POST.get('source')
        dest=request.POST.get('destination')
        date=request.POST.get('date')
        key=Bus_details.objects.filter(start_location=src,destination=dest,date=date)
        if key.exists():
            return render(request,"book.html",{'data':key})
        elif src==dest:
            messages.error(request, "Source and Destination can't be same")
            return redirect('home')

        else:
            print("Doesn't exist")
            messages.error(request,'No bus available')
            return redirect('home')

#cancellation page
@login_required(login_url='/')
def cancellation(request):
  #  user_id = request.user
    user_id=request.user.id
    book = Book.objects.filter(user_id=user_id)
    return render(request, 'cancellation.html', {'data': book})

##mybooking

#@login_required(login_url='/')
#def mybookings(request):
#    user_id = request.user.id
 #   book = Book.objects.filter(user_id=user_id)

  #  return render(request, 'mybookings.html', {'data': book})

@login_required(login_url='/')
def seat_selection(request,id=None):
    if id!=None:
            existing_seats = Book.objects.filter(bus_id=id)
            seats=[]
            gender=[]
            d=[]
            for i in existing_seats:
                if i.seat_number!=0:
                    seats.append(i.seat_number)
                    gender.append((i.pass_gender))
                    d.append({"seat_number":i.seat_number,"gender":i.pass_gender})
            for i in d:
                print(i)
            info={"seats":seats,'gender':gender}
            context = {
                'info':info,
                'existing_seats': seats,
                "gender":gender,
                'bus_id':id
            }
            print("seats booked",seats)
            print("Request ethod", request.method)
            return render(request, 'seat.html',context)
    else:
            user_id=request.user.id
            print(user_id)
            print("Request method",request.method)
            bus_id = request.POST.get('bus_id')
            seat_numbers = request.POST.getlist('seat_numbers[]')
            name = request.POST.getlist('name[]')
            age = request.POST.getlist('age[]')
            gender = request.POST.getlist('gender[]')
            print("Updated ",bus_id)
            print("selected seats", seat_numbers)
            print("Pass_names", name)
            print("pass_age", age)
            print("pass_gender", gender)
            try:
                bus = Bus_details.objects.get(id=bus_id)
                user = User.objects.get(id=user_id)  ###Hard-coded
                if bus:
                    print("Bus exists")
                    if bus.rem >= len(seat_numbers):
                        travelsname = bus.travels_name
                        bustype = bus.bus_type
                        cost = bus.price
                        src = bus.start_location
                        dest_r = bus.destination

                        time_r = bus.time
                        date_r = bus.date

                        user_mail = user.email
                        user_name = user.username
                        rem_r = bus.rem - len(seat_numbers)

                        # existing_bookings = Book.objects.filter(id=id_r)
                        existing_bookings = Book.objects.filter(bus_id=bus_id)

                        # Generate a list of already-occupied seat numbers
                        occupied_seats = [booking.seat_number for booking in existing_bookings]

                        booking_ids = []
                        seats_numbers = []

                        for i in range(len(seat_numbers)):
                            occupied_seats.append(seat_numbers[i])
                            seats_numbers.append(seat_numbers[i])
                            print(f'Database name-- {name[i]} {age[i]}  {gender[i]}')

                            book = Book.objects.create(name=user_name, bus_type=bustype, mailid=user_mail,
                                                        user_id=user_id,
                                                        source=src, pass_name=name[i], pass_age=age[i],
                                                        pass_gender=gender[i],
                                                dest=dest_r, price=cost, bus_id=bus_id, date=date_r, time=time_r,
                                                status='Booked', seat_number=seat_numbers[i],
                                                travels_name=travelsname)
                            print("BOOKING ID", book.id)
                            booking_ids.append(book.id)
                        Bus_details.objects.filter(id=bus_id).update(rem=rem_r)
                        locals_dict ={'bus_id':bus_id,'busName':travelsname}
                        print(locals_dict)
                        response_data = json.dumps(locals_dict)

                        # Return JSON response with correct mimetype
                        return HttpResponse(response_data, content_type='application/json')

            except:
                print("exception")
                messages.error(request, 'No bus exists with ID ')
                locals_dict = {k: v for k, v in locals().items() if k != 'request'}
                print(locals_dict)
                response_data = json.dumps(locals_dict)
                # Return JSON response with correct mimetype
                return HttpResponse(response_data, content_type='application/json')

@login_required(login_url='/')
def confirm(request,id=None):
    if id!=None:
        splt=id.split(',')
        bus_id=splt[0]
        seat_numbers=splt[1:]
        book=Book.objects.filter(bus_id=bus_id,seat_number__in=seat_numbers)
        print(book)
        pass_names=[]
        pass_gender=[]
        price=0
        book_id=""
        for i in book:
            pass_names.append(i.pass_name)
            book_id+=str(i.id)+" "
            pass_gender.append(i.pass_gender)
            price=+i.price
            src=i.source
            dest=i.dest
            status=i.trip_status
            date=i.date
            time=i.time
            travels=i.travels_name
        print(book_id)
        print()


        #books={"travels":travels,'price':price,"pass_bus":pass_bus,'pass_names':pass_names,'pass_gender':pass_gender,'time':time,'status':status,'seats':seats,'src':src,'dest':dest}
        context={'book':book}
        return render(request,'bookings.html',locals())
    else:
        print("POST method")
        return render(request,'bookings.html')

##booking phase
@login_required(login_url='/')
def book(request):
    if request.method=="GET":#GET METHOD
        user_id = request.user.id
        print("User Id get method",user_id)
        today=date.today()
        print(today)
        book = Book.objects.filter(user_id=user_id)
        for i in book:
            print(i.date)
            if i.status!='Booked':
                i.trip_status="Trip Cancelled"
                i.save()
            elif i.date==today:
                i.trip_status = "On Process"
                i.save()
            elif i.date < today:
                i.trip_status = "Completed"
                i.save()

        return render(request, 'mybookings.html', {'data': book})

## cancellation phase
@login_required(login_url='/')
def cancel(request):
    context={}
    if request.method=='POST':
        to_date = date.today()
        print(to_date)
        try:
            book_id=request.POST.getlist('ids[]')
            print(book_id)
            if len(book_id)==0:
                messages.error(request,"Kindly click the checkbox to cancel")
                return redirect("cancellation")
            user_id=request.user.id
            try:
                for id_ in book_id:
                    id_ = int(id_)
                    print("BOOK ID", id_)
                    obj = Book.objects.get(id=id_)
                    print("getting obj",obj)
                    print("bus_id",obj.bus_id)
                    bus = Bus_details.objects.get(id=obj.bus_id)
                    print("getting bus obj",bus)
                    bus_date = bus.date
                    print("details----", obj)
                    print("ticket status", obj.status)
                    if to_date > bus_date:
                        messages.error(request, "You can't cancel the bus that already started its Trip ")
                        return redirect('cancellation')

                    else:
                        print("##check", bus_date)
                        rem_r = (bus.rem) + 1
                        Book.objects.filter(id=id_).update(status='CANCELLED', seat_number=0,trip_status="Cancel")
                        Bus_details.objects.filter(id=obj.bus_id).update(rem=rem_r)
                        print(obj)
                messages.success(request, "Your Ticket Cancelled successfully")
                return redirect('cancellation')

            except:
                print("exception phase ")
                messages.error(request, "Invalid Booking Id")
                return redirect('cancellation')
        except:
            print("exception phase ")
            messages.error(request, "Invalid Booking Id")
            return redirect('cancellation')


def log_out(request):
    print("Logout phase ")
    logout(request)
    print("LOGOUT success")
    return redirect('/')
