from django.contrib import admin
from django.contrib import messages

from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'id', 'total_cost', 'created_at', 'is_returned', 'request_to_return')
    list_filter = ('is_returned', 'created_at', 'request_to_return')
    search_fields = ('user__username', 'id')

    actions = ['process_return_request']

    def process_return_request(self, request, queryset):
        for order in queryset:
            if order.request_to_return and not order.is_returned:
                order.return_order()
                messages.success(request, f"Order {order.id} has been returned.")
            else:
                messages.warning(request, f"Order {order.id} doesn't have a return request or has already been returned.")

    process_return_request.short_description = "Process return request"

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
