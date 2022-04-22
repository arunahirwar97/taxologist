from django.contrib import admin
from . models import *
# Regifrom ster your models here.
from account.models import *

admin.site.register(Contactus)
admin.site.register(Get_Quote)
admin.site.register(Pricing_Plan)
admin.site.register(Order)
admin.site.register(individual_popular_plan)
admin.site.register(bussiness_popular_plan)
admin.site.register(Transaction)
admin.site.register(main_topic)
admin.site.register(review_database)
admin.site.register(footer)
admin.site.register(popular_and_recent_blog_lists)
admin.site.register(abouts_us_page_heading_description)
admin.site.register(google_login_id)

# class TaxFieldsInline(admin.TabularInline):
#     model = blog_categories_and_Sub_categories

# class PageAdmin(admin.ModelAdmin):
#     inlines = [
#         TaxFieldsInline
#     ]
# admin.site.register(TaxFieldsInline,PageAdmin)
class OfferPropertyInline(admin.TabularInline):
    model = blog_categories_and_Sub_categories_sub

class OfferAdmin(admin.ModelAdmin):
    inlines = [
        OfferPropertyInline
    ]

admin.site.register(blog_categories_and_Sub_categories, OfferAdmin)

# admin.site.register(abouts_us_page_heading_description)
# admin.site.register(myorder_invoice_test)
admin.site.register(myorder_invoice)
admin.site.register(product_home)