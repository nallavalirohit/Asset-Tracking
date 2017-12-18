from django.shortcuts import render_to_response,HttpResponseRedirect
from UAM.models import *
from asset_mgmt.models import *
from django.http import HttpResponse
from asset_mgmt.forms import People_Registration,RegistrationForm,Asset_Assign, ContactForm
import logging
from django.http import HttpResponse
#from reports import ReportPurchase
from geraldo.generators import PDFGenerator
import mimetypes, os
from django.core.servers.basehttp import FileWrapper
import reports
from asset_track1 import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from asset_track1 import settings

def url_parser(request, feature_id, feat_item_id):
    logging.debug('This is a sample debug message')
    logging.info('This is a sample informational message')
    logging.warn('This is a sample warning message')
    logging.error('This is a sample error message')
    logging.critical('This is a sample critical message')
    featurename = Feature_Group.objects.get(id = feature_id).Name
    feature_item = Feature_Items.objects.get(id = feat_item_id).Name
    fnname = (featurename+"_"+feature_item).replace(' ','')
    print '/asset_track1/'+fnname+'/'
    return HttpResponseRedirect('/asset_track1/'+fnname+'/')
     
#    AssetRegistration_Add = ''
#    AssetRegistration_Add = AssetRegistration_Add()
#    vars()[str(fnname)]()
#    feature_options = { 'AssetRegistration_Add' : AssetRegistration_Add, 'AssetRegistration_Edit' : AssetRegistration_Edit }
#    vars()[str(fnname)]()
#    sm = locals()[str(fnname)]()
#    fname = []
#    fname.append(featurename)
#    fname.append("_")
#    fname.append(feature_item)
#    fnname = (''.join(fname))()
    
def AssetRegistration_Add(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    if request.method == 'POST': # If the form has been submitted...
        form = None
        form = RegistrationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            name = form.cleaned_data['name']
            model_no = form.cleaned_data['model_no']
            barcode = form.cleaned_data['barcode']
            serial_no = form.cleaned_data['serial_no']
            asset_category = form.cleaned_data['asset_category']
            asset_class = form.cleaned_data['asset_class']
            security = form.cleaned_data['security']
            asset_status = form.cleaned_data['asset_status']
            asset_type = form.cleaned_data['asset_type']
#            enter_date = form.cleaned_data['enter_date']
            priority = form.cleaned_data['priority']
            warranty = form.cleaned_data['warranty']
            created_date = form.cleaned_data['created_date']
            updated_date = form.cleaned_data['updated_date']
            p = Asset(name=name,model_no= model_no,barcode = barcode, serial_no = serial_no, asset_category = asset_category,\
                      asset_class = asset_class,security = security,asset_status = asset_status,asset_type = asset_type, priority=priority,\
                      warranty = warranty,created_date = created_date,updated_date = updated_date)
            p.save()
            return render_to_response('asset_mgmt/register_common.html',{"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups,'fname':name})
    else:
        print "in else contact"
        form = RegistrationForm() # An unbound form
        return render_to_response('asset_mgmt/Registration.html', {'form': form,"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})# Create your views here.
    print "contact"
def AssetRegistration_Edit(request):
    return HttpResponse("ok")

def PeopleRegestration_Add(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    if request.method == 'POST': # If the form has been submitted...
        form = None
        form = People_Registration(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
#            First_Name = form.cleaned_data['First_Name']
#            Last_Name = form.cleaned_data['Last_Name']
#            Gender = form.cleaned_data['Gender']
#            Address = form.cleaned_data['Address']
#            Mobile = form.cleaned_data['Mobile']
#            Primary_Email = form.cleaned_data['Primary_Email']
#            Secondary_Email = form.cleaned_data['Secondary_Email']
#            #Image = form.cleaned_data['Image']
#            
#            q = People(First_Name = First_Name, Last_Name= Last_Name, Gender = Gender, Address = Address,Mobile = Mobile,\
#                      Primary_Email = Primary_Email, Secondary_Email = Secondary_Email)
            form.save()
            return render_to_response('asset_mgmt/register_common.html',{"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})
    else:
        print "in else contact"
        form = People_Registration() # An unbound form
        return render_to_response('asset_mgmt/PeopleRegistration.html', {'form': form,"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})# Create your views here.
    print "contact"
def PeopleRegestration_Edit(request):
    return HttpResponse("ok")


    
def Personreport(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    return render_to_response('asset_mgmt/perreport.html',{"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})
    
#def Person_Report(request):
#    feature_list = request.session['feature_list']
#    featuresgroups = request.session['featuresgroups']
#    request.session['car'] = request.POST['car']
##    request.session['from1'] = str(request.POST['from1'])[0:10]+' '+ '00:00:00'
##    request.session['to'] = str(request.POST['to'])[0:10]+' '+ '23:59:59'
#    name = request.session['car']
##    from1=request.session['from1']
##    to = request.session['to']
#    txnobj = People.objects.filter(First_Name=(name))
#    print "7777777",txnobj
#    return render_to_response('asset_mgmt/HReport.html',{"personrepo":txnobj,"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})

def send_file(request):
    if 'print' in request.POST:            
        filename  = 'E:\My Work Location\Example\WorkSpace\\asset_track1\media\\'+str(2)+".pdf" # Select your file here.
        download_name = str(2)+".pdf"
        wrapper      = FileWrapper(open(filename))
        content_type = mimetypes.guess_type(filename)[0]
        response     = HttpResponse(wrapper,content_type=content_type)
        response['Content-Length']      = os.path.getsize(filename)    
        response['Content-Disposition'] = "attachment; filename=%s"%download_name
        return response
    elif 'view' in request.POST:
#       f = StringIO.StringIO()
        pdf_data = open('E:\My Work Location\Example\WorkSpace\\asset_track1\media\\'+str(2)+".pdf", "rb").read()
        print 'E:\My Work Location\Example\WorkSpace\asset_track1\media\\'+str(2)+".pdf"
        return HttpResponse(pdf_data, mimetype="application/pdf")

def person_report(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    r_repo = request.POST['car']
    id_obj = People.objects.filter(First_Name = r_repo)
    report = reports.per_repo(queryset=id_obj)
    print id_obj
    report.generate_by(PDFGenerator, filename= 'E:\My Work Location\Example\WorkSpace\\asset_track1\media\\'+str(2)+".pdf")
    return render_to_response('asset_mgmt/HReport.html',{"contacts":id_obj,'root': settings.MEDIA_ROOT,'len':len(feature_list)-1,"featuresgroups":featuresgroups})
   
def assets_show(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    asset_obj = Asset_Assignment_Employee.objects.filter(Employee__id = 2)
    return render_to_response('asset_mgmt/assets_show.html',{'root': settings.MEDIA_ROOT,'len':len(feature_list)-1,"featuresgroups":featuresgroups,"asset_obj":asset_obj,"contacts":feature_list,})


#    email = EmailMessage('Hello', 'Message from django', to=['rohit@coresonant.com'])
#    email.send()














