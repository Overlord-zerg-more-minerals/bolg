from django.contrib import admin
from articel.models import *

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Comments)
admin.site.register(Tag)