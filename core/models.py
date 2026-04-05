# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# class Category(models.Model):
#     """Categories for saints (Martyrs, Doctors, etc.)"""
#     CATEGORY_TYPES = [
#         ('lords-feasts', "Lord's Feasts"),
#         ('marian-feasts', 'Marian Feasts'),
#         ('apostles', 'Apostles'),
#         ('evangelists', 'Evangelists'),
#         ('martyrs', 'Martyrs'),
#         ('doctors', 'Doctors of the Church'),
#         ('pastors', 'Pastors'),
#         ('founders', 'Founders'),
#         ('mystics', 'Mystics'),
#         ('virgins', 'Virgins'),
#         ('confessors', 'Confessors'),
#         ('religious', 'Religious'),
#         ('lay-people', 'Lay People'),
#         ('salesian', 'Salesian Sanctity'),
#         ('church', "Church's Feasts"),
#     ]
    
#     id = models.CharField(max_length=50, primary_key=True)
#     name = models.CharField(max_length=100)
#     icon = models.CharField(max_length=10, blank=True, default='📖')
#     description = models.TextField(blank=True)
    
#     class Meta:
#         verbose_name_plural = "Categories"
    
#     def __str__(self):
#         return self.name

# class Saint(models.Model):
#     """Saint model with complete biography"""
#     id = models.CharField(max_length=100, primary_key=True)
#     name = models.CharField(max_length=200, db_index=True)
#     img = models.URLField(max_length=500, blank=True)
#     born = models.CharField(max_length=200, blank=True)
#     died = models.CharField(max_length=200, blank=True)
#     feast = models.CharField(max_length=100, blank=True, db_index=True)
#     desc = models.TextField(blank=True)
#     canonized_on = models.CharField(max_length=200, blank=True)
#     canonized_by = models.CharField(max_length=200, blank=True)
    
#     categories = models.ManyToManyField(Category, related_name='saints', blank=True)
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         ordering = ['name']
#         indexes = [
#             models.Index(fields=['name']),
#             models.Index(fields=['feast']),
#         ]
    
#     def __str__(self):
#         return self.name

# class Quote(models.Model):
#     """Quote model with saint reference"""
#     RANK_CHOICES = [
#         ('solemnity', 'Solemnity'),
#         ('feast', 'Feast'),
#         ('memorial', 'Memorial'),
#         ('optional_memorial', 'Optional Memorial'),
#     ]
    
#     id = models.CharField(max_length=100, primary_key=True)
#     text = models.TextField()
#     saint = models.ForeignKey(Saint, on_delete=models.CASCADE, related_name='quotes')
#     rank = models.CharField(max_length=50, choices=RANK_CHOICES, blank=True)
#     date = models.DateField(db_index=True)
    
#     categories = models.ManyToManyField(Category, related_name='quotes', blank=True)
    
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         ordering = ['-date']
#         indexes = [
#             models.Index(fields=['-date']),
#             models.Index(fields=['saint', '-date']),
#         ]
    
#     def __str__(self):
#         return f"{self.saint.name}: {self.text[:50]}..."

# class Resource(models.Model):
#     """Prayers and devotional resources"""
#     TYPE_CHOICES = [
#         ('prayer', 'Prayer'),
#         ('devotion', 'Devotion'),
#         ('hymn', 'Hymn'),
#         ('meditation', 'Meditation'),
#     ]
    
#     id = models.CharField(max_length=100, primary_key=True)
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='prayer')
#     tags = models.CharField(max_length=500, blank=True)
    
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def get_tags_list(self):
#         return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
    
#     def __str__(self):
#         return self.title

# class Favorite(models.Model):
#     """User favorites"""
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     session_id = models.CharField(max_length=100, blank=True)
#     quote = models.ForeignKey(Quote, on_delete=models.CASCADE, null=True, blank=True)
#     saint = models.ForeignKey(Saint, on_delete=models.CASCADE, null=True, blank=True)
#     resource = models.ForeignKey(Resource, on_delete=models.CASCADE, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         unique_together = [
#             ['user', 'quote'], ['user', 'saint'], ['user', 'resource'],
#             ['session_id', 'quote'], ['session_id', 'saint'], ['session_id', 'resource']
#         ]
    
#     def __str__(self):
#         user = self.user.username if self.user else self.session_id
#         item = self.quote or self.saint or self.resource
#         return f"Favorite by {user}: {item}"


from django.db import models

class Category(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return self.name

class Saint(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=200)
    img = models.URLField(max_length=500, blank=True)
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
    date = models.DateField()
    categories = models.ManyToManyField(Category, blank=True)
    
    def __str__(self):
        return f"{self.saint.name}: {self.text[:50]}"