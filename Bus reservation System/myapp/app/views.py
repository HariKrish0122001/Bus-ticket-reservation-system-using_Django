from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus_details, User_Details, Book
from django.http import JsonResponse
import json


# Create your views here.

def index(request):
    key = Bus_details.objects.all()
    return render(request, 'user.html', {'data': key})


def book(request):
    if request.method == 'POST':

        id_r = int(request.POST.get('bus_id'))
        seats_r = int(request.POST.get('no_seats'))
        for i in range(1,seats_r+1):
            name = request.POST.get('name_' + str(i))
            age=int(request.POST.get('age_' + str(i)))
            gender=request.POST.get('gender_' + str(i))
            print(f'name --{name}--age--- {age}---gender {gender}')
        print("method call------------")

        bus = Bus_details.objects.get(id=id_r)
        user = User_Details.objects.get(id=1)###Hard-coded
        if bus:
            print("Bus exists")
            if bus.rem != '0':
                for i in range(1, seats_r + 1):
                    name = request.POST.get('name_' + str(i))
                    age = int(request.POST.get('age_' + str(i)))
                    gender = request.POST.get('gender_' + str(i))
                    print(f'name --{name}--age--- {age}---gender {gender}')
                    busname = bus.bus_name
                    cost = bus.price
                    src = bus.start_location
                    dest_r = bus.destination

                    time_r = bus.time
                    date_r = bus.date

                    user__id = 1
                    user_mail = user.mailid
                    user_name = user.name
                    rem_r = bus.rem - seats_r

                # existing_bookings = Book.objects.filter(id=id_r)
                    existing_bookings = Book.objects.filter(bus_id=id_r)

                # Generate a list of already-occupied seat numbers
                    occupied_seats = [booking.seat_number for booking in existing_bookings]

                    booking_ids = []
                    seats_numbers=[]

                    for i in range(seats_r):
                        seat_number = i + 1
                        while seat_number in occupied_seats:
                            seat_number += 1
                        occupied_seats.append(seat_number)
                        seats_numbers.append(seat_number)

                        book = Book.objects.create(name=user_name, bus_name=busname, mailid=user_mail, user_id=user__id,
                                                   source=src,pass_name=name,pass_age=age,pass_gender=gender,
                                                   dest=dest_r, price=cost, bus_id=id_r, date=date_r, time=time_r,
                                                    status='Booked', seat_number=seat_number)
                        print("BOOKING ID", book.id)
                        booking_ids.append(book.id)
                    Bus_details.objects.filter(id=id_r).update(rem=rem_r)
                    response_data = render(request, 'user.html')
                    # Return a JSON response with the booking IDs
                    total_cost=seats_r*bus.price
                    return render(request, 'myapp/bookings.html', locals())
                    return JsonResponse({'message': 'Data received successfully.', 'booking_ids': booking_ids,'seat_no':seats_numbers,'total_cost':total_cost})

                # Return a JSON response indicating an error
            return HttpResponse('Invalid request.')
            # return JsonResponse({'message': 'Data received successfully.', 'booking_ids': booking_ids})

            # return response_data

#                  return render(request,'user.html')
