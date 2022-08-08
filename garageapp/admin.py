from django.contrib import admin
from .models import(Article, DemandedRepairs, Demands, Labour, LabourDetails, LabourMaster, Parts, PartsBatch, PartsDetails, PartsMaster,ServiceType, Stock, 
Vehicle,Customer,JobCard,Color,
 Vehiclemodel, Vehiclevariant,Employee,PartsBatch)
# Register your models here.


admin.site.register(JobCard)
admin.site.register(Vehicle)
admin.site.register(Customer)
admin.site.register(Color)
admin.site.register(Vehiclevariant)
admin.site.register(Vehiclemodel)
admin.site.register(ServiceType)
admin.site.register(Employee)
admin.site.register(Article)
admin.site.register(Demands)
admin.site.register(DemandedRepairs)
admin.site.register(Parts)
admin.site.register(PartsMaster)
admin.site.register(PartsDetails)
admin.site.register(Stock)
admin.site.register(Labour)
admin.site.register(LabourDetails)
admin.site.register(LabourMaster)
admin.site.register(PartsBatch)