# WIP, NOTHING WORKS
import sys, re
sys.path.append('/users/Sofia/desktop/pattern-2.6') # specific for my machine, pattern sucks and only works in python2
from pattern.web import URL, plaintext

import requests
from bs4 import BeautifulSoup

class WikiParser:
    def __init__(self):
        pass

    def __get_text(self, link):
        
        s = URL(link).download()
        s = plaintext(s, keep={})
        
        while '\n' in s:
            s = s.replace('\n', ' ')
        while '  ' in s:
            s = s.replace('  ', ' ')
            
        s = re.sub(r'[^\w\s]','',s)
        return s
    
    def __get_links(self, s_link):
        
        all_links = set()
        req = requests.get(s_link)
        soup = BeautifulSoup(req.text, 'lxml')
        
        for a in soup.find_all('a', href=True):
         
            link = a['href']
            if link.startswith('/wiki/'):

                link = 'https://en.wikipedia.org' + link
                all_links.add(link)
                     
        return all_links
    
    def get_articles(self, start, depth = 1, max_count = 10):

        list_of_strings = set()
        start_link = 'https://en.wikipedia.org/wiki/' + start
        text = self.__get_text(start_link)
        all_links = self.__get_links(start_link)
        
        list_of_strings.add(text)
        
        d_count, m_count = 1, 1
        
        while d_count <= depth and m_count <= max_count:

            new_links = set()
            
            if all_links:
                for l in all_links:
                    text1 = self.__get_text(l)
                    list_of_strings.add(text1)
                    
                    m_count += 1
                
                    all_links1 = self.__get_links(l)
        
                    for j in all_links1:   
                        new_links.add(j)
                        m_count += 1
                                         
                d_count += 1
                all_links = new_links
                
            else:
                break
                
        for k in all_links:
            text2 = self.__get_text(k)
            list_of_strings.add(text1)
            
        return list_of_strings
