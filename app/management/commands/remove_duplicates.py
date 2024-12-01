from django.core.management.base import BaseCommand
from app.models import Bike

class Command(BaseCommand):
    help = 'Remove duplicate bike entries without images'

    def handle(self, *args, **kwargs):
        bikes = Bike.objects.all()
        unique_bikes = []
        unique_names = set()

        for bike in bikes:
            if bike.image:
                unique_bikes.append(bike)
                unique_names.add(bike.name)
            else:
                if bike.name not in unique_names:
                    unique_bikes.append(bike)
                    unique_names.add(bike.name)

        Bike.objects.exclude(id__in=[b.id for b in unique_bikes]).delete()
        self.stdout.write(self.style.SUCCESS('Duplicate bike entries without images removed successfully'))
