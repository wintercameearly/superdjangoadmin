import threading
from django.contrib import admin, messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.translation import ngettext
from django.core.mail import send_mail, send_mass_mail, BadHeaderError, EmailMessage


class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)
        UserAdmin.list_display = list(UserAdmin.list_display) + ['date_joined', 'is_active']

    list_filter = ("date_joined",)
    change_list_template = 'admin/auth/users_change_list.html'
    actions = ['set_as_active', 'set_as_inactive']
    search_fields = ['username', 'email']

    list_editable = ('email',)

    def set_as_active(self, request, queryset):
        updated = queryset.update(is_active="True")
        self.message_user(request, ngettext(
            '%d User was successfully activated',
            '%d Users were successfully activated',
            updated,
        ) % updated, messages.SUCCESS)

    def set_as_inactive(self, request, queryset):
        updated = queryset.update(is_active="False")
        self.message_user(request, ngettext(
            '%d User was successfully de-activated',
            '%d Users were successfully de-activated',
            updated,
        ) % updated, messages.SUCCESS)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('send_email/', self.send_email, name="send_email"),
        ]
        return my_urls + urls

    def send_email(self, request):
        if request.user.is_staff or request.user.is_superuser:
            if request.method == 'GET':
                user = request.user
                context = dict(
                    user= user
                )
                return TemplateResponse(request, "send_email.html", context)
            elif request.method == 'POST':
                subject = request.POST.get("subject")
                message = request.POST.get('message')
                list_email_user = [p.email for p in User.objects.all()]
                email = (subject, message, 'admin@gmail.com', list_email_user)
                send_mass_mail((email,), fail_silently=False)
                self.message_user(request,'Email sent successfully')
                return redirect('/admin/auth/user')
        else:
            return redirect("/admin")


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.site_header = "Internship Dashboard"
admin.site.site_title = "Dashboard"
admin.site.index_title = "Admin for Internship Test "
