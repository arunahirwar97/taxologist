# from functools import _Descriptor
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from core.storage_backends import PrivateMediaStorage,PublicMediaStorage
from ckeditor.fields import RichTextField

# Create your models here.
BUSINESS_CATAGORY = (
    # ("sp","Salaried Person"),         
    ("ptn","Partnership"),
    ("pco","Private Company/OPC"),
    ("pc","Public Company"),
    ("nc","NPO Company"),
    ("sngo","Sociaty/NGO"),
    ("sp","Sole proprietor"),
    ("nri","NRI"),
)
class Business_Profile(models.Model):
    # first_name = models.CharField(max_length=20)
    # email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bussines_catagory = models.CharField(choices=BUSINESS_CATAGORY,max_length=4,blank=True)
    # choise = models.ch
    name = models.CharField(max_length=50,blank=True)
    firm_name = models.CharField(max_length=50, blank=True)
    company_name = models.CharField(max_length=50, blank=True)
    c_i_n = models.CharField(max_length=50, blank=True)
    pan_number = models.CharField(max_length=30,blank=True)
    mobile_number = models.CharField(max_length=12,blank=True)
    email = models.EmailField(blank=True)
    r_no_c_i_n = models.CharField(max_length=50,blank=True)
    registration_number = models.CharField(max_length=50,blank=True)
    u_i_n = models.CharField(max_length=50,blank=True)

    # pan_number = models.CharField(max_length=20, default='none', blank=True)
    tan_number = models.CharField(max_length=20, default='none', blank=True)
    account_number = models.CharField(max_length=30,default='none', blank=True)
    ifsc_code = models.CharField(max_length=20, default='none', blank=True)
    bank_name = models.CharField(max_length=100,default='none', blank=True)
    postal_code = models.CharField(max_length=20, default='none', blank=True)
    aadhar_number = models.CharField(max_length=20, default='none', blank=True)




# from os import truncate
# from django.core.files import storage
# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.fields import files 

# class terms_and_conndition_with_privacy_policy1(models.Model):
#     PAGE_CHOICES = (
#         ('TAC', 'Terms And Connditions'),
#         ('PAP', 'Privacy And Policy'),
#     )
#     page = models.CharField(max_length=3,choices=PAGE_CHOICES, null=True, blank=True)
#     title_condition = models.CharField(max_length=50, null=True, blank=True)
#     title = models.CharField(max_length=100000, null=True, blank=True)
#     Paragraph = models.CharField(max_length=100000, null=True, blank=True)

#     def __str__(self):
#         return self.page
# # Create your models here.
# class assistanceexpertcalldata(models.Model):
#     user_name = models.CharField(blank=True, null=True, max_length=500)
#     email = models.CharField(blank=True, null=True, max_length=500)
#     contact_number = models.CharField(blank=True, null=True, max_length=500)
#     calling_status = models.CharField(blank=True, null=True, max_length=500)
#     current_time = models.CharField(blank=True, null=True, max_length=500)
#     current_date = models.CharField(blank=True, null=True, max_length=500)
#     def __str__(self):
#         return self.user_name


class BUSINESS_GST_DASHBAORD_XMLFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) 
    # json_file = models.FileField(upload_to="business_dashbaord/gst/",storage=PrivateMediaStorage())
    json_file = models.FileField(upload_to="business_dashbaord/gst/")




class BUSINESS_GST_DASHBOARD_XMLFileData(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    # start Form_ITR1
    legal_name = models.CharField(blank=True, null=True, max_length=500)
    gst_number = models.CharField(blank=True, null=True, max_length=500)
    gst_paid = models.CharField(blank=True, null=True, max_length=500)
    itc = models.CharField(blank=True, null=True, max_length=500)
    cash_legar = models.CharField(blank=True, null=True, max_length=500)
    credit_legar = models.CharField(blank=True, null=True, max_length=500)
    year = models.CharField(blank=True, null=True, max_length=500)
    total_sales = models.CharField(blank=True, null=True, max_length=500)
    total_gst = models.CharField(blank=True, null=True, max_length=500)
    total_revenue = models.CharField(blank=True, null=True, max_length=500)





class business_gst_dashboard_checklist_selectbox(models.Model):
    checklist_select = models.CharField(blank=True, null=True, max_length=500)
    class Meta:
        verbose_name = 'gst-dashboard-checklist-selectbox'  

    def __str__(self):
        return self.checklist_select



class business_gst_dashboard_checklist_selectbox_main_data(models.Model):
    checklist  = models.ForeignKey(business_gst_dashboard_checklist_selectbox, on_delete=models.CASCADE,null=True,blank=True)
    checklist_data = models.CharField(blank=True, null=True, max_length=500)
    checklist_data_id = models.IntegerField()
    class Meta:
        verbose_name = ' gst checklist-selectbox-data'  

    def __str__(self):
        return self.checklist_data


class business_gst_dahsboard_registrations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    user_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    gst_number = models.CharField(max_length=15,blank=True,null=True)
    reg_status = models.CharField(max_length=20,blank=True,null=True)
    xmlfile = models.FileField(upload_to="registration_xml_file")
    class Meta:
        verbose_name = 'gst-dahsboard registrations Without XML Registration'  
    
    def __str__(self):
        return self.name



class business_gst_dashbaord_super_user_registrations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True,null=True)
    gst_number = models.CharField(max_length=15)
    reg_status = models.CharField(max_length=20)
    xmlfile = models.FileField(upload_to="business_incometax_dashbaord_super_user_registrations")
    class Meta:
        verbose_name = 'gst-dashbaord-super-user-registrations without XML Registration'  
    
    def __str__(self):
        return self.name












class BUSINESS_INCOME_TAX_DASHBAORD_XMLFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) 
    xmlfile = models.FileField(upload_to="business_income_tax/xml_file/")
    # xmlfile = models.FileField(upload_to="business_income_tax/xml_file/",storage=PrivateMediaStorage())


class BUSINESS_INCOME_TAX_DASHBAORD_JSON_File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) 
    json_file = models.FileField(upload_to="business_income_tax/xml_file/")
    # xmlfile = models.FileField(upload_to="business_income_tax/xml_file/",storage=PrivateMediaStorage())


class BUSINESS_INCOME_TAX_DASHBAORD_JSON_FILEDATA(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    xmlns_ns3 = models.CharField(max_length = 1000,blank=True, null=True)
    xmlns = models.CharField(max_length = 1000,blank=True, null=True)
    xmlns_ns2 = models.CharField(max_length = 1000,blank=True, null=True)
    XMLCreatedBy = models.CharField(max_length = 1000,blank=True, null=True)
    XMLCreationDate = models.CharField(max_length = 1000,blank=True, null=True)
    SWVersionNo = models.CharField(max_length = 1000,blank=True, null=True,)
    SWCreatedBy = models.CharField(max_length = 1000,blank=True, null=True,)
    JSONCreatedBy = models.CharField(max_length = 1000,blank=True, null=True,)
    JSONCreationDate = models.CharField(max_length = 1000,blank=True, null=True,)
    Digest = models.CharField(max_length = 1000,blank=True, null=True,)
    IntermediaryCity = models.CharField(max_length = 1000,blank=True, null=True,)
    FormName = models.CharField(max_length = 1000,blank=True, null=True,)
    Description = models.CharField(max_length = 1000,blank=True, null=True,)
    AssessmentYear = models.CharField(max_length = 1000,blank=True, null=True,)
    SchemaVer = models.CharField(max_length = 1000,blank=True, null=True,)
    FormVer = models.CharField(max_length = 1000,blank=True, null=True,)
    FirstName = models.CharField(max_length = 1000,blank=True, null=True,)
    SurNameOrOrgName = models.CharField(max_length = 1000,blank=True, null=True,)
    ResidenceNo = models.CharField(max_length = 1000,blank=True, null=True,)
    ResidenceName = models.CharField(max_length = 1000,blank=True, null=True,)
    RoadOrStreet = models.CharField(max_length = 1000,blank=True, null=True,)
    LocalityOrArea = models.CharField(max_length = 1000,blank=True, null=True,)
    CityOrTownOrDistrict = models.CharField(max_length = 1000,blank=True, null=True,)
    StateCode = models.CharField(max_length = 1000,blank=True, null=True,)
    CountryCode = models.CharField(max_length = 1000,blank=True, null=True,)
    PinCode = models.CharField(max_length = 1000,blank=True, null=True,)
    CountryCodeMobile = models.CharField(max_length = 1000,blank=True, null=True,)
    MobileNo = models.CharField(max_length = 1000,blank=True, null=True,)
    EmailAddress = models.CharField(max_length = 1000,blank=True, null=True,)
    PAN = models.CharField(max_length = 1000,blank=True, null=True,)
    DOB = models.CharField(max_length = 1000,blank=True, null=True,)
    EmployerCategory = models.CharField(max_length = 1000,blank=True, null=True,)
    AadhaarCardNo = models.CharField(max_length = 1000,blank=True, null=True,)
    ReturnFileSec = models.CharField(max_length = 1000,blank=True, null=True,)
    NewTaxRegime = models.CharField(max_length = 1000,blank=True, null=True,)
    SeventhProvisio139 = models.CharField(max_length = 1000,blank=True, null=True,)
    ReturnType = models.CharField(max_length = 1000,blank=True, null=True,)
    ResidentialStatus = models.CharField(max_length = 1000,blank=True, null=True,)
    PortugeseCC5A = models.CharField(max_length = 1000,blank=True, null=True,)
    DepAmtAggAmtExcd1CrPrYrFlg = models.CharField(max_length = 1000,blank=True, null=True,)
    IncrExpAggAmt2LkTrvFrgnCntryFlg = models.CharField(max_length = 1000,blank=True, null=True,)
    IncrExpAggAmt1LkElctrctyPrYrFlg = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalAllwncExemptUs10 = models.CharField(max_length = 1000,blank=True, null=True,)
    OthSrcNatureDesc = models.CharField(max_length = 1000,blank=True, null=True,)
    OthSrcOthNatOfInc = models.CharField(max_length = 1000,blank=True, null=True,)
    OthSrcOthAmount = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80C = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80CCC = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80CCDEmployeeOrSE = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80CCD1B = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80CCDEmployer = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80D = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80DD = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80DDB = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80E = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80EE = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80EEA = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80GG = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80GGA = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80GGC = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80U = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80TTA = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80TTB = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80RRB = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80QQB = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80CCG = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalChapVIADeductions = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80G = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80C = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80CCC = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80CCDEmployeeOrSE = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80CCD1B = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80CCDEmployer = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80D = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80DD = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80DDB = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80E = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80EE = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80EEA = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80EEB = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80G = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80GG = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80GGA = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80GGC = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80U = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80TTA = models.CharField(max_length = 1000,blank=True, null=True,)
    Section80TTB = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalChapVIADeductions = models.CharField(max_length = 1000,blank=True, null=True,)
    ExemptIncAgriOthUs10Total = models.CharField(max_length = 1000,blank=True, null=True,)
    GrossSalary = models.CharField(max_length = 1000,blank=True, null=True,)
    Salary = models.CharField(max_length = 1000,blank=True, null=True,)
    PerquisitesValue = models.CharField(max_length = 1000,blank=True, null=True,)
    ProfitsInSalary = models.CharField(max_length = 1000,blank=True, null=True,)
    NetSalary = models.CharField(max_length = 1000,blank=True, null=True,)
    TaxPaidlocalAuth = models.CharField(max_length = 1000,blank=True, null=True,)
    DeductionUs16 = models.CharField(max_length = 1000,blank=True, null=True,)
    DeductionUs16ia = models.CharField(max_length = 1000,blank=True, null=True,)
    EntertainmentAlw16ii = models.CharField(max_length = 1000,blank=True, null=True,)
    ProfessionalTaxUs16iii = models.CharField(max_length = 1000,blank=True, null=True,)
    IncomeFromSal = models.CharField(max_length = 1000,blank=True, null=True,)
    TypeOfHP = models.CharField(max_length = 1000,blank=True, null=True,)
    GrossRentReceived = models.CharField(max_length = 1000,blank=True, null=True,)
    AnnualValue = models.CharField(max_length = 1000,blank=True, null=True,)
    StandardDeduction = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalIncomeOfHP = models.CharField(max_length = 1000,blank=True, null=True,)
    IncomeOthSrc = models.CharField(max_length = 1000,blank=True, null=True,)
    DeductionUs57iia = models.CharField(max_length = 1000,blank=True, null=True,)
    GrossTotIncome = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalIncome = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalDonationsUs80GGA = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalDonationAmtCash80GGA = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalDonationAmtOtherMode80GGA = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalEligibleDonationAmt80GGA = models.CharField(max_length = 1000,blank=True, null=True,)
    IntrstPayUs234A = models.CharField(max_length = 1000,blank=True, null=True,)
    IntrstPayUs234B = models.CharField(max_length = 1000,blank=True, null=True,)
    IntrstPayUs234C = models.CharField(max_length = 1000,blank=True, null=True,)
    LateFilingFee234F = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalTaxPayable = models.CharField(max_length = 1000,blank=True, null=True,)
    Rebate87A = models.CharField(max_length = 1000,blank=True, null=True,)
    TaxPayableOnRebate = models.CharField(max_length = 1000,blank=True, null=True,)
    EducationCess = models.CharField(max_length = 1000,blank=True, null=True,)
    GrossTaxLiability = models.CharField(max_length = 1000,blank=True, null=True,)
    Section89 = models.CharField(max_length = 1000,blank=True, null=True,)
    NetTaxLiability = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalIntrstPay = models.CharField(max_length = 1000,blank=True, null=True,)
    TotTaxPlusIntrstPay = models.CharField(max_length = 1000,blank=True, null=True,)
    AdvanceTax = models.CharField(max_length = 1000,blank=True, null=True,)
    TDS = models.CharField(max_length = 1000,blank=True, null=True,)
    TCS = models.CharField(max_length = 1000,blank=True, null=True,)
    SelfAssessmentTax = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalTaxesPaid = models.CharField(max_length = 1000,blank=True, null=True,)
    BalTaxPayable = models.CharField(max_length = 1000,blank=True, null=True,)
    ExcIncSec1038 = models.CharField(max_length = 1000,blank=True, null=True,)
    ExcIncSec1034 = models.CharField(max_length = 1000,blank=True, null=True,)
    IFSCCode = models.CharField(max_length = 1000,blank=True, null=True,)
    BankName = models.CharField(max_length = 1000,blank=True, null=True,)
    InterestPayable = models.CharField(max_length = 1000,blank=True, null=True)
    BankAccountNo = models.CharField(max_length = 1000,blank=True, null=True,)
    UseForRefund = models.CharField(max_length = 1000,blank=True, null=True,)
    RefundDue = models.CharField(max_length = 1000,blank=True, null=True,)
    DepPayInvClmUndDednVIA = models.CharField(max_length = 1000,blank=True, null=True)
    TotDon100PercentCash = models.CharField(max_length = 1000,blank=True, null=True,)
    TotDon100PercentOtherMode = models.CharField(max_length = 1000,blank=True, null=True,)
    TotDon100Percent = models.CharField(max_length = 1000,blank=True, null=True,)
    TotEligibleDon100Percent = models.CharField(max_length = 1000,blank=True, null=True,)
    TotDon50PercentNoApprReqdCash = models.CharField(max_length = 1000,blank=True, null=True,)
    TotDon50PercentNoApprReqdOtherMode = models.CharField(max_length = 1000,blank=True, null=True,)
    TotDon50PercentNoApprReqd = models.CharField(max_length = 1000,blank=True, null=True,)
    TotEligibleDon50Percent = models.CharField(max_length = 1000,blank=True, null=True,)
    TotDon100PercentApprReqdCash = models.CharField(max_length = 1000,blank=True, null=True,)
    TotDon100PercentApprReqdOtherMode = models.CharField(max_length = 1000,blank=True, null=True,)
    TotDon100PercentApprReqd = models.CharField(max_length = 1000,blank=True, null=True,)
    TotEligibleDon100PercentApprReqd = models.CharField(max_length = 1000,blank=True, null=True,)
    TotDon50PercentApprReqdCash = models.CharField(max_length = 1000,blank=True, null=True,)
    TotDon50PercentApprReqdOtherMode = models.CharField(max_length = 1000,blank=True, null=True,)
    TotDon50PercentApprReqd = models.CharField(max_length = 1000,blank=True, null=True,)
    TotEligibleDon50PercentApprReqd = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalDonationsUs80GCash = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalDonationsUs80GOtherMode = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalDonationsUs80G = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalEligibleDonationsUs80G = models.CharField(max_length = 1000,blank=True, null=True,)
    SeniorCitizenFlag = models.CharField(max_length = 1000,blank=True, null=True,)
    SelfAndFamily = models.CharField(max_length = 1000,blank=True, null=True,)
    SelfAndFamilySeniorCitizen = models.CharField(max_length = 1000,blank=True, null=True,)
    ParentsSeniorCitizenFlag = models.CharField(max_length = 1000,blank=True, null=True,)
    HealthInsPremSlfFam = models.CharField(max_length = 1000,blank=True, null=True)
    ScheduleDI = models.CharField(max_length = 1000,blank=True, null=True)
    Parents = models.CharField(max_length = 1000,blank=True, null=True,)
    PrevHlthChckUpSlfFamSrCtzn = models.CharField(max_length = 1000,blank=True, null=True)
    MedicalExpSlfFamSrCtzn = models.CharField(max_length = 1000,blank=True, null=True)
    ParentsSeniorCitizen = models.CharField(max_length = 1000,blank=True, null=True,)
    HlthInsPremSlfFamSrCtzn = models.CharField(max_length = 1000,blank=True, null=True)
    HlthInsPremParents = models.CharField(max_length = 1000,blank=True, null=True)
    EligibleAmountOfDedn = models.CharField(max_length = 1000,blank=True, null=True,)
    HlthInsPremParentsSrCtzn = models.CharField(max_length = 1000,blank=True, null=True)
    PrevHlthChckUpParentsSrCtzn = models.CharField(max_length = 1000,blank=True, null=True)
    MedicalExpParentsSrCtzn = models.CharField(max_length = 1000,blank=True, null=True)
    TotalTDSonSalaries = models.CharField(max_length = 1000,blank=True, null=True,)
    TaxExmpIntInc = models.CharField(max_length = 1000,blank=True, null=True,)
    TAN = models.CharField(max_length = 1000,blank=True, null=True)
    EmployerOrDeductorOrCollecterName = models.CharField(max_length = 1000,blank=True, null=True)
    IncChrgSal = models.CharField(max_length = 1000,blank=True, null=True)
    TotalTDSSal = models.CharField(max_length = 1000,blank=True, null=True)
    PrevHlthChckUpParents = models.CharField(max_length = 1000,blank=True, null=True)
    TotalTDSonOthThanSals = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalTDS3Details = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalSchTCS = models.CharField(max_length = 1000,blank=True, null=True,)
    PrevHlthChckUpSlfFam = models.CharField(max_length = 1000,blank=True, null=True)
    TotalTaxPayments = models.CharField(max_length = 1000,blank=True, null=True,)
    AssesseeVerName = models.CharField(max_length = 1000,blank=True, null=True,)
    FatherName = models.CharField(max_length = 1000,blank=True, null=True,)
    AssesseeVerPAN = models.CharField(max_length = 1000,blank=True, null=True,)
    Capacity = models.CharField(max_length = 1000,blank=True, null=True,)
    Place = models.CharField(max_length = 1000,blank=True, null=True,)
    Date = models.CharField(max_length = 1000,blank=True, null=True,)

class BUSINESS_INCOME_TAX_DASHBOARD_XMLFileData(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    # start Form_ITR1
    xmlns_ns3 = models.CharField(max_length = 1000,blank=True, null=True)
    xmlns = models.CharField(max_length = 1000,blank=True, null=True)
    xmlns_ns2 = models.CharField(max_length = 1000,blank=True, null=True)
    SWVersionNo = models.CharField(max_length = 1000,blank=True, null=True)
    SWCreatedBy = models.CharField(max_length = 1000,blank=True, null=True)
    XMLCreatedBy = models.CharField(max_length = 1000,blank=True, null=True)
    XMLCreationDate = models.CharField(max_length = 1000,blank=True, null=True)
    IntermediaryCity = models.CharField(max_length = 1000,blank=True, null=True)
    Digest = models.CharField(max_length = 1000,blank=True, null=True)
    FormName = models.CharField(max_length = 1000,blank=True, null=True)
    Description = models.CharField(max_length = 1000,blank=True, null=True)
    AssessmentYear = models.CharField(max_length = 1000,blank=True, null=True)
    SchemaVer = models.CharField(max_length = 1000,blank=True, null=True)
    FormVer = models.CharField(max_length = 1000,blank=True, null=True)
    FirstName = models.CharField(max_length = 1000,blank=True, null=True)
    SurNameOrOrgName = models.CharField(max_length = 1000,blank=True, null=True)
    PAN = models.CharField(max_length = 1000,blank=True, null=True)
    ResidenceNo = models.CharField(max_length = 1000,blank=True, null=True)
    RoadOrStreet = models.CharField(max_length = 1000,blank=True, null=True)
    LocalityOrArea = models.CharField(max_length = 1000,blank=True, null=True)
    CityOrTownOrDistrict = models.CharField(max_length = 1000,blank=True, null=True)
    StateCode = models.CharField(max_length = 1000,blank=True, null=True)
    CountryCode = models.CharField(max_length = 1000,blank=True, null=True)
    PinCode = models.CharField(max_length = 1000,blank=True, null=True)
    CountryCodeMobile = models.CharField(max_length = 1000,blank=True, null=True)
    MobileNo = models.CharField(max_length = 1000,blank=True, null=True)
    EmailAddress = models.CharField(max_length = 1000,blank=True, null=True)
    DOB = models.CharField(max_length = 1000,blank=True, null=True)
    EmployerCategory = models.CharField(max_length = 1000,blank=True, null=True)
    AadhaarCardNo = models.CharField(max_length = 1000,blank=True, null=True)
    ReturnFileSec = models.CharField(max_length = 1000,blank=True, null=True)
    SeventhProvisio139 = models.CharField(max_length = 1000,blank=True, null=True)
    GrossSalary = models.CharField(max_length = 1000,blank=True, null=True)
    Salary = models.CharField(max_length = 1000,blank=True, null=True)
    PerquisitesValue = models.CharField(max_length = 1000,blank=True, null=True)
    ProfitsInSalary = models.CharField(max_length = 1000,blank=True, null=True)
    TotalAllwncExemptUs10 = models.CharField(max_length = 1000,blank=True, null=True)
    NetSalary = models.CharField(max_length = 1000,blank=True, null=True)
    DeductionUs16 = models.CharField(max_length = 1000,blank=True, null=True)
    DeductionUs16ia = models.CharField(max_length = 1000,blank=True, null=True)
    EntertainmentAlw16ii = models.CharField(max_length = 1000,blank=True, null=True)
    ProfessionalTaxUs16iii = models.CharField(max_length = 1000,blank=True, null=True)
    IncomeFromSal = models.CharField(max_length = 1000,blank=True, null=True)
    TypeOfHP = models.CharField(max_length = 1000,blank=True, null=True)
    GrossRentReceived = models.CharField(max_length = 1000,blank=True, null=True)
    TaxPaidlocalAuth = models.CharField(max_length = 1000,blank=True, null=True)
    AnnualValue = models.CharField(max_length = 1000,blank=True, null=True)
    StandardDeduction = models.CharField(max_length = 1000,blank=True, null=True)
    InterestPayable = models.CharField(max_length = 1000,blank=True, null=True)
    TotalIncomeOfHP = models.CharField(max_length = 1000,blank=True, null=True)
    IncomeOthSrc = models.CharField(max_length = 1000,blank=True, null=True)
    DeductionUs57iia = models.CharField(max_length = 1000,blank=True, null=True)
    GrossTotIncome = models.CharField(max_length = 1000,blank=True, null=True)
    DepPayInvClmUndDednVIA = models.CharField(max_length = 1000,blank=True, null=True)
    Section80C = models.CharField(max_length = 1000,blank=True, null=True)
    Section80CCC = models.CharField(max_length = 1000,blank=True, null=True)
    Section80CCDEmployeeOrSE = models.CharField(max_length = 1000,blank=True, null=True)
    Section80CCD1B = models.CharField(max_length = 1000,blank=True, null=True)
    Section80CCDEmployer = models.CharField(max_length = 1000,blank=True, null=True)
    Section80D = models.CharField(max_length = 1000,blank=True, null=True)
    Section80DD = models.CharField(max_length = 1000,blank=True, null=True)
    Section80DDB = models.CharField(max_length = 1000,blank=True, null=True)
    Section80E = models.CharField(max_length = 1000,blank=True, null=True)
    Section80EE = models.CharField(max_length = 1000,blank=True, null=True)
    Section80EEA = models.CharField(max_length = 1000,blank=True, null=True)
    Section80EEB = models.CharField(max_length = 1000,blank=True, null=True)
    Section80G = models.CharField(max_length = 1000,blank=True, null=True)
    Section80GG = models.CharField(max_length = 1000,blank=True, null=True)
    Section80GGA = models.CharField(max_length = 1000,blank=True, null=True)
    Section80GGC = models.CharField(max_length = 1000,blank=True, null=True)
    Section80U = models.CharField(max_length = 1000,blank=True, null=True)
    Section80TTA = models.CharField(max_length = 1000,blank=True, null=True)
    Section80TTB = models.CharField(max_length = 1000,blank=True, null=True)
    TotalChapVIADeductions = models.CharField(max_length = 1000,blank=True, null=True)
    Section80C = models.CharField(max_length = 1000,blank=True, null=True)
    Section80CCC = models.CharField(max_length = 1000,blank=True, null=True)
    Section80CCDEmployeeOrSE = models.CharField(max_length = 1000,blank=True, null=True)
    Section80CCD1B = models.CharField(max_length = 1000,blank=True, null=True)
    Section80CCDEmployer = models.CharField(max_length = 1000,blank=True, null=True)
    Section80D = models.CharField(max_length = 1000,blank=True, null=True)
    Section80DD = models.CharField(max_length = 1000,blank=True, null=True)
    Section80DDB = models.CharField(max_length = 1000,blank=True, null=True)
    Section80E = models.CharField(max_length = 1000,blank=True, null=True)
    Section80EE = models.CharField(max_length = 1000,blank=True, null=True)
    Section80EEA = models.CharField(max_length = 1000,blank=True, null=True)
    Section80EEB = models.CharField(max_length = 1000,blank=True, null=True)
    Section80G = models.CharField(max_length = 1000,blank=True, null=True)
    Section80GG = models.CharField(max_length = 1000,blank=True, null=True)
    Section80GGA = models.CharField(max_length = 1000,blank=True, null=True)
    Section80GGC = models.CharField(max_length = 1000,blank=True, null=True)
    Section80U = models.CharField(max_length = 1000,blank=True, null=True)
    Section80TTA = models.CharField(max_length = 1000,blank=True, null=True)
    Section80TTB = models.CharField(max_length = 1000,blank=True, null=True)
    TotalChapVIADeductions = models.CharField(max_length = 1000,blank=True, null=True)
    TotalIncome = models.CharField(max_length = 1000,blank=True, null=True)
    TotalTaxPayable = models.CharField(max_length = 1000,blank=True, null=True)
    Rebate87A = models.CharField(max_length = 1000,blank=True, null=True)
    TaxPayableOnRebate = models.CharField(max_length = 1000,blank=True, null=True)
    EducationCess = models.CharField(max_length = 1000,blank=True, null=True)
    GrossTaxLiability = models.CharField(max_length = 1000,blank=True, null=True)
    Section89 = models.CharField(max_length = 1000,blank=True, null=True)
    NetTaxLiability = models.CharField(max_length = 1000,blank=True, null=True)
    TotalIntrstPay = models.CharField(max_length = 1000,blank=True, null=True)
    IntrstPayUs234A = models.CharField(max_length = 1000,blank=True, null=True)
    IntrstPayUs234B = models.CharField(max_length = 1000,blank=True, null=True)
    IntrstPayUs234C = models.CharField(max_length = 1000,blank=True, null=True)
    LateFilingFee234F = models.CharField(max_length = 1000,blank=True, null=True)
    TotTaxPlusIntrstPay = models.CharField(max_length = 1000,blank=True, null=True)
    AdvanceTax = models.CharField(max_length = 1000,blank=True, null=True)
    TDS = models.CharField(max_length = 1000,blank=True, null=True)
    TCS = models.CharField(max_length = 1000,blank=True, null=True)
    SelfAssessmentTax = models.CharField(max_length = 1000,blank=True, null=True)
    TotalTaxesPaid = models.CharField(max_length = 1000,blank=True, null=True)
    BalTaxPayable = models.CharField(max_length = 1000,blank=True, null=True)
    RefundDue = models.CharField(max_length = 1000,blank=True, null=True)
    IFSCCode = models.CharField(max_length = 1000,blank=True, null=True)
    BankName = models.CharField(max_length = 1000,blank=True, null=True)
    BankAccountNo = models.CharField(max_length = 1000,blank=True, null=True)
    UseForRefund = models.CharField(max_length = 1000,blank=True, null=True)
    ScheduleDI = models.CharField(max_length = 1000,blank=True, null=True)
    SeniorCitizenFlag = models.CharField(max_length = 1000,blank=True, null=True)
    SelfAndFamily = models.CharField(max_length = 1000,blank=True, null=True)
    HealthInsPremSlfFam = models.CharField(max_length = 1000,blank=True, null=True)
    SelfAndFamilySeniorCitizen = models.CharField(max_length = 1000,blank=True, null=True)
    HlthInsPremSlfFamSrCtzn = models.CharField(max_length = 1000,blank=True, null=True)
    PrevHlthChckUpSlfFam = models.CharField(max_length = 1000,blank=True, null=True)
    PrevHlthChckUpSlfFamSrCtzn = models.CharField(max_length = 1000,blank=True, null=True)
    MedicalExpSlfFamSrCtzn = models.CharField(max_length = 1000,blank=True, null=True)
    ParentsSeniorCitizenFlag = models.CharField(max_length = 1000,blank=True, null=True)
    Parents = models.CharField(max_length = 1000,blank=True, null=True)
    HlthInsPremParents = models.CharField(max_length = 1000,blank=True, null=True)
    PrevHlthChckUpParents = models.CharField(max_length = 1000,blank=True, null=True)
    ParentsSeniorCitizen = models.CharField(max_length = 1000,blank=True, null=True)
    HlthInsPremParentsSrCtzn = models.CharField(max_length = 1000,blank=True, null=True)
    PrevHlthChckUpParentsSrCtzn = models.CharField(max_length = 1000,blank=True, null=True)
    MedicalExpParentsSrCtzn = models.CharField(max_length = 1000,blank=True, null=True)
    EligibleAmountOfDedn = models.CharField(max_length = 1000,blank=True, null=True)
    TAN = models.CharField(max_length = 1000,blank=True, null=True)
    EmployerOrDeductorOrCollecterName = models.CharField(max_length = 1000,blank=True, null=True)
    IncChrgSal = models.CharField(max_length = 1000,blank=True, null=True)
    TotalTDSSal = models.CharField(max_length = 1000,blank=True, null=True)
    TotalTDSonSalaries = models.CharField(max_length = 1000,blank=True, null=True)
    AssesseeVerName = models.CharField(max_length = 1000,blank=True, null=True)
    FatherName = models.CharField(max_length = 1000,blank=True, null=True)
    AssesseeVerPAN = models.CharField(max_length = 1000,blank=True, null=True)
    Capacity = models.CharField(max_length = 1000,blank=True, null=True)
    Place = models.CharField(max_length = 1000,blank=True, null=True)

    
#     # xmlfile = models.FileField(upload_to="xml-data-files/",blank=True, null=True)





# class ManualForm16(models.Model):
#     first_name = models.TextField(blank=True, null=True)
#     middle_name = models.TextField(blank=True, null=True)
#     last_name = models.CharField(max_length=30,blank=True, null=True)
#     gender = models.CharField(max_length=30,blank=True,null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     father_name = models.CharField(max_length=30,blank=True,null=True)
#     merried_status = models.CharField(max_length=30,blank=True,null=True)
    
#     pan_number = models.CharField(max_length=20,blank=True, null=True)
#     tan_number = models.CharField(max_length=20,blank=True, null=True)
#     taxable_income_from_salary = models.CharField(max_length=20,blank=True, null=True)
#     gross_total_income = models.CharField(max_length=20,blank=True, null=True)
#     total_deductions = models.CharField(max_length=20,blank=True, null=True)
#     total_income = models.CharField(max_length=20,blank=True, null=True)


#     email = models.EmailField(blank=True, null=True)
     
#     pdf = models.FileField(upload_to="form-16-pdf/", blank=True, null=True,storage=PrivateMediaStorage())
#     # def __str__(self):
#     #     return self.first_name


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="update_profile")
#     email = models.EmailField()
#     first_name = models.CharField(max_length=20)
#     dob = models.DateField(null=True)
#     account_number = models.CharField(max_length=40,null=True, blank=True)
#     ifsc_code = models.CharField(max_length=20,null=True, blank=True)
#     bank_name = models.CharField(max_length=20,null=True, blank=True)
#     postal_code = models.CharField(max_length=20,null=True, blank=True)
#     aadhar_number = models.CharField(max_length=20,null=True, blank=True)
#     mobile_number = models.CharField(max_length=20,null=True, blank=True)
#     pan_number = models.CharField(max_length=20,null=True, blank=True)
#     profile_image = models.ImageField(upload_to='profile_images', null=True)
#     form_16_data = models.OneToOneField(ManualForm16, on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self.first_name



# class Referral_points(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     tree_plants = models.IntegerField(default=0)
#     list_of_referral = models.ManyToManyField(User, related_name="list_of_referral",default=0)
#     referral_id = models.IntegerField() 

# class Tax_Learn_video_category(models.Model):
#     category_name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.category_name

# class Tax_Learn_video(models.Model):
#     category = models.ForeignKey(Tax_Learn_video_category,on_delete=models.CASCADE,related_name='topic_content_type')
#     sub_category = models.CharField(max_length=100,unique=True)
#     unique_sub_category_name = models.CharField(max_length=500)
#     with_unique_sub_sub_category_name = models.CharField(max_length=500)
#     title = models.CharField(max_length=100,unique=True)
#     description = models.TextField(blank=True,null=True,default="")
#     video_url = models.TextField(blank=False,null=True)
#     video_image = models.ImageField(storage=PrivateMediaStorage(),upload_to="video_url_category/video_image/",blank = True,null=True)
    
#     def __str__(self):
#         return self.sub_category


#     # @staticmethod
#     # def get_all_video():
#     #     return Tax_Learn_video.objects.all()
    
#     # @staticmethod
#     # def get_all_video_by_id(category_id):
#     #     if category_id:
#     #         category = Tax_Learn_video_category.objects.get(id=category_id)
#     #         print(category)
#     #         return Tax_Learn_video.objects.filter(category=category)
#     #     else:
#     #         return Tax_Learn_video.get_all_video()



# class Tax_Plan_Page(models.Model):
    
#     name = models.CharField(max_length=100)
#     # heading = models.CharField(max_length=500)
#     order = models.IntegerField(null=True,blank=True)

#     def __str__(self):
#         return self.name

# class Tax_Plan_Block(models.Model):
#     page = models.ForeignKey(Tax_Plan_Page,on_delete=models.CASCADE)
#     heading = models.CharField(max_length=500)
#     # sub_heading = models.CharField(max_length=500)
#     order = models.IntegerField(null=True,blank=True)
    
#     class Meta:
#         verbose_name = 'Tax Planner'
        
#     def __str__(self):
#         return self.heading + " | " + self.page.name


# class Tax_Plan_Fields(models.Model):
#     block = models.ForeignKey(Tax_Plan_Block,on_delete=models.CASCADE)
#     question = models.CharField(max_length=500)
#     # anser = models.CharField(max_length=500)
#     # field_type = models.CharField(max_length=500)
#     order = models.IntegerField(null=True,blank=True)


# ###################################################################################################
# ###################################################################################################

# class tax_planner_answer_question_year(models.Model):
    
#     year = models.CharField(max_length=100)
#     pan_card_number = models.CharField(max_length=100)
#     # heading = models.CharField(max_length=500)
#     # order = models.IntegerField(null=True,blank=True)

#     def __str__(self):
#         return self.pan_card_number + "|" + self.year 

# class tax_planner_main_heading(models.Model):
#     year = models.ForeignKey(tax_planner_answer_question_year,on_delete=models.CASCADE,null=True)
#     name = models.CharField(max_length=500)
#     # sub_heading = models.CharField(max_length=500)
#     main_heading = models.CharField(max_length=500)
#     block_heading = models.CharField(max_length=500)
    
#     class Meta:
#         verbose_name = 'Tax Plan main heading And block heading '
        
#     def __str__(self):
#         return self.main_heading + " | " + self.block_heading

        
# class tax_planner_question_and_answer(models.Model):
#     block = models.ForeignKey(tax_planner_main_heading,on_delete=models.CASCADE , null=True)
#     question = models.CharField(max_length=5000)
#     answer = models.CharField(max_length=5000)
#     current_time = models.CharField(max_length=50,null=True)
#     current_date = models.CharField(max_length=50,null=True)
#     # field_type = models.CharField(max_length=500)

# ###################################################################################################
# ###################################################################################################

# class Tax_Plan_page_file_upload(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) 
#     current_time = models.CharField(max_length=100,blank=True) 
#     current_date = models.CharField(max_length=100,blank=True) 
#     pan_number = models.CharField(max_length=100,blank=True,null=True)
#     files = models.FileField(upload_to="Tax_Plan_page_file_upload/")
    


# class django_Upload(models.Model):
#     image = models.FileField(upload_to='Files')

#     def __str__(self):
#         return str(self.pk)

# # start detail page database 
# class Detail_plan_name(models.Model):
#     id = models.AutoField(primary_key=True)
#     plan_name = models.CharField(max_length=1000)
#     class Meta:
#         verbose_name = 'plan_name'
    
#     def __str__(self):
#         return self.plan_name
# class Detail_plan_about_us(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     about_the_plan = models.CharField(max_length=10000)
#     class Meta:
#         verbose_name = 'about_plan'
    
#     def __str__(self):
#         return self.about_the_plan
# class detail_page_plan_faqs(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     question = models.CharField(max_length=2000)
#     answer = models.CharField(max_length=2000)
#     class Meta:
#         verbose_name = 'faqs'   
    
#     def __str__(self):
#         return self.question

# class detail_page_service_covered(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     plan_service_covered = models.CharField(max_length=5000)
#     class Meta:
#         verbose_name = 'plan_service_covered'   
    
#     def __str__(self):
#         return self.plan_service_covered

# class detail_page_who_should_buy(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     who_should_buy = models.CharField(max_length=5000)
#     class Meta:
#         verbose_name = 'who_should_buy'   
    
#     def __str__(self):
#         return self.who_should_buy


# class detail_page_information_guide(models.Model):
#     plaan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     information_guide = models.CharField(max_length=5000)
#     class Meta:
#         verbose_name = 'information_guide'  

#     def __str__(self):
#         return self.information_guide
# class detail_page_reviews(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     reviews_name = models.CharField(max_length=800)
#     reviews_msg = models.CharField(max_length=10000)
#     class Meta:
#         verbose_name = 'reviews_name'  

#     def __str__(self):
#         return self.reviews_name

# class detail_page_howitsworks_image(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name, on_delete=models.CASCADE,null=True,blank=True) 
#     last1 = models.CharField(max_length=100,blank=True,null=True)
#     detail_of_how_its_work = models.CharField(max_length=50000)
#     class Meta:
#         verbose_name = 'detail_page_howitsworks_image'  

#     def __str__(self):
#         return self.plan_name


class business_income_dahsboard_registrations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    user_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True,null=True)
    pan_card_number = models.CharField(max_length=15)
    reg_status = models.CharField(max_length=20)
    xmlfile = models.FileField(upload_to="registration_xml_file")
    class Meta:
        verbose_name = 'Without XML Registration'  
    
    def __str__(self):
        return self.name



class business_incometax_dashbaord_super_user_registrations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True,null=True)
    pan_card_number = models.CharField(max_length=15)
    reg_status = models.CharField(max_length=20)
    xmlfile = models.FileField(upload_to="business_incometax_dashbaord_super_user_registrations")
    class Meta:
        verbose_name = 'business_incometax_dashbaord_super_user_registrations without XML Registration'  
    
    def __str__(self):
        return self.name




# class REG_XMLFile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) 
#     xmlfile = models.FileField(upload_to="registration_xml-files/", blank=True, null=True)



# class REG_XMLFileData(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
#     # start Form_ITR1
#     FormName = models.CharField(blank=True, null=True, max_length=500)
#     Description = models.CharField(blank=True, null=True, max_length=500)
#     AssessmentYear = models.CharField(blank=True, null=True, max_length=500)
#     SchemaVer = models.CharField(blank=True, null=True, max_length=500)
#     FormVer = models.CharField(blank=True, null=True, max_length=500)
#     # end Form_ITR1
#     # start personla informations
#     # start AssesseeName
#     FirstName = models.CharField(blank=True, null=True, max_length=500)
#     SurNameOrOrgName = models.CharField(blank=True, null=True, max_length=500)
#     # end AssesseeName
#     # srart address 
#     ResidenceNo = models.CharField(blank=True, null=True, max_length=500)
#     RoadOrStreet = models.CharField(blank=True, null=True, max_length=500)
#     LocalityOrArea = models.CharField(blank=True, null=True, max_length=500)
#     CityOrTownOrDistrict = models.CharField(blank=True, null=True, max_length=500)
#     StateCode = models.CharField(blank=True, null=True, max_length=500)
#     CountryCode = models.CharField(blank=True, null=True, max_length=500)
#     PinCode = models.CharField(blank=True, null=True, max_length=500)
#     CountryCodeMobile = models.CharField(blank=True, null=True, max_length=500)
#     MobileNo = models.CharField(blank=True, null=True, max_length=500)
#     EmailAddress = models.CharField(blank=True, null=True, max_length=500)
#     # end address feild 
#     DOB = models.CharField(blank=True, null=True, max_length=500)
#     EmployerCategory = models.CharField(blank=True, null=True, max_length=500)
#     AadhaarCardFlg = models.CharField(blank=True, null=True, max_length=500)
#     AadhaarCardNo = models.CharField(blank=True, null=True, max_length=500)
#     # end personal informations
#     # start FilingStatus
#     ReturnFileSec = models.CharField(blank=True, null=True, max_length=500)
#     SeventhProvisio139 = models.CharField(blank=True, null=True, max_length=500)
#     # end FilingStatus
#     # start ITR1_IncomeDeductions
#     GrossSalary = models.CharField(blank=True, null=True, max_length=500)
#     salary = models.CharField(blank=True, null=True, max_length=500)
#     ProfitsInSalary = models.CharField(blank=True, null=True, max_length=500)
#     PerquisitesValue = models.CharField(blank=True, null=True, max_length=500)
#     # start AllwncExemptUs10
#     TotalAllwncExemptUs10= models.CharField(blank=True, null=True, max_length=500)
#     # end AllwncExemptUs10
#     NetSalary = models.CharField(blank=True, null=True, max_length=500)
#     DeductionUs16 = models.CharField(blank=True, null=True, max_length=500)
#     DeductionUs16ia= models.CharField(blank=True, null=True, max_length=500)
#     EntertainmentAlw16ii= models.CharField(blank=True, null=True, max_length=500)
#     ProfessionalTaxUs16iii= models.CharField(blank=True, null=True, max_length=500)
#     IncomeFromSal= models.CharField(blank=True, null=True, max_length=500)
#     TypeOfHP= models.CharField(blank=True, null=True, max_length=500)
#     GrossRentReceived = models.CharField(blank=True, null=True, max_length=500)
#     TaxPaidlocalAuth = models.CharField(blank=True, null=True, max_length=500)
#     AnnualValue = models.CharField(blank=True, null=True, max_length=500)
#     StandardDeduction = models.CharField(blank=True, null=True, max_length=500)
#     InterestPayable = models.CharField(blank=True, null=True, max_length=500)
#     TotalIncomeOfHP = models.CharField(blank=True, null=True, max_length=500)
#     IncomeOthSrc = models.CharField(blank=True, null=True, max_length=500)
#     DeductionUs57iia = models.CharField(blank=True, null=True, max_length=500)
#     GrossTotIncome = models.CharField(blank=True, null=True, max_length=500)
#     DepPayInvClmUndDednVIA = models.CharField(blank=True, null=True, max_length=500)
#     # start UsrDeductUndChapVIA
#     Section80C = models.CharField(blank=True, null=True, max_length=500)
#     Section80CCC = models.CharField(blank=True, null=True, max_length=500)
#     Section80CCDEmployeeOrSE = models.CharField(blank=True, null=True, max_length=500)
#     Section80CCD1B = models.CharField(blank=True, null=True, max_length=500)
#     Section80CCDEmployer = models.CharField(blank=True, null=True, max_length=500)
#     Section80D = models.CharField(blank=True, null=True, max_length=500)
#     Section80DD = models.CharField(blank=True, null=True, max_length=500)
#     Section80DDB = models.CharField(blank=True, null=True, max_length=500)
#     Section80E = models.CharField(blank=True, null=True, max_length=500)
#     Section80EE = models.CharField(blank=True, null=True, max_length=500)
#     Section80EEA = models.CharField(blank=True, null=True, max_length=500)
#     Section80EEB = models.CharField(blank=True, null=True, max_length=500)
#     Section80G = models.CharField(blank=True, null=True, max_length=500)
#     Section80GG = models.CharField(blank=True, null=True, max_length=500)
#     Section80GGA = models.CharField(blank=True, null=True, max_length=500)
#     Section80GGC = models.CharField(blank=True, null=True, max_length=500)
#     Section80U = models.CharField(blank=True, null=True, max_length=500)
#     Section80TTA = models.CharField(blank=True, null=True, max_length=500)
#     Section80TTB = models.CharField(blank=True, null=True, max_length=500)
#     TotalChapVIADeductions = models.CharField(blank=True, null=True, max_length=500)
#     # end UsrDeductUndChapVIA
#     # start DeductUndChapVIA
#     Section80C = models.CharField(blank=True, null=True, max_length=500)
#     Section80CCC = models.CharField(blank=True, null=True, max_length=500)
#     Section80CCDEmployeeOrSE = models.CharField(blank=True, null=True, max_length=500)
#     Section80CCD1B = models.CharField(blank=True, null=True, max_length=500)
#     Section80CCDEmployer = models.CharField(blank=True, null=True, max_length=500)
#     Section80D = models.CharField(blank=True, null=True, max_length=500)
#     Section80DD = models.CharField(blank=True, null=True, max_length=500)
#     Section80DDB = models.CharField(blank=True, null=True, max_length=500)
#     Section80E = models.CharField(blank=True, null=True, max_length=500)
#     Section80EE = models.CharField(blank=True, null=True, max_length=500)
#     Section80EEA = models.CharField(blank=True, null=True, max_length=500)
#     Section80EEB = models.CharField(blank=True, null=True, max_length=500)
#     Section80G = models.CharField(blank=True, null=True, max_length=500)
#     Section80GG = models.CharField(blank=True, null=True, max_length=500)
#     Section80GGA = models.CharField(blank=True, null=True, max_length=500)
#     Section80GGC = models.CharField(blank=True, null=True, max_length=500)
#     Section80U = models.CharField(blank=True, null=True, max_length=500)
#     Section80TTA = models.CharField(blank=True, null=True, max_length=500)
#     Section80TTB = models.CharField(blank=True, null=True, max_length=500)
#     TotalChapVIADeductions = models.CharField(blank=True, null=True, max_length=500)
#     # end DeductUndChapVIA
#     TotalIncome = models.CharField(blank=True, null=True, max_length=500)
#     # end ITR1_IncomeDeductions
    
#     # start ITR1_TaxComputation
#     TotalTaxPayable = models.CharField(blank=True, null=True, max_length=500)
#     Rebate87A = models.CharField(blank=True, null=True, max_length=500)
#     TaxPayableOnRebate = models.CharField(blank=True, null=True, max_length=500)
#     EducationCess = models.CharField(blank=True, null=True, max_length=500)
#     GrossTaxLiability = models.CharField(blank=True, null=True, max_length=500)
#     Section89 = models.CharField(blank=True, null=True, max_length=500)
#     NetTaxLiability = models.CharField(blank=True, null=True, max_length=500)
#     TotalIntrstPay = models.CharField(blank=True, null=True, max_length=500)
#     # start IntrstPay
#     IntrstPayUs234A = models.CharField(blank=True, null=True, max_length=500)
#     IntrstPayUs234B = models.CharField(blank=True, null=True, max_length=500)
#     IntrstPayUs234C = models.CharField(blank=True, null=True, max_length=500)
#     LateFilingFee234F = models.CharField(blank=True, null=True, max_length=500)
#     # end IntrstPay

#     TotTaxPlusIntrstPay = models.CharField(blank=True, null=True, max_length=500)
    
#     # end ITR1_TaxComputation

#     # start TaxPaid
#     # start TaxesPaid
#     AdvanceTax = models.CharField(blank=True, null=True, max_length=500)
#     TDS = models.CharField(blank=True, null=True, max_length=500)
#     TCS = models.CharField(blank=True, null=True, max_length=500)
#     SelfAssessmentTax = models.CharField(blank=True, null=True, max_length=500)
#     TotalTaxesPaid = models.CharField(blank=True, null=True, max_length=500)
#     # end TaxesPaid
#     BalTaxPayable = models.CharField(blank=True, null=True, max_length=500)
#     # end TaxPaid

#     # start Refund
#     RefundDue = models.CharField(blank=True, null=True, max_length=500)
#     # start BankAccountDtls
#     # start AddtnlBankDetails
#     IFSCCode = models.CharField(blank=True, null=True, max_length=500)
#     BankName = models.CharField(blank=True, null=True, max_length=500)
#     BankAccountNo = models.CharField(blank=True, null=True, max_length=500)
#     UseForRefund = models.CharField(blank=True, null=True, max_length=500)
#     # end AddtnlBankDetails
#     # end BankAccountDtls
#     # end refund

#     # start Schedule80D 
#     # start Sec80DSelfFamSrCtznHealth
#     SeniorCitizenFlag = models.CharField(blank=True, null=True, max_length=500)
#     SelfAndFamily = models.CharField(blank=True, null=True, max_length=500)
#     HealthInsPremSlfFam = models.CharField(blank=True, null=True, max_length=500)
#     PrevHlthChckUpSlfFam = models.CharField(blank=True, null=True, max_length=500)
#     SelfAndFamilySeniorCitizen = models.CharField(blank=True, null=True, max_length=500)
#     HlthInsPremSlfFamSrCtzn = models.CharField(blank=True, null=True, max_length=500)
#     PrevHlthChckUpSlfFamSrCtzn = models.CharField(blank=True, null=True, max_length=500)
#     MedicalExpSlfFamSrCtzn = models.CharField(blank=True, null=True, max_length=500)
#     ParentsSeniorCitizenFlag = models.CharField(blank=True, null=True, max_length=500)
#     Parents = models.CharField(blank=True, null=True, max_length=500)
#     HlthInsPremParents = models.CharField(blank=True, null=True, max_length=500)
#     PrevHlthChckUpParents = models.CharField(blank=True, null=True, max_length=500)
#     ParentsSeniorCitizen = models.CharField(blank=True, null=True, max_length=500)
#     HlthInsPremParentsSrCtzn = models.CharField(blank=True, null=True, max_length=500)
#     PrevHlthChckUpParentsSrCtzn = models.CharField(blank=True, null=True, max_length=500)
#     MedicalExpParentsSrCtzn = models.CharField(blank=True, null=True, max_length=500)
#     EligibleAmountOfDedn = models.CharField(blank=True, null=True, max_length=500)
#     # end Sec80DSelfFamSrCtznHealth
#     # end Schedule80D

#     # start TDSonSalaries
#     # start TDSonSalary
#     # start EmployerOrDeductorOrCollectDetl
#     TAN = models.CharField(blank=True, null=True, max_length=500)
#     EmployerOrDeductorOrCollecterName = models.CharField(blank=True, null=True, max_length=500)
#     # end EmployerOrDeductorOrCollectDetl
#     IncChrgSal = models.CharField(blank=True, null=True, max_length=500)
#     TotalTDSSal = models.CharField(blank=True, null=True, max_length=500)
#     # end TDSonSalary
#     TotalTDSonSalaries = models.CharField(blank=True, null=True, max_length=500)
#     # end TDSonSalaries

#     # start Verification
#     # start Declaration
#     AssesseeVerName = models.CharField(blank=True, null=True, max_length=500)
#     FatherName = models.CharField(blank=True, null=True, max_length=500)
#     AssesseeVerPAN = models.CharField(blank=True, null=True, max_length=500)
#     # end Declaration
#     Capacity = models.CharField(blank=True, null=True, max_length=500)
#     Place = models.CharField(blank=True, null=True, max_length=500)
#     # end Verification
 

     
#     xmlfile = models.FileField(upload_to="add_registrationxml-files/", blank=True, null=True)

# # dashboard reviews slider 
# class plan_reviews_with_category(models.Model):
#     category = models.CharField(blank=True, null=True, max_length=500)
#     name = models.CharField(blank=True, null=True, max_length=500)
#     start_length = models.CharField(blank=True, null=True, max_length=500)
#     reviews_description = models.CharField(blank=True, null=True, max_length=500)
#     reviews_update_time = models.CharField(blank=True, null=True, max_length=500)
#     reviewers_profile_image = models.ImageField(upload_to='reviews/profile/images', null=True)
#     class Meta:
#         verbose_name = 'category'  

#     def __str__(self):
#         return self.category


class business_income_tax_dashboard_checklist_selectbox(models.Model):
    checklist_select = models.CharField(blank=True, null=True, max_length=500)
    class Meta:
        verbose_name = 'dashboard_checklist_selectbox'  

    def __str__(self):
        return self.checklist_select



class business_income_tax_dashboard_checklist_selectbox_main_data(models.Model):
    checklist  = models.ForeignKey(business_income_tax_dashboard_checklist_selectbox, on_delete=models.CASCADE,null=True,blank=True)
    checklist_data = models.CharField(blank=True, null=True, max_length=500)
    checklist_data_id = models.IntegerField()
    class Meta:
        verbose_name = 'dashboard_checklist_selectbox_data'  

    def __str__(self):
        return self.checklist_data





# class service_page_reviews(models.Model):
#     review_category = models.CharField(blank=True, null=True, max_length=500)
#     review_name = models.CharField(blank=True, null=True, max_length=500)
#     review_message = models.CharField(blank=True, null=True, max_length=5000)
#     review_updated_time = models.CharField(blank=True, null=True, max_length=500)
#     review_unique_category = models.CharField(blank=True, null=True, max_length=500)
#     review_image = models.ImageField(upload_to="service_page_reviews/review_image/",null=True)
#     total_start = models.CharField(blank=True, null=True, max_length=6)
#     class Meta:
#         verbose_name = 'service_page_review'  

#     def __str__(self):
#         return self.review_category


# class tax_planner_2_question_answer(models.Model):
#     pan_card_numnber  = models.CharField(blank=True, null=True, max_length=500)
#     data_of_question = models.CharField(blank=True, null=True, max_length=500)
#     data_of_answer = models.CharField(blank=True, null=True, max_length=5000)
#     year = models.CharField(blank=True, null=True, max_length=500)
#     block_heading = models.CharField(blank=True, null=True, max_length=500)
#     name = models.CharField(blank=True, null=True, max_length=60)
#     main_heading = models.CharField(blank=True, null=True, max_length=500)
#     current_date = models.CharField(blank=True, null=True, max_length=20)
#     current_time = models.CharField(blank=True, null=True, max_length=20)
#     class Meta:
#         verbose_name = 'tax_planner_2_question_answer'  

#     def __str__(self):
#         return self.year

# class fianl_tax_planner2_year_data(models.Model):
#     year = models.CharField(blank=True, null=True, max_length=500)
#     class Meta:
#         verbose_name = 'fianl_tax_planner2_year_data'
    
#     def __str__(self):
#         return self.year
# class fianl_tax_planner_question_and_answer_data(models.Model):
#     year  = models.ForeignKey(fianl_tax_planner2_year_data, on_delete=models.CASCADE,null=True,blank=True)
#     pan_card_numnber  = models.CharField(blank=True, null=True, max_length=500)
#     data_of_question = models.CharField(blank=True, null=True, max_length=500)
#     data_of_answer = models.CharField(blank=True, null=True, max_length=5000)
#     year = models.CharField(blank=True, null=True, max_length=500)
#     block_heading = models.CharField(blank=True, null=True, max_length=500)
#     name = models.CharField(blank=True, null=True, max_length=60)
#     main_heading = models.CharField(blank=True, null=True, max_length=500)
#     current_date = models.CharField(blank=True, null=True, max_length=20)
#     current_time = models.CharField(blank=True, null=True, max_length=20)
#     class Meta:
#         verbose_name = 'fianl_tax_planner_question_and_answer_data'  

#     def __str__(self):
#         return self.year


# Start gst dashbaord data 
# Type of Ledger / Register	IGST	CGST	SGST	CESS		
# Electronic Cash Ledger	182	17	17	0		
# Electronic Liability Register (Return related)	0	0	0	0		
# Electronic Credit Ledger	22873	1457	1457	0		

class gst_dashbaord_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    year  = models.CharField(blank=True, null=True, max_length=500)
    months  = models.CharField(blank=True, null=True, max_length=500)
    gstin  = models.CharField(blank=True, null=True, max_length=500)
    trade_name  = models.CharField(blank=True, null=True, max_length=500)
    # gst3_pdf = models.FileField(upload_to="GST3/", blank=True, null=True,storage=PrivateMediaStorage())
    gst3_pdf = models.FileField(upload_to="GST3/", blank=True, null=True)

    class Meta:
        verbose_name = 'gst_dashbaord_data'  

    def __str__(self):
        return self.gstin

class case_ledgel_and_credit_ledgle(models.Model):
    gst_dashbaord_data = models.ForeignKey(gst_dashbaord_data, on_delete=models.CASCADE,null=True,blank=True)
    case_ledgel  = models.CharField(blank=True, null=True, max_length=500)
    credit_ledgel  = models.CharField(blank=True, null=True, max_length=500)

    class Meta:
        verbose_name = 'case_ledgel_and_credit_ledgle'  

    def __str__(self):
        return self.case_ledgel or ''

class Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge(models.Model):
    gst_dashbaord_data = models.ForeignKey(gst_dashbaord_data, on_delete=models.CASCADE,null=True,blank=True)
    Nature_of_Supplies = models.CharField(blank=True, null=True, max_length=5000)
    Total_Taxable_Value = models.CharField(blank=True, null=True, max_length=5000)
    Integrated_Tax = models.CharField(blank=True, null=True, max_length=5000)
    Central_Tax = models.CharField(blank=True, null=True, max_length=5000)
    State_UT_Tax = models.CharField(blank=True, null=True, max_length=5000)
    Cess = models.CharField(blank=True, null=True, max_length=5000)

    class Meta:
        verbose_name = 'Details_of_Outward_supplies_and_inward_supplies_liable_to_reverse_charge'  

    def __str__(self):
        return self.Nature_of_Supplies or ''

choise_data = (
    ('Net ITC available (A-B)','Net ITC available (A-B)'),
    ('Ineligible ITC','Ineligible ITC'),
    )

class Eligible_ITC(models.Model):
    gst_dashbaord_data = models.ForeignKey(gst_dashbaord_data, on_delete=models.CASCADE,null=True,blank=True)
    Details = models.CharField(blank=True, null=True, max_length=5000,choices=choise_data)
    Integrated_Tax = models.CharField(blank=True, null=True, max_length=5000)
    Central_Tax = models.CharField(blank=True, null=True, max_length=5000)
    State_UT_Tax = models.CharField(blank=True, null=True, max_length=5000)
    Cess = models.CharField(blank=True, null=True, max_length=5000)
    
    class Meta:
        verbose_name = 'Eligible_ITC'  

    def __str__(self):
        return self.Details or ''

Tax_paid_through_ITC_choise = (
    ('(A) Other than reverse charge','(A) Other than reverse charge'),
    ('(B) Reverse charge','(B) Reverse charge'),
)
field_choose_data = (
    ('Integrated Tax',"Integrated Tax"),
    ('Central Tax',"Central Tax"),
    ('State UT Tax','State UT Tax'),
    ('Cess',"Cess"),
)
class Tax_paid_through_ITC(models.Model):
    gst_dashbaord_data = models.ForeignKey(gst_dashbaord_data, on_delete=models.CASCADE,null=True,blank=True)
    description_for_Tax_paid_through_ITC = models.CharField(choices=Tax_paid_through_ITC_choise,blank=True, null=True, max_length=5000)
    field_choose = models.CharField(choices=field_choose_data,blank=True, null=True, max_length=5000)
    Integrated_Tax = models.CharField(blank=True, null=True, max_length=5000)
    Central_Tax = models.CharField(blank=True, null=True, max_length=5000)
    State_UT_Tax = models.CharField(blank=True, null=True, max_length=5000)
    Cess = models.CharField(blank=True, null=True, max_length=5000)
    class Meta:
        verbose_name = 'Tax_paid_through_ITC'  

    def __str__(self):
        return self.field_choose or ''

payment_of_tax_choise = (
    ('(A) Other than reverse charge','(A) Other than reverse charge'),
    ('(B) Reverse charge','(B) Reverse charge'),
)

description_choose_data = (
    ('Integrated Tax',"Integrated Tax"),
    ('Central Tax',"Central Tax"),
    ('State UT Tax','State UT Tax'),
    ('Cess',"Cess"),
)

class payment_of_tax(models.Model):
    gst_dashbaord_data = models.ForeignKey(gst_dashbaord_data, on_delete=models.CASCADE,null=True,blank=True)
    Tax_paid_through_ITC = models.ForeignKey(Tax_paid_through_ITC, on_delete=models.CASCADE,null=True,blank=True)
    Description = models.CharField(blank=True, null=True, max_length=5000,choices=payment_of_tax_choise)
    Description_choose = models.CharField(blank=True, null=True, max_length=5000,choices=description_choose_data)
    interest_paid_in_cash = models.CharField(blank=True, null=True, max_length=5000)
    late_fee_paid_in_cash = models.CharField(blank=True, null=True, max_length=5000)
    Total_Tax_payable = models.CharField(blank=True, null=True, max_length=5000)
    Tax_paid_in_cash = models.CharField(blank=True, null=True, max_length=5000)
    
    class Meta:
        verbose_name = 'payment_of_tax'  

    def __str__(self):
        return self.Description or ''



###################################################################################################
###################################################################################################



class business_Tax_Plan_Page(models.Model):
    field_choose = (
        ('ITR 4', 'ITR 4'),
        ('ITR 5', 'ITR 5'),
        ('ITR 6', 'ITR 6'),
        ('ITR 7', 'ITR 7'),
    )
    name = models.CharField(max_length=100)
    plan_code = models.CharField(max_length=5,choices=field_choose,blank=True)
    # heading = models.CharField(max_length=500)
    order = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

# class Tax_Plan_Block(models.Model):
#     page = models.ForeignKey(Tax_Plan_Page,on_delete=models.CASCADE)
#     heading = models.CharField(max_length=500)
#     # sub_heading = models.CharField(max_length=500)
#     tax_plan_name = models.CharField(max_length=500,null=True,blank=True)
#     order = models.IntegerField(null=True,blank=True)
    
#     class Meta:
#         verbose_name = 'Tax Planner'
        
#     def __str__(self):
#         return self.page.name
#         # return self.heading + " | " + self.page.name

class business_Tax_Plan_Block(models.Model):

    heading = models.ForeignKey(business_Tax_Plan_Page,on_delete=models.CASCADE,default=None)
    sub_heading = models.CharField(max_length=500,null=True,blank=True,default=None)
    # sub_heading = models.CharField(max_length=500)
    tax_plan_name = models.CharField(max_length=500,null=True,blank=True,default=None)
    order = models.IntegerField(null=True,blank=True,default=None)
    
    
    class Meta:
        verbose_name = 'Tax Planner'
        
    def __str__(self):
        return self.heading.name
        # return self.heading + " | " + self.page.name



class business_Tax_Plan_Fields(models.Model):
    block = models.ForeignKey(business_Tax_Plan_Block,on_delete=models.CASCADE,default=None)
    question =RichTextField(max_length=5000,null=True,blank=True,default=None)
    yes_answer = RichTextField(max_length=5000,null=True,blank=True,default=None)
    no_answer = RichTextField(max_length=5000,null=True,blank=True,default=None)
    # field_type = models.CharField(max_length=500)
    order = models.IntegerField(null=True,blank=True,default=None)
    


class business_tax_planner_answer_question_year(models.Model):
    
    year = models.CharField(max_length=1000,null=True,blank=True,default=None)
    pan_card_number = models.CharField(max_length=1000,null=True,blank=True,default=None)
    # heading = models.CharField(max_length=500)
    # order = models.IntegerField(null=True,blank=True)
    

    def __str__(self):
        return self.year 
class business_tax_planner_main_heading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,default=None) 
    # year = models.ForeignKey(tax_planner_answer_question_year,on_delete=models.CASCADE,null=True,default=None)
    name = models.CharField(max_length=5000,default=None)
    tax_plan_name = models.CharField(max_length=5000,null=True,blank=True,default=None)
    # sub_heading = models.CharField(max_length=500)
    pan_card_number = models.CharField(max_length=1000,null=True,blank=True,default=None)
    current_time = models.CharField(max_length=1000,blank=True,default=None) 
    current_date = models.CharField(max_length=1000,blank=True,default=None) 
    plan_code = models.CharField(max_length=1000,blank=True,default=None) 

    class Meta:
        verbose_name = 'Tax Plan main heading And block heading '
        
    def __str__(self):
        return self.name + " | " + self.pan_card_number

        
class business_tax_planner_question_and_answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,default=None) 
    year = models.CharField(max_length=100,null=True,blank=True,default=None)
    pan_card_number = models.CharField(max_length=100,null=True,blank=True,default=None)
    block = models.ForeignKey(business_tax_planner_main_heading,on_delete=models.CASCADE , null=True,default=None)
    name = models.CharField(max_length=5000,null=True,blank=True,default=None)
    question = RichTextField(max_length=5000,null=True,blank=True,default=None)
    answer = RichTextField(max_length=5000,null=True,blank=True,default=None)
    user_answer = models.CharField(max_length=5000,null=True,blank=True,default=None)
    current_time = models.CharField(max_length=50,null=True,blank=True,default=None)
    current_date = models.CharField(max_length=50,null=True,blank=True,default=None)
    main_heading = models.CharField(max_length=50,null=True,blank=True,default=None)
    block_heading = models.CharField(max_length=50,null=True,blank=True,default=None)
    
    # field_type = models.CharField(max_length=500)
    # field_type = models.CharField(max_length=500)


class business_tax_planner_2_question_answer(models.Model):
    pan_card_numnber  = models.CharField(blank=True, null=True, max_length=5000,default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,default=None) 
    user_name  = models.CharField(blank=True, null=True, max_length=5000,default=None)
    name  = models.CharField(blank=True, null=True, max_length=5000,default=None)
    data_of_question = models.CharField(blank=True, null=True, max_length=50000,default=None)
    suggestion_answer = models.CharField(blank=True, null=True, max_length=50000,default=None)
    user_answer = models.CharField(blank=True, null=True, max_length=50000,default=None)
    year = models.CharField(blank=True, null=True, max_length=5000,default=None)
    block_heading = models.CharField(blank=True, null=True, max_length=5000,default=None)
    name = models.CharField(blank=True, null=True, max_length=6000,default=None)
    main_heading = models.CharField(blank=True, null=True, max_length=5000)
    current_date = models.CharField(blank=True, null=True, max_length=20)
    current_time = models.CharField(blank=True, null=True, max_length=20)
    tax_plan_name = models.CharField(blank=True, null=True, max_length=200)
    plan_code = models.CharField(blank=True, null=True, max_length=200)
    
    class Meta:
        verbose_name = 'tax_planner_2_question_answer'  

    def __str__(self):
        return self.year

class business_fianl_tax_planner2_year_data(models.Model):
    year = models.CharField(blank=True, null=True, max_length=500)
    class Meta:
        verbose_name = 'business_fianl_tax_planner2_year_data'
    
    def __str__(self):
        return self.year
class business_fianl_tax_planner_question_and_answer_data(models.Model):
    year  = models.ForeignKey(business_tax_planner_2_question_answer, on_delete=models.CASCADE,null=True,default=None,blank=True)
    pan_card_numnber  = models.CharField(blank=True, null=True, max_length=5000,default=None)
    data_of_question = models.CharField(blank=True, null=True, max_length=5000,default=None)
    data_of_answer = models.CharField(blank=True, null=True, max_length=50000,default=None)
    year = models.CharField(blank=True, null=True, max_length=5000,default=None)
    block_heading = models.CharField(blank=True, null=True, max_length=5000,default=None)
    name = models.CharField(blank=True, null=True, max_length=6000,default=None)
    main_heading = models.CharField(blank=True, null=True, max_length=50000,default=None)
    current_date = models.CharField(blank=True, null=True, max_length=200)
    current_time = models.CharField(blank=True, null=True, max_length=200)
    plan_code = models.CharField(blank=True, null=True, max_length=200)
    
    class Meta:
        verbose_name = 'fianl_tax_planner_question_and_answer_data'  

    def __str__(self):
        return self.year



###################################################################################################
###################################################################################################


class business_help_page_data(models.Model):
    help_center_title = models.CharField(max_length=5000,blank=True, null=True)
    help_center_title_page_link = models.CharField(max_length=5000,blank=True, null=True)
    help_center_description = models.TextField(max_length=5000,blank=True, null=True)
    background_color_name = models.CharField(max_length=5000,blank=True, null=True)
    background_color_code = models.CharField(max_length=5000,blank=True, null=True)
    class Meta:
        verbose_name = 'business help page data '  

    def __str__(self):
        return self.help_center_title or ""
    
