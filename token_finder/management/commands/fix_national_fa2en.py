from django.core.management.base import BaseCommand

from token_finder.models import SpotPlayer


class Command(BaseCommand):
    help = "Fix persian national codes"
    _numbers_arabic = '۰۱۲۳۴۵۶۷۸۹'
    _numbers_english = '0123456789'
    number_translation_table = str.maketrans(_numbers_arabic, _numbers_english)

    def handle(self, *args, **options):
        for item in SpotPlayer.objects.all():
            if str(int(item.national_code)) != item.national_code:
                item.national_code = str(item.national_code).translate(self.number_translation_table)
                item.save()
