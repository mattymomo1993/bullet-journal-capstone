from django.db import models
from django.utils import timezone
from journaluser.models import BulletJournalUser

# Create your models here.

class Assignments(models.Model):
    TYPE = (
      ('New', 'New'),
      ('Lesson', 'Lesson'),
      ('Activity', 'Activity'),
      ('Quiz', 'Quiz'),
      ('Assessment', 'Assessment'),
      ('Completed', 'Completed'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, default=None)
    date_filed = models.DateTimeField(default=timezone.now)
    assignment_type = models.CharField(max_length=200, choices=TYPE)
    user_created = models.ForeignKey(BulletJournalUser, on_delete=models.CASCADE,
                                     related_name="created_by_bulletjournaluser", blank=True, null=True, default=None)
    
    def __str__(self):
        return f"{self.title}"


class ReflectionPost(models.Model):
    name_choices = ((True, 'Morning Reflection'), (False, 'Evening Reflection'))
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True, default=None)
    submission_time = models.DateTimeField(default=timezone.now)
    name_post = models.BooleanField(choices=name_choices)
    reflection_user_created = models.ForeignKey(BulletJournalUser, on_delete=models.CASCADE,
                                     related_name="reflection_created_by_bulletjournaluser", blank=True, null=True, default=None)

    def __str__(self):
      return f"{self.title}"
