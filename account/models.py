from email.policy import default
from os import truncate
from django.core.files import storage
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import files 
from core.storage_backends import PrivateMediaStorage,PublicMediaStorage
from ckeditor.fields import RichTextField

# class test_acc_Pricing_Plan(models.Model):
#     item_group = models.CharField(max_length=500,default=None,null=True)
#     item = models.CharField(max_length=500,default=None,null=True)
#     plan_name = models.CharField(max_length=500,default=None,null=True)
#     plan_sort_name = models.CharField(max_length=500,default=None,null=True)
#     plan_id = models.CharField(max_length=500,unique=True)
#     regullar_price = models.IntegerField(default=None,null=True)
#     discount = models.IntegerField(default=None,null=True)
#     gst = models.IntegerField(default=None,null=True)
#     total_discount = models.IntegerField(default=None,null=True)
#     our_price = models.IntegerField(default=None,null=True)
#     total_gst = models.IntegerField(default=None,null=True)
#     total_price_and_gst = models.IntegerField(default=None,null=True)
#     duration = models.CharField(max_length=500,default=None,null=True)
#     # start plan detail columns 
#     plan_detail1 = models.CharField(max_length=500,null=True,default=None)
#     plan_detail2 = models.CharField(max_length=500,null=True,default=None)
#     plan_detail3 = models.CharField(max_length=500,null=True,default=None)
#     plan_detail4 = models.CharField(max_length=500,null=True,default=None)
#     plan_detail14 = models.CharField(max_length=500,null=True,default=None)
#     plan_detail41 = models.CharField(max_length=500,null=True,default=None)
#     plan_detail42 = models.CharField(max_length=500,null=True,default=None)
#     # end plan detail columns
    
#     # start preferred image 
#     pr_img1 = models.ImageField(upload_to="pricing_plan_image/preferred_plan_image1/",blank = True,null=True)
#     pr_img2 = models.ImageField(upload_to="pricing_plan_image/preferred_plan_image2/",blank = True,null=True)
#     pr_img3 = models.ImageField(upload_to="pricing_plan_image/preferred_plan_image3/",blank = True,null=True)
#     # end preferred image 
#     def __str__(self):
#         return self.plan_name or " "



class terms_and_conndition_with_privacy_policy1(models.Model):
    PAGE_CHOICES = (
        ('TAC', 'Terms And Connditions'),
        ('PAP', 'Privacy And Policy'),
    )
    page = models.CharField(max_length=3,choices=PAGE_CHOICES, null=True, blank=True)
    title_condition = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=100000, null=True, blank=True)
    Paragraph = RichTextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.page or " "
# Create your models here.
class assistanceexpertcalldata(models.Model):
    user_name = models.CharField(blank=True, null=True, max_length=500)
    email = models.CharField(blank=True, null=True, max_length=500)
    contact_number = models.CharField(blank=True, null=True, max_length=500)
    calling_status = models.CharField(blank=True, null=True, max_length=500)
    current_time = models.CharField(blank=True, null=True, max_length=500)
    current_date = models.CharField(blank=True, null=True, max_length=500)
    def __str__(self):
        return self.user_name or " "

class XMLFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) 
    # xmlfile = models.FileField(upload_to="xml_files")
    xmlfile = models.FileField(upload_to="xml_files",)
    # xmlfile = models.FileField(upload_to="xml_files",storage=PrivateMediaStorage())


class XMLFileData(models.Model):
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



# class XMLFileData(models.Model):

#     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
#     # start Form_ITR1
#     form_name = models.CharField(blank=True, null=True, max_length=500)
#     description = models.CharField(blank=True, null=True, max_length=500)
#     assessmentyear = models.CharField(blank=True, null=True, max_length=500)
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
#     Status = models.CharField(blank=True, null=True, max_length=500)
#     AadhaarCardFlg = models.CharField(blank=True, null=True, max_length=500)
#     AadhaarCardNo = models.CharField(blank=True, null=True, max_length=500)
#     # end personal informations
#     # start FilingStatus
#     ReturnFileSec = models.CharField(blank=True, null=True, max_length=500)
#     SeventhProvisio139 = models.CharField(blank=True, null=True, max_length=500)
#     ResidentialStatus = models.CharField(blank=True, null=True, max_length=500)
#     TaxStatus = models.CharField(blank=True, null=True, max_length=500)
#     PortugeseCC5A = models.CharField(blank=True, null=True, max_length=500)

#     # end FilingStatus
#     # start ITR1_IncomeDeductions
#     grosssalary = models.CharField(blank=True, null=True, max_length=500)
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
#     Section80RRB  = models.CharField(blank=True, null=True, max_length=500)
#     Section80QQB= models.CharField(blank=True, null=True, max_length=500)
#     Section80CCG= models.CharField(blank=True, null=True, max_length=500)
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
#     # Date = models.CharField(blank=True, null=True, max_length=500)
#     # end Verification
    
#     # xmlfile = models.FileField(upload_to="xml-data-files/",blank=True, null=True)






class ManualForm16(models.Model):
    first_name = models.TextField(blank=True, null=True)
    middle_name = models.TextField(blank=True, null=True)
    last_name = models.CharField(max_length=30,blank=True, null=True)
    gender = models.CharField(max_length=30,blank=True,null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    father_name = models.CharField(max_length=30,blank=True,null=True)
    merried_status = models.CharField(max_length=30,blank=True,null=True)
    
    pan_number = models.CharField(max_length=20,blank=True, null=True)
    tan_number = models.CharField(max_length=20,blank=True, null=True)
    taxable_income_from_salary = models.CharField(max_length=20,blank=True, null=True)
    gross_total_income = models.CharField(max_length=20,blank=True, null=True)
    total_deductions = models.CharField(max_length=20,blank=True, null=True)
    total_income = models.CharField(max_length=20,blank=True, null=True)


    email = models.EmailField(blank=True, null=True)
     
    pdf = models.FileField(upload_to="form-16-pdf/", blank=True, null=True)
    # pdf = models.FileField(upload_to="form-16-pdf/", blank=True, null=True,storage=PrivateMediaStorage())
    # def __str__(self):
    #     return self.first_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="update_profile")
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    dob = models.DateField(null=True)
    account_number = models.CharField(max_length=40,null=True, blank=True)
    ifsc_code = models.CharField(max_length=20,null=True, blank=True)
    bank_name = models.CharField(max_length=20,null=True, blank=True)
    postal_code = models.CharField(max_length=20,null=True, blank=True)
    aadhar_number = models.CharField(max_length=20,null=True, blank=True)
    mobile_number = models.CharField(max_length=20,null=True, blank=True)
    pan_number = models.CharField(max_length=20,null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True)
    form_16_data = models.OneToOneField(ManualForm16, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.first_name | self.user or " "



class Referral_points(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tree_plants = models.IntegerField(default=0)
    list_of_referral = models.ManyToManyField(User, related_name="list_of_referral",default=0)
    referral_id = models.IntegerField() 

class Tax_Learn_video_category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name or " "

class Tax_Learn_video(models.Model):
    category = models.ForeignKey(Tax_Learn_video_category,on_delete=models.CASCADE,related_name='topic_content_type')
    sub_category = models.CharField(max_length=100,blank=True,null=True,default=None)
    unique_sub_category_name = models.CharField(max_length=500,blank=True,null=True,default=None)
    with_unique_sub_sub_category_name = models.CharField(max_length=500,blank=True,null=True,default=None)
    title = RichTextField(max_length=100,unique=True)
    description = RichTextField(blank=True,null=True,default=None)
    sort_description = RichTextField(blank=True,null=True,default=None)
    video_url = models.TextField(blank=False,null=True)
    # video_image = models.ImageField(storage=PublicMediaStorage(),upload_to="video_url_category/video_image/",blank = True,null=True)
    video_image = models.ImageField(upload_to="video_url_category/video_image/",blank = True,null=True)
    
    def __str__(self):
        return self.sub_category or " "

    # @staticmethod
    # def get_all_video():
    #     return Tax_Learn_video.objects.all()
    
    # @staticmethod
    # def get_all_video_by_id(category_id):
    #     if category_id:
    #         category = Tax_Learn_video_category.objects.get(id=category_id)
    #         print(category)
    #         return Tax_Learn_video.objects.filter(category=category)
    #     else:
    #         return Tax_Learn_video.get_all_video()


# class Tax_Plan_Page_test_test(models.Model):
#     field_choose = (
#         ('ITR 1', 'ITR 1'),
#         ('ITR 2', 'ITR 2'),
#         ('ITR 3', 'ITR 3'),
#     )
#     name = models.CharField(max_length=100)
#     plan_code = models.CharField(max_length=5,choices=field_choose,blank=True)
#     # heading = models.CharField(max_length=500)
#     order = models.IntegerField(null=True,blank=True)

#     def __str__(self):
#         return self.name
# class Tax_Plan_Page(models.Model):
#     field_choose = (
#         ('ITR 1', 'ITR 1'),
#         ('ITR 2', 'ITR 2'),
#         ('ITR 3', 'ITR 3'),
#     )
#     name = models.CharField(max_length=10000,null=True,blank=True,default=None)
#     plan_code = models.CharField(max_length=5,choices=field_choose,blank=True,null=True)
#     # heading = models.CharField(max_length=500)
#     order = models.IntegerField(null=True,blank=True,default=None)

#     def __str__(self):
#         return self.name or " "

# # # class Tax_Plan_Block(models.Model):
# # #     page = models.ForeignKey(Tax_Plan_Page,on_delete=models.CASCADE)
# # #     heading = models.CharField(max_length=500)
# # #     # sub_heading = models.CharField(max_length=500)
# # #     tax_plan_name = models.CharField(max_length=500,null=True,blank=True)
# # #     order = models.IntegerField(null=True,blank=True)
    
# # #     class Meta:
# # #         verbose_name = 'Tax Planner'
        
# # #     def __str__(self):
# # #         return self.page.name
# # #         # return self.heading + " | " + self.page.name

# class Tax_Plan_Block(models.Model):

#     heading = models.ForeignKey(Tax_Plan_Page,on_delete=models.CASCADE,default=None)
#     sub_heading = models.CharField(max_length=500,null=True,blank=True,default=None)
#     # sub_heading = models.CharField(max_length=500)
#     tax_plan_name = models.CharField(max_length=500,null=True,blank=True,default=None)
#     order = models.IntegerField(null=True,blank=True,default=None)
    
#     class Meta:
#         verbose_name = 'Tax Planner'
        
#     def __str__(self):
#         return self.heading.name or " "
#         # return self.heading + " | " + self.page.name



# class Tax_Plan_Fields(models.Model):
#     block = models.ForeignKey(Tax_Plan_Block,on_delete=models.CASCADE,default=None)
#     question = models.CharField(max_length=5000,null=True,blank=True,default=None)
#     yes_answer = models.CharField(max_length=5000,null=True,blank=True,default=None)
#     no_answer = models.CharField(max_length=5000,null=True,blank=True,default=None)
#     # field_type = models.CharField(max_length=500)
#     order = models.IntegerField(null=True,blank=True,default=None)


# # ###################################################################################################
# # ###################################################################################################

# class tax_planner_answer_question_year(models.Model):
    
#     year = models.CharField(max_length=1000,null=True,blank=True,default=None)
#     pan_card_number = models.CharField(max_length=1000,null=True,blank=True,default=None)
#     # heading = models.CharField(max_length=500)
#     # order = models.IntegerField(null=True,blank=True)

#     def __str__(self):
#         return self.year or " "

# class tax_planner_main_heading(models.Model):
#     year = models.ForeignKey(tax_planner_answer_question_year,on_delete=models.CASCADE,null=True,default=None)
#     name = models.CharField(max_length=5000,default=None)
#     tax_plan_name = models.CharField(max_length=5000,null=True,blank=True,default=None)
#     # sub_heading = models.CharField(max_length=500)
#     pan_card_number = models.CharField(max_length=1000,null=True,blank=True,default=None)
#     current_time = models.CharField(max_length=1000,blank=True,default=None) 
#     current_date = models.CharField(max_length=1000,blank=True,default=None) 
#     plan_code = models.CharField(max_length=1000,blank=True,default=None) 

#     class Meta:
#         verbose_name = 'Tax Plan main heading And block heading '
        
#     def __str__(self):
#         return self.name + " | " + self.pan_card_number or " "

        
# class tax_planner_question_and_answer(models.Model):
#     year = models.CharField(max_length=100,null=True,blank=True,default=None)
#     pan_card_number = models.CharField(max_length=100,null=True,blank=True,default=None)
#     block = models.ForeignKey(tax_planner_main_heading,on_delete=models.CASCADE , null=True,default=None)
#     question = models.CharField(max_length=5000,null=True,blank=True,default=None)
#     answer = models.CharField(max_length=5000,null=True,blank=True,default=None)
#     user_answer = models.CharField(max_length=5000,null=True,blank=True,default=None)
#     current_time = models.CharField(max_length=50,null=True,blank=True,default=None)
#     current_date = models.CharField(max_length=50,null=True,blank=True,default=None)
#     main_heading = models.CharField(max_length=50,null=True,blank=True,default=None)
#     block_heading = models.CharField(max_length=50,null=True,blank=True,default=None)
    
#     # field_type = models.CharField(max_length=500)
#     # field_type = models.CharField(max_length=500)



# class tax_planner_2_question_answer(models.Model):
#     pan_card_numnber  = models.CharField(blank=True, null=True, max_length=5000,default=None)
#     data_of_question = models.CharField(blank=True, null=True, max_length=50000,default=None)
#     suggestion_answer = models.CharField(blank=True, null=True, max_length=50000,default=None)
#     user_answer = models.CharField(blank=True, null=True, max_length=50000,default=None)
#     year = models.CharField(blank=True, null=True, max_length=5000,default=None)
#     block_heading = models.CharField(blank=True, null=True, max_length=5000,default=None)
#     name = models.CharField(blank=True, null=True, max_length=6000,default=None)
#     main_heading = models.CharField(blank=True, null=True, max_length=5000)
#     current_date = models.CharField(blank=True, null=True, max_length=20)
#     current_time = models.CharField(blank=True, null=True, max_length=20)
#     tax_plan_name = models.CharField(blank=True, null=True, max_length=20)
#     plan_code = models.CharField(blank=True, null=True, max_length=200)
    
#     class Meta:
#         verbose_name = 'tax_planner_2_question_answer'  

#     def __str__(self):
#         return self.year or ""

# class fianl_tax_planner2_year_data(models.Model):
#     year = models.CharField(blank=True, null=True, max_length=5000,default=None)
#     class Meta:
#         verbose_name = 'fianl_tax_planner2_year_data'
    
#     def __str__(self):
#         return self.year or " "
# class fianl_tax_planner_question_and_answer_data(models.Model):
#     year  = models.ForeignKey(fianl_tax_planner2_year_data, on_delete=models.CASCADE,null=True,default=None,blank=True)
#     pan_card_numnber  = models.CharField(blank=True, null=True, max_length=5000,default=None)
#     data_of_question = models.CharField(blank=True, null=True, max_length=5000,default=None)
#     data_of_answer = models.CharField(blank=True, null=True, max_length=50000,default=None)
#     year = models.CharField(blank=True, null=True, max_length=5000,default=None)
#     block_heading = models.CharField(blank=True, null=True, max_length=5000,default=None)
#     name = models.CharField(blank=True, null=True, max_length=6000,default=None)
#     main_heading = models.CharField(blank=True, null=True, max_length=50000,default=None)
#     current_date = models.CharField(blank=True, null=True, max_length=200)
#     current_time = models.CharField(blank=True, null=True, max_length=200)
#     plan_code = models.CharField(blank=True, null=True, max_length=200)
    
#     class Meta:
#         verbose_name = 'fianl_tax_planner_question_and_answer_data'  

#     def __str__(self):
#         return self.year or ""

# class Tax_Plan_Page(models.Model):
#     field_choose = (
#         ('ITR 1', 'ITR 1'),
#         ('ITR 2', 'ITR 2'),
#         ('ITR 3', 'ITR 3'),
#     )
#     name = models.CharField(max_length=100,null=True,blank=True,default=None)
#     plan_code = models.CharField(max_length=5,choices=field_choose,blank=True,default=None)
#     # heading = models.CharField(max_length=500)
#     order = models.IntegerField(null=True,blank=True,default=None)
#     def __str__(self):
#         return self.name

# class Tax_Plan_Block(models.Model):
#     page = models.ForeignKey(Tax_Plan_Page,on_delete=models.CASCADE)
#     heading = models.CharField(max_length=500,null=True,blank=True)
#     # sub_heading = models.CharField(max_length=500)
#     order = models.IntegerField(null=True,blank=True)
    
#     class Meta:
#         verbose_name = 'Tax Planner'
        
#     def __str__(self):
#         return self.heading + " | " + self.page.name



# class Tax_Plan_Fields(models.Model):
#     block = models.ForeignKey(Tax_Plan_Block,on_delete=models.CASCADE)
#     question = models.CharField(max_length=500,null=True,blank=True)
#     # anser = models.CharField(max_length=500)
#     # field_type = models.CharField(max_length=500)
#     order = models.IntegerField(null=True,blank=True)


###################################################################################################
###################################################################################################

# class tax_planner_answer_question_year(models.Model):
    
#     year = models.CharField(max_length=100,null=True,blank=True)
#     pan_card_number = models.CharField(max_length=100,null=True,blank=True)
#     # heading = models.CharField(max_length=500)
#     # order = models.IntegerField(null=True,blank=True)

#     def __str__(self):
#         return self.pan_card_number + "|" + self.year 
# class tax_planner_main_heading(models.Model):
#     year = models.ForeignKey(tax_planner_answer_question_year,on_delete=models.CASCADE,null=True)
#     name = models.CharField(max_length=500,null=True,blank=True)
#     # sub_heading = models.CharField(max_length=500)
#     main_heading = models.CharField(max_length=500,null=True,blank=True)
#     block_heading = models.CharField(max_length=500,null=True,blank=True)
    
#     class Meta:
#         verbose_name = 'Tax Plan main heading And block heading '
        
#     def __str__(self):
#         return self.main_heading + " | " + self.block_heading

        
# class tax_planner_question_and_answer(models.Model):
#     block = models.ForeignKey(tax_planner_main_heading,on_delete=models.CASCADE , null=True)
#     question = models.CharField(max_length=5000,null=True,blank=True)
#     answer = models.CharField(max_length=5000,null=True,blank=True)
#     current_time = models.CharField(max_length=50,null=True,blank=True)
#     current_date = models.CharField(max_length=50,null=True,blank=True)
#     # field_type = models.CharField(max_length=500)

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
# #         return self.year
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




###################################################################################################
###################################################################################################

class Tax_Plan_page_file_upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) 
    current_time = models.CharField(max_length=100,blank=True) 
    current_date = models.CharField(max_length=100,blank=True) 
    pan_number = models.CharField(max_length=100,blank=True,null=True)
    files = models.FileField(upload_to="Tax_Plan_page_file_upload/")
    


class django_Upload(models.Model):
    image = models.FileField(upload_to='Files')

    def __str__(self):
        return str(self.pk)

# start detail page database 
class Detail_plan_name1(models.Model):
    id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=1000,blank=True, null=True)
    # more_About_page_header_image = models.ImageField(upload_to='more_detail_page/header/images',blank=True, null=True)
    sort_description_plan = RichTextField(max_length=10000,blank=True, null=True,default=None)
    # class Meta:
    #     verbose_name = 'plan more detail page plan name data'
    
class Detail_plan_about_us1(models.Model):
    plan_name = models.ForeignKey(Detail_plan_name1,on_delete=models.CASCADE,blank=True, null=True)
    about_the_plan = RichTextField(max_length=10000,blank=True, null=True,default=None)
    class Meta:
        verbose_name = 'plan more detail page  about us data'
    

    def __str__(self):
        return self.about_the_plan

class detail_page_service_covered1(models.Model):
    plan_name = models.ForeignKey(Detail_plan_name1,on_delete=models.CASCADE,blank=True, null=True)
    plan_service_covered = RichTextField(max_length=50000,blank=True, null=True,default=None)
    class Meta:
        verbose_name = 'plan more detail page  plan service covered data'   
    
    def __str__(self):
        return self.plan_name.plan_name + "|" + self.plan_service_covered or " "

class detail_page_who_should_buy1(models.Model):
    plan_name = models.ForeignKey(Detail_plan_name1,on_delete=models.CASCADE,blank=True, null=True)
    who_should_buy = RichTextField(max_length=5000,blank=True, null=True,default=None)
    class Meta:
        verbose_name = 'plan more detail page who should buy data'   
    
    def __str__(self):
        return self.plan_name.plan_name or " "

class detail_page_plan_faqs1(models.Model):
    plan_name = models.ForeignKey(Detail_plan_name1,on_delete=models.CASCADE,blank=True, null=True)
    question = models.TextField(max_length=20000,blank=True, null=True)
    answer = RichTextField(max_length=200000,blank=True, null=True,default=None)
    class Meta:
        verbose_name = 'plan more detail page faqs data1'   
    
    def __str__(self):
        return self.plan_name.plan_name or " "



class detail_page_information_guide1(models.Model):
    plaan_name = models.ForeignKey(Detail_plan_name1,on_delete=models.CASCADE,blank=True, null=True)
    information_guide = RichTextField(default=None,max_length=5000,blank=True,null=True)
    badge_color = models.TextField(max_length=5000,blank=True,null=True)
    icon_code = models.TextField(max_length=5000,blank=True,null=True)
    class Meta:
        verbose_name = 'plan more detail page information guide data'  

    def __str__(self):
        return self.plaan_name.plan_name or " "
class detail_page_reviews1(models.Model):
    plan_name = models.ForeignKey(Detail_plan_name1,on_delete=models.CASCADE,blank=True, null=True)
    reviews_name = models.CharField(max_length=800,blank=True, null=True)
    reviews_rating = models.CharField(max_length=10000,blank=True, null=True)
    more_About_page_header_image = models.ImageField(upload_to='more_detail_page/reviews/images', null=True,blank = True)
    reviews_rating_star = models.CharField(max_length=10000,blank=True,null=True)
    reviews_rating_blank = models.CharField(max_length=10000,blank=True,null=True)
    reviews_msg = RichTextField(default=None,max_length=10000,blank=True,null=True)
    class Meta:
        verbose_name = 'plan more detail page reviews data'  

    def __str__(self):
        return self.plan_name.plan_name or " "

class detail_page_how_its_work_heading_days_name1(models.Model):
    plan_name = models.ForeignKey(Detail_plan_name1,on_delete=models.CASCADE,blank=True, null=True)
    main_heading_name = models.TextField(max_length=80000,blank=True,null=True)
    estimated_days = models.TextField(max_length=10000,blank=True,null=True)
    class Meta:
        verbose_name = 'Plan more detail page  how its working days '  

    def __str__(self):
        return self.plan_name.plan_name or " "



class detail_page_howitsworks_image1(models.Model):
    plan_name = models.ForeignKey(Detail_plan_name1, on_delete=models.CASCADE,null=True,blank=True) 
    last1 = models.TextField(max_length=100,blank=True,null=True)
    detail_of_how_its_work = RichTextField(max_length=50000,blank=True, null=True,default=None)
    class Meta:
        verbose_name = 'Plan more detail page how its work data '  

    def __str__(self):
        return self.plan_name.plan_name or " "
################ End How its work1 ###########################
class plan_detail_1_abouts_page(Detail_plan_name1):


    class Meta:
        proxy = True

    def __str__(self):
        data = Detail_plan_about_us1.objects.filter(plan_name__plan_name=self.plan_name).values("about_the_plan")

        if len(data)>0:
            return self.plan_name + "|" + "{}".format("Data Filed")  or " "
        else:
            return self.plan_name + "|" +"{}".format("No Data")  or " "
class plan_detail_2_service_covered1(Detail_plan_name1):
    class Meta:
        proxy = True
    def __str__(self):
        data = detail_page_service_covered1.objects.filter(plan_name__plan_name=self.plan_name).values("plan_service_covered")

        if len(data)>0:
            return self.plan_name + "|" + "{}".format("Data Filed")  or " "
        else:
            return self.plan_name + "|" +"{}".format("No Data")  or " "

class plan_detail_3_who_should_buy1(Detail_plan_name1):
    class Meta:
        proxy = True
    def __str__(self):
        data = detail_page_who_should_buy1.objects.filter(plan_name__plan_name=self.plan_name).values("who_should_buy")

        if len(data)>0:
            return self.plan_name + "|" + "{}".format("Data Filed")  or " "
        else:
            return self.plan_name + "|" +"{}".format("No Data")  or " "


class plan_detail_4_plan_faqs1(Detail_plan_name1):
    class Meta:
        proxy = True
    def __str__(self):
        data = detail_page_plan_faqs1.objects.filter(plan_name__plan_name=self.plan_name).values("question","answer")

        if len(data)>0:
            return self.plan_name + "|" + "{}".format("Data Filed")  or " "
        else:
            return self.plan_name + "|" +"{}".format("No Data")  or " "

class plan_detail_5_Document(Detail_plan_name1):
    class Meta:
        proxy = True
    def __str__(self):
        data = detail_page_information_guide1.objects.filter(plaan_name__plan_name=self.plan_name).values("information_guide")

        if len(data)>0:
            return self.plan_name + "|" + "{}".format("Data Filed")  or " "
        else:
            return self.plan_name + "|" +"{}".format("No Data")  or " "

class plan_detail_6_reviews1(Detail_plan_name1):
    class Meta:
        proxy = True
    def __str__(self):
        data = detail_page_reviews1.objects.filter(plan_name__plan_name=self.plan_name).values("reviews_name","reviews_msg")

        if len(data)>0:
            return self.plan_name + "|" + "{}".format("Data Filed")  or " "
        else:
            return self.plan_name + "|" +"{}".format("No Data")  or " "

class plan_detail_7_how_its_work_heading_days_name1(Detail_plan_name1):
    class Meta:
        proxy = True
    def __str__(self):
        data = detail_page_how_its_work_heading_days_name1.objects.filter(plan_name__plan_name=self.plan_name).values("main_heading_name")

        if len(data)>0:
            return self.plan_name + "|" + "{}".format("Data Filed")  or " "
        else:
            return self.plan_name + "|" +"{}".format("No Data")  or " "
class plan_detail_8_howitsworks_image1(Detail_plan_name1):
    class Meta:
        proxy = True
    def __str__(self):
        data = detail_page_howitsworks_image1.objects.filter(plan_name__plan_name=self.plan_name).values("detail_of_how_its_work")

        if len(data)>0:
            return self.plan_name + "|" + "{}".format("Data Filed")  or " "
        else:
            return self.plan_name + "|" +"{}".format("No Data")  or " "


# start detail page database 
# class Detail_plan_name(models.Model):
#     id = models.AutoField(primary_key=True)
#     plan_name = models.CharField(max_length=1000,blank=True, null=True)
        # more_About_page_header_image = models.ImageField(upload_to='more_detail_page/header/images',blank=True, null=True)
#     more_About_page_header_image = models.ImageField(storage=PrivateMediaStorage(),upload_to='more_detail_page/header/images',blank=True,default=None, null=True)
#     class Meta:
#         verbose_name = 'plan more detail page plan name data' or " "
    
# #     def __str__(self):
# #         return self.plan_name or " "
# class Detail_plan_about_us(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     about_the_plan = models.CharField(max_length=10000)
#     class Meta:
#         verbose_name = 'plan more detail page  about us data'
    
#     def __str__(self):
#         return self.about_the_plan


# class detail_page_service_covered(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     plan_service_covered = models.CharField(max_length=5000)
#     class Meta:
#         verbose_name = 'plan more detail page  plan service covered data'   
    
#     def __str__(self):
#         return self.plan_service_covered

# class detail_page_who_should_buy(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     who_should_buy = models.CharField(max_length=5000)
#     class Meta:
#         verbose_name = 'plan more detail page who should buy data'   
    
#     def __str__(self):
#         return self.who_should_buy or " "

# class detail_page_plan_faqs(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     question = models.CharField(max_length=2000)
#     answer = models.CharField(max_length=2000)
#     class Meta:
#         verbose_name = 'plan more detail page faqs data'   
    
#     def __str__(self):
#         return self.question or " "



# class detail_page_information_guide(models.Model):
#     plaan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     information_guide = models.CharField(max_length=5000,blank=True,null=True)
#     badge_color = models.CharField(max_length=5000,blank=True,null=True)
#     icon_code = models.CharField(max_length=5000,blank=True,null=True)
#     class Meta:
#         verbose_name = 'plan more detail page information guide data'  

#     def __str__(self):
#         return self.information_guide or ''
# class detail_page_reviews(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     reviews_name = models.CharField(max_length=800)
#     reviews_rating = models.CharField(max_length=10000)
#     more_About_page_header_image = models.ImageField(upload_to='more_detail_page/reviews/images', null=True)
#     reviews_rating_star = models.CharField(max_length=10000,blank=True,null=True)
#     reviews_rating_blank = models.CharField(max_length=10000,blank=True,null=True)
#     reviews_msg = models.TextField(max_length=10000,blank=True,null=True)
#     class Meta:
#         verbose_name = 'plan more detail page reviews data'  

#     def __str__(self):
#         return self.reviews_name

# class detail_page_how_its_work_heading_days_name(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name,on_delete=models.CASCADE)
#     main_heading_name = models.CharField(max_length=80000,blank=True,null=True)
#     estimated_days = models.CharField(max_length=10000,blank=True,null=True)
#     class Meta:
#         verbose_name = 'Plan more detail page  how its working days '  

#     def __str__(self):
#         return self.main_heading_name or ''



# class detail_page_howitsworks_image(models.Model):
#     plan_name = models.ForeignKey(Detail_plan_name, on_delete=models.CASCADE,null=True,blank=True) 
#     last1 = models.CharField(max_length=100,blank=True,null=True)
#     detail_of_how_its_work = models.CharField(max_length=50000)
#     class Meta:
#         verbose_name = 'Plan more detail page how its work data '  

#     def __str__(self):
#         return self.detail_of_how_its_work or " "
################ End How its work ###########################




class registrations(models.Model):
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
        return self.name or " "



class super_user_registrations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True,null=True)
    pan_card_number = models.CharField(max_length=15)
    reg_status = models.CharField(max_length=20)
    xmlfile = models.FileField(upload_to="super_user_registration_xml_file")
    class Meta:
        verbose_name = 'super_user_registrationsWithout XML Registration'  
    
    def __str__(self):
        return self.name or " "




class REG_XMLFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) 
    xmlfile = models.FileField(upload_to="registration_xml-files/", blank=True, null=True)


class REG_XMLFileData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    # start Form_ITR1
    FormName = models.CharField(blank=True, null=True, max_length=500)
    Description = models.CharField(blank=True, null=True, max_length=500)
    AssessmentYear = models.CharField(blank=True, null=True, max_length=500)
    SchemaVer = models.CharField(blank=True, null=True, max_length=500)
    FormVer = models.CharField(blank=True, null=True, max_length=500)
    # end Form_ITR1
    # start personla informations
    # start AssesseeName
    FirstName = models.CharField(blank=True, null=True, max_length=500)
    SurNameOrOrgName = models.CharField(blank=True, null=True, max_length=500)
    # end AssesseeName
    # srart address 
    ResidenceNo = models.CharField(blank=True, null=True, max_length=500)
    RoadOrStreet = models.CharField(blank=True, null=True, max_length=500)
    LocalityOrArea = models.CharField(blank=True, null=True, max_length=500)
    CityOrTownOrDistrict = models.CharField(blank=True, null=True, max_length=500)
    StateCode = models.CharField(blank=True, null=True, max_length=500)
    CountryCode = models.CharField(blank=True, null=True, max_length=500)
    PinCode = models.CharField(blank=True, null=True, max_length=500)
    CountryCodeMobile = models.CharField(blank=True, null=True, max_length=500)
    MobileNo = models.CharField(blank=True, null=True, max_length=500)
    EmailAddress = models.CharField(blank=True, null=True, max_length=500)
    # end address feild 
    DOB = models.CharField(blank=True, null=True, max_length=500)
    EmployerCategory = models.CharField(blank=True, null=True, max_length=500)
    AadhaarCardFlg = models.CharField(blank=True, null=True, max_length=500)
    AadhaarCardNo = models.CharField(blank=True, null=True, max_length=500)
    # end personal informations
    # start FilingStatus
    ReturnFileSec = models.CharField(blank=True, null=True, max_length=500)
    SeventhProvisio139 = models.CharField(blank=True, null=True, max_length=500)
    # end FilingStatus
    # start ITR1_IncomeDeductions
    GrossSalary = models.CharField(blank=True, null=True, max_length=500)
    salary = models.CharField(blank=True, null=True, max_length=500)
    ProfitsInSalary = models.CharField(blank=True, null=True, max_length=500)
    PerquisitesValue = models.CharField(blank=True, null=True, max_length=500)
    # start AllwncExemptUs10
    TotalAllwncExemptUs10= models.CharField(blank=True, null=True, max_length=500)
    # end AllwncExemptUs10
    NetSalary = models.CharField(blank=True, null=True, max_length=500)
    DeductionUs16 = models.CharField(blank=True, null=True, max_length=500)
    DeductionUs16ia= models.CharField(blank=True, null=True, max_length=500)
    EntertainmentAlw16ii= models.CharField(blank=True, null=True, max_length=500)
    ProfessionalTaxUs16iii= models.CharField(blank=True, null=True, max_length=500)
    IncomeFromSal= models.CharField(blank=True, null=True, max_length=500)
    TypeOfHP= models.CharField(blank=True, null=True, max_length=500)
    GrossRentReceived = models.CharField(blank=True, null=True, max_length=500)
    TaxPaidlocalAuth = models.CharField(blank=True, null=True, max_length=500)
    AnnualValue = models.CharField(blank=True, null=True, max_length=500)
    StandardDeduction = models.CharField(blank=True, null=True, max_length=500)
    InterestPayable = models.CharField(blank=True, null=True, max_length=500)
    TotalIncomeOfHP = models.CharField(blank=True, null=True, max_length=500)
    IncomeOthSrc = models.CharField(blank=True, null=True, max_length=500)
    DeductionUs57iia = models.CharField(blank=True, null=True, max_length=500)
    GrossTotIncome = models.CharField(blank=True, null=True, max_length=500)
    DepPayInvClmUndDednVIA = models.CharField(blank=True, null=True, max_length=500)
    # start UsrDeductUndChapVIA
    Section80C = models.CharField(blank=True, null=True, max_length=500)
    Section80CCC = models.CharField(blank=True, null=True, max_length=500)
    Section80CCDEmployeeOrSE = models.CharField(blank=True, null=True, max_length=500)
    Section80CCD1B = models.CharField(blank=True, null=True, max_length=500)
    Section80CCDEmployer = models.CharField(blank=True, null=True, max_length=500)
    Section80D = models.CharField(blank=True, null=True, max_length=500)
    Section80DD = models.CharField(blank=True, null=True, max_length=500)
    Section80DDB = models.CharField(blank=True, null=True, max_length=500)
    Section80E = models.CharField(blank=True, null=True, max_length=500)
    Section80EE = models.CharField(blank=True, null=True, max_length=500)
    Section80EEA = models.CharField(blank=True, null=True, max_length=500)
    Section80EEB = models.CharField(blank=True, null=True, max_length=500)
    Section80G = models.CharField(blank=True, null=True, max_length=500)
    Section80GG = models.CharField(blank=True, null=True, max_length=500)
    Section80GGA = models.CharField(blank=True, null=True, max_length=500)
    Section80GGC = models.CharField(blank=True, null=True, max_length=500)
    Section80U = models.CharField(blank=True, null=True, max_length=500)
    Section80TTA = models.CharField(blank=True, null=True, max_length=500)
    Section80TTB = models.CharField(blank=True, null=True, max_length=500)
    TotalChapVIADeductions = models.CharField(blank=True, null=True, max_length=500)
    # end UsrDeductUndChapVIA
    # start DeductUndChapVIA
    Section80C = models.CharField(blank=True, null=True, max_length=500)
    Section80CCC = models.CharField(blank=True, null=True, max_length=500)
    Section80CCDEmployeeOrSE = models.CharField(blank=True, null=True, max_length=500)
    Section80CCD1B = models.CharField(blank=True, null=True, max_length=500)
    Section80CCDEmployer = models.CharField(blank=True, null=True, max_length=500)
    Section80D = models.CharField(blank=True, null=True, max_length=500)
    Section80DD = models.CharField(blank=True, null=True, max_length=500)
    Section80DDB = models.CharField(blank=True, null=True, max_length=500)
    Section80E = models.CharField(blank=True, null=True, max_length=500)
    Section80EE = models.CharField(blank=True, null=True, max_length=500)
    Section80EEA = models.CharField(blank=True, null=True, max_length=500)
    Section80EEB = models.CharField(blank=True, null=True, max_length=500)
    Section80G = models.CharField(blank=True, null=True, max_length=500)
    Section80GG = models.CharField(blank=True, null=True, max_length=500)
    Section80GGA = models.CharField(blank=True, null=True, max_length=500)
    Section80GGC = models.CharField(blank=True, null=True, max_length=500)
    Section80U = models.CharField(blank=True, null=True, max_length=500)
    Section80TTA = models.CharField(blank=True, null=True, max_length=500)
    Section80TTB = models.CharField(blank=True, null=True, max_length=500)
    TotalChapVIADeductions = models.CharField(blank=True, null=True, max_length=500)
    # end DeductUndChapVIA
    TotalIncome = models.CharField(blank=True, null=True, max_length=500)
    # end ITR1_IncomeDeductions
    
    # start ITR1_TaxComputation
    TotalTaxPayable = models.CharField(blank=True, null=True, max_length=500)
    Rebate87A = models.CharField(blank=True, null=True, max_length=500)
    TaxPayableOnRebate = models.CharField(blank=True, null=True, max_length=500)
    EducationCess = models.CharField(blank=True, null=True, max_length=500)
    GrossTaxLiability = models.CharField(blank=True, null=True, max_length=500)
    Section89 = models.CharField(blank=True, null=True, max_length=500)
    NetTaxLiability = models.CharField(blank=True, null=True, max_length=500)
    TotalIntrstPay = models.CharField(blank=True, null=True, max_length=500)
    # start IntrstPay
    IntrstPayUs234A = models.CharField(blank=True, null=True, max_length=500)
    IntrstPayUs234B = models.CharField(blank=True, null=True, max_length=500)
    IntrstPayUs234C = models.CharField(blank=True, null=True, max_length=500)
    LateFilingFee234F = models.CharField(blank=True, null=True, max_length=500)
    # end IntrstPay

    TotTaxPlusIntrstPay = models.CharField(blank=True, null=True, max_length=500)
    
    # end ITR1_TaxComputation

    # start TaxPaid
    # start TaxesPaid
    AdvanceTax = models.CharField(blank=True, null=True, max_length=500)
    TDS = models.CharField(blank=True, null=True, max_length=500)
    TCS = models.CharField(blank=True, null=True, max_length=500)
    SelfAssessmentTax = models.CharField(blank=True, null=True, max_length=500)
    TotalTaxesPaid = models.CharField(blank=True, null=True, max_length=500)
    # end TaxesPaid
    BalTaxPayable = models.CharField(blank=True, null=True, max_length=500)
    # end TaxPaid

    # start Refund
    RefundDue = models.CharField(blank=True, null=True, max_length=500)
    # start BankAccountDtls
    # start AddtnlBankDetails
    IFSCCode = models.CharField(blank=True, null=True, max_length=500)
    BankName = models.CharField(blank=True, null=True, max_length=500)
    BankAccountNo = models.CharField(blank=True, null=True, max_length=500)
    UseForRefund = models.CharField(blank=True, null=True, max_length=500)
    # end AddtnlBankDetails
    # end BankAccountDtls
    # end refund

    # start Schedule80D 
    # start Sec80DSelfFamSrCtznHealth
    SeniorCitizenFlag = models.CharField(blank=True, null=True, max_length=500)
    SelfAndFamily = models.CharField(blank=True, null=True, max_length=500)
    HealthInsPremSlfFam = models.CharField(blank=True, null=True, max_length=500)
    PrevHlthChckUpSlfFam = models.CharField(blank=True, null=True, max_length=500)
    SelfAndFamilySeniorCitizen = models.CharField(blank=True, null=True, max_length=500)
    HlthInsPremSlfFamSrCtzn = models.CharField(blank=True, null=True, max_length=500)
    PrevHlthChckUpSlfFamSrCtzn = models.CharField(blank=True, null=True, max_length=500)
    MedicalExpSlfFamSrCtzn = models.CharField(blank=True, null=True, max_length=500)
    ParentsSeniorCitizenFlag = models.CharField(blank=True, null=True, max_length=500)
    Parents = models.CharField(blank=True, null=True, max_length=500)
    HlthInsPremParents = models.CharField(blank=True, null=True, max_length=500)
    PrevHlthChckUpParents = models.CharField(blank=True, null=True, max_length=500)
    ParentsSeniorCitizen = models.CharField(blank=True, null=True, max_length=500)
    HlthInsPremParentsSrCtzn = models.CharField(blank=True, null=True, max_length=500)
    PrevHlthChckUpParentsSrCtzn = models.CharField(blank=True, null=True, max_length=500)
    MedicalExpParentsSrCtzn = models.CharField(blank=True, null=True, max_length=500)
    EligibleAmountOfDedn = models.CharField(blank=True, null=True, max_length=500)
    # end Sec80DSelfFamSrCtznHealth
    # end Schedule80D

    # start TDSonSalaries
    # start TDSonSalary
    # start EmployerOrDeductorOrCollectDetl
    TAN = models.CharField(blank=True, null=True, max_length=500)
    EmployerOrDeductorOrCollecterName = models.CharField(blank=True, null=True, max_length=500)
    # end EmployerOrDeductorOrCollectDetl
    IncChrgSal = models.CharField(blank=True, null=True, max_length=500)
    TotalTDSSal = models.CharField(blank=True, null=True, max_length=500)
    # end TDSonSalary
    TotalTDSonSalaries = models.CharField(blank=True, null=True, max_length=500)
    # end TDSonSalaries

    # start Verification
    # start Declaration
    AssesseeVerName = models.CharField(blank=True, null=True, max_length=500)
    FatherName = models.CharField(blank=True, null=True, max_length=500)
    AssesseeVerPAN = models.CharField(blank=True, null=True, max_length=500)
    # end Declaration
    Capacity = models.CharField(blank=True, null=True, max_length=500)
    Place = models.CharField(blank=True, null=True, max_length=500)
    # end Verification
 

     
    xmlfile = models.FileField(upload_to="add_registrationxml-files/", blank=True, null=True)

# dashboard reviews slider 
class plan_reviews_with_category(models.Model):
    category = models.CharField(blank=True, null=True, max_length=500)
    name = models.CharField(blank=True, null=True, max_length=500)
    start_length = models.CharField(blank=True, null=True, max_length=500)
    reviews_description = models.CharField(blank=True, null=True, max_length=500)
    reviews_update_time = models.CharField(blank=True, null=True, max_length=500)
    reviewers_profile_image = models.ImageField(upload_to='reviews/profile/images', null=True)
    class Meta:
        verbose_name = 'category'  

    def __str__(self):
        return self.category or " "


class dashboard_checklist_selectbox(models.Model):
    checklist_select = models.CharField(blank=True, null=True, max_length=500)
    class Meta:
        verbose_name = 'dashboard_checklist_selectbox'  

    def __str__(self):
        return self.checklist_select or " "



class dashboard_checklist_selectbox_main_data(models.Model):
    checklist  = models.ForeignKey(dashboard_checklist_selectbox, on_delete=models.CASCADE,null=True,blank=True)
    checklist_data = models.CharField(blank=True, null=True, max_length=500)
    checklist_data_id = models.IntegerField()
    class Meta:
        verbose_name = 'dashboard_checklist_selectbox_data'  

    def __str__(self):
        return self.checklist_data or " "





class service_page_reviews(models.Model):
    review_category = models.CharField(blank=True, null=True, max_length=500)
    review_name = models.CharField(blank=True, null=True, max_length=500)
    review_message = models.CharField(blank=True, null=True, max_length=5000)
    review_updated_time = models.CharField(blank=True, null=True, max_length=500)
    review_unique_category = models.CharField(blank=True, null=True, max_length=500)
    review_image = models.ImageField(upload_to="service_page_reviews/review_image/",null=True)
    total_start = models.CharField(blank=True, null=True, max_length=6)
    class Meta:
        verbose_name = 'service_page_review'  

    def __str__(self):
        return self.review_category or " "



class JSON_FileData(models.Model):
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
    IFSCCode = models.CharField(max_length = 1000,blank=True, null=True,)
    BankName = models.CharField(max_length = 1000,blank=True, null=True,)
    BankAccountNo = models.CharField(max_length = 1000,blank=True, null=True,)
    UseForRefund = models.CharField(max_length = 1000,blank=True, null=True,)
    RefundDue = models.CharField(max_length = 1000,blank=True, null=True,)
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
    Parents = models.CharField(max_length = 1000,blank=True, null=True,)
    ParentsSeniorCitizen = models.CharField(max_length = 1000,blank=True, null=True,)
    EligibleAmountOfDedn = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalTDSonSalaries = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalTDSonOthThanSals = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalTDS3Details = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalSchTCS = models.CharField(max_length = 1000,blank=True, null=True,)
    TotalTaxPayments = models.CharField(max_length = 1000,blank=True, null=True,)
    AssesseeVerName = models.CharField(max_length = 1000,blank=True, null=True,)
    FatherName = models.CharField(max_length = 1000,blank=True, null=True,)
    AssesseeVerPAN = models.CharField(max_length = 1000,blank=True, null=True,)
    Capacity = models.CharField(max_length = 1000,blank=True, null=True,)
    Place = models.CharField(max_length = 1000,blank=True, null=True,)







class help_page_data(models.Model):
    help_center_title = models.CharField(max_length=5000,blank=True, null=True)
    help_center_title_page_link = models.CharField(max_length=5000,blank=True, null=True)
    help_center_description = RichTextField(max_length=50000,blank=True, null=True)
    background_color_name = models.CharField(max_length=5000,blank=True, null=True)
    background_color_code = models.CharField(max_length=5000,blank=True, null=True)
    class Meta:
        verbose_name = 'help_page_data'  

    def __str__(self):
        return self.help_center_title or ""
    
    
    
class User_auth(models.Model):
    username = models.CharField(max_length=5000,blank=True, null=True)
    email = models.EmailField()
    user_uid = models.CharField(max_length=5000,blank=True, null=True)
    user_image = models.CharField(max_length=5000,blank=True, null=True)
    user_name = models.CharField(max_length=5000,blank=True, null=True)
    class Meta:
        verbose_name = 'User_auth'  

    def __str__(self):
        return self.username or ""

# class product_home(models.Model):

#     PAGE_CHOICES = (
#         ('ABC', 'Absolute Compliance '),
#         ('KDC', 'Knowledge Center'),
#         ('TXP', 'Tax Planner'),
#     )
#     select_link_title = models.CharField(max_length=3,choices=PAGE_CHOICES, null=True, blank=True)
#     title_url = models.CharField(max_length=5000,blank=True, null=True)
#     title_url = models.CharField(max_length=5000,blank=True, null=True)
#     class Meta:
#         verbose_name = 'Production Home Page'  

#     def __str__(self):
#         return self.select_link_title or ""


# class product_home_test(models.Model):

#     PAGE_CHOICES = (
#         ('ABC', 'Absolute Compliance '),
#         ('KDC', 'Knowledge Center'),
#         ('TXP', 'Tax Planner'),
#     )
#     select_link_title = models.CharField(max_length=3,choices=PAGE_CHOICES, null=True, blank=True)
#     select_link_title1 = models.CharField(max_length=3,choices=PAGE_CHOICES, null=True, blank=True)
#     title_url = models.CharField(max_length=5000,blank=True, null=True)
#     class Meta:
#         verbose_name = 'Production Home Page test'  

#     def __str__(self):
#         return self.select_link_title or ""


# class myorder_invoice(models.Model):
#     sailer_account = models.CharField(max_length=5000,blank=True, null=True,default=None)
#     sailer_bank_acc_name = models.CharField(max_length=5000,blank=True, null=True,default=None)
#     sailer_address = models.TextField(max_length=5000,blank=True, null=True,default=None)
#     sailer_acc_ifsc_code = models.CharField(max_length=5000,blank=True, null=True,default=None)
#     sailer_acc_holder_name = models.CharField(max_length=5000,blank=True, null=True,default=None)
#     class Meta:
#         verbose_name = 'myorder invoice for buyer for test data '  

#     def __str__(self):
#         return self.sailer_address or ""
    
# class myorder_invoice_test(models.Model):
#     sailer_account = models.CharField(max_length=5000,blank=True, null=True)
#     sailer_bank_acc_name = models.CharField(max_length=5000,blank=True, null=True)
#     sailer_address = models.TextField(max_length=5000,blank=True, null=True)
#     sailer_acc_ifsc_code = models.CharField(max_length=5000,blank=True, null=True)
#     sailer_acc_holder_name = models.CharField(max_length=5000,blank=True, null=True)
#     sailer_acc_holder_name1 = models.CharField(max_length=5000,blank=True, null=True)
#     sailer_acc_holder_name11 = models.CharField(max_length=5000,blank=True, null=True)
#     sailer_acc_holder_name111 = models.CharField(max_length=5000,blank=True, null=True)
#     class Meta:
#         verbose_name = 'myorder invoice for buyer'  

#     def __str__(self):
#         return self.sailer_address or ""
    





class Tax_Plan_Page(models.Model):
    field_choose = (
        ('ITR 1', 'ITR 1'),
        ('ITR 2', 'ITR 2'),
        ('ITR 3', 'ITR 3'),
    )
    name = models.CharField(max_length=10000,null=True,blank=True,default=None)
    plan_code = models.CharField(max_length=5,choices=field_choose,blank=True,null=True)
    # heading = models.CharField(max_length=500)
    order = models.IntegerField(null=True,blank=True,default=None)
    

    def __str__(self):
        return self.name or " "

# # class Tax_Plan_Block(models.Model):
# #     page = models.ForeignKey(Tax_Plan_Page,on_delete=models.CASCADE)
# #     heading = models.CharField(max_length=500)
# #     # sub_heading = models.CharField(max_length=500)
# #     tax_plan_name = models.CharField(max_length=500,null=True,blank=True)
# #     order = models.IntegerField(null=True,blank=True)
    
# #     class Meta:
# #         verbose_name = 'Tax Planner'
        
# #     def __str__(self):
# #         return self.page.name
# #         # return self.heading + " | " + self.page.name

class Tax_Plan_Block(models.Model):

    heading = models.ForeignKey(Tax_Plan_Page,on_delete=models.CASCADE,default=None)
    sub_heading = models.CharField(max_length=500,null=True,blank=True,default=None)
    # sub_heading = models.CharField(max_length=500)
    tax_plan_name = models.CharField(max_length=500,null=True,blank=True,default=None)
    order = models.IntegerField(null=True,blank=True,default=None)
    
    
    class Meta:
        verbose_name = 'Tax Planner'
        
    def __str__(self):
        return self.heading.name or " "
        # return self.heading + " | " + self.page.name



class Tax_Plan_Fields(models.Model):
    block = models.ForeignKey(Tax_Plan_Block,on_delete=models.CASCADE,default=None)
    question =RichTextField(max_length=5000,null=True,blank=True,default=None)
    yes_answer = RichTextField(max_length=5000,null=True,blank=True,default=None)
    no_answer = RichTextField(max_length=5000,null=True,blank=True,default=None)
    # field_type = models.CharField(max_length=500)
    order = models.IntegerField(null=True,blank=True,default=None)
    


# ###################################################################################################
# ###################################################################################################

class tax_planner_answer_question_year(models.Model):
    
    year = models.CharField(max_length=1000,null=True,blank=True,default=None)
    pan_card_number = models.CharField(max_length=1000,null=True,blank=True,default=None)
    # heading = models.CharField(max_length=500)
    # order = models.IntegerField(null=True,blank=True)
    

    def __str__(self):
        return self.year or " "

class tax_planner_main_heading(models.Model):
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
        return self.name + " | " + self.pan_card_number or " "

        
class tax_planner_question_and_answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,default=None) 
    year = models.CharField(max_length=100,null=True,blank=True,default=None)
    pan_card_number = models.CharField(max_length=100,null=True,blank=True,default=None)
    block = models.ForeignKey(tax_planner_main_heading,on_delete=models.CASCADE , null=True,default=None)
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



class tax_planner_2_question_answer(models.Model):
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
        return self.year or ""

class fianl_tax_planner2_year_data(models.Model):
    year = models.CharField(blank=True, null=True, max_length=5000,default=None)
    
    class Meta:
        verbose_name = 'fianl_tax_planner2_year_data'
    
    def __str__(self):
        return self.year or " "
class fianl_tax_planner_question_and_answer_data(models.Model):
    year  = models.ForeignKey(fianl_tax_planner2_year_data, on_delete=models.CASCADE,null=True,default=None,blank=True)
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
        return self.year or ""
