from blogs.models import Post, Tag
from django.contrib import admin

class TagAdmin (admin.ModelAdmin):

	save_on_top = True
	list_per_page = 50
	
	prepopulated_fields = {"slug": ("name",)}
	
	def titlezed(obj):
		return obj.name.title()
		
	def countTags(obj):
		return Post.objects.filter(tags__slug=obj.slug).count()
			
	titlezed.short_description = 'Name'
	countTags.short_description = 'Attached to posts'
	
	list_display = ('id', titlezed, countTags)
	
	search_fields = ['name']

class PostAdmin(admin.ModelAdmin):

	list_display = ('id', 'title', 'createdAt', 'visible')
	list_filter = ('visible',)
	
	fields = ('title','text', 'visible', 'createdAt', 'tags')
	
	filter_horizontal = ['tags']
	
	list_per_page = 50
	save_on_top = True
	search_fields = ['title', 'text']
	
	class Media: 
		css = {"all": ("/admin/general.css", "/admin/cleditor/jquery.cleditor.css")}
		js = ("https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js", "/admin/cleditor/jquery.cleditor.js", "/admin/general.js")
	                                                                                                         	
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
