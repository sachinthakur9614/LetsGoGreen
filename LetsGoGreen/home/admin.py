from django.contrib import admin

# Register your models here.


from .models import AboutDescription, TeamInfo,OurServices,Contact




from .models import  Slider,OurPartner


admin.site.register(AboutDescription)

admin.site.register(TeamInfo)

admin.site.register(OurServices)




class SliderAdmin(admin.ModelAdmin):
	list_display = ('id','slide1','slide2','slide3')
	list_display_links = ('id','slide1')
	list_filter =('slide1',)
	list_editable=('slide2',)
	search_fields=('slide1','slide2')
	list_per_page=2



admin.site.register(Slider,SliderAdmin)


admin.site.register(OurPartner)




class ContactAdmin(admin.ModelAdmin):
	list_display = ('id','name','email','phone')
	list_display_links =('id','name')
	search_fields =('name','email','phone')
	list_per_page=20


# admin.site.register(Contact,ContactAdmin)
