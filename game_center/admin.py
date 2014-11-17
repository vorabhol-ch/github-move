
# Register your models here.


from django.contrib import admin
from game_center.models import Category, Page,Game,Score

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Game)
admin.site.register(Score)

