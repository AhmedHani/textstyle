import os
import nltk
import string


def nltk_bleu_score(hypothesis, reference):
    if len(hypothesis.split()) <= 3:
        return nltk.translate.bleu_score.sentence_bleu([reference], hypothesis, weights = (0.5, 0.5))

    return nltk.translate.bleu_score.sentence_bleu([reference], hypothesis)


def my_bleu_score(hypothesis, reference):
    pass