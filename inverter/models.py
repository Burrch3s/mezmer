from django.db import models

# Create your models here.
class FileInstance(models.Model):
    name = models.CharField(max_length=120, default='new_file')
    my_file = models.ImageField(upload_to='img')
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
#    def __str__(self):
#        """
#        String for representing the MyModelName object (in Admin site etc.)
#        """
#        return self.field_name
