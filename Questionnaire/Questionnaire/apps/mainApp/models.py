from django.db import models
from django.contrib.auth.models import User


class questionnaireData(models.Model):
    questionnaire_name = models.TextField('Назва тестування')
    questions_text = models.TextField('Запитання')
    questions_answers = models.TextField('Відповіді')

    def __str__(self):
        return self.questionnaire_name

    class Meta:
        verbose_name = 'Тестування'
        verbose_name_plural = 'Тестування'


class questionnaireAnswers(models.Model):
    questionnaire_name_fk = models.ForeignKey(questionnaireData, on_delete=models.CASCADE, verbose_name='Тестування')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')
    answers = models.TextField('Відповіді')

    def __str__(self):
        return self.user.username + "/" + self.questionnaire_name_fk.questionnaire_name

    class Meta:
        verbose_name = 'Відповідь'
        verbose_name_plural = 'Відповіді'


class lection(models.Model):
    lection_name = models.TextField(verbose_name='Назва лекції')
    lection_text = models.TextField(verbose_name='Текст лекції')
    questionnaire_fk = models.ForeignKey(questionnaireData, on_delete=models.CASCADE, verbose_name='Тестування')

    def __str__(self):
        return self.lection_name

    class Meta:
        verbose_name = 'Лекція'
        verbose_name_plural = 'Лекції'
