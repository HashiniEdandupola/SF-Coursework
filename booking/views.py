from django.shortcuts import render
from .forms import BookingForm
from .models import Booking_detail
from django.shortcuts import redirect, render

# Create your views here.
def booking_success(request):
    booking_info = Booking_detail.objects.last()
    context ={
        'last_detail':booking_info 
    }
    return render(request, 'booking/booking_success.html',context)

# CRUD
def booking_list(request):
    bookings = Booking_detail.objects.all()
    # users_count = users.count()
    context = {
        'booking_list':bookings,
    }
    return render(request,'booking/booking_list.html',context)

def booking_form(request, id=0):
    if request.method == "GET":
        single_room = 5
        single_room_book_count = Booking_detail.objects.filter(room ="single").count()
        remaining_single_room = single_room - single_room_book_count

        double_room = 5
        double_room_book_count = Booking_detail.objects.filter(room ="double").count()
        remaining_double_room = double_room - double_room_book_count

        king_room = 5
        king_room_book_count = Booking_detail.objects.filter(room ="king").count()
        remaining_king_room = king_room - king_room_book_count
        
        if id==0:
            form = BookingForm()
        else:
            booking = Booking_detail.objects.get(pk=id)
            form = BookingForm(instance=booking)
        context = {
            'remain_single': remaining_single_room,
            'remain_double': remaining_double_room,
            'remain_king': remaining_king_room,
            'form':form
        }
        return render(request, 'booking/booking_form.html',context)
    else:
        if id==0:
            form = BookingForm(request.POST)
        else:
            booking = Booking_detail.objects.get(pk=id)
            form = BookingForm(request.POST,instance=booking)
        if form.is_valid():
            form.save()
        return redirect('/booking/success')

def booking_delete(request,id):
    booking = Booking_detail.objects.get(pk=id)
    booking.delete()
    return redirect('/booking/list')