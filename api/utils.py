import os
import json


class Utils:

    @staticmethod
    def make_path(path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def convert_list_to_dict(list_data):
        return {"result": json.loads(list_data.text)}
