from typing import List

import ruamel.yaml


class ConfigRedactor:
    def __init__(self, config_file_path: str):
        self.config_file_path = config_file_path

    def _redactor(func):
        def wrapper(self, *args, **kwargs):
            yaml = ruamel.yaml.YAML()
            config_file_data = None

            with open(self.config_file_path, 'r') as f:
                config_file_data = yaml.load(f)

            with open(self.config_file_path, 'w') as f:
                f.truncate(0)
                func(self, config_file_data=config_file_data, *args, **kwargs)
                yaml.dump(config_file_data, f)

        return wrapper

    @_redactor
    def redactor_input_files(self, config_file_data, input_files):
        config_file_data['steps'][0]['parameters']['inputs'] = input_files

    @_redactor
    def redactor_output_files(self, config_file_data, output_files):
        config_file_data['steps'][0]['parameters']['outputs'] = output_files

    @_redactor
    def redactor_list_of_languages(self, config_file_data, languages: List[str]):
        config_file_data['steps'][0]['parameters']['outputs'] = languages


if __name__ == "__main__":
    redactor = ConfigRedactor('../config.yaml')
    redactor.redactor_input_files(input_files=['WikiMatrix.en-ru.en', 'WikiMatrix.en-ru.ru'])
    redactor.redactor_output_files(output_files=['test_1.txt', 'test_2.txt'])
    redactor.redactor_list_of_languages(languges=['en','ru'])