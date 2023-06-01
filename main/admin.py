from django.contrib import admin
from .models import HotelBuilding, Position, Staff, Client, TypeService, Service, Room, EntryCustomer, \
    DenyRoom, DepartureCustomer


MODEL_CLASSES = (HotelBuilding, Position, Staff, Client, TypeService, Service, Room, EntryCustomer,
                 DenyRoom, DepartureCustomer)

for model in MODEL_CLASSES:
    admin.site.register(model)


