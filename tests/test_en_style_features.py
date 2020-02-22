from textstyle.en_style_features import get_basic_style_features


def test_get_basic_style_features():
    text_corpus = [
        "I like to eat broccoli and bananas.",
        "I ate a banana and spinach smoothie for breakfast.",
        "Chinchillas and kittens are cute.",
        "My sister adopted a kitten yesterday.",
        "Look at this cute hamster munching on a piece of broccoli."
    ]
    words_count = [7, 9, 5, 6, 11]
    chars_count = [35, 50, 33, 37, 58]
    capital_chars_count = [1, 1, 1, 1, 1]
    lower_chars_count = [27, 40, 27, 30, 46]
    punc_count = [1, 1, 1, 1, 1]
    stopwords_count = [2, 3, 2, 1, 5]
    nouns_count = [2, 4, 2, 3, 5]
    verbs_count = [2, 1, 1, 1, 1]
    pascal_case_count = [1, 1, 1, 1, 1]
    all_capital_case_count = [1, 1, 0, 0, 0]
    inter_count = [0, 0, 0, 0, 0]

    results = get_basic_style_features(text_corpus)

    assert len(results) == 12
    assert results['words_count'] == words_count
    assert results['chars_count'] == chars_count
    assert results['capital_chars_count'] == capital_chars_count
    assert results['lower_chars_count'] == lower_chars_count
    assert results['punc_count'] == punc_count
    assert results['stopwords_count'] == stopwords_count
    assert results['nouns_count'] == nouns_count
    assert results['verbs_count'] == verbs_count
    assert results['pascal_case_count'] == pascal_case_count
    assert results['all_capital_case_count'] == all_capital_case_count
    assert results['interruptions_count'] == inter_count
