from django.contrib import admin
from  .models import Role, Category, SubCategory, Project, Submission, Reviewer, Objective, Spec, Resource

# Register your models here.

admin.site.register(Role)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Submission)
admin.site.register(Reviewer)
# admin.site.register(Objective)
# admin.site.register(Spec)
# admin.site.register(Resource)

class ObjectiveInline(admin.TabularInline):
	model = Objective

class SpecInline(admin.TabularInline):
	model = Spec

class ResourceInline(admin.TabularInline):
	model = Resource

class ProjectAdmin(admin.ModelAdmin):
	inlines = [
				ObjectiveInline,
				SpecInline,
				ResourceInline
			]

admin.site.register(Project, ProjectAdmin)
