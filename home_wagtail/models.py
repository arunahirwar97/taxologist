# from django.db import models
# from django.db.models.fields import BLANK_CHOICE_DASH

# from wagtail.core.models import Page
# from wagtail.core.fields import RichTextField
# from wagtail.admin.edit_handlers import FieldPanel

# from django.db import models

# from modelcluster.fields import ParentalKey

# from wagtail.core.models import Page, Orderable
# from wagtail.core.fields import StreamField
# from wagtail.core import blocks

# from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel

# from wagtail.images.edit_handlers import ImageChooserPanel

# from wagtail.contrib.settings.models import BaseSetting, register_setting
# from wagtail.contrib.routable_page.models import RoutablePageMixin, route
# # from wagtail.wagtailimages.blocks import ImageChooserBlock

# class mtb_blog(blocks.StreamBlock):
#     body = RichTextField(blank=True)
#     title_image = models.ForeignKey(
#     'wagtailimages.Image',
#     null=True,
#     blank=True,
#     on_delete=models.PROTECT,
#     related_name='+'
#     )
#     mtb_title = models.CharField(max_length=255)
#     short_description = models.TextField(blank=True, null=True)
#     long_description = models.TextField(blank=True, null=True,max_length=500000)

#     image = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.PROTECT,
#         related_name='+'
#     )
#     content_panels = Page.content_panels + [
#         FieldPanel('body', classname='full'),
#         ImageChooserPanel('title_image'),
#         FieldPanel('mtb_title'),
#         FieldPanel('short_description'),
#         FieldPanel('long_description'),
#         ImageChooserPanel('image'),
#     ]


# class PersonBlock(blocks.StructBlock):
#     first_name = blocks.CharBlock(required=True)
#     surname = blocks.CharBlock(required=True)
#     # photo = ImageChooserBlock()
#     biography = blocks.RichTextBlock()

#     class Meta:
#         icon = 'user'


# class HomePage(Page):
#     body = StreamField([
#     ('heading', blocks.CharBlock(classname="full title")),
#     ('paragraph', blocks.RichTextBlock()),
#     ('person', PersonBlock()),
# ])



# # class HomePage(Page):
# #     def get_context(self, request):
# #         context = super().get_context(request)

# #         context['mytaxboard_cms'] = mytaxboard_cms.objects.child_of(self).live()

# #         return context

# # class mytaxboard_cms(Page):
# #     title_image = models.ForeignKey(
# #     'wagtailimages.Image',
# #     null=True,
# #     blank=True,
# #     on_delete=models.PROTECT,
# #     related_name='+'
# #     )
# #     mtb_title = models.CharField(max_length=255)
# #     short_description = models.TextField(blank=True, null=True)
# #     long_description = models.TextField(blank=True, null=True,max_length=500000)

# #     image = models.ForeignKey(
# #         'wagtailimages.Image',
# #         null=True,
# #         blank=True,
# #         on_delete=models.PROTECT,
# #         related_name='+'
# #     )
# #     content_panels = Page.content_panels + [
# #         ImageChooserPanel('title_image'),
# #         FieldPanel('mtb_title'),
# #         FieldPanel('short_description'),
# #         FieldPanel('long_description'),
# #         ImageChooserPanel('image'),

# #         # InlinePanel('custom_fields', label='Custom fields'),
# #     ]

# #     def get_context(self, request):
# #         context = super().get_context(request)
# #         fields = []
# #         for f in self.custom_fields.get_object_list():
# #             if f.options:
# #                 f.options_array = f.options.split('|')
# #                 fields.append(f)
# #             else:
# #                 fields.append(f)

# #         context['custom_fields'] = fields

# #         return context

# # class ProductCustomField(Orderable):
# #     product = ParentalKey(mytaxboard_cms, on_delete=models.PROTECT, related_name='custom_fields')
# #     name = models.CharField(max_length=255)
# #     options = models.CharField(max_length=500, null=True, blank=True)

# #     panels = [
# #         FieldPanel('name'),
# #         FieldPanel('options')
# #     ]

# # @register_setting
# # class SnipcartSettings(BaseSetting):
# #     api_key = models.CharField(
# #         max_length=255,
# #         help_text='Your Snipcart public API key'
# #     )


from pyexpat import model
from django.db import models
from django.db.models.enums import Choices

from wagtail.core.models import *
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from home.models import *
from wagtail.api import APIField
 
from core.storage_backends import PrivateMediaStorage,PublicMediaStorage



from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'HomePage',
        related_name='tagged_items',
        on_delete=models.PROTECT,
    )
class HomePage(Page):
    sort_description_body = RichTextField(blank=True)
    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='+',
    )
    # main_page_title_image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.PROTECT
    # )

    title_image1 = models.ImageField(upload_to="wagtail_image/",blank = True,null=True)
    # title_image1 = models.ImageField(upload_to="wagtail_image/",blank = True,null=True,storage=PublicMediaStorage())
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    blog_category = models.ForeignKey(blog_categories_and_Sub_categories,on_delete=models.PROTECT)
    blog_sub_category = models.ForeignKey(blog_categories_and_Sub_categories_sub,on_delete=models.PROTECT)
    body = RichTextField(blank=True)
    writter_name = models.TextField(blank=True)
    Blog_category_CHOICES = (
    ('POPULAR', 'popular blog list'),
    ('RECENT', 'recent blog list'),
    )
    slect_box = models.CharField(blank=True,choices=Blog_category_CHOICES,max_length=120)
    select_box_date = models.DateField(blank=True,null=True)
    select_box_time = models.TimeField(blank=True,null=True)
    enter_blog_time_read = models.CharField(blank=True,max_length=120)
    Blog_category_CHOICES1 = (
    ('center_blog_show', 'center blog show'),
    ('left_site_blog_show', 'left_site_blog_show'),
    ('right_site_blog_show', 'right_site_blog_show'),
    ('left_site_with_sticky_blog_show', 'left_site_with_sticky_blog_show'),
    )
    blog_category_for_side_coose= models.CharField(blank=True,choices=Blog_category_CHOICES1,max_length=120)

    content_panels = Page.content_panels + [
        FieldPanel('sort_description_body', classname="full"),
        ImageChooserPanel('title_image'),
        # ImageChooserPanel('main_page_title_image'),
        FieldPanel('tags', classname="full"),
        FieldPanel('body', classname="full"),
        FieldPanel('slect_box', classname="full"),
        FieldPanel('select_box_date', classname="full"),
        FieldPanel('select_box_time', classname="full"),
        FieldPanel('enter_blog_time_read', classname="full"),
        FieldPanel('writter_name', classname="full"),
        FieldPanel('blog_category', classname="full"),
        FieldPanel('blog_category_for_side_coose', classname="full"),
        FieldPanel('blog_sub_category', classname="full"),

    ]
    api_fields = [
        APIField('sort_description_body'),
        APIField('title_image'),
        APIField('body'),
        APIField('slect_box'),
        APIField('select_box_date'),
        APIField('enter_blog_time_read'),
        APIField('writter_name'),
        APIField('tags'),
        APIField('blog_sub_category'),
        APIField('blog_category_for_side_coose'),
    ]
    def get_context(self, request):
        # Update context to include only published posts,
        # in reverse chronological order
        context = super(HomePage, self).get_context(request)
        live_blogpages = self.get_children().live()
        context['blogpages'] = live_blogpages.order_by('-first_published_at')
        context['main_page1'] = HomePage.objects.all()
        context["main_data11"] = LEFTSIDEHomePage.objects.all()
        context["main_data2"]  = LEFTSIDEWITHSTICKYNOTEHomePage.objects.all()
        context["main_data3"]  = RIGHTSIDEHomePage.objects.all()
        context["main_data4"]  = RIGHTSIDEWITHSTICKYNOTEHomePage.objects.all()
        context['main_data'] = blog_categories_and_Sub_categories_sub.objects.all()
        context['main_data1'] = blog_categories_and_Sub_categories.objects.all()
        context['main_page4'] = popular_and_recent_blog_lists.objects.all()
        return context

class BlogDetailPage(Page):
    # Fields here...
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    content_panels = Page.content_panels + [
        # Custom panels 
        FieldPanel("tags"),
    ]

################# LEft side blog show ###################

class LEFTSIDEHomePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'LEFTSIDEHomePage',
        related_name='tagged_items',
        on_delete=models.PROTECT,
    ) 

class LEFTSIDEHomePage(Page):
    sort_description_body = RichTextField(blank=True)
    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    title_image1 = models.ImageField(upload_to="wagtail_image/",blank = True,null=True,storage=PublicMediaStorage())
    tags = ClusterTaggableManager(through=LEFTSIDEHomePageTag, blank=True)

    blog_category = models.ForeignKey(blog_categories_and_Sub_categories,on_delete=models.PROTECT)
    blog_sub_category = models.ForeignKey(blog_categories_and_Sub_categories_sub,on_delete=models.PROTECT)
    body = RichTextField(blank=True)
    writter_name = models.TextField(blank=True)
    Blog_category_CHOICES = (
    ('POPULAR', 'popular blog list'),
    ('RECENT', 'recent blog list'),
    )
    slect_box = models.CharField(blank=True,choices=Blog_category_CHOICES,max_length=120)
    select_box_date = models.DateField(blank=True,null=True)
    select_box_time = models.TimeField(blank=True,null=True)
    enter_blog_time_read = models.CharField(blank=True,max_length=120)
    # main_page_title_image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.PROTECT
    # )

    content_panels = Page.content_panels + [
        FieldPanel('sort_description_body', classname="full"),
        ImageChooserPanel('title_image'),
        FieldPanel('tags'),
        FieldPanel('body', classname="full"),
        FieldPanel('slect_box', classname="full"),
        FieldPanel('select_box_date', classname="full"),
        FieldPanel('select_box_time', classname="full"),
        FieldPanel('enter_blog_time_read', classname="full"),
        FieldPanel('writter_name', classname="full"),
        FieldPanel('blog_category', classname="full"),
        FieldPanel('blog_sub_category', classname="full"),

    ]
    api_fields = [
        APIField('sort_description_body'),
        APIField('title_image'),
        APIField('body'),
        APIField('slect_box'),
        APIField('select_box_date'),
        APIField('enter_blog_time_read'),
        APIField('writter_name'),
        APIField('blog_category'),
        APIField('blog_sub_category'),
        APIField('tags'),
        
    ]
    def get_context(self, request):
        # Update context to include only published posts,
        # in reverse chronological order
        context = super(LEFTSIDEHomePage, self).get_context(request)
        live_blogpages = self.get_children().live()
        context['blogpages'] = live_blogpages.order_by('-first_published_at')
        context['main_page1'] = LEFTSIDEHomePage.objects.all()
        context["main_data11"] = HomePage.objects.all()
        context["main_data2"]  = LEFTSIDEWITHSTICKYNOTEHomePage.objects.all()
        context["main_data3"]  = RIGHTSIDEHomePage.objects.all()
        context["main_data4"]  = RIGHTSIDEWITHSTICKYNOTEHomePage.objects.all()
        context['main_data'] = blog_categories_and_Sub_categories_sub.objects.all()
        context['main_data1'] = blog_categories_and_Sub_categories.objects.all()
        context['main_page4'] = popular_and_recent_blog_lists.objects.all()
        return context

class LEFTSIDEWITHSTICKYNOTEHomePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'LEFTSIDEWITHSTICKYNOTEHomePage',
        related_name='tagged_items',
        on_delete=models.PROTECT,
    ) 


class LEFTSIDEWITHSTICKYNOTEHomePage(Page):
    sort_description_body = RichTextField(blank=True)
    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    title_image1 = models.ImageField(upload_to="wagtail_image/",blank = True,null=True,storage=PublicMediaStorage())
    tags = ClusterTaggableManager(through=LEFTSIDEWITHSTICKYNOTEHomePageTag, blank=True)

    blog_category = models.ForeignKey(blog_categories_and_Sub_categories,on_delete=models.PROTECT)
    blog_sub_category = models.ForeignKey(blog_categories_and_Sub_categories_sub,on_delete=models.PROTECT)
    body = RichTextField(blank=True)
    writter_name = models.TextField(blank=True)
    Blog_category_CHOICES = (
    ('POPULAR', 'popular blog list'),
    ('RECENT', 'recent blog list'),
    )
    slect_box = models.CharField(blank=True,choices=Blog_category_CHOICES,max_length=120)
    select_box_date = models.DateField(blank=True,null=True)
    select_box_time = models.TimeField(blank=True,null=True)
    enter_blog_time_read = models.CharField(blank=True,max_length=120)
    # main_page_title_image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.PROTECT
    # )

    content_panels = Page.content_panels + [
        FieldPanel('sort_description_body', classname="full"),
        ImageChooserPanel('title_image'),
        FieldPanel('tags'),
        FieldPanel('body', classname="full"),
        FieldPanel('slect_box', classname="full"),
        FieldPanel('select_box_date', classname="full"),
        FieldPanel('select_box_time', classname="full"),
        FieldPanel('enter_blog_time_read', classname="full"),
        FieldPanel('writter_name', classname="full"),
        FieldPanel('blog_category', classname="full"),
        FieldPanel('blog_sub_category', classname="full"),

    ]
    api_fields = [
        APIField('sort_description_body'),
        APIField('title_image'),
        APIField('body'),
        APIField('slect_box'),
        APIField('select_box_date'),
        APIField('enter_blog_time_read'),
        APIField('writter_name'),
        APIField('blog_category'),
        APIField('blog_sub_category'),
        APIField('tags'),
    ]

    def get_context(self, request):
        # Update context to include only published posts,
        # in reverse chronological order
        context = super(LEFTSIDEWITHSTICKYNOTEHomePage, self).get_context(request)
        live_blogpages = self.get_children().live()
        context['blogpages'] = live_blogpages.order_by('-first_published_at')
        context['main_page1'] = LEFTSIDEWITHSTICKYNOTEHomePage.objects.all()
        context['main_data2'] = LEFTSIDEHomePage.objects.all()
        context["main_data11"] = HomePage.objects.all()
        context["main_data3"]  = RIGHTSIDEHomePage.objects.all()
        context["main_data4"]  = RIGHTSIDEWITHSTICKYNOTEHomePage.objects.all()
        context['main_data'] = blog_categories_and_Sub_categories_sub.objects.all()
        context['main_data1'] = blog_categories_and_Sub_categories.objects.all()
        context['main_page4'] = popular_and_recent_blog_lists.objects.all()
        return context


################# End LEft side blog show ###################




################# LEft side blog show ###################
class RIGHTSIDEHomePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'RIGHTSIDEHomePage',
        related_name='tagged_items',
        on_delete=models.PROTECT,
    ) 
class RIGHTSIDEHomePage(Page):
    sort_description_body = RichTextField(blank=True)
    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    title_image1 = models.ImageField(upload_to="wagtail_image/",blank = True,null=True,storage=PublicMediaStorage())
    tags = ClusterTaggableManager(through=RIGHTSIDEHomePageTag, blank=True)

    blog_category = models.ForeignKey(blog_categories_and_Sub_categories,on_delete=models.PROTECT)
    blog_sub_category = models.ForeignKey(blog_categories_and_Sub_categories_sub,on_delete=models.PROTECT)
    body = RichTextField(blank=True)
    writter_name = models.TextField(blank=True)
    Blog_category_CHOICES = (
    ('POPULAR', 'popular blog list'),
    ('RECENT', 'recent blog list'),
    )
    slect_box = models.CharField(blank=True,choices=Blog_category_CHOICES,max_length=120)
    select_box_date = models.DateField(blank=True,null=True)
    select_box_time = models.TimeField(blank=True,null=True)
    enter_blog_time_read = models.CharField(blank=True,max_length=120)
    # main_page_title_image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.PROTECT
    # )

    content_panels = Page.content_panels + [
        FieldPanel('sort_description_body', classname="full"),
        ImageChooserPanel('title_image'),
        FieldPanel('tags'),
        FieldPanel('body', classname="full"),
        FieldPanel('slect_box', classname="full"),
        FieldPanel('select_box_date', classname="full"),
        FieldPanel('select_box_time', classname="full"),
        FieldPanel('enter_blog_time_read', classname="full"),
        FieldPanel('writter_name', classname="full"),
        FieldPanel('blog_category', classname="full"),
        FieldPanel('blog_sub_category', classname="full"),

    ]
    api_fields = [
        APIField('sort_description_body'),
        APIField('title_image'),
        APIField('body'),
        APIField('slect_box'),
        APIField('select_box_date'),
        APIField('enter_blog_time_read'),
        APIField('writter_name'),
        APIField('blog_category'),
        APIField('blog_sub_category'),
        APIField('tags'),
    ]
    def get_context(self, request):
        # Update context to include only published posts,
        # in reverse chronological order
        context = super(RIGHTSIDEHomePage, self).get_context(request)
        live_blogpages = self.get_children().live()
        context['blogpages'] = live_blogpages.order_by('-first_published_at')
        context['main_page1'] = RIGHTSIDEHomePage.objects.all()
        context['main_data3'] = LEFTSIDEWITHSTICKYNOTEHomePage.objects.all()
        context['main_data2'] = LEFTSIDEHomePage.objects.all()
        context["main_data11"] = HomePage.objects.all()
        context["main_data4"]  = RIGHTSIDEWITHSTICKYNOTEHomePage.objects.all()
        context['main_data'] = blog_categories_and_Sub_categories_sub.objects.all()
        context['main_data1'] = blog_categories_and_Sub_categories.objects.all()
        context['main_page4'] = popular_and_recent_blog_lists.objects.all()
        return context

class RIGHTSIDEWITHSTICKYNOTEHomePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'RIGHTSIDEWITHSTICKYNOTEHomePage',
        related_name='tagged_items',
        on_delete=models.PROTECT,
    ) 


class RIGHTSIDEWITHSTICKYNOTEHomePage(Page):
    sort_description_body = RichTextField(blank=True)
    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    tags = ClusterTaggableManager(through=RIGHTSIDEWITHSTICKYNOTEHomePageTag, blank=True)
    blog_category = models.ForeignKey(blog_categories_and_Sub_categories,on_delete=models.PROTECT)
    body = RichTextField(blank=True)
    writter_name = models.TextField(blank=True)
    Blog_category_CHOICES = (
    ('POPULAR', 'popular blog list'),
    ('RECENT', 'recent blog list'),
    )
    slect_box = models.CharField(blank=True,choices=Blog_category_CHOICES,max_length=120)
    select_box_date = models.DateField(blank=True,null=True)
    select_box_time = models.TimeField(blank=True,null=True)
    enter_blog_time_read = models.CharField(blank=True,choices=Blog_category_CHOICES,max_length=120)
    # main_page_title_image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.PROTECT
    # )

    content_panels = Page.content_panels + [
        FieldPanel('sort_description_body', classname="full"),
        ImageChooserPanel('tags'),
        ImageChooserPanel('title_image'),
        FieldPanel('body', classname="full"),
        FieldPanel('slect_box', classname="full"),
        FieldPanel('select_box_date', classname="full"),
        FieldPanel('select_box_time', classname="full"),
        FieldPanel('enter_blog_time_read', classname="full"),
        FieldPanel('writter_name', classname="full"),
        FieldPanel('blog_category', classname="full"),

    ]
    api_fields = [
        APIField('sort_description_body'),
        APIField('title_image'),
        APIField('body'),
        APIField('slect_box'),
        APIField('select_box_date'),
        APIField('enter_blog_time_read'),
        APIField('writter_name'),
        APIField('blog_category'),
        APIField('tags'),
    ]
    
    def get_context(self, request):
        # Update context to include only published posts,
        # in reverse chronological order
        context = super(RIGHTSIDEWITHSTICKYNOTEHomePage, self).get_context(request)
        live_blogpages = self.get_children().live()
        context['blogpages'] = live_blogpages.order_by('-first_published_at')
        context['main_page1'] = RIGHTSIDEWITHSTICKYNOTEHomePage.objects.all()
        context['main_data4'] = RIGHTSIDEHomePage.objects.all()
        context['main_data3'] = LEFTSIDEWITHSTICKYNOTEHomePage.objects.all()
        context['main_data2'] = LEFTSIDEHomePage.objects.all()
        context["main_data11"] = HomePage.objects.all()
        context['main_data'] = blog_categories_and_Sub_categories_sub.objects.all()
        context['main_data1'] = blog_categories_and_Sub_categories.objects.all()
        context['main_page4'] = popular_and_recent_blog_lists.objects.all()
        return context


################# End LEft side blog show ###################
