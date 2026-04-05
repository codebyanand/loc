
# from django.db import models

# class Category(models.Model):
#     id = models.CharField(max_length=50, primary_key=True)
#     name = models.CharField(max_length=100)
#     icon = models.CharField(max_length=10, blank=True)
    
#     def __str__(self):
#         return self.name

# class Saint(models.Model):
#     id = models.CharField(max_length=100, primary_key=True)
#     name = models.CharField(max_length=200)
#     img = models.URLField(max_length=500, blank=True)
#     born = models.CharField(max_length=200, blank=True)
#     died = models.CharField(max_length=200, blank=True)
#     feast = models.CharField(max_length=100, blank=True)
#     desc = models.TextField(blank=True)
#     categories = models.ManyToManyField(Category, blank=True)
    
#     def __str__(self):
#         return self.name

# class Quote(models.Model):
#     id = models.CharField(max_length=100, primary_key=True)
#     text = models.TextField()
#     saint = models.ForeignKey(Saint, on_delete=models.CASCADE, related_name='quotes')
#     rank = models.CharField(max_length=50, blank=True)
#     date = models.DateField()
#     categories = models.ManyToManyField(Category, blank=True)
    
#     def __str__(self):
#         return f"{self.saint.name}: {self.text[:50]}"

from django.db import models

class Category(models.Model):
    # Using default AutoField (integer) is usually better unless you have specific IDs
    id = models.CharField(max_length=50, primary_key=True) 
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return self.name

class Saint(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    
    # CHANGE: Changed from URLField to ImageField for Cloudinary support
    img = models.ImageField(upload_to='saints/', blank=True, null=True)
    
    born = models.CharField(max_length=200, blank=True)
    died = models.CharField(max_length=200, blank=True)
    feast = models.CharField(max_length=100, blank=True)
    desc = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    
    def __str__(self):
        return self.name

class Quote(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    text = models.TextField()
    saint = models.ForeignKey(Saint, on_delete=models.CASCADE, related_name='quotes')
    rank = models.CharField(max_length=50, blank=True)
    date = models.DateField() # Perfect for "Daily Quote" logic
    categories = models.ManyToManyField(Category, blank=True)
    
    def __str__(self):
        return f"{self.saint.name}: {self.text[:50]}"