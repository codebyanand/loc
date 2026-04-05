import os
from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import Category, Saint, Quote, Resource
from datetime import date

class Command(BaseCommand):
    help = 'Populates the database with initial data from your HTML file'

    def handle(self, *args, **options):
        self.stdout.write('Starting database population...')
        
        # Create Categories
        categories_data = [
            ('lords-feasts', "Lord's Feasts", '👑'),
            ('marian-feasts', 'Marian Feasts', '🌹'),
            ('apostles', 'Apostles', '🕊️'),
            ('evangelists', 'Evangelists', '📖'),
            ('martyrs', 'Martyrs', '🛡️'),
            ('doctors', 'Doctors of the Church', '📚'),
            ('pastors', 'Pastors', '⛪'),
            ('founders', 'Founders', '🏛️'),
            ('mystics', 'Mystics', '✨'),
            ('virgins', 'Virgins', '🌷'),
            ('confessors', 'Confessors', '✝️'),
            ('religious', 'Religious', '🙏'),
            ('lay-people', 'Lay People', '👥'),
            ('salesian', 'Salesian Sanctity', '💙'),
            ('church', "Church's Feasts", '⛪'),
        ]
        
        categories = {}
        for cat_id, name, icon in categories_data:
            cat, created = Category.objects.get_or_create(
                id=cat_id,
                defaults={'name': name, 'icon': icon}
            )
            categories[cat_id] = cat
            self.stdout.write(f"{'Created' if created else 'Found'} category: {name}")
        
        # Create Saints (Add your saints from DEFAULT_SAINTS)
        # I'll add a few samples, you'll need to add all your saints
        saints_data = [
            {
                'id': 'mary-mother-of-god',
                'name': 'Mary, Mother of God',
                'img': 'https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/42-religious-mary-mother-of-god-the-pristine-artist.jpg',
                'feast': 'January 1',
                'desc': 'The Theotokos (God-bearer), chosen by God from all eternity to be the Mother of His Son.',
                'categories': ['marian-feasts', 'virgins']
            },
            {
                'id': 'st-francis-assisi',
                'name': 'St. Francis of Assisi',
                'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Francis_of_Assisi_in_ecstasy_%28Caravaggio%29.jpg/800px-Francis_of_Assisi_in_ecstasy_%28Caravaggio%29.jpg',
                'feast': 'October 4',
                'desc': 'Founder of the Franciscan Order, known for his love of nature and the poor.',
                'categories': ['founders', 'mystics', 'religious']
            },
            # Add all your other saints here from the DEFAULT_SAINTS array
        ]
        
        for saint_data in saints_data:
            saint, created = Saint.objects.get_or_create(
                id=saint_data['id'],
                defaults={
                    'name': saint_data['name'],
                    'img': saint_data['img'],
                    'feast': saint_data['feast'],
                    'desc': saint_data['desc'],
                }
            )
            
            for cat_id in saint_data.get('categories', []):
                if cat_id in categories:
                    saint.categories.add(categories[cat_id])
            
            self.stdout.write(f"{'Created' if created else 'Found'} saint: {saint.name}")
        
        # Create Resources (Prayers)
        resources_data = [
            {
                'id': 'prayer-to-st-michael',
                'title': 'Prayer to St. Michael the Archangel',
                'content': 'St. Michael the Archangel, defend us in battle...',
                'type': 'prayer',
                'tags': 'protection,archangel,spiritual-warfare'
            },
            {
                'id': 'act-of-contrition',
                'title': 'Act of Contrition',
                'content': 'O my God, I am heartily sorry for having offended Thee...',
                'type': 'prayer',
                'tags': 'confession,repentance,mercy'
            },
            {
                'id': 'hail-holy-queen',
                'title': 'Hail Holy Queen',
                'content': 'Hail, holy Queen, Mother of mercy, our life, our sweetness and our hope...',
                'type': 'prayer',
                'tags': 'mary,rosary,queen'
            },
        ]
        
        for resource_data in resources_data:
            resource, created = Resource.objects.get_or_create(
                id=resource_data['id'],
                defaults={
                    'title': resource_data['title'],
                    'content': resource_data['content'],
                    'type': resource_data['type'],
                    'tags': resource_data['tags'],
                }
            )
            self.stdout.write(f"{'Created' if created else 'Found'} resource: {resource.title}")
        
        self.stdout.write(self.style.SUCCESS('✅ Database population complete!'))
        self.stdout.write(f"📊 Statistics:")
        self.stdout.write(f"   - Categories: {Category.objects.count()}")
        self.stdout.write(f"   - Saints: {Saint.objects.count()}")
        self.stdout.write(f"   - Resources: {Resource.objects.count()}")