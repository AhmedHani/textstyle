import re
import nltk
import string
import seaborn as sb
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag
sb.set(style='darkgrid')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


__stopwords_list = set(stopwords.words('english'))


def get_basic_style_features(text, split_to_sentences=False):
    if isinstance(text, str) and split_to_sentences:
        text = nltk.sent_tokenize(text)
    # words count
    words_count = [len(sample.split()) for sample in text]

    # chars counts
    chars_count = [len(sample) for sample in text]

    # capital case letters count
    capital_chars_count = [len([c for c in sample if c.isupper()]) for sample in text]

    # lower case letters count
    lower_chars_count = [len([c for c in sample if c.islower()]) for sample in text]

    # punctuations count
    punc_count = [len([c for c in sample if c in string.punctuation]) for sample in text]

    # stopwords count
    stopwords_count = [len([word for word in sample.split() if word in __stopwords_list]) for sample in text]

    # nouns count
    nouns_count = [sum(1 for word, pos in pos_tag(word_tokenize(sample)) if pos.startswith('NN')) for sample in text]

    # verbs count
    verbs_count = [sum(1 for word, pos in pos_tag(word_tokenize(sample)) if pos.startswith('VB')) for sample in text]

    # pascal case string
    pascal_case_count = [sum(1 for word in sample.split() if word[0].isupper()) for sample in text]

    # all capitcal cases
    all_capital_case_count = [sum(1 for word in sample.split() if word.isupper()) for sample in text]

    # interruptions count
    interruptions_count = [len(re.findall('\,.*?\,', sample)) for sample in text]

    return {
        'text': text,
        'words_count': words_count,
        'chars_count': chars_count,
        'capital_chars_count': capital_chars_count,
        'lower_chars_count': lower_chars_count,
        'punc_count': punc_count,
        'stopwords_count': stopwords_count,
        'nouns_count': nouns_count,
        'verbs_count': verbs_count,
        'pascal_case_count': pascal_case_count,
        'all_capital_case_count': all_capital_case_count,
        'interruptions_count': interruptions_count
    }
