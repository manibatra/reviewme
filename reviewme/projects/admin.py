from django.contrib import admin
from  .models import Role, Category, SubCategory, Project, Submission

# Register your models here.

admin.site.register(Role)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Project)
admin.site.register(Submission)

