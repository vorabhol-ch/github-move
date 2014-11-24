
# Register your models here.


from django.contrib import admin
from game_center.models import Category, Page,Game,Score

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)


admin.site.register(Game)
admin.site.register(Score)

