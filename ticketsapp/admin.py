from django.contrib import admin

# Register your models here.
from .models import Ticket, Project

admin.site.register(Ticket)
admin.site.register(Project)
