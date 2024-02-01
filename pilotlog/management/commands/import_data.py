import json

from django.core.management.base import BaseCommand

from json_importer import import_data_from_json


class Command(BaseCommand):
    help = 'Import data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            import_data_from_json(file_path)
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'File not found: {file_path}'))
        except json.JSONDecodeError as e:
            self.stderr.write(self.style.ERROR(f'Invalid JSON format in the file {e.msg}'))
