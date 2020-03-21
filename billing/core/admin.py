from django.contrib import admin

from .models import Balance, Order, Configurations

# admin.site.register(Balance)
# admin.site.register(Order)
# admin.site.register(Configurations)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'datetime', 'configuration', 'countuser', 'amount')
    list_filter = ('configuration', )

# Register the admin class with the associated model
admin.site.register(Order, AuthorAdmin)


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'datetime')
    list_filter = ('user', )

@admin.register(Configurations) 
class ConfigurationsAdmin(admin.ModelAdmin):
	list_display = ('name', 'tarif')
