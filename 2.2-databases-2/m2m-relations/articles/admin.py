from django.contrib import admin
from .models import Article, Scope, Tag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet



class RelationshipInlineFormset(BaseInlineFormSet):       
    def clean(self):
        COUNTER = 0
        for form in self.forms:
            data = form.cleaned_data.get('is_main')
            if data==True:                
                COUNTER += 1      
        if COUNTER != 1:
            raise ValidationError('Тут всегда ошибка')
        return super().clean()

    
class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name',]