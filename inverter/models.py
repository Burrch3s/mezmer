from django.db import models

# Create your models here.
class FileInstance(models.Model):
    my_file = models.ImageField(max_length=20, help_text="Enter field documentation")
    # Metadata
    class Meta: 
        ordering = ["-my_file"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name
