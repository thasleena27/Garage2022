from tabnanny import verbose
from django.db import models
class Article(models.Model):
    articleid=models.IntegerField(primary_key=True,auto_created=True)
    articletitle=models.CharField(verbose_name="title",max_length=50)
    articlepubdate=models.DateTimeField(verbose_name="pub date")

class Practice(models.Model):
    itemid=models.IntegerField(primary_key=True,auto_created=True)
    itemcode=models.CharField(verbose_name="Code",max_length=50)
    itemdescription=models.CharField(verbose_name="Description",max_length=50)
    
# Create your models here.
class JobCard(models.Model):
    jobcardid=models.IntegerField(primary_key=True,auto_created=True)
    jobcardno=models.IntegerField(verbose_name="JobCard Number")
    datetime=models.DateTimeField(verbose_name="Date & Time")
    checkindatetime=models.DateTimeField(verbose_name="Check In Date & Time")
    isactive=models.BooleanField(default=False)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")
    def __str__(self):
        return str(self.jobcardno)

class Vehicle(models.Model):
    wash_choices=(
        ('Select','Select'),
        ('Wash','Wash'),
        ('No wash','No wash'),
    )
    vehicleid=models.IntegerField(primary_key=True,auto_created=True)
    regno=models.CharField(verbose_name="Reg No",max_length=50)
    omr=models.CharField(verbose_name="OMR",max_length=50)
    servicetype=models.CharField(verbose_name="Service Type",max_length=50)
    washtype=models.CharField(verbose_name="Wash Type",max_length=50,choices=wash_choices)
    service_advisor=models.CharField(verbose_name="Service Advisor",max_length=50)
    technician=models.CharField(verbose_name="Technician",max_length=50)
    technical_advisor=models.CharField(verbose_name="Technical Advisor",max_length=50)
    vehiclemodel=models.CharField(verbose_name="Vehicle Model",max_length=50)
    chasisno=models.IntegerField(verbose_name="Chasis No")
    vehiclevariant=models.CharField(verbose_name="Vehicle Variant",max_length=50)
    color=models.CharField(verbose_name="Color",max_length=50)
    jobcardobj=models.ForeignKey(JobCard,verbose_name="JobCard",on_delete=models.PROTECT,null=True,blank=True)
    isactive=models.BooleanField(default=False)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")

class Customer(models.Model):
    customerid=models.IntegerField(primary_key=True,auto_created=True)
    customername=models.CharField(verbose_name="Name",max_length=50)
    customeraddress=models.CharField(verbose_name="Address",max_length=50)
    city=models.CharField(verbose_name="City",max_length=50)
    state=models.CharField(verbose_name="State",max_length=50)
    email=models.CharField(verbose_name="Email",max_length=50)
    phone=models.CharField(verbose_name="Phone",max_length=50)
    mobile=models.CharField(verbose_name="Mobile",max_length=50)
    gstin=models.CharField(verbose_name="GSTIN",max_length=50)
    pan=models.CharField(verbose_name="PAN",max_length=50)
    outstanding_amt=models.IntegerField(verbose_name="Outstanding Amount")
    jobcardobj=models.ForeignKey(JobCard,verbose_name="JobCard",on_delete=models.PROTECT,null=True,blank=True)
    isactive=models.BooleanField(default=True)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")

class Color(models.Model):
    colorid=models.IntegerField(primary_key=True,auto_created=True)
    colorcode=models.CharField(verbose_name="Color Code",max_length=50)
    colorname=models.CharField(verbose_name="Color Name",max_length=50)
    def __str__(self):
        return self.colorname

class Vehiclevariant(models.Model):
    variantid=models.IntegerField(primary_key=True,auto_created=True)
    variantcode=models.CharField(verbose_name="Vehicle Variant",max_length=50)
    variantname=models.CharField(verbose_name="Variant Name",max_length=50)
    def __str__(self):
        return self.variantname

class Vehiclemodel(models.Model):
    modelid=models.IntegerField(primary_key=True,auto_created=True)
    vehiclemodel=models.CharField(verbose_name="Vehicle Model",max_length=50)
    modelname=models.CharField(verbose_name="VehicleModelName",max_length=50)
    def __str__(self):
        return self.modelname

class ServiceType(models.Model):
    servicetypeid=models.IntegerField(primary_key=True,auto_created=True)
    servicetype=models.CharField(verbose_name="Service Type",max_length=50)
    servicename=models.CharField(verbose_name="Service Name",max_length=50)
    def __str__(self):
        return self.servicename

        
class Employee(models.Model):
    gender_choices=(
        ('female','female'),
        ('male','male'),
        ('others','others'))
    empid=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(verbose_name="Name",max_length=50)
    age=models.IntegerField(verbose_name="Age")
    gender=models.CharField(verbose_name="Gender",max_length=50,choices=gender_choices)
    phone=models.CharField(verbose_name="Phone",max_length=50)
    email=models.CharField(verbose_name="Email",max_length=50)
    address=models.CharField(verbose_name="Address",max_length=50)
    aadharno=models.IntegerField(verbose_name="Aadhar No")
    isServiceAdvisor=models.BooleanField(verbose_name="IsServiceAdvisor",default=False)
    isTechnician=models.BooleanField(verbose_name="IsTechnician",default=False)
    isTechnicalAdvisor=models.BooleanField(verbose_name="IsTechnicalAdvisor",default=False)
    isactive=models.BooleanField(default=True)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")

class Service(models.Model):
    serviceid=models.IntegerField(primary_key=True,auto_created=True)
    servicename=models.CharField(verbose_name="Service Name",max_length=50)
    servicecost=models.DecimalField(verbose_name="Service Amount",decimal_places=3,max_digits=13)
    isactive=models.BooleanField(default=False)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")
    def __str__(self):
        return self.servicename

class Demands(models.Model):
    demandid=models.IntegerField(primary_key=True,auto_created=True)
    demandcode=models.CharField(verbose_name="Demand Code",max_length=50)
    demand_desc=models.CharField(verbose_name="Demand Description",max_length=50)
    isactive=models.BooleanField(default=True)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")
    def __str__(self):
        return self.demandcode
    

class DemandedRepairs(models.Model):
    demandrepairsid=models.IntegerField(primary_key=True,auto_created=True)
    demandcode=models.ForeignKey(Demands,verbose_name="Demand Code",on_delete=models.PROTECT,null=True,blank=True)
    customerprb=models.CharField(verbose_name="Customer Problem",max_length=50)
    reportedby=models.CharField(verbose_name="Reported By",max_length=50)
    jobcardobj=models.ForeignKey(JobCard,verbose_name="JobCardobj",on_delete=models.PROTECT,null=True,blank=True)
    status=models.CharField(verbose_name="Status",max_length=50,default="In Progress")
    isactive=models.BooleanField(default=True)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")
    
class Parts(models.Model):
    partsid=models.IntegerField(primary_key=True,auto_created=True)
    partscode=models.CharField(verbose_name="Parts Code",max_length=50)
    partsdesc=models.CharField(verbose_name="Parts Description",max_length=50)
    partsbin=models.CharField(verbose_name="Bin",max_length=50)
    batch=models.CharField(verbose_name="Batch",max_length=50,null=True,blank=True,default="")
    isactive=models.BooleanField(default=True)
    reorderlevel=models.IntegerField()
    minqty=models.IntegerField()
    maxqty=models.IntegerField()
    baseunit=models.CharField(verbose_name="Base unit",default="Nos",max_length=5)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")
    def __str__(self):
        return self.partscode

class Stock(models.Model):
    stockid=models.IntegerField(primary_key=True,auto_created=True)
    partsobj=models.ForeignKey(Parts,on_delete=models.CASCADE,null=True,blank=True)
    currentstock=models.IntegerField()
    baseunit=models.CharField(verbose_name="Base unit",default="Nos",max_length=5)
    isactive=models.BooleanField(default=True)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")

class PartsMaster(models.Model):
    partsmasterid=models.IntegerField(primary_key=True,auto_created=True)
    issueno=models.IntegerField(verbose_name="Issue No")
    issuedate=models.DateTimeField(verbose_name="Issue Date")
    regno=models.CharField(verbose_name="Registration No",max_length=50)
    stores=models.CharField(verbose_name="Stores",max_length=50)
    jobcardno=models.ForeignKey(JobCard,verbose_name="JobCard No",on_delete=models.PROTECT,null=True,blank=True)
    partdescription=models.CharField(verbose_name="Part Description",max_length=50,null=True,blank=True)
    splitdescription=models.CharField(verbose_name="Split Description",max_length=50,null=True,blank=True)
    issuereason=models.CharField(verbose_name="Issue Reason",max_length=50,null=True,blank=True)
    cust=models.CharField(verbose_name="CUST",max_length=50,null=True,blank=True)
    ins=models.CharField(verbose_name="INS",max_length=50,null=True,blank=True)
    dlr=models.CharField(verbose_name="DLR",max_length=50,null=True,blank=True)
    oem=models.CharField(verbose_name="OEM",max_length=50,null=True,blank=True)
    isactive=models.BooleanField(default=True)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")

class PartsDetails(models.Model):
    partdetailsid=models.IntegerField(primary_key=True,auto_created=True)
    partno=models.ForeignKey(Parts,verbose_name="PartNo",on_delete=models.PROTECT,null=True,blank=True)
    partsmasterobj=models.ForeignKey(PartsMaster,on_delete=models.PROTECT,null=True,blank=True)
    requestedqty=models.IntegerField(verbose_name="Requested Qty")
    issuedqty=models.IntegerField(verbose_name="Issued Qty")
    storebinlocation=models.CharField(verbose_name="Store Bin Location",max_length=50,null=True,blank=True)
    currentstock=models.IntegerField(verbose_name="Current Stock")
    floatstock=models.IntegerField(verbose_name="Float Stock",null=True,blank=True)
    issuetype=models.CharField(verbose_name="Issue Type",max_length=50,null=True,blank=True)
    issueqty=models.IntegerField(verbose_name="Issue Qty")
    isactive=models.BooleanField(default=True)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")

class Labour(models.Model):
    labourid=models.IntegerField(primary_key=True,auto_created=True)
    labourcode=models.CharField(verbose_name="Labour Code",max_length=50)
    labourdesc=models.CharField(verbose_name="Labour Description",max_length=50)
    labouramount=models.IntegerField(verbose_name="Labour Charge")
    isactive=models.BooleanField(default=True)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")
    def __str__(self):
        return self.labourcode

class LabourMaster(models.Model):
    labourmasterid=models.IntegerField(primary_key=True,auto_created=True)
    jobcardobj=models.ForeignKey(JobCard,on_delete=models.PROTECT,null=True,blank=True)
    subcontractor=models.CharField(verbose_name="Sub Contractor",max_length=50)
    approvalstatus=models.CharField(verbose_name="Approval Status",max_length=50)
    isactive=models.BooleanField(default=True)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")


class LabourDetails(models.Model):
    labourdetailsid=models.IntegerField(primary_key=True,auto_created=True)
    labourmasterobj=models.ForeignKey(LabourMaster,on_delete=models.PROTECT,null=True,blank=True)
    labour=models.ForeignKey(Labour,on_delete=models.PROTECT,null=True,blank=True)
    mod=models.CharField(verbose_name="Mod Y/N",max_length=50)
    flatamount=models.IntegerField(verbose_name="Flat Amount")
    billabletype=models.CharField(verbose_name="Billable Type",max_length=50,null=True,blank=True)
    percent=models.IntegerField(verbose_name="%")
    value=models.IntegerField(verbose_name="Value")
    splitratio=models.IntegerField(verbose_name="Split Ratio")
    cust=models.CharField(verbose_name="CUST",max_length=50,null=True,blank=True)
    ins=models.CharField(verbose_name="INS",max_length=50,null=True,blank=True)
    dlr=models.CharField(verbose_name="DLR",max_length=50,null=True,blank=True)
    oem=models.CharField(verbose_name="OEM",max_length=50,null=True,blank=True)
    labouramt=models.IntegerField(verbose_name="Labour Amount")
    frmhrs=models.IntegerField(verbose_name="FRM Hrs")
    technician1=models.CharField(verbose_name="Technician",max_length=50)
    technician2=models.CharField(verbose_name="Technician2",max_length=50)
    isactive=models.BooleanField(default=True)
    created_by=models.CharField(verbose_name="Created By",max_length=50)
    created_on=models.DateTimeField(verbose_name="Created On")
    updated_by=models.CharField(verbose_name="Updated By",max_length=50)
    updated_on=models.DateTimeField(verbose_name="Updated On")

class PartsBatch(models.Model):
    partsbatchid=models.IntegerField(primary_key=True,auto_created=True)
    partscodeid=models.ForeignKey(Parts,on_delete=models.PROTECT,null=True,blank=True)
    batchcode=models.CharField(verbose_name="Batchcode",max_length=50,default="")
