import subprocess
from services.config_redactor import ConfigRedactor
from services.deleted_line_counter import DeletedLinesCounter


# path to the configuration file
config_file = "config.yaml"
# path to source files
input_files = ['WikiMatrix.en-ru.en','WikiMatrix.en-ru.ru']
# path to filtered files
output_files= ['resultWikiMatrix_en.txt', 'resultWikiMatrix_ru.txt']
# languages used
languages= ['en','ru']

# setting up a configuration file
config_redactor = ConfigRedactor(config_file)
config_redactor.redactor_input_files(input_files=input_files)
config_redactor.redactor_output_files(output_files=output_files)
config_redactor.redactor_list_of_languages(languages=languages)

# run OpusFilter with configuration file
subprocess.run(["opusfilter", config_file])

# information about the number of filtered rows
deleted_line_counter = DeletedLinesCounter(input_files, output_files)
print(f"Number of original lines: {deleted_line_counter.original_number_of_lines}")
print(f'Number of deleted string: {deleted_line_counter.number_of_deleted_lines}')
