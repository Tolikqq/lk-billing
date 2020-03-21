from django.contrib import admin
from .models import Feedback

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'datetime', 'text')
    list_filter = ('author', )

# Register the admin class with the associated model
admin.site.register(Feedback, AuthorAdmin)
