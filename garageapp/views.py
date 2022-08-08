
from django.shortcuts import render
from garageapp.forms import (JobcardModelForm,VehicleModelForm,CustomerModelForm,EmployeeModelForm,
ArticleForm,DemandForm,PartsDetailsModelForm,PartsMasterModelForm,LabourModelForm,PracticeForm)
from garageapp.models import(JobCard,Article,Vehicle,Customer,Color,Vehiclevariant,Employee,
Vehiclemodel,ServiceType,DemandedRepairs,Demands,PartsDetails,PartsMaster,LabourDetails,LabourMaster,
Labour,Parts,PartsBatch)
import datetime
from django.http.response import HttpResponse,JsonResponse
from django.forms import formset_factory, modelformset_factory
from itertools import chain




def CreatePartsDetailsModelFormSet(request):
    template_name="garageapp/parts.html"
    PartsDetailsModelFormSet=modelformset_factory(PartsDetails,extra=2,fields=('partno','requestedqty','issuedqty','storebinlocation','currentstock','floatstock','issuetype','issueqty'))
    modelformset=PartsDetailsModelFormSet(queryset=PartsDetails.objects.filter(partdetailsid=0),initial=[{'requestedqty':0,'issuedqty':0,'storebinlocation':'','currentstock':0,'floatstock':0,'issuetype':'','issueqty':0}])
    #print(modelformset)
    modelformset[0].fields["partno"].widget.attrs.update({"class":"partnoclass"})
    modelformset[0].fields["requestedqty"].widget.attrs.update({"class":"reqclass"})
    modelformset[0].fields["issuedqty"].widget.attrs.update({"class":"issuedclass"})
    modelformset[0].fields["issueqty"].widget.attrs.update({"class":"issueclass","readonly":"readonly"})
    modelformset[1].fields["partno"].widget.attrs.update({"class":"partnoclass"})
    modelformset[1].fields["requestedqty"].widget.attrs.update({"class":"reqclass"})
    modelformset[1].fields["issuedqty"].widget.attrs.update({"class":"issuedclass"})
    modelformset[1].fields["issueqty"].widget.attrs.update({"class":"issueclass","readonly":"readonly"})
    partsmaster=PartsMasterModelForm()
    partscodelist=Parts.objects.all()
    if request.method=='GET':
        return render(request,template_name,context={"modelform":partsmaster,"forms":modelformset,"partscodelist":partscodelist})
    elif request.method=='POST':
        modelformset=PartsDetailsModelFormSet(request.POST)
        partsmaster=PartsMasterModelForm(request.POST)
        #jobcardobj=request.POST.get('hdjobcard')
        #print(jobcard)
        #jobcardobj=JobCard.objects.get(jobcardid=jobcard)
        modelformset.is_valid()
        print(modelformset.errors)
        partsmaster.is_valid()
        print(partsmaster.errors)
        if partsmaster.is_valid():
            print("I am valid")
            partsmasterinstance=partsmaster.save(commit=False)
            partsmasterinstance.created_on=datetime.datetime.now()
            partsmasterinstance.created_by="thasleena"
            partsmasterinstance.updated_by=""
            partsmasterinstance.updated_on=datetime.datetime.min
            partsmasterinstance.save()
            partsmasterobj=PartsMaster.objects.latest("partsmasterid")
        if modelformset.is_valid():
            for form in modelformset:
                partsdetailsobj=form.save(commit=False)
                partsdetailsobj.created_on=datetime.datetime.now()
                partsdetailsobj.created_by="thasleena"
                partsdetailsobj.updated_by=""
                partsdetailsobj.updated_on=datetime.datetime.now()
                partsdetailsobj.partsmasterobj=partsmasterobj
                partsdetailsobj.save()
                print(modelformset)
                modelformset=PartsDetailsModelFormSet()
            context={"modelform":partsmaster,"forms":modelformset}
            return render(request,template_name,context)
        
        else:
            print("not valid")
            print(partsmaster.errors)
            print(modelformset.errors)
            context={"modelform":partsmaster,"forms":modelformset}
            return render(request,template_name,context)

def addLabour(request):
    template_name="garageapp/addlabour.html"
    labourobjform=LabourModelForm()
    context={"form":labourobjform}
    if request.method=='GET':
        return render(request,template_name,context)
    elif request.method=='POST':
        labourobjform=LabourModelForm(request.POST)
        context={"form":labourobjform}
        if labourobjform.is_valid():
            labourinstance=labourobjform.save(commit=False)
            labourinstance.created_on=datetime.datetime.now()
            labourinstance.created_by="thasleena"
            labourinstance.updated_by=""
            labourinstance.updated_on=datetime.datetime.min
            labourinstance.save()
            context={"form":labourobjform}
            return render(request,template_name,context)
        return render(request,template_name,context)


def CreateLabourDetails(request):
    template_name="garageapp/labour.html"
    LabourDetailsModelFormSet=modelformset_factory(LabourDetails,extra=2,fields=('labour','mod','flatamount','billabletype','percent','value','splitratio','cust','ins','dlr','oem','labouramt','frmhrs','technician1','technician2'))
    modelformset=LabourDetailsModelFormSet(initial=[{'labouramt':0}])
    # Updating the widget at views.py
    modelformset[0].fields["labour"].widget.attrs.update({"class":"lbspecial"})
    modelformset[0].fields["labouramt"].widget.attrs.update({"class":"lbamtspecial"})
    modelformset[1].fields["labour"].widget.attrs.update({"class":"lbspecial"})
    modelformset[1].fields["labouramt"].widget.attrs.update({"class":"lbamtspecial"})
    if request.method=='GET':
        return render(request,template_name,context={"forms":modelformset})

def CreatePracticeFormset(request):
    template_name="garageapp/practiceformset.html"
    PracticeFormSet=formset_factory(PracticeForm,extra=2)
    formset=PracticeFormSet()
    formset[0].fields["itemcode"].widget.attrs.update({"class":"classitemcode"})
    formset[0].fields["itemdesc"].widget.attrs.update({"class":"classitemdesc"})
    formset[1].fields["itemcode"].widget.attrs.update({"class":"classitemcode"})
    formset[1].fields["itemdesc"].widget.attrs.update({"class":"classitemdesc"})
    if request.method=='GET':
        return render(request,template_name,context={"forms":formset})
    elif request.method=='POST':
        return render(request,template_name,context={"forms":formset})


def CreateArticleFormSet(request):
    template_name="garageapp/formset.html"
    context={"form":ArticleForm}
    ArticleFormSet=formset_factory(ArticleForm,extra=2)
    formset=ArticleFormSet()
    if request.method=='GET':
        return render(request,template_name,context={'forms':formset})
    elif request.method=='POST':        
        formset=ArticleFormSet(request.POST)               
        if formset.is_valid():                       
            for form in formset:
                mdl=Article()
                mdl.articletitle=form.cleaned_data['title']
                mdl.articlepubdate=form.cleaned_data['pub_date']
                mdl.save()
                print(form.cleaned_data['title'])
            return render(request,template_name)
        else:            
            return render(request,template_name,context={'forms':formset})
    return render(request,template_name,context)

def CreateDemandRepairsFormset(request):
    template_name="garageapp/demandrepairsformset.html"
    DemandFormSet=formset_factory(DemandForm,extra=5)
    formset=DemandFormSet()
    '''for form in formset.forms:
        form.fields['demandcode'].choices =[(('n','m'),('k','l'))]
    print(formset)'''
    if request.method=='GET':
        return render(request,template_name,context={"forms":formset})
    elif request.method=='POST':
        formset=DemandFormSet(request.POST)
        jobcard=request.POST.get('hdjobcard')
        print(jobcard)
        jobcardobj=JobCard.objects.get(jobcardid=jobcard)
        formset.is_valid()
        print(formset.errors)
        if formset.is_valid():
            for form in formset:
                demobj=DemandedRepairs()
                demandid=form.cleaned_data['demandcode']
                demandobj=Demands.objects.get(demandid=demandid)
                demobj.demandcode=demandobj
                demobj.customerprb=form.cleaned_data['custprblm']
                demobj.reportedby=form.cleaned_data['reportedby']
                demobj.jobcardobj=jobcardobj
                demobj.created_by="thasleena"
                demobj.created_on=datetime.datetime.now()
                demobj.updated_by=""
                demobj.updated_on=datetime.datetime.min
                demobj.save()
                print(formset)
            formset=DemandFormSet()
            context={"form":formset}
            return render(request,template_name,context)
        else:
            return render(request,template_name,context={"form":formset})
                    

# Create your views here.
def Createjobcard(request):
    template_name="garageapp/createjob.html"
    jobcardobjform=JobcardModelForm()
    context={"form":jobcardobjform}
    if request.method=='GET':
        return render(request,template_name,context)
    elif request.method=='POST':
        jobcardobjform=JobcardModelForm(request.POST)
        context={"form":jobcardobjform}
        if jobcardobjform.is_valid():
            jobcardobjform.save()
            context={"form":jobcardobjform}
            return render(request,template_name,context)
        else:
            return render(request,template_name)
'''def AddVehicle(request):
    template_name="garageapp/createjob.html"
    vehicleobjform=VehicleModelForm()
    context={"form":vehicleobjform}
    if request.method=='GET':
        return render(request,template_name,context)
    elif request.method=='POST':
        vehicleobjform=VehicleModelForm(request.POST)
        context={"form":vehicleobjform}
        if vehicleobjform.is_valid():
            vehicleobjform.save()
            context={"form":vehicleobjform}
            return render(request,template_name,context)
        else:
            return render(request,template_name,context)

def AddCustomer(request):
    template_name="garageapp/createjob.html"
    customerobjform=CustomerModelForm()
    context={"form":customerobjform}
    if request.method=='GET':
        return render(request,template_name,context)
    elif request.method=='POST':
        customerobjform=CustomerModelForm(request.POST)
        context={"form":customerobjform}
        if customerobjform.is_valid():
            customerobjform.save()
            context={"form":customerobjform}
            return render(request,template_name,context)
        else:
            return render(request,template_name,context)'''

def generateView(request):
    template_name="garageapp/createjob.html"
    jobcardobjform=JobcardModelForm(prefix="jobcard_form")
    vehicleobjform=VehicleModelForm(prefix="vehicle_form")
    customerobjform=CustomerModelForm(prefix="customer_form")
    context={"jobcardform":jobcardobjform,"vehicleform":vehicleobjform,"customerform":customerobjform}
    if request.method=='GET':
        return render(request,template_name,context)
    elif request.method=='POST':
        jobcardobjform=JobcardModelForm(request.POST,prefix="jobcard_form")
        vehicleobjform=VehicleModelForm(request.POST,prefix="vehicle_form")
        customerobjform=CustomerModelForm(request.POST,prefix="customer_form")
        if jobcardobjform.is_valid() and vehicleobjform.is_valid() and customerobjform.is_valid():
            print("All validations passed")
            jobcard_form=jobcardobjform.save(commit=False)
            jobcard_form.created_on=datetime.datetime.now()
            jobcard_form.created_by="thasleena"
            jobcard_form.updated_by=""
            jobcard_form.updated_on=datetime.datetime.min
            jobcard_form.save()
            jobcardobj=JobCard.objects.latest('jobcardid')
            vehicle_form=vehicleobjform.save(commit=False)
            vehicle_form.jobcardobj=jobcardobj
            vehicle_form.created_on=datetime.datetime.now()
            vehicle_form.created_by="thasleena"
            vehicle_form.updated_by=""
            vehicle_form.updated_on=datetime.datetime.min
            vehicle_form.save()
            customer_form=customerobjform.save(commit=False)
            customer_form.jobcardobj=jobcardobj
            customer_form.created_on=datetime.datetime.now()
            customer_form.created_by="thasleena"
            customer_form.updated_on=datetime.datetime.min
            customer_form.updated_by=""
            customer_form.save()
            context={"jobcardform":jobcardobjform,"vehicleform":vehicleobjform,"customerform":customerobjform}
            return render(request,template_name,context)
        else:
            context={"jobcardform":jobcardobjform,"vehicleform":vehicleobjform,"customerform":customerobjform}
            return render(request,template_name,context)
            

def getcolorname(request,colorcodeview):
    
    colorobj=Color.objects.filter(colorcode='#'+colorcodeview).values('colorname')
    print(colorobj)
    return JsonResponse(list(colorobj),safe=False)

def getvariantname(request,variantcodeview):
    variantobj=Vehiclevariant.objects.filter(variantcode=variantcodeview).values('variantname')
    print(variantobj)
    return JsonResponse(list(variantobj),safe=False)

def getmodelname(request,modelcodeview):
    modelobj=Vehiclemodel.objects.filter(vehiclemodel=modelcodeview).values('modelname')
    print(modelobj)
    return JsonResponse(list(modelobj),safe=False)

def getservicename(request,servicecodeview):
    serviceobj=ServiceType.objects.filter(servicetype=servicecodeview).values('servicename')
    print(serviceobj)
    return JsonResponse(list(serviceobj),safe=False)

def getserviceadvisor(request,serviceadvisorcodeview):
    empobj=Employee.objects.filter(empid=serviceadvisorcodeview,isServiceAdvisor=True).values('name')
    print(empobj)
    return JsonResponse(list(empobj),safe=False)

def gettechnician(request,technicianview):
    empobj=Employee.objects.filter(empid=technicianview,isTechnician=True).values('name')
    print(empobj)
    return JsonResponse(list(empobj),safe=False)

def gettechnicaladvisor(request,technicaladvisorcodeview):
    empobj=Employee.objects.filter(empid=technicaladvisorcodeview,isTechnicalAdvisor=True).values('name')
    print(empobj)
    return JsonResponse(list(empobj),safe=False)

def getDemanddescription(request,demandcodeview):
    demandobj=Demands.objects.filter(demandid=demandcodeview).values('demand_desc')
    print(demandobj)
    return JsonResponse(list(demandobj),safe=False)

def getLabourdescription(request,labourcodeview):
    labourobj=Labour.objects.filter(labourid=labourcodeview).values('labourdesc')
    print(labourobj)
    return JsonResponse(list(labourobj),safe=False)

def getLabouramount(request,labourcodeview):
    labourobj=Labour.objects.filter(labourid=labourcodeview).values('labouramount')
    print(labourobj)
    return JsonResponse(list(labourobj),safe=False)

def getBatchCode(request,partscodeview):
    partscode=Parts.objects.get(partsid=partscodeview)
    partsbatchobj=PartsBatch.objects.filter(partscodeid=partscode).values('batchcode')
    print(partsbatchobj)
    return JsonResponse(list(partsbatchobj),safe=False)



def addEmployee(request):
    template_name="garageapp/employee.html"
    employeeobjform=EmployeeModelForm()
    context={"form":employeeobjform}
    if request.method=='GET':
        return render(request,template_name,context)
    elif request.method=='POST':
        employeeobjform=EmployeeModelForm(request.POST)
        context={"form":employeeobjform}
        if employeeobjform.is_valid():
            employeeinstance=employeeobjform.save(commit=False)
            employeeinstance.created_on=datetime.datetime.now()
            employeeinstance.created_by="thasleena"
            employeeinstance.updated_by=""
            employeeinstance.updated_on=datetime.datetime.min
            employeeinstance.save()
            context={"form":employeeobjform}
            return render(request,template_name,context)
        return render(request,template_name,context)

def getAllEmployees(request):
    template_name="garageapp/employeelist.html"
    if request.method=="GET":
        employeelist=Employee.objects.all()
        context={"employeelist":employeelist}
        return render(request,template_name,context)

def EditJobcard(request,objjobcardid):
    template_name="garageapp/createjob.html"
    jobcardinstance=JobCard.objects.get(jobcardid=objjobcardid)
    if request.method=='GET':
        jobcardform=JobcardModelForm(instance=jobcardinstance)
        context={"form":jobcardform}
        return render(request,template_name,context)
    elif request.method=='POST':
        jobcardform=JobcardModelForm(request.POST,instance=jobcardinstance)
        if jobcardform.is_valid():
            jobcardform.save()
            context={"form":jobcardform}
            return render(request,template_name,context)
        else:
            return render(request,template_name,context)

def getJobcardDetails(request,objjobcardid):
    dependentvalue={}
    template_name="garageapp/createjob.html"
    jobcardobj=JobCard.objects.get(jobcardno=objjobcardid)
    jobcardinstance=JobCard.objects.filter(jobcardno=objjobcardid).values('jobcardno','datetime','checkindatetime','jobcardid')
    vehicleinstance=Vehicle.objects.filter(jobcardobj=jobcardobj).values('regno','omr','servicetype','washtype','service_advisor','technician','technical_advisor','vehiclemodel','chasisno','vehiclevariant','color')
    hi=(vehicleinstance[0]['color'])
    colortofind=Color.objects.filter(colorcode='#'+hi).values('colorname')
    #dependentvalue={'Color':colortofind}
    print(colortofind)
    #print(jobcardinstance)
    service=(vehicleinstance[0]['servicetype'])
    servicetofind=ServiceType.objects.filter(servicetype=service).values('servicename')
    print(servicetofind)
    variantview=(vehicleinstance[0]['vehiclevariant'])
    varianttofind=Vehiclevariant.objects.filter(variantcode=variantview).values('variantname')
    print(varianttofind)
    customerinstance=Customer.objects.filter(jobcardobj=jobcardobj).values('customername','customeraddress','city','state','email','phone','mobile','gstin','pan','outstanding_amt')
    result=list(chain(jobcardinstance,vehicleinstance,customerinstance,colortofind,servicetofind,varianttofind))
    # print(result)
    #customerinstance=Customer.objects.get(jobcardobj=objjobcardid)
    if request.method=='GET':
        #customerform=CustomerModelForm(instance=customerinstance,prefix="customer_form")
        return JsonResponse(list(result),safe=False)
    

        