from django.contrib import admin
from .models import questionnaireAnswers, questionnaireData, lection
admin.site.register(questionnaireAnswers)
admin.site.register(questionnaireData)
admin.site.register(lection)

