from string import ascii_lowercase

import numpy as np
from sklearn.feature_extraction import stop_words

def generate_dict(dict_len, min_word_len, max_word_len):
    dictionary=[]
    for _ in range(dict_len):
        word_len=np.random.randint(min_word_len, max_word_len)
        random_letters=np.random.choice(list(ascii_lowercase), word_len)
        random_word=''.join(random_letters)
        dictionary.append(random_word)
    return dictionary

def generate_text(text_len, dictionary):
    text=np.random.choice(dictionary, text_len)
    text=' '.join(text)
    return text

def generate_corpus(corpus_len, min_text_len, max_text_len, **kwargs):
    '''
    **kwargs:
    generate_dict kwargs
    '''
    dictionary=generate_dict(kwargs['dict_len'], kwargs['min_word_len'], kwargs['max_word_len'])
    dictionary+=list(stop_words.ENGLISH_STOP_WORDS)
    corpus=[]
    
    for _ in range(corpus_len):
        text_len=np.random.randint(min_text_len, max_text_len)
        text=generate_text(text_len, dictionary)
        corpus.append(text)
        
    return corpus