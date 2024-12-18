from django.db import models
import string
import random

# Create your models here.

class Shortener(models.Model):
    url = models.URLField(max_length=255)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.url
    
    def generate_short_code(self):
        """
        Generates a random short code consisting of letters and digits.

        The length of the short code is randomly chosen between 5 and 10 characters.

        Returns:
            str: A randomly generated short code.
        """
        
        length = random.randint(5, 10)
        characters = string.ascii_letters + string.digits
        short_code = ''.join(random.choice(characters) for _ in range(length))
        return short_code
    
    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()
            while Shortener.objects.filter(short_code=self.short_code).exists():
                self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)