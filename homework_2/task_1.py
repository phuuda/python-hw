import sys, re
sys.path.append('/users/Sofia/desktop/pattern-2.6') # specific for my machine
from pattern.web import Wikipedia

class WikiParser:
    def __init__(self):
        pass
    
    def __get_text(self, search_term):
        
        article = Wikipedia().search(search_term)
        if article:
            s = article.string        
            if s:
                while '\n' in s:
                    s = s.replace('\n', ' ')
                while '  ' in s:
                    s = s.replace('  ', ' ')

                s = re.sub(r'[^\w\s]','',s)
                s = s.lower()
                return s
    
            else:
                return None

        else:
            return None
    
    def get_articles(self, search_term):
        text_list = []
        
        article = Wikipedia().search(search_term)
        links = article.links
        
        s = self.__get_text(search_term)
        text_list.append(s)
        
        for link in links:
            text_list.append(self.__get_text(link))
            print(link)

        return text_list
