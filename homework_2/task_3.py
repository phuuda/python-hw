import sys, re
sys.path.append('/users/Sofia/desktop/pattern-2.6') # machine-specific
from pattern.web import Wikipedia
from nltk import ngrams
from collections import Counter
from tabulate import tabulate

from task_1 import Wikiparser
from task_2 import TextStatistics

class Experiment:
    def __init__(self):
        pass
    
    def __phrase_print(self, term_list, freq_list):
        
        data = []
        for a, b in zip(term_list, freq_list):
            add = [' '.join(a), str(b)]
            data.append(add)
        print tabulate(data)
        
    def __word_print(self, term_list, freq_list):
        
        data = []
        for a, b in zip(term_list, freq_list):
            add = [''.join(a), str(b)]
            data.append(add)
        print tabulate(data)
    
    def show_results(self):
        
        a = WikiParser()
        nlp_corpus = a.get_articles('Natural_language_processing')
        nlp_text = [nlp_corpus[0]]

        b = TextStatistics(nlp_text)

        nlp_three_grams = b.get_top_3grams(5)
        print('top 5 NLP page 3-grams:\n')
        self.__phrase_print(nlp_three_grams[0], nlp_three_grams[1])

        nlp_top_words = b.get_top_words(5)
        print('\ntop 5 NLP page words:\n')
        self.__word_print(nlp_top_words[0], nlp_top_words[1])

        c = TextStatistics(nlp_corpus)    

        three_grams = c.get_top_3grams(20)
        print('\ntop 20 NLP Corpus 3-grams:\n')
        self.__phrase_print(three_grams[0], three_grams[1])

        top_words = c.get_top_words(20)
        print('\ntop 20 NLP Corpus words:\n')
        self.__word_print(top_words[0], top_words[1])


"""
top 5 NLP page 3-grams:

---------------------------  --
natural language processing  12
a chunk of                    6
chunk of text                 6
of natural language           5
systems based on              4
---------------------------  --

top 5 NLP page words:

--------  --
and       72
to        54
language  53
is        47
natural   33
--------  --

top 20 NLP Corpus 3-grams:

---------------------------  ---
from the original            306
archived from the            296
natural language processing  283
the original on              238
the use of                   234
as well as                   219
one of the                   195
a b c                        194
proceedings of the           191
cambridge university press   161
such as the                  153
the european union           150
the number of                146
university press isbn        142
a number of                  138
of the european              138
for example the              138
a set of                     132
based on the                 129
in order to                  120
---------------------------  ---

top 20 NLP Corpus words:

---------  -----
and        16145
to         11723
is          8643
that        4844
are         4318
or          3720
language    3677
be          3363
it          2649
this        2311
which       2177
can         1954
not         1914
was         1773
such        1735
retrieved   1710
have        1661
also        1660
words       1629
english     1625
---------  -----
"""
