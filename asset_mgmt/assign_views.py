from django.shortcuts import render_to_response,HttpResponseRedirect
from UAM.models import *
from asset_mgmt.models import *
from django.http import HttpResponse
from asset_mgmt.forms import Asset_Assign,Asset_Assign_Emp,ContactForm,AssetRequestForm,MyAsts,AssetDeassignForm,SplMvmt,AssetAssociation,AssetDeassociation
from django.shortcuts import render
from django.http import HttpResponseRedirect
from geraldo.generators import PDFGenerator
import mimetypes, os
from django.core.servers.basehttp import FileWrapper
from asset_track1 import settings
import datetime
import json
import reports
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError
from matplotlib.pylab import *
from django.template.defaultfilters import title
from reportlab.graphics.charts import axes
from ImageShow import show
from geraldo import Report


def AssetAssignment_Employee(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    if request.method == 'POST': # If the form has been submitted...
        form = Asset_Assign_Emp(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return render_to_response('asset_mgmt/register_common.html',{"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups,'fname':form.cleaned_data['Employee']})
    else:
        print "in else contact"
        form = Asset_Assign_Emp(initial = {'Date_of_return':datetime.datetime.now()}) # An unbound form
    return render_to_response('asset_mgmt/AssetAssingmenttoemp.html', {'form': form,"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})# Create your views here.
    print "contact"

def AssetAssignment_Department(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    if request.method == 'POST': # If the form has been submitted...
        form = Asset_Assign(request.POST) # A form bound to the POST data
        print "before form valid"
        if form.is_valid(): # All validation rules pass
            form.save()
            return render_to_response('asset_mgmt/register_common.html',{"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups,'fname':form.cleaned_data['Department']})
    else:
        print "in else contact"
        form = Asset_Assign(initial = {'Date_of_return':datetime.datetime.now()}) # An unbound form
    return render_to_response('asset_mgmt/AssetAssignment.html', {'form': form,"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})# Create your views here.
    print "contact"
    
def contact(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()                        
            return render_to_response('asset_mgmt/register_common.html',{"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups,'fname':form.cleaned_data['Department']})
    else:
        print "in else contact"
        form = ContactForm()
        #(initial = {'Date_of_return':datetime.datetime.now()}) # An unbound form
    return render_to_response('asset_mgmt/contact.html', {'form': form,"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})# Create your views here.
    print "contact hello"

def email(request):
#    email = EmailMessage('Hello', 'Message from django', to=['harihara@coresonant.com'])
#    email.send()
#    to = request.POST['To'] 
#    subject = request.POST['subject']
#    message = request.POST['message']
#    email = EmailMessage(subject=request.POST['subject'], message=request.POST['message'], to=request.POST['To'])
#    email.send()
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    to = request.POST.get('To', '')
#    print subject, message , to
    email = EmailMessage(subject, message, to = [to])
    email.send()
#    if subject and message and to:
#        try:
#            send_mail(subject, message, to, ['rohit@coresonant.com'])
#        except BadHeaderError:
#            return HttpResponse('Invalid header found.')
    return render_to_response('asset_mgmt/MailSent.html', {"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})
#    else:
#        # In reality we'd use a form class
#        # to get proper validation errors.
#        return HttpResponse('Make sure all fields are entered and valid.')

def AssetReq(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    #roles = Roles.objects.filter(Role_Name = "Asset Manager")
    #People = People.objects.filter(Primary_Email)
    if request.method == 'POST': # If the form has been submitted...
        form = AssetRequestForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            sub = request.POST['subject']
            msg = request.POST['message']
            print "dfdfdf"
            mail = []
#            for i in to:
            ppl = People_Role_Map.objects.filter(Role_Id__Role_Name= 'Asset Manager')
            print ppl[0].People_Id
            mail.append(str(ppl[0].People_Id.Primary_Email))            
            print mail
            email = EmailMessage(sub, msg, to= mail)
            email.send()  
            return render_to_response('asset_mgmt/MailSent.html',{"contacts":feature_list, 'len':len(feature_list)-1,"featuresgroups":featuresgroups})
    else:
        print "in else contact"
        form = AssetRequestForm()
        #(initial = {'Date_of_return':datetime.datetime.now()}) # An unbound form
    return render_to_response('asset_mgmt/AssetRequestForm.html', {'form': form, "contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})# Create your views here.
    
def AssetDeassign(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    pplid=request.session['pplid']
    if request.method == 'POST': # If the form has been submitted...
        form = AssetDeassignForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            ast = json.dumps(request.POST.getlist('asset'))
            sub = request.POST['subject']
            msg = request.POST['message']
            print "dfdfdf",ast
            mail = []
#            for i in to:
            ppl = People_Role_Map.objects.filter(Role_Id__Role_Name= 'Asset Manager')
            print ppl[0].People_Id
            mail.append(str(ppl[0].People_Id.Primary_Email))            
            print mail
            email = EmailMessage(sub+str(ast), msg, to= mail)
            email.send()
            return render_to_response('asset_mgmt/MailSent.html',{"contacts":feature_list, 'len':len(feature_list)-1,"featuresgroups":featuresgroups})
    else:
        print "in else contact"
        id_obj = Asset_Assignment_Employee.objects.filter(Employee__People = pplid)
        print "rohit",id_obj
        form = AssetDeassignForm()
        #(initial = {'Date_of_return':datetime.datetime.now()}) # An unbound form
    return render_to_response('asset_mgmt/AssetDeassignForm.html', {'form': form, "contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups,'assertlist':id_obj})


def SpecialReq(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    #roles = Roles.objects.filter(Role_Name = "Asset Manager")
    #People = People.objects.filter(Primary_Email)
    if request.method == 'POST': # If the form has been submitted...
        form = SplMvmt(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            sub = request.POST['subject']
            msg = request.POST['message']
            print "dfdfdf"
            mail = []
#            for i in to:
            ppl = People_Role_Map.objects.filter(Role_Id__Role_Name= 'Asset Manager')
            print ppl[0].People_Id
            mail.append(str(ppl[0].People_Id.Primary_Email))            
            print mail
            email = EmailMessage(sub, msg, to= mail)
            email.send()  
            return render_to_response('asset_mgmt/MailSent.html',{"contacts":feature_list, 'len':len(feature_list)-1,"featuresgroups":featuresgroups})
    else:
        print "in else contact"
        form = SplMvmt()
        #(initial = {'Date_of_return':datetime.datetime.now()}) # An unbound form
    return render_to_response('asset_mgmt/SplReqForm.html', {'form': form, "contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})


def AssetAssn(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    #roles = Roles.objects.filter(Role_Name = "Asset Manager")
    #People = People.objects.filter(Primary_Email)
    if request.method == 'POST': # If the form has been submitted...
        form = AssetAssociation(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            sub = request.POST['subject']
            msg = request.POST['message']
            print "dfdfdf"
            mail = []
#            for i in to:
            ppl = People_Role_Map.objects.filter(Role_Id__Role_Name= 'Asset Manager')
            print ppl[0].People_Id
            mail.append(str(ppl[0].People_Id.Primary_Email))            
            print mail
            email = EmailMessage(sub, msg, to= mail)
            email.send()  
            return render_to_response('asset_mgmt/MailSent.html',{"contacts":feature_list, 'len':len(feature_list)-1,"featuresgroups":featuresgroups})
    else:
        print "in else contact"
        form = AssetAssociation()
        #(initial = {'Date_of_return':datetime.datetime.now()}) # An unbound form
    return render_to_response('asset_mgmt/AssetAssociation.html', {'form': form, "contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})


def AssetDeassn(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    #roles = Roles.objects.filter(Role_Name = "Asset Manager")
    #People = People.objects.filter(Primary_Email)
    if request.method == 'POST': # If the form has been submitted...
        form = AssetDeassociation(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            sub = request.POST['subject']
            msg = request.POST['message']
            print "dfdfdf"
            mail = []
#            for i in to:
            ppl = People_Role_Map.objects.filter(Role_Id__Role_Name= 'Asset Manager')
            print ppl[0].People_Id
            mail.append(str(ppl[0].People_Id.Primary_Email))            
            print mail
            email = EmailMessage(sub, msg, to= mail)
            email.send()   
            return render_to_response('asset_mgmt/MailSent.html',{"contacts":feature_list, 'len':len(feature_list)-1,"featuresgroups":featuresgroups})
    else:
        print "in else contact"
        form = AssetDeassociation()
        #(initial = {'Date_of_return':datetime.datetime.now()}) # An unbound form
    return render_to_response('asset_mgmt/AssetDeassociation.html', {'form': form, "contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})


def Assetreport(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    return render_to_response('asset_mgmt/astreport.html',{"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups})

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


#def MyAssets(request):
#    print "hello world"
#    feature_list = request.session['feature_list']
#    featuresgroups = request.session['featuresgroups']
#    pplid=request.session['pplid']
#    #r_repo = request.POST['car']
#    print pplid
#    id_obj = Asset_Assignment_Employee.objects.filter(Employee__People=pplid)
#    print id_obj
#    report = reports.ast_repo(queryset=id_obj)
#    report.generate_by(PDFGenerator, filename= 'E:\My Work Location\Example\WorkSpace\\asset_track1\media\\'+str(2)+".pdf")
#    return render_to_response('asset_mgmt/astreport.html',{"contacts":feature_list,'root': settings.MEDIA_ROOT,'len':len(feature_list)-1,"featuresgroups":featuresgroups,'assertlist':id_obj})
#
def itemmove(request):
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    drr = Door.objects.all()
    print drr, "super"
    return render_to_response('asset_mgmt/itemmove.html',{"contacts":feature_list,'len':len(feature_list)-1,"featuresgroups":featuresgroups,'doornm':drr})

def itemmoved(request):
    print "hello world"
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
#    pplid=request.session['pplid']
    r_repo = request.POST['d_id']
    print r_repo,"111111111111111111111"
    id_obj = Asset_Trace.objects.filter(door = int(r_repo))
    print id_obj, "super222"
    report = reports.ast_repo(queryset=id_obj)
    report.generate_by(PDFGenerator, filename= 'E:\My Work Location\Example\WorkSpace\\asset_track1\media\\'+str(2)+".pdf")
    return render_to_response('asset_mgmt/itemmove2.html',{"contacts":feature_list,'root': settings.MEDIA_ROOT,'len':len(feature_list)-1,"featuresgroups":featuresgroups,'assertlist':id_obj})
#
#def pierepo(request):
#    print "heiiiiiii"
#    feature_list = request.session['feature_list']
#    featuresgroups = request.session['featuresgroups']
#    figure(1, figsize=(6,6))
#    ax = axes([0.1, 0.1, 0.8, 0.8])
#    
#    # The slices will be ordered and plotted counter-clockwise.
#    labels = 'Asset Name', 'Department', 'Employee', 'Date_of_assign', 'Date_of_return'
#    fracs = [15, 30, 45, 10,15]
#    explode=(0, 0, 0, 0.05,0)
#    
#    pie(fracs, explode=explode, labels=labels,
#                    autopct='%1.1f%%', shadow=True)
#                    # The default startangle is 0, which would start
#                    # the Frogs slice on the x-axis.  With startangle=90,
#                    # everything is rotated counter-clockwise by 90 degrees,
#                    # so the plotting starts on the positive y-axis.
#    
#    title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
#    
#    show()

def AssetMovement(request):
    print "AssetMovement"
    feature_list = request.session['feature_list']
    featuresgroups = request.session['featuresgroups']
    pplid=request.session['pplid']
    #r_repo = request.POST['car']
#    print pplid
    empnm = Asset_Assignment_Employee.objects.filter(Employee__People=pplid)
    print empnm
    id_obj = Asset_Track.objects.all()
    print id_obj
    report = reports.astmvmt_repo(queryset=id_obj)
    report.generate_by(PDFGenerator, filename= 'E:\My Work Location\Example\WorkSpace\\asset_track1\media\\'+str(2)+".pdf")
    return render_to_response('asset_mgmt/astmvmtReport.html',{"contacts":feature_list,'root': settings.MEDIA_ROOT,'len':len(feature_list)-1,"featuresgroups":featuresgroups,'assertlist':id_obj})

