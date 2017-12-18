'''
Created on Oct 26, 2012

@author: god
'''
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
#import django_cron
#django_cron.autodiscover()
admin.autodiscover()
urlpatterns = patterns('asset_mgmt.reg_views',
        url(r'(?P<feature_id>\d+)/(?P<feat_item_id>\d+)/$','url_parser'),
        url(r'^Create_Assets/$','AssetRegistration_Add'),
        url(r'^Register_Asset/$','AssetRegistration_Add'), 
        url(r'^AssetRegistration_Add/$','AssetRegistration_Add'),
        url(r'^PeopleRegestration_Add/$','PeopleRegestration_Add'),
        url(r'^Reports_person/$','Personreport'),
        url(r'^HReport/$','person_report'),
        url(r'^viewordown\.pdf$','send_file'),  #Geraldo Report
        url(r'^MyAssets_Assets/$','assets_show'),
)      
     
urlpatterns += patterns('asset_mgmt.assign_views',
#        url(r'(?P<feature_id>\d+)/(?P<feat_item_id>\d+)/$','url_parser'),
        url(r'^AssetAssign_Employee/$','AssetAssignment_Employee'),
#        url(r'^AssetAssign_Department/$','AssetAssignment_Employee'),
        url(r'^AssetAssignment_Department/$','AssetAssignment_Department'),
#        url(r'^AssetAssign_Person/$','AssetAssignment_Department'),
        url(r'^Contact_contact/$','contact'),
        url(r'^email/$','email'),
        url(r'^RequestForm_AssetRequestForm/$','AssetReq'),
        url(r'^RequestForm_AssetDe-AssignForm/$','AssetDeassign'),
        url(r'^RequestForm_SpecialRequestForm/$','SpecialReq'),
        url(r'^RequestForm_AssetAssociation/$','AssetAssn'),
        url(r'^RequestForm_AssetDe-AssociationForm/$','AssetDeassn'),
        url(r'^ContactForm_AssetAdmin/$','contact'),
        url(r'^email/$','email'),
        url(r'^Contact_Contact/$','contact'),
        url(r'^email/$','email'),
        url(r'^Reports_MyAsset/$','Assetreport'),
#        url(r'^Scan_Assets/$','MyAssets'),
#        url(r'^viewordown\.pdf$','send_file'), 
        url(r'^Scan_AssetMovement/$','AssetMovement'),
        url(r'^viewordown\.pdf$','send_file'), 
#        url(r'^viewordown\.jpg$','send_file'),
        
        url(r'^Scan_Assets/$','itemmove'),
        url(r'^itemmove2/$','itemmoved'),
        url(r'^viewordown\.pdf$','send_file'),


#        url(r'^PeopleRegestration_Add/$','PeopleRegestration_Add'),
#        url(r'^PeopleRegistration_Edit\.php$','PeopleRegestration_Edit'),
#        url(r'^AssetAssignment_Department\.php$','AssetAssignment_Department'),
#         #        url(r'^AssetRegistration_Delete/$','AssetRegistration_Delete'),
    )    
urlpatterns += patterns('django.views.static',
        (r'mymedia/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^admin/', include(admin.site.urls)),
    )