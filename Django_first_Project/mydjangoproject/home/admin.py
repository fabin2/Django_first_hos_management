from django.contrib import admin

from .models import Departments, Doctors, Booking  # F .model here its  current folder, Departments is the model we have created 

# Register your models here.
admin.site.register(Departments)    # F registering the (Departments)
admin.site.register(Doctors)        # registering the doctors and this model(table) will be available in admin panel

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date', 'booked_on')

admin.site.register(Booking, BookingAdmin) 