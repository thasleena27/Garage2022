"""garageproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from garageapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.generateView,name='index'),
    path('addjobcard',views.generateView,name='addjobcard'),
    path('getcolorname/<str:colorcodeview>',views.getcolorname,name='getcolorname'),
    path('getvariantname/<str:variantcodeview>',views.getvariantname,name='getvariantname'),
    path('addemployee',views.addEmployee,name='addemployee'),
    path('getmodelname/<str:modelcodeview>',views.getmodelname,name='getmodelname'),
    path('getservicename/<str:servicecodeview>',views.getservicename,name='getservicename'),
    path('getallemployees',views.getAllEmployees,name='getallemployees'),
    path('getserviceadvisor/<str:serviceadvisorcodeview>',views.getserviceadvisor,name="getserviceadvisor"),
    path('gettechnician/<str:technicianview>',views.gettechnician,name="gettechnician"),
    path('sampleformset',views.CreateArticleFormSet,name='getsampleformset'),
    path('gettechnicaladvisor/<str:technicaladvisorcodeview>',views.gettechnicaladvisor,name='gettechnicaladvisor'),
    path('editjobcard/<int:objjobcardid>',views.EditJobcard,name='editjobcard'),
    path('getJobcardDetails/<int:objjobcardid>',views.getJobcardDetails,name='getjobcarddetails'),
    path('demandedrepairs',views.CreateDemandRepairsFormset,name='demandrepairs'),
    path('getDemanddescription/<str:demandcodeview>',views.getDemanddescription,name='getdemanddesc'),
    path('createpartsdetails',views.CreatePartsDetailsModelFormSet,name='createpartsdetails'),
    path('createlabourdetails',views.CreateLabourDetails,name='createlabourdetails'),
    path('addlabour',views.addLabour,name='addlabour'),
    path('getLabourdescription/<str:labourcodeview>',views.getLabourdescription,name='getlabourdescription'),
    path('getLabouramount/<str:labourcodeview>',views.getLabouramount,name='getlabouramount'),
    path('practiceformset',views.CreatePracticeFormset,name='practiceformset'),
    path('getBatchcode/<int:partscodeview>',views.getBatchCode,name='getBatchcode'),
]