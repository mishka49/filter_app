import opusfilter


class SentenceQuantityFilter(opusfilter.FilterABC):
    score_direction = opusfilter.CLEAN_LOW

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def quantity_of_sentences(self, sentence):
        return len(sentence.split('.|?|!|."|?"|!"'))


    def score(self, pairs):
        for pair in pairs:
            yield [self.quantity_of_sentences(text) for text in pair]

    def accept(self, score):
        return all(ratio for ratio in score)
