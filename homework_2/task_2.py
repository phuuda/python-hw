from nltk import ngrams
from collections import Counter

class TextStatistics:
    def __init__(self, articles):        
        self.articles = articles
        pass

    def get_top_3grams(self, n):
        
        all_three_grams = []
        
        for article in self.articles:
            words = article.split(' ')
            for word in words:
                if word.isdigit():
                    words.remove(word)

            three_grams = ngrams(words, 3)
            for gram in three_grams:
                all_three_grams.append(gram)
                
        freq_list = Counter(tuple(i) for i in all_three_grams)
        freq_list = freq_list.most_common(n)

        list_of_3grams_in_descending_order_by_freq = []
        list_of_their_corresponding_freq = []
        
        for i in freq_list:
            list_of_3grams_in_descending_order_by_freq.append(i[0])
            list_of_their_corresponding_freq.append(i[1])
            
        return (list_of_3grams_in_descending_order_by_freq, list_of_their_corresponding_freq)

    def get_top_words(self, n):
        
        all_words = []

        bad_list = ['a', 'an', 'the', 'aboard', 'about', 'above', 'across', 'between',
                    'afore', 'after', 'against', 'along', 'amid', 'amidst', 'among',
                    'amongst', 'around', 'as', 'aside', 'aslant', 'astride', 'at',
                    'athwart', 'atop', 'before', 'behind', 'below', 'beneath', 'beside',
                    'besides', 'between', 'betwixt', 'beyond', 'by', 'circa', 'despite',
                    'down', 'except', 'for', 'from', 'in', 'inside', 'into', 'like', 'near',
                    'neath', 'next', 'of', 'off', 'on', 'opposite', 'out', 'outside', 'over',
                    'per', 'through', 'till'', toward', 'towards', 'under', 'underneath',
                    'unlike', 'until', 'up', 'with', 'without']
        
        for article in self.articles:
            words = article.split(' ')
            
            for word in words:
                if word.isdigit():
                    words.remove(word)
                        
            for word in words:
                all_words.append(word)
          
        for b in bad_list:
            while b in all_words:
                all_words.remove(b)
        
        word_count = Counter(all_words)
        word_count = word_count.most_common(n)

        list_of_words_in_descending_order_by_freq = []
        list_of_their_corresponding_freq = []
        
        for i in word_count:
            list_of_words_in_descending_order_by_freq.append(i[0])
            list_of_their_corresponding_freq.append(i[1])
        
        return (list_of_words_in_descending_order_by_freq, list_of_their_corresponding_freq)
