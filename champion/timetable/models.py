from django.db import models
from django.utils.safestring import mark_safe

class Timetable(models.Model):
    name = models.CharField('название', max_length=100)
    monday = models.CharField('понедельник', max_length=11, default='---')
    tuesday = models.CharField('вторник', max_length=11, default='---')
    wednesday = models.CharField('среда', max_length=11, default='---')
    thursday = models.CharField('четверг', max_length=11, default='---')
    friday = models.CharField('пятница', max_length=11, default='---')
    saturday = models.CharField('суббота', max_length=11, default='---')

    @property
    def formated_days(self):
        days_map = [
            ('ПН', self.monday),
            ('ВТ', self.tuesday),
            ('СР', self.wednesday),
            ('ЧТ', self.thursday),
            ('ПТ', self.friday),
            ('СБ', self.saturday),
        ]

        result = []

        for label, value in days_map:
            formated_value = value
            if value and value != '---':
                parts = value.split()
                if len(parts) == 2:
                    formated_value = mark_safe(f'{parts[0]}<br>{parts[1]}')
            result.append({
                'label': label,
                'value': formated_value,
            })
        return result

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'расписания'


