import re
import opusfilter
import pymorphy2


class ExistanceWordsFilter(opusfilter.FilterABC):
    score_direction = opusfilter.CLEAN_LOW
    threshold = 0.75

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _split_sentence_to_words(self, sentence):
        separators = "[, .;?!]"

        split_line = re.split(separators, sentence)
        return split_line

    def _calc_probability_existence(self, split_line):
        threshold = 0.75
        existence_words = 0
        non_existence_words = 0

        morph = pymorphy2.MorphAnalyzer()
        for word in split_line:
            p = morph.parse(word)
            score = p[0].score

            if score >= threshold:
                existence_words+=1
            else:
                non_existence_words+=1

        return existence_words/(existence_words + non_existence_words)


    def score(self, pairs):
        for pair in pairs:
            yield [self._calc_probability_existence(self._split_sentence_to_words(text)) for text in pair]

    def accept(self, score):
        threshold = 0.5
        return (ratio>=threshold for ratio in score)


