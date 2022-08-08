from django import forms
from django import forms
from garageapp.models import (JobCard,Vehicle,Customer,Employee,Service,Demands,
Parts, PartsDetails, PartsMaster,Labour,LabourDetails,LabourMaster)


class ArticleForm(forms.Form):
    title=forms.CharField()
    pub_date=forms.DateField()

class PracticeForm(forms.Form):
    codechoices=(('001','001'),('002','002'),('003','003'))
    itemcode=forms.ChoiceField(choices=codechoices)
    itemdesc=forms.CharField()
    

class PartsModelForm(forms.ModelForm):
    class Meta:
        model=Parts
        exclude=('isactive','created_by','created_on','updated_by','updated_on')


class PartsMasterModelForm(forms.ModelForm):
    class Meta:
        model=PartsMaster
        exclude=('partsmasterid','isactive','created_by','created_on','updated_by','updated_on')

class PartsDetailsModelForm(forms.ModelForm):
    class Meta:
        model=PartsDetails
        exclude=('isactive','created_by','created_on','updated_by','updated_on')

class LabourModelForm(forms.ModelForm):
    class Meta:
        model=Labour
        exclude=('labourid','isactive','created_by','created_on','updated_by','updated_on')

        
class LabourDetailsModelForm(forms.ModelForm):
    #def __init__(self,*args,**kwargs):
        #super().__init__(*args,**kwargs) 
        #self.fields['labour'].widget.attrs.update({'class':'lbspecial'})
    
    class Meta:
        model=LabourDetails
        exclude=('isactive','created_by','created_on','updated_by','updated_on')

class LabourMasterModelForm(forms.ModelForm):
    class Meta:
        model=LabourMaster
        exclude=('isactive','created_by','created_on','updated_by','updated_on')


class DemandForm(forms.Form):
    mychoices=Demands.objects.all().values_list('demandid','demandcode')
    #def __init__(self,*args,**kwargs):
        #super().__init__(args,kwargs)
        #self.fields['demandcode']=forms.ChoiceField(choices=(('n','m'),('y','n')),widget=forms.Select)
    demandcode=forms.ChoiceField(choices=mychoices,widget=forms.Select(attrs={"class":"Demandform_Demandcode"}))
    custprblm=forms.CharField()
    reportedby=forms.CharField()













class JobcardModelForm(forms.ModelForm):
    class Meta:
        model=JobCard
        exclude=('jobcardid','isactive','created_by','created_on','updated_by','updated_on')

class VehicleModelForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        exclude=('vehicleid','isactive','created_by','created_on','updated_by','updated_on','jobcardobj')

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model=Customer
        exclude=('customerid','isactive','created_by','created_on','updated_by','updated_on','jobcardobj')

class EmployeeModelForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) 
        self.fields['name'].widget.attrs.update({'class':'special'})
    class Meta:
        model=Employee
        exclude=('empid','isactive','created_by','created_on','updated_by','updated_on')

class ServiceModelForm(forms.ModelForm):
    class Meta:
        model=Service
        exclude=('serviceid','isactive','created_by','created_on','updated_by','updated_on')

