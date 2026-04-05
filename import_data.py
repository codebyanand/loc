import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'livesofchrist.settings')
django.setup()

from core.models import Category, Saint, Quote

def import_categories():
    """Import categories from your HTML app"""
    categories = [
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
    
    for cat_id, name, icon in categories:
        cat, created = Category.objects.get_or_create(
            id=cat_id,
            defaults={'name': name, 'icon': icon}
        )
        print(f"{'Created' if created else 'Found'} category: {name}")

def import_saints():
    """Import sample saints"""
    
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
        {
            'id': 'st-therese-lisieux',
            'name': 'St. Thérèse of Lisieux',
            'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Thérèse_of_Lisieux_1895.jpg/800px-Thérèse_of_Lisieux_1895.jpg',
            'feast': 'October 1',
            'desc': 'Known as "The Little Flower," she developed the "Little Way" of spiritual childhood.',
            'categories': ['doctors', 'virgins', 'mystics']
        },
        {
            'id': 'st-john-bosco',
            'name': 'St. John Bosco',
            'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Don_Bosco.jpg/800px-Don_Bosco.jpg',
            'feast': 'January 31',
            'desc': 'Founder of the Salesian Society, dedicated to education and welfare of youth.',
            'categories': ['founders', 'pastors', 'salesian']
        },
        {
            'id': 'st-augustine',
            'name': 'St. Augustine of Hippo',
            'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Fra_Angelico_031.jpg/800px-Fra_Angelico_031.jpg',
            'feast': 'August 28',
            'desc': 'Doctor of the Church, author of "Confessions" and "City of God."',
            'categories': ['doctors', 'pastors']
        },
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
        
        # Add categories
        for cat_id in saint_data.get('categories', []):
            try:
                cat = Category.objects.get(id=cat_id)
                saint.categories.add(cat)
            except Category.DoesNotExist:
                print(f"Warning: Category {cat_id} not found")
        
        print(f"{'Created' if created else 'Found'} saint: {saint.name}")

def import_quotes():
    """Import sample quotes"""
    
    quotes_data = [
        {
            'id': 'q1',
            'text': 'Preach the Gospel at all times. If necessary, use words.',
            'saint_id': 'st-francis-assisi',
            'date': '2024-10-04'
        },
        {
            'id': 'q2',
            'text': 'My vocation is love!',
            'saint_id': 'st-therese-lisieux',
            'date': '2024-10-01'
        },
        {
            'id': 'q3',
            'text': 'Do ordinary things with extraordinary love.',
            'saint_id': 'st-therese-lisieux',
            'date': '2024-10-01'
        },
        {
            'id': 'q4',
            'text': 'Run, jump, shout, but do not sin.',
            'saint_id': 'st-john-bosco',
            'date': '2024-01-31'
        },
        {
            'id': 'q5',
            'text': 'You have made us for yourself, O Lord, and our hearts are restless until they rest in you.',
            'saint_id': 'st-augustine',
            'date': '2024-08-28'
        },
        {
            'id': 'q6',
            'text': 'Hail, full of grace, the Lord is with thee!',
            'saint_id': 'mary-mother-of-god',
            'date': '2024-01-01'
        },
    ]
    
    for quote_data in quotes_data:
        try:
            saint = Saint.objects.get(id=quote_data['saint_id'])
            quote, created = Quote.objects.get_or_create(
                id=quote_data['id'],
                defaults={
                    'text': quote_data['text'],
                    'saint': saint,
                    'date': quote_data['date'],
                }
            )
            print(f"{'Created' if created else 'Found'} quote: {quote.text[:50]}...")
        except Saint.DoesNotExist:
            print(f"Warning: Saint {quote_data['saint_id']} not found")

if __name__ == '__main__':
    print("=" * 50)
    print("Starting data import for Lives of Christ...")
    print("=" * 50)
    
    import_categories()
    print("-" * 30)
    import_saints()
    print("-" * 30)
    import_quotes()
    
    print("=" * 50)
    print(f"Import complete!")
    print(f"Categories: {Category.objects.count()}")
    print(f"Saints: {Saint.objects.count()}")
    print(f"Quotes: {Quote.objects.count()}")
    print("=" * 50)