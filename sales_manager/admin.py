from django.contrib import admin

# Register your models here.
from sales_manager.models import Book, Comment

# class CommentAdmin(admin.StackedInline):
#     model = Comment
#     # readonly_fields = ('like', )
#
# class BookInLine(admin.ModelAdmin):
#     inlines = (CommentAdmin, )
#     # readonly_fields = ('likes', )
#     list_filter = ('data_publish',)
#     list_editable = ('text', )




admin.site.register(Book)

