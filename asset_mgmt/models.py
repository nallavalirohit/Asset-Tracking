from UAM.models import People
from django.db import models


class Asset_Class(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = False, blank = True)
    def __str__(self):
        return '%s' %(self.name)

class Asset_Type(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
#    desccs = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Asset_Category(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Asset_Security(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Asset_Priority(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Asset_Stage(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Asset_Req_Type(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Asset_Event(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Role(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Reader(models.Model):
    name = models.CharField(max_length = 100)
    ip = models.IPAddressField()
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Gate(models.Model):
    name = models.CharField(max_length = 100)
    reader = models.ForeignKey(Reader, null=True)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Door(models.Model):
    name = models.CharField(max_length = 100)
    reader = models.ForeignKey(Reader, null=True)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Asset_Status(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Asset_Discovery(models.Model):
    name = models.CharField(max_length = 100)
    model_no = models.CharField(max_length = 100)
    qty = models.IntegerField()
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Asset_Manufacture(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class warranty(models.Model):
    mnfr_date = models.DateField()
    exp_date = models.DateField()
    Asset_Manufacture = models.ForeignKey(Asset_Manufacture)
    made_in = models.CharField(max_length = 100)
    def __str__(self):
        return '%s' %(self.exp_date) 
    
class Asset(models.Model):
    name = models.CharField(max_length = 100)
    model_no = models.CharField(max_length = 100)
    barcode = models.CharField(max_length = 100)
    serial_no = models.CharField(max_length = 100)
    asset_category = models.ForeignKey(Asset_Category, blank = True)
    asset_class = models.ForeignKey(Asset_Class, blank = True)
    security = models.ForeignKey(Asset_Security, blank = True)
    asset_status = models.ForeignKey(Asset_Status)
    asset_type = models.ForeignKey(Asset_Type)
    enter_date = models.DateTimeField(auto_now_add = True)
    #asset_associate = models.ForeignKey(Asset, related_name = 'associated', null = True)
    priority = models.ForeignKey(Asset_Priority)
    warranty = models.ForeignKey(warranty)
    created_date = models.DateTimeField()
#   created_by = models.DateTimeField()   
    updated_date = models.DateTimeField()   
#   updated_by = models.DateTimeField() 
    def __str__(self):
        return '%s' %(self.name)
    
class Asset_tag_map(models.Model):
    Asset = models.ForeignKey(Asset)
    TagID = models.CharField(max_length = 100)
    def __str__(self):
        return '%s''-''%s' %(self.Asset, self.TagID)

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    ) 
class Person(models.Model):
    First_Name = models.CharField(max_length = 100)
    Last_Name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 100, choices = GENDER_CHOICES)
    Address = models.CharField(max_length = 100)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Image = models.ImageField(upload_to = 'C:\Documents and Settings\All Users\Documents\My Pictures\Sample Pictures', blank = True)
    def __str__(self):
        return '%s' %(self.First_Name)
    
class Feature_Type(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    priority = models.ForeignKey(Asset_Priority)
    def __str__(self):
        return '%s' %(self.name)
    
class Stage_Event_Map(models.Model):
    before_stage = models.ForeignKey(Asset_Stage, related_name = 'previous')
    Asset_Event = models.ForeignKey(Asset_Event)
    next_stage = models.ForeignKey(Asset_Stage, related_name = 'next')
    def __str__(self):
        return '%s''-''%s''-''%s' %(self.before_stage, self.Asset_Event, self.next_stage)
      
class Class_Lifecycle(models.Model):
    Asset_Class = models.ForeignKey(Asset_Class)
    Stage_Event_Map = models.ForeignKey(Stage_Event_Map)
    
class Feature(models.Model):
    name = models.CharField(max_length = 100)
    Asset = models.ForeignKey(Asset)
    Feature_Type = models.ForeignKey(Feature_Type)
    def __str__(self):
        return '%s' %(self.name)
    
class Asset_Event_Stage_Map(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    Asset = models.ForeignKey(Asset)
    Stage_Event_Map = models.ForeignKey(Stage_Event_Map)
    time = models.TimeField()
    def __str__(self):
        return '%s''-''%s' %(self.Asset, self.Stage_Event_Map)
    
class Floor(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    Door = models.ForeignKey(Door)
    def __str__(self):
        return '%s' %(self.name)
    
class Building(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    Floor = models.ForeignKey(Floor)
    def __str__(self):
        return '%s' %(self.name)
    
class Sublocation(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    Building = models.ForeignKey(Building)
    def __str__(self):
        return '%s' %(self.name)
    
class Location(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    Sublocation = models.ForeignKey(Sublocation)
    def __str__(self):
        return '%s' %(self.name)
    
class Checkpoint(models.Model):
    Location = models.ForeignKey(Location)
    Sublocation = models.ForeignKey(Sublocation)
    Building = models.ForeignKey(Building)
    Floor = models.ForeignKey(Floor)
    Door = models.ForeignKey(Door)
    Gate = models.ForeignKey(Gate)
    def __str__(self):
        return '%s' %(self.Gate)
    
    
class Designation(models.Model):
    name = models.CharField(max_length = 100)
    abbr = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Employee_Status(models.Model):
    status = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.status)
    
class Division(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    Location = models.ForeignKey(Location)
    def __str__(self):
        return '%s' %(self.name)
    
class Department(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    abbr = models.CharField(max_length = 100)
    Division = models.ForeignKey(Division)
    Location = models.ForeignKey(Location)
    def __str__(self):
        return '%s' %(self.name)
    
class Employee(models.Model):
    Join_Date = models.DateField()
    Salary = models.FloatField()
    Department = models.ForeignKey(Department)
    People = models.ForeignKey(People)
    Designation = models.ForeignKey(Designation)
    Employee_Status = models.ForeignKey(Employee_Status)
    def __str__(self):
        return '%s' %(self.People)
    
class Employee_Role_Map(models.Model):
    Employee = models.ForeignKey(Employee)
    Role = models.ForeignKey(Role)
    def __str__(self):
        return '%s''--''%s'%(self.Role, self.Employee)
    
class Asset_Assignment(models.Model):
    Asset_id = models.CharField(max_length = 50)
    Department = models.ForeignKey(Department)
    Date_of_return = models.DateField()
    Date_of_assign = models.DateTimeField(auto_now = True, blank = True, editable = False)
    def __str__(self):
        return '%s''----''%s''----''%s' %(self.Asset_id, self.Department, self.Department)
    
class Asset_Assignment_Employee(models.Model):
    Asset = models.ForeignKey(Asset)
    Department = models.ForeignKey(Department)
    Employee = models.ForeignKey(Employee)
    Tag_ID =  models.CharField(max_length = 50)
    Date_of_return = models.DateField()
    Date_of_assign = models.DateTimeField(auto_now = True, blank = True, editable = False)
    def __str__(self):
        return '%s''----''%s''----''%s' %(self.Asset_id, self.Department, self.Employee)
    
class Asset_Track(models.Model):
    Asset = models.ForeignKey(Asset)
    ast_emp = models.ForeignKey(Asset_Assignment_Employee)
    TagID = models.CharField(max_length = 100)
    reader = models.ForeignKey(Reader)
    E_TagID = models.CharField(max_length = 100)
    Entry_Time = models.TimeField()
    Exit_Time = models.TimeField()
    Date_Time = models.DateTimeField()
    Associate_Flag = models.BooleanField()
    Asset_in_flag = models.BooleanField()
    Asset_out_flag = models.BooleanField()
    Checkpoint = models.ForeignKey(Checkpoint)
    def __str__(self):
        return '%s' %(self.Asset)
    
class Asset_Trace(models.Model):
    Asset = models.ForeignKey(Asset)
    ast_emp = models.ForeignKey(Asset_Assignment_Employee)
    TagID = models.CharField(max_length = 100)
    reader = models.ForeignKey(Reader)    
    door = models.ForeignKey(Door)
    Entry_Time = models.TimeField()
    Exit_Time = models.TimeField()
    def __str__(self):
        return '%s' %(self.Asset)

class Access(models.Model):
    name = models.CharField(max_length = 100)
    Type = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    
class Access_Role_Map(models.Model):
    Role = models.ForeignKey(Role)
    Access = models.ForeignKey(Access)
    
class Team(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    size = models.CharField(max_length = 100)
    Department = models.ForeignKey(Department)
    def __str__(self):
        return '%s' %(self.name)
    
class Request_Status(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    def __str__(self):
        return '%s' %(self.name)
    
class Request(models.Model):
    Request_Sub = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    Asset_Req_Type = models.ForeignKey(Asset_Req_Type)
    Department = models.ForeignKey(Department)
    Request_Status = models.ForeignKey(Request_Status)
    Employee = models.ForeignKey(Employee)
    Date_Time = models.DateTimeField()
    def __str__(self):
        return '%s' %(self.Request_Sub)
    
class Dept_rule(models.Model):
    Department = models.ForeignKey(Department)
    Asset = models.ForeignKey(Asset)
    desc = models.CharField(max_length = 255, null = True, blank = True)
    
class Gate_rule(models.Model):
    Gate = models.ForeignKey(Gate)
    Asset = models.ForeignKey(Asset)
    desc = models.CharField(max_length = 255, null = True, blank = True) 