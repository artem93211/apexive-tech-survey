import json

from pilotlog.models import Aircraft


def import_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(len(data))

        # for record in data:
        #     table_name = record.get('table', None)
        #     meta = record.get('meta', None)
        #
        #     if table_name and meta:
        #         model_class = None
        #         if table_name == 'Aircraft':
        #             model_class = Aircraft
        #
        #         if model_class:
        #             instance = model_class.objects.create(**meta)
        return data
