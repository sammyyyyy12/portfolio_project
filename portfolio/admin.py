from .models import Project
from django.contrib import admin
from .models import Resume
from .models import Poem
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack')
    search_fields = ('title', 'tech_stack')
    list_filter = ('tech_stack',)
    ordering = ('-id',)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('version', 'uploaded_at', 'is_active')
    list_filter = ('is_active',)
@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)  
