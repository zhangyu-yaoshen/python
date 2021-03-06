
# Register your models here.
from django.contrib import admin

from asset import models


from asset import core







# class ServerInline(admin.TabularInline):
#     model = models.Server
#     exclude = ('memo',)
#     #readonly_fields = ['create_date']
#
# class CPUInline(admin.TabularInline):
#     model = models.CPU
#     exclude = ('memo',)
#     readonly_fields = ['create_date']
#
# class NICInline(admin.TabularInline):
#     model = models.NIC
#     exclude = ('memo',)
#     readonly_fields = ['create_date']
#
# class RAMInline(admin.TabularInline):
#     model = models.RAM
#     exclude = ('memo',)
#     readonly_fields = ['create_date']
#
# class DiskInline(admin.TabularInline):
#     model = models.Disk
#     exclude = ('memo',)
#     readonly_fields = ['create_date']
#
#
# class NicAdmin(admin.ModelAdmin):
#     list_display = ('name','macaddress','ipaddress','netmask','bonding')
#     search_fields = ('macaddress','ipaddress')
#



class AssetApprovalAdmin(admin.ModelAdmin):
    list_display = ('sn','asset_type','manufactory','model','cpu_model','os_type','os_release','approved')

    list_filter = ('asset_type','os_type')
    search_fields = ('sn','os_type')
    list_editable = ('asset_type','approved')

    actions = ['asset_approval',]
    def asset_approval(self,request,querysets):
        print("--------asset approval.....",self,request,querysets)

        for obj in querysets:
            asset_handler = core.Asset(request)
            if asset_handler.data_is_valid_without_id(obj):
                asset_handler.data_inject() #注射
                obj.approved = True

                obj.save()
                print(asset_handler.response)

    asset_approval.short_description = "新资产审批"



# Now register the new UserAdmin...
admin.site.register(models.UserProfile)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)



admin.site.register(models.Asset)
admin.site.register(models.Server)
admin.site.register(models.NetworkDevice)
admin.site.register(models.IDC)
admin.site.register(models.BusinessUnit)
admin.site.register(models.Contract)
admin.site.register(models.CPU)
admin.site.register(models.Disk)
admin.site.register(models.NIC)
admin.site.register(models.RAM)
admin.site.register(models.Manufactory)
admin.site.register(models.Tag)
admin.site.register(models.Software)
admin.site.register(models.EventLog)
admin.site.register(models.NewAssetApprovalZone,AssetApprovalAdmin)
