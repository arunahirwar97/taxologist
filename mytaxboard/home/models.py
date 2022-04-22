from django.db import models
from django.contrib.auth.models import User 
from django.db import models

# Create your models here.

class Get_Quote(models.Model):
    email = models.EmailField()
    option = models.CharField(max_length=50)
    mobile_input = models.CharField(max_length=50)
    def __str__(self):
        return self.email
    class Meta:
        verbose_name = 'Get Quote data'  


class Contactus(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name = 'Contact us data'  

    
class Pricing_Plan(models.Model):
    item_group = models.CharField(max_length=500,default=None,null=True)
    item = models.CharField(max_length=500,default=None,null=True)
    plan_name = models.CharField(max_length=500,default=None,null=True)
    plan_sort_name = models.CharField(max_length=500,default=None,null=True)
    plan_id = models.CharField(max_length=500,unique=True)
    regullar_price = models.IntegerField(default=None,null=True)
    discount = models.IntegerField(default=None,null=True)
    gst = models.IntegerField(default=None,null=True)
    total_discount = models.IntegerField(default=None,null=True)
    our_price = models.IntegerField(default=None,null=True)
    total_gst = models.IntegerField(default=None,null=True)
    total_price_and_gst = models.IntegerField(default=None,null=True)
    duration = models.CharField(max_length=500,default=None,null=True)
    # start plan detail columns 
    plan_detail1 = models.CharField(max_length=500,null=True,default=None)
    plan_detail2 = models.CharField(max_length=500,null=True,default=None)
    plan_detail3 = models.CharField(max_length=500,null=True,default=None)
    plan_detail4 = models.CharField(max_length=500,null=True,default=None)
    # end plan detail columns
    
    # start preferred image 
    # pr_img1 = models.CharField(max_length=500,null=True,default=None)
    # pr_img2 = models.CharField(max_length=500,null=True,default=None)
    # pr_img3 = models.CharField(max_length=500,null=True,default=None)

    pr_img1 = models.ImageField(upload_to="pricing_plan_image/preferred_plan_image1/",blank = True,null=True)
    pr_img2 = models.ImageField(upload_to="pricing_plan_image/preferred_plan_image2/",blank = True,null=True)
    pr_img3 = models.ImageField(upload_to="pricing_plan_image/preferred_plan_image3/",blank = True,null=True)
    # end preferred image 
    class Meta:
        verbose_name = 'All plans details'  

    def __str__(self):
        return self.plan_name


class individual_popular_plan(models.Model):
    ind_popular_item_group = models.CharField(max_length=500,default=None,null=True)
    ind_popular_item = models.CharField(max_length=500,default=None,null=True)
    ind_popular_plan_name = models.CharField(max_length=500,default=None,null=True)
    ind_popular_plan_sort_name = models.CharField(max_length=500,default=None,null=True)
    ind_popular_plan_id = models.CharField(max_length=500,unique=True)
    ind_popular_regullar_price = models.IntegerField(default=None,null=True)
    ind_popular_discount = models.IntegerField(default=None,null=True)
    ind_popular_gst = models.IntegerField(default=None,null=True)
    ind_popular_total_discount = models.IntegerField(default=None,null=True)
    ind_popular_our_price = models.IntegerField(default=None,null=True)
    ind_popular_total_gst = models.IntegerField(default=None,null=True)
    ind_popular_total_price_and_gst = models.IntegerField(default=None,null=True)
    ind_popular_duration = models.CharField(max_length=500,default=None,null=True)
    # start plan detail columns 
    ind_popular_plan_detail1 = models.CharField(max_length=500,null=True,default=None)
    ind_popular_plan_detail2 = models.CharField(max_length=500,null=True,default=None)
    ind_popular_plan_detail3 = models.CharField(max_length=500,null=True,default=None)
    ind_popular_plan_detail4 = models.CharField(max_length=500,null=True,default=None)
    # end plan detail columns
    
    # start preferred image 
    ind_popular_pr_img1 = models.ImageField(upload_to="individual_popular_plan/preferred_plan_image1/",blank = True,null=True)
    ind_popular_pr_img2 = models.ImageField(upload_to="individual_popular_plan/preferred_plan_image2/",blank = True,null=True)
    ind_popular_pr_img3 = models.ImageField(upload_to="individual_popular_plan/preferred_plan_image3/",blank = True,null=True)
    # end preferred image 
    class Meta:
        verbose_name = 'Indivisual popular plans'  

    def __str__(self):
        return self.ind_popular_plan_name

class bussiness_popular_plan(models.Model):
    buss_popular_item_group = models.CharField(max_length=500,default=None,null=True)
    buss_popular_item = models.CharField(max_length=500,default=None,null=True)
    buss_popular_plan_name = models.CharField(max_length=500,default=None,null=True)
    buss_popular_plan_sort_name = models.CharField(max_length=500,default=None,null=True)
    buss_popular_plan_id = models.CharField(max_length=500,unique=True)
    buss_popular_regullar_price = models.IntegerField(default=None,null=True)
    buss_popular_discount = models.IntegerField(default=None,null=True)
    buss_popular_gst = models.IntegerField(default=None,null=True)
    buss_popular_total_discount = models.IntegerField(default=None,null=True)
    buss_popular_our_price = models.IntegerField(default=None,null=True)
    buss_popular_total_gst = models.IntegerField(default=None,null=True)
    buss_popular_total_price_and_gst = models.IntegerField(default=None,null=True)
    buss_popular_duration = models.CharField(max_length=500,default=None,null=True)
    # start plan detail columns 
    buss_popular_plan_detail1 = models.CharField(max_length=500,null=True,default=None)
    buss_popular_plan_detail2 = models.CharField(max_length=500,null=True,default=None)
    buss_popular_plan_detail3 = models.CharField(max_length=500,null=True,default=None)
    buss_popular_plan_detail4 = models.CharField(max_length=500,null=True,default=None)
    # end plan detail columns
    
    # start preferred image 
    buss_popular_pr_img1 = models.ImageField(upload_to="bussiness_popular_plan/preferred_plan_image1/",blank = True,null=True)
    buss_popular_pr_img2 = models.ImageField(upload_to="bussiness_popular_plan/preferred_plan_image2/",blank = True,null=True)
    buss_popular_pr_img3 = models.ImageField(upload_to="bussiness_popular_plan/preferred_plan_image3/",blank = True,null=True)
    # end preferred image 
    class Meta:
        verbose_name = 'Business Popular plans'  

    def __str__(self):
        return self.buss_popular_plan_id or " "
class abouts_us_page_heading_description(models.Model):
    Blog_category_CHOICES = (
        ('heading', 'Main heading '),
        )
    heading_des = models.CharField(max_length=1000,null=True,blank=True,default=None)
    main_heading = models.CharField(max_length=1000,choices=Blog_category_CHOICES,null=True,blank=True,default=None)
    def __str__(self):
        return self.heading_des or ""
    class Meta:
        verbose_name = 'About us page section 3'  

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pricing_plan = models.ForeignKey(Pricing_Plan,on_delete=models.CASCADE)
    main_user_name = models.CharField(max_length=100,default=None,null=True)
    # price = models.IntegerField(default=None,null=True)
    email = models.EmailField()
    plan_id = models.CharField(max_length=100,default=None,null=True)
    name = models.CharField(max_length=100,default=None,null=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    pan_number = models.CharField(max_length=100,default=None,null=True)
    state = models.CharField(max_length=200,default=None,null=True)
    order_id = models.CharField(max_length=2000,default=None,null=True)
    made_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10000, null=True, blank=True,default=None,)
    gstin = models.CharField(max_length=10000, null=True, blank=True,default=None,)
    company_name = models.CharField(max_length=10000, null=True, blank=True,default=None,)
    company_add = models.CharField(max_length=100000, null=True, blank=True,default=None,)
    # pricing_plan_ind1 = models.CharField(max_length=100000, null=True, blank=True,default=None,)
    # pricing_plan_buss1 = models.CharField(max_length=100000, null=True, blank=True,default=None,)
    pin_code = models.CharField(max_length=10000, null=True, blank=True,default=None,)
    pricing_plan_ind = models.ForeignKey(individual_popular_plan,default=None,on_delete=models.CASCADE, null=True, blank=True)
    pricing_plan_buss = models.ForeignKey(bussiness_popular_plan,default=None,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE,default=None,)
    pricing_plan = models.ForeignKey(Pricing_Plan,on_delete=models.CASCADE, null=True, blank=True,default=None,)
    # pricing_plan_ind = models.ForeignKey(individual_popular_plan,default=None,on_delete=models.CASCADE, null=True, blank=True)
    # pricing_plan_buss = models.ForeignKey(bussiness_popular_plan,default=None,on_delete=models.CASCADE, null=True, blank=True)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=1000, null=True, blank=True,default=None,)
    contact_number = models.CharField(max_length=1000, null=True, blank=True,default=None,)
    email = models.EmailField()                 
    name = models.CharField(max_length=100000, null=True, blank=True,default=None,)
    fname = models.CharField(max_length=100000, null=True, blank=True,default=None,)
    state = models.CharField(max_length=100000, null=True, blank=True,default=None,)
    order_id = models.CharField(unique=True, max_length=10000, null=True, blank=True)
    plan_id = models.CharField(max_length=10000,default=None,null=True)
    total_plan = models.CharField(max_length=10000,default=None,null=True)
    status = models.CharField(max_length=10000, null=True, blank=True,default=None,)
    gstin = models.CharField(max_length=10000, null=True, blank=True,default=None,)
    company_name = models.CharField(max_length=10000, null=True, blank=True,default=None,)
    company_add = models.CharField(max_length=100000, null=True, blank=True,default=None,)
    pin_code = models.CharField(max_length=10000, null=True, blank=True,default=None,)
    pricing_plan_ind = models.CharField(max_length=100, null=True, blank=True,default=None,)
    pricing_plan_buss = models.CharField(max_length=100, null=True, blank=True,default=None,)
    status1 = models.CharField(max_length=100, null=True, blank=True,default=None,)
    # status12 = models.CharField(max_length=100, null=True, blank=True,default=None,)

    def __str__(self):
        return str(self.order_id)
        
    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('MTB%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

# class Transaction_final(models.Model):
#     made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE,default=None,)
#     pricing_plan = models.ForeignKey(Pricing_Plan,on_delete=models.CASCADE, null=True, blank=True,default=None,)
#     pricing_plan_ind = models.ForeignKey(individual_popular_plan,default=None,on_delete=models.CASCADE, null=True, blank=True)
#     pricing_plan_buss = models.ForeignKey(bussiness_popular_plan,default=None,on_delete=models.CASCADE, null=True, blank=True)
#     made_on = models.DateTimeField(auto_now_add=True)
#     amount = models.CharField(max_length=1000, null=True, blank=True,default=None,)
#     contact_number = models.CharField(max_length=1000, null=True, blank=True,default=None,)
#     email = models.EmailField()                 
#     name = models.CharField(max_length=100000, null=True, blank=True,default=None,)
#     fname = models.CharField(max_length=100000, null=True, blank=True,default=None,)
#     state = models.CharField(max_length=100000, null=True, blank=True,default=None,)
#     order_id = models.CharField(unique=True, max_length=10000, null=True, blank=True)
#     plan_id = models.CharField(max_length=10000,default=None,null=True)
#     total_plan = models.CharField(max_length=10000,default=None,null=True)
#     status = models.CharField(max_length=10000, null=True, blank=True,default=None,)
#     gstin = models.CharField(max_length=10000, null=True, blank=True,default=None,)
#     company_name = models.CharField(max_length=10000, null=True, blank=True,default=None,)
#     company_add = models.CharField(max_length=100000, null=True, blank=True,default=None,)
#     pin_code = models.CharField(max_length=10000, null=True, blank=True,default=None,)
    
#     status1 = models.CharField(max_length=100, null=True, blank=True,default=None,)
#     status12 = models.CharField(max_length=100, null=True, blank=True,default=None,)

#     def __str__(self):
#         return str(self.order_id)
        
#     def save(self, *args, **kwargs):
#         if self.order_id is None and self.made_on and self.id:
#             self.order_id = self.made_on.strftime('MYTAXBOARD%Y%m%dODR') + str(self.id)
#         return super().save(*args, **kwargs)




# class Transaction_test(models.Model):
#     made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
#     pricing_plan = models.ForeignKey(Pricing_Plan,on_delete=models.CASCADE, null=True, blank=True)
#     pricing_plan_ind = models.ForeignKey(individual_popular_plan,on_delete=models.CASCADE, null=True, blank=True)
#     pricing_plan_buss = models.ForeignKey(bussiness_popular_plan,on_delete=models.CASCADE, null=True, blank=True)
#     made_on = models.DateTimeField(auto_now_add=True)
#     amount = models.CharField(max_length=1000, null=True, blank=True)
#     contact_number = models.CharField(max_length=1000, null=True, blank=True)
#     email = models.EmailField()                 
#     name = models.CharField(max_length=100000, null=True, blank=True)
#     fname = models.CharField(max_length=100000, null=True, blank=True)
#     state = models.CharField(max_length=100000, null=True, blank=True)
#     order_id = models.CharField(unique=True, max_length=10000, null=True, blank=True)
#     plan_id = models.CharField(max_length=10000,default=None,null=True)
#     total_plan = models.CharField(max_length=10000,default=None,null=True)
#     status = models.CharField(max_length=10000, null=True, blank=True)

#     gstin = models.CharField(max_length=10000, null=True, blank=True)
#     company_name = models.CharField(max_length=10000, null=True, blank=True)
#     company_add = models.CharField(max_length=100000, null=True, blank=True)
#     pin_code = models.CharField(max_length=10000, null=True, blank=True)
#     pin_code_test = models.CharField(max_length=10000, null=True, blank=True)
#     pin_code_test1 = models.CharField(max_length=10000, null=True, blank=True)
    
#     def __str__(self):
#         return str(self.order_id)
#     class Meta:
#         verbose_name = 'Transaction data base terst'  

        
#     def save(self, *args, **kwargs):
#         if self.order_id is None and self.made_on and self.id:
#             self.order_id = self.made_on.strftime('MTB%Y%m%d') + str(self.id)
#         return super().save(*args, **kwargs)


# Start reviews database 
class main_topic(models.Model):
    topic = models.CharField(max_length=100000, null=True, blank=True)
    def __str__(self):
        return self.topic
    class Meta:
        verbose_name = 'FAQ"s main heading like Frequently Asked Question '
class review_database(models.Model):
    question = models.CharField(max_length=100000, null=True, blank=True)
    answer = models.CharField(max_length=100000, null=True, blank=True)

    def __str__(self):
        return self.question
    class Meta:
        verbose_name = 'FAQ"s question and answer '   

# End reviews database 


# Start Footer Links 
class footer(models.Model):
    title_col = models.CharField(max_length=100000, null=True, blank=True)
    title_name = models.CharField(max_length=100000, null=True, blank=True)
    title_link = models.CharField(max_length=100000, null=True, blank=True)

    def __str__(self):
        return self.title_name
    class Meta:
        verbose_name = 'Footer page data'  

# End Footer Links 



# Start blog content database 


class blog_categories_and_Sub_categories(models.Model):
    main_category = models.CharField(max_length=1000)

    def __str__(self):
        return self.main_category or ""

    class Meta:
        verbose_name = 'Blog category '  

class blog_categories_and_Sub_categories_sub(models.Model):
    main_category = models.ForeignKey(blog_categories_and_Sub_categories, on_delete=models.CASCADE,default=None)
    sub_categories = models.CharField(max_length=5000,default=None)
    sub_categories_links = models.CharField(max_length=5000,null=True,blank=True,default=None)

    def __str__(self):
        return self.sub_categories or ""
    class Meta:
        verbose_name = 'main category and sub category in blog pages '  



class popular_and_recent_blog_lists(models.Model):
    Blog_category_CHOICES = (
        ('POPULAR', 'popular blog list'),
        ('RECENT', 'recent blog list'),
        )
    title = models.CharField(max_length=1000)
    title_blog_url = models.CharField(max_length=1000)
    blog_category = models.CharField(max_length=1000,choices=Blog_category_CHOICES)
    date = models.CharField(max_length=1000)
    time = models.CharField(max_length=1000)
    def __str__(self):
        return self.title or ""
    class Meta:
        verbose_name = 'Popular and recent blog categories'  

class google_login_id(models.Model):
    login_id = models.CharField(max_length=10000,null=True,blank=True)
    def __str__(self):
        return self.login_id or ""
    class Meta:
        verbose_name = 'Google Login id'  

from django.db import models

# Create your models here.
class product_home(models.Model):

    PAGE_CHOICES = (
        ('ABC', 'Absolute Compliance '),
        ('KDC', 'Knowledge Center'),
        ('TXP', 'Tax Planner'),
    )
    select_link_title = models.CharField(max_length=3,choices=PAGE_CHOICES, null=True, blank=True)
    title_url = models.CharField(max_length=5000,blank=True, null=True)
    class Meta:
        verbose_name = 'Production Home Page dropdown links'  

    def __str__(self):
        return self.select_link_title or ""


# class abouts_us_page_heading_description(models.Model):
#     Blog_category_CHOICES = (
#         ('heading', 'Main heading '),
#         )
#     heading_des = models.CharField(max_length=1000,null=True,blank=True,default=None)
#     
#     main_heading = models.CharField(max_length=1000,choices=Blog_category_CHOICES,null=True,blank=True,default=None)
#     def __str__(self):
#         return self.heading_des or ""
#     class Meta:
#         verbose_name = 'About us page section 3'  


class myorder_invoice(models.Model):
    sailer_account = models.CharField(max_length=5000,blank=True, null=True)
    sailer_bank_acc_name = models.CharField(max_length=5000,blank=True, null=True)
    sailer_address = models.TextField(max_length=5000,blank=True, null=True)
    sailer_acc_ifsc_code = models.CharField(max_length=5000,blank=True, null=True)
    sailer_acc_holder_name = models.CharField(max_length=5000,blank=True, null=True)
    # sailer_acc_holder_name1 = models.CharField(max_length=5000,blank=True, null=True,default=None)
    class Meta:
        verbose_name = 'myorder invoice for buyer'  

    def __str__(self):
        return self.sailer_address or ""
    