from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from isodur_app.models import Project


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title',)
