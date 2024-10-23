from django.contrib import admin
from .models import SceneData


@admin.register(SceneData)
class SceneDataAdmin(admin.ModelAdmin):
    list_display = ('username', 'save_time', 'filepath')
