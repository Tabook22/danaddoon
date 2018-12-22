from django.contrib import admin
from .models import Tutorial

#here am creating a class called TutorialAdmin, this class will be used
#customize the admin page
class TutorialAdmin(admin.ModelAdmin):
    #the name list_display is important to write it exatly as it is otherwise it will not work
    list_display=('id','title','date_published', 'is_published')
    #here we need to choose which list item we are going to choose to make them as links
    list_display_links=('id','title')

    #here we want to filter it by date displyed
    list_filter=('title',)  # putting the last "comma" is important otherwise will give error
    ordering = ('-date_published',) # The negative sign indicate descendent order
    list_editable=('is_published',)   # we need to click on is published to enable that choose in the list
    search_fields =('title', 'l_desc','date_published') # here we are putting the fields we need to search by
    
    #defining number of items or tutorials per page
    list_per_page=25

admin.site.register(Tutorial,TutorialAdmin)
