from matplotlib.pylab import *
from django.template.defaultfilters import title
from reportlab.graphics.charts import axes
from ImageShow import show
from geraldo import Report

# make a square figure and axes
class ast_repo(Report):
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    
    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Asset Name', 'Department', 'Employee', 'Date_of_assign', 'Date_of_return'
    fracs = [15, 30, 45, 10,15]
    explode=(0, 0, 0, 0.05,0)
    
    pie(fracs, explode=explode, labels=labels,
                    autopct='%1.1f%%', shadow=True)
                    # The default startangle is 0, which would start
                    # the Frogs slice on the x-axis.  With startangle=90,
                    # everything is rotated counter-clockwise by 90 degrees,
                    # so the plotting starts on the positive y-axis.
    
    title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
    
    show()