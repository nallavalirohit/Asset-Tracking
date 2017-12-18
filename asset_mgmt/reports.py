from geraldo import Report, ReportBand, ObjectValue, Label, DetailBand, SystemField, BAND_WIDTH
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_LEFT


class per_repo(Report):
        title = 'People Report'
        class band_detail(DetailBand):
            height = 0.7*cm
            elements = [
                ObjectValue(expression='id', left=0.8*cm, style={'alignment': TA_LEFT}),
                ObjectValue(expression='First_Name', left=1.5*cm,  style={'alignment': TA_LEFT}),
                ObjectValue(expression='Last_Name', left=4.5*cm,style={'alignment': TA_LEFT}),
                ObjectValue(expression='Gender', left=7.5*cm,style={'alignment': TA_LEFT}),
                ObjectValue(expression='Address', left=9.5*cm,style={'alignment': TA_LEFT}),
                ObjectValue(expression='Primary_Email', left=12.5*cm,style={'alignment': TA_LEFT}),
#                ObjectValue(expression='Number_of_products', left=9.0*cm,style={'alignment': TA_LEFT}),#, get_value=lambda instance: instance.people_acc.acc_no.balance.str('%s')),
#                ObjectValue(expression='id', left=8.8*cm,style={'alignment': TA_RIGHT}),
#                ObjectValue(expression='inst_id', left=11*cm,style={'alignment': TA_RIGHT}),
            ]
            borders = {'all': True}





        class band_page_header(ReportBand):
            height = 1.3*cm
            elements = [
                SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                    style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
                SystemField(expression=u'Page %(page_number)d of %(page_count)d', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                Label(text="ID", top=0.8*cm, left=0.6*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="First_Name", top=0.8*cm, left=1.4*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Last_Name", top=0.8*cm, left=4.5*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Gender", top=0.8*cm, left=7.5*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Address", top=0.8*cm, left=9.5*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Primary_Email", top=0.8*cm, left=12.5*cm, style={'fontName': 'Helvetica-Bold'}),
            ]
            borders = {'all': True}
        

class ast_repo(Report):
        title = 'Asset Report'
#        class band_detail(DetailBand):
        height = 0.7*cm
        elements = [
                ObjectValue(expression='Asset.name', left=0.8*cm, style={'alignment': TA_LEFT}),
                ObjectValue(expression='Department', left=3.4*cm,  style={'alignment': TA_LEFT}),
                ObjectValue(expression='Employee', left=6.5*cm,style={'alignment': TA_LEFT}),
                ObjectValue(expression='Date_of_return', left=9.5*cm,style={'alignment': TA_LEFT}),
                ObjectValue(expression='Date_of_assign', left=13.5*cm,style={'alignment': TA_LEFT}),
#                ObjectValue(expression='Primary_Email', left=12.5*cm,style={'alignment': TA_LEFT}),
#                ObjectValue(expression='Number_of_products', left=9.0*cm,style={'alignment': TA_LEFT}),#, get_value=lambda instance: instance.people_acc.acc_no.balance.str('%s')),
#                ObjectValue(expression='id', left=8.8*cm,style={'alignment': TA_RIGHT}),
#                ObjectValue(expression='inst_id', left=11*cm,style={'alignment': TA_RIGHT}),
            ]
        borders = {'all': True}
        class band_page_header(ReportBand):
            height = 1.3*cm
            elements = [
                SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                    style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
                SystemField(expression=u'Page %(page_number)d of %(page_count)d', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                Label(text="Asset Name", top=0.8*cm, left=0.6*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Department", top=0.8*cm, left=3.4*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Employee", top=0.8*cm, left=6.5*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Date_of_return", top=0.8*cm, left=9.5*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Date_of_assign", top=0.8*cm, left=13.5*cm, style={'fontName': 'Helvetica-Bold'}),
#                Label(text="Primary_Email", top=0.8*cm, left=12.5*cm, style={'fontName': 'Helvetica-Bold'}),
#                Label(text="Txn No", top=0.8*cm, left=12.6*cm, style={'fontName': 'Helvetica-Bold'}),
#                Label(text="PGID/", top=0.4*cm, left=14.6*cm, style={'fontName': 'Helvetica-Bold'}),
#                Label(text="Staff ID", top=0.8*cm, left=14.6*cm, style={'fontName': 'Helvetica-Bold'}),
            ]
            borders = {'all': True}


            
            
            
class astmvmt_repo(Report):
        title = 'Asset Report'
#        class band_detail(DetailBand):
        height = 0.7*cm
        elements = [
                ObjectValue(expression='Asset.name', left=0.8*cm, style={'alignment': TA_LEFT}),
                ObjectValue(expression='TagID', left=3.4*cm,  style={'alignment': TA_LEFT}),
                ObjectValue(expression='E_TagID', left=6.5*cm,style={'alignment': TA_LEFT}),
                ObjectValue(expression='Entry_Time', left=9.5*cm,style={'alignment': TA_LEFT}),
                ObjectValue(expression='Exit_Time', left=12.5*cm,style={'alignment': TA_LEFT}),
                ObjectValue(expression='Checkpoint', left=15.5*cm,style={'alignment': TA_LEFT}),
#                ObjectValue(expression='Primary_Email', left=12.5*cm,style={'alignment': TA_LEFT}),
#                ObjectValue(expression='Number_of_products', left=9.0*cm,style={'alignment': TA_LEFT}),#, get_value=lambda instance: instance.people_acc.acc_no.balance.str('%s')),
#                ObjectValue(expression='id', left=8.8*cm,style={'alignment': TA_RIGHT}),
#                ObjectValue(expression='inst_id', left=11*cm,style={'alignment': TA_RIGHT}),
            ]
        borders = {'all': True}
        class band_page_header(ReportBand):
            height = 1.3*cm
            elements = [
                SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                    style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
                SystemField(expression=u'Page %(page_number)d of %(page_count)d', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                Label(text="Asset Name", top=0.8*cm, left=0.6*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Tag-ID", top=0.8*cm, left=3.4*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Employee-TagID", top=0.8*cm, left=6.5*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Entry_Time", top=0.8*cm, left=9.5*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Exit_Time", top=0.8*cm, left=12.5*cm, style={'fontName': 'Helvetica-Bold'}),
                Label(text="Checkpoint", top=0.8*cm, left=15.5*cm, style={'fontName': 'Helvetica-Bold'}),
#                Label(text="Primary_Email", top=0.8*cm, left=12.5*cm, style={'fontName': 'Helvetica-Bold'}),
#                Label(text="Txn No", top=0.8*cm, left=12.6*cm, style={'fontName': 'Helvetica-Bold'}),
#                Label(text="PGID/", top=0.4*cm, left=14.6*cm, style={'fontName': 'Helvetica-Bold'}),
#                Label(text="Staff ID", top=0.8*cm, left=14.6*cm, style={'fontName': 'Helvetica-Bold'}),
            ]
            borders = {'all': True}
