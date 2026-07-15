from django.contrib import admin
from .models import Profile, Project, HomeSection, Page, ProjectMedia

# TabularInline PARA StackedInline
class ProjectMediaInline(admin.StackedInline):
    model = ProjectMedia
    
    # O usuário terá que clicar ativamente em "Adicionar Mídia" para subir algo novo.
    extra = 0 

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectMediaInline]

admin.site.register(Profile)
admin.site.register(Project, ProjectAdmin)
admin.site.register(HomeSection)
admin.site.register(Page)