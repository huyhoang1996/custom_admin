from django.contrib import admin
from django.shortcuts import render
from models import Notification, UserIntermediate
from django.conf.urls import url
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Register your models here.

# class UserProfileInline(admin.StackedInline):
#     model = Notification.users.through
#     filter_horizontal = ('user',)

# class UserInline(admin.TabularInline):
#     model = Notification.users.through

class UserIntermediateAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserIntermediate, UserIntermediateAdmin)


class NotificationAdmin(admin.ModelAdmin):
    # inlines = [
    #     UserInline,
    # ]
    # exclude = ('users',)
    # inlines = [UserProfileInline]
    filter_horizontal = ('users',)

    list_display = (
        'id',
        'name',
        'account_actions', 
    )

    def get_urls(self):
        print "### GET URLS "
        urls = super(NotificationAdmin, self).get_urls()
        custom_urls = [
            url(
                r'^(?P<notification_id>.+)/push/$',
                self.admin_site.admin_view(self.process_push_notification),
                name='notification-push-to-users',
            ),
            url(
                r'^(?P<notification_id>.+)/clear/$',
                self.admin_site.admin_view(self.process_clear_notification),
                name='notification-clear',
            ),
        ]
        return custom_urls + urls

    def account_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Push</a>&nbsp;'
            '<a class="button" href="{}">Clear</a>',
            reverse('admin:notification-push-to-users', args=[obj.pk]),
            reverse('admin:notification-clear', args=[obj.pk]),
        )
    account_actions.short_description = 'Notification Actions'
    account_actions.allow_tags = True

    def process_push_notification(self, request, notification_id, *args, **kwargs):
        print "### notification_id ",notification_id
        self.message_user(request, "Push notification successfully.")
        return super(NotificationAdmin,self).changelist_view(request)

        # return super(NotificationAdmin, self)
        # return self.process_action(
        #     request=request,
        #     account_id=account_id,
        #     action_form=DepositForm,
        #     action_title='Deposit',
        # )

    def process_clear_notification(self, request, notification_id, *args, **kwargs):
        self.message_user(request, "Clear notification successfully.")
        # return self.process_action(
        #     request=request,
        #     account_id=account_id,
        #     action_form=WithdrawForm,
        #     action_title='Withdraw',
        # )

    class Media:
        js = ('/static/admin/js/jquery-3.2.1.min.js', '/static/admin/js/notification_hide_attribute.js',)

    
admin.site.register(Notification, NotificationAdmin)