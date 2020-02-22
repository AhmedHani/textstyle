import re
import nltk
import string
import copy as cp
from functools import reduce
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


__stopwords_list = set(stopwords.words('english'))


def text2sents(text):
    return nltk.sent_tokenize(text)


def remove_extra_spaces(text):
    if isinstance(text, list):
        return [re.sub(' +', ' ', one) for one in text]

    return re.sub(' +', ' ', text)


def normalize_text(text):
    if isinstance(text, list):
        return [one.lower() for one in text]

    return ' '.join([word.lower() for word in text.split()])


def replace_apostrophes(text):
    apostrophes_mapping = {'\'s': ' is', '\'ve': ' have', 'n\'t': ' not', '\'d': ' would',
                           '\'m': ' am', '\'ll': ' will', '\'re': ' are'}

    # elegant! https://stackoverflow.com/a/9479972
    if isinstance(text, list):
        return [reduce(lambda a, kv: a.replace(*kv), apostrophes_mapping.items(), s) for s in text]

    return reduce(lambda a, kv: a.replace(*kv), apostrophes_mapping.items(), text)


def remove_punctuations(text):
    if isinstance(text, list):
        return [re.sub(r'[^\w\s]', '', one) for one in text]

    return re.sub(r'[^\w\s]', '', text)


def separate_punctuations(text):
    for punc in string.punctuation:
        text = text.replace(punc, ' ' + punc)

    return text


def remove_custom_chars(text, chars_list):
    if isinstance(text, list):
        return [re.sub("|".join(chars_list), "", one) for one in text]

    return re.sub("|".join(chars_list), "", text)


def remove_stop_words(text):
    nltk_stop_words = __stopwords_list

    if isinstance(text, list):
        return [' '.join([word for word in one.split() if word not in nltk_stop_words]) for one in text]

    return ' '.join([word for word in text.split(' ') if word not in nltk_stop_words])


def word_based_pad(sentences_list, size=None, token='pad'):
    sentences = cp.deepcopy(sentences_list)

    if size is None:
        size = max([len(sentence.split()) for sentence in sentences])

    for i, sentence in enumerate(sentences):
        sentence_tokens = sentence.split()

        while len(sentence_tokens) < size:
            sentence_tokens.append(token)

        sentences[i] = ' '.join(sentence_tokens)

    return sentences


def word_based_truncate(sentences_list, size):
    sentences = cp.deepcopy(sentences_list)

    for i, sentence in enumerate(sentences):
        sentence_tokens = sentence.split()
        sentences[i] = ' '.join(sentence_tokens[0:size])

    return sentences


def char_based_pad(sentences_list, size=None, token='#'):
    sentences = cp.deepcopy(sentences_list)

    if size is None:
        size = max([len(list(sentence)) for sentence in sentences])

    for i, sentence in enumerate(sentences):
        sentence_tokens = list(sentence)

        while len(sentence_tokens) < size:
            sentence_tokens.append(token)

        sentences[i] = ''.join(sentence_tokens)

    return sentences


def chat_based_truncate(sentences_list, size):
    sentences = cp.deepcopy(sentences_list)

    for i, sentence in enumerate(sentences):
        sentence_tokens = list(sentence)
        sentences[i] = ''.join(sentence_tokens[0:size])

    return sentences


def remove_verbs(text):
    if isinstance(text, str):
        return ' '.join([word for word, pos in pos_tag(word_tokenize(text)) if not pos.startswith('VB')])

    return [' '.join([word for word, pos in pos_tag(word_tokenize(sentence)) if not pos.startswith('VB')]) for sentence in text]


def remove_nouns(text):
    if isinstance(text, str):
        return ' '.join([word for word, pos in pos_tag(word_tokenize(text)) if not pos.startswith('VB')])

    return [' '.join([word for word, pos in pos_tag(word_tokenize(sentence)) if not pos.startswith('NN')]) for sentence in text]

