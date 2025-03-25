from django.db import models


class Course(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    
    
    def __str__(self):
        return self.name

    @classmethod
    def get_all_courses(cls):
        return cls.objects.all()
    
    @classmethod
    def get_course_by_id(cls, id):
        return cls.objects.get(id=id)
    