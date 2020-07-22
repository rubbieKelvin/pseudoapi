from django.contrib import admin

from .models import Dev, Project, Route, Variable

# Register your models here.
admin.site.register(Dev)
admin.site.register(Project)
admin.site.register(Route)
admin.site.register(Variable)