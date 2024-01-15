import re

import opusfilter
from langid import classify


class CorrectLanguageFilter(opusfilter.FilterABC):
    score_direction = opusfilter.CLEAN_LOW

    def __init__(self, languages, **kwargs):
        self.languages = languages
        super().__init__(**kwargs)


    def _delete_lang_explanation(self, sentence):
        separators = "[«»'англ.','рус.']"

        return "".join(re.split(separators, sentence))

    def _lang_detect(self, sentence):
        lang, _ = classify(self._delete_lang_explanation(sentence))
        return lang

    def score(self, pairs):
        for pair in pairs:
            yield [self._lang_detect(text) for text in pair]

    def accept(self, score):
        for index, lang in enumerate(score):
            if lang not in self.languages:
                score[index] = self.languages[index]

        return score == self.languages

