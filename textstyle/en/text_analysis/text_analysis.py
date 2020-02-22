import os
import re
import sys
import nltk
import codecs
import string
import copy as cp
import seaborn as sns
from functools import reduce
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag

sns.set(style="darkgrid")
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def words_count(text):
    if isinstance(text, list):
        text = ' '.join(text)

    words_dict = {}

    for word in word_tokenize(text):
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    return words_dict


def words_ids(text):
    if isinstance(text, list):
        text = ' '.join(text)

    words_dict = {word: id_ for word, id_ in enumerate(set(word_tokenize(text)))}
    ids_dict = {id_: word for id_, word in words_dict.items()}

    return words_dict, ids_dict

