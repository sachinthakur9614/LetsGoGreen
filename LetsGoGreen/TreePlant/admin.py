from django.contrib import admin

# Register your models here.
from .models import TreeCatalog,TreeGrowth,TreeGrowthApproval


from django.contrib.auth.models import User




class TreeCataLogAdmin(admin.ModelAdmin):
	list_display = ('id','treeName','treeImage','treeDescription','lifeTime')
	list_display_links =('id','treeName')
	# search_fields =('treeName')
	list_per_page=20


# @admin.register(TreeGrowth)
class TreeGrowthAdmin(admin.ModelAdmin):
	list_display = ('id','firstImage','secondImage','thirdImage','us_id')
	list_display_links =('id','firstImage','secondImage')
	readonly_fields = ["headshot_image"]
	list_per_page=20

	def headshot_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format( url = obj.firstImage.url,width=obj.secongImage.width,height=obj.thirdImage.height )
	# search_fields =('firstImage')
	)

# admin.site.register(TreeGrowthApproval)


admin.site.register(TreeCatalog,TreeCataLogAdmin)

admin.site.register(TreeGrowth,TreeGrowthAdmin)

