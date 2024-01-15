class DeletedLinesCounter:
    def __init__(self, original_files, result_files):
        self.original_number_of_lines = self._counter_number_of_lines(original_files[0])
        self.result_number_of_lines = self._counter_number_of_lines(result_files[0])
        self.number_of_deleted_lines = self._number_of_deleted_lines()


    def _counter_number_of_lines(self, file):
        number_of_lines = 0

        with open(file) as f:
            for line in f:
                number_of_lines+=1

        return number_of_lines

    def _number_of_deleted_lines(self):
        return self.original_number_of_lines-self.result_number_of_lines