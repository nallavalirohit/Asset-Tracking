from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from forms import RegistrationForm, People_Registration
from asset_mgmt.models import Asset, Person



def registration(request):
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
            p = Asset(name=name,model_no= model_no,barcode = barcode, serial_no = serial_no,asset_category = asset_category,\
                      asset_class = asset_class,security = security,asset_status = asset_status,asset_type = asset_type, priority=priority,\
                      warranty = warranty,created_date = created_date,updated_date = updated_date)
            p.save()
            return HttpResponse('Record Created')
    else:
        print "in else contact"
        form = RegistrationForm() # An unbound form
        return render_to_response('asset_mgmt/Registration.html', {'form': form,})# Create your views here.
    print "contact"
    
    
def PeopleRegistration(request):
    if request.method == 'POST': # If the form has been submitted...
        form = None
        form = People_Registration(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            First_Name = form.cleaned_data['First_Name']
            Last_Name = form.cleaned_data['Last_Name']
            gender = form.cleaned_data['gender']
            Address = form.cleaned_data['Address']
            Phone = form.cleaned_data['Phone']
            Email = form.cleaned_data['Email']
            Image = form.cleaned_data['Image']
            
            q = Person(First_Name = First_Name,Last_Name= Last_Name, gender = gender, Address = Address,Phone = Phone,\
                      Email = Email,Image = Image)
            q.save()
            return HttpResponse('Record Created')
    else:
        print "in else contact"
        form = People_Registration() # An unbound form
        return render_to_response('asset_mgmt/PeopleRegistration.html', {'form': form,})# Create your views here.
    print "contact"
    

