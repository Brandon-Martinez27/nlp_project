import pandas as pd
import numpy as np

import os
import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import env


# Acquire stage

def make_soup(url):
    '''
    This helper function takes in a url and requests and parses HTML
    returning a soup object.
    '''
    headers = {'User-Agent': 'Sir Galahad'} 
    response = get(url, headers=headers)    
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_language_urls():
    '''
    This function scrapes all of the Codeup blog urls from
    the main Codeup blog page and returns a list of urls.
    '''
    
    urls = []
    
    languages = ['JavaScript', 'Python']
    
    for language in languages:
        for i in range(1,40):
            # first page for most starred repos on GH
            url = f'https://github.com/search?l={language}&p={i}&q=stars%3A%3E0&s=stars&type=Repositories'

            urls.append(url)
    return urls


def get_single_language_urls(lang_choice):
    '''
    This function scrapes all of the Codeup blog urls from
    the main Codeup blog page and returns a list of urls.
    '''
    
    urls = []
    
    languages = [f'{lang_choice}']
    
    for language in languages:
        for i in range(1,40):
            # first page for most starred repos on GH
            url = f'https://github.com/search?l={language}&p={i}&q=stars%3A%3E0&s=stars&type=Repositories'

            urls.append(url)
    return urls


def get_all_urls(urls):
    '''
    This function scrapes all of the urls from
    the list of github search result urls and returns a list of urls.
    '''
    
    repo_urls = []
    n = 0
    for url in urls:
        # Make request and soup object using helper
        soup = make_soup(url)
        sleep(3)
        n = n + 1
        print(f"Scraping loop number {n}")
        # Create a list of the anchor elements that hold the urls.
        urls_list = soup.find_all('a', class_='v-align-middle')
    
        # I'm using a set comprehension to return only unique urls.
        urls_set = {'https://github.com' + link.get('href') for link in urls_list}
        urls_set = list(urls_set)
        repo_urls.extend(urls_set)

    # I'm converting my set to a list of urls.
    # urls = list(urls) 
        
    return repo_urls


# Make sure to import the .json then do the Prepare stage functions below:

# functions
def basic_clean(string):
    '''
    This function takes in a string and
    returns the string normalized.
    '''
    string = unicodedata.normalize('NFKC', string)\
             .encode('ascii', 'ignore')\
             .decode('utf-8', 'ignore')
    string = re.sub(r'[^\w\s]', '', string).lower()
    return string

##############################

def tokenize(string):
    '''
    This function takes in a string and
    returns a tokenized string.
    '''
    # Create tokenizer.
    tokenizer = nltk.tokenize.ToktokTokenizer()
    
    # Use tokenizer
    string = tokenizer.tokenize(string, return_str=True)
    
    return string

#############################

def stem(string):
    '''
    This function takes in a string and
    returns a string with words stemmed.
    '''
    # Create porter stemmer.
    ps = nltk.porter.PorterStemmer()
    
    # Use the stemmer to stem each word in the list of words we created by using split.
    stems = [ps.stem(word) for word in string.split()]
    
    # Join our lists of words into a string again and assign to a variable.
    string = ' '.join(stems)
    
    return string

#############################


def lemmatize(string):
    '''
    This function takes in string for and
    returns a string with words lemmatized.
    '''
    # Create the lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()
    
    # Use the lemmatizer on each word in the list of words we created by using split.
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    # Join our list of words into a string again and assign to a variable.
    string = ' '.join(lemmas)
    
    return string

#############################


def remove_stopwords(string, extra_words=[], exclude_words=[]):
    '''
    This function takes in a string, optional extra_words and exclude_words parameters
    with default empty lists and returns a string.
    '''
    # Create stopword_list.
    stopword_list = stopwords.words('english')
    
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    stopword_list = set(stopword_list) - set(exclude_words)

    # Add in 'extra_words' to stopword_list.
    stopword_list = stopword_list.union(set(extra_words))
    
    # Split words in string.
    words = string.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    
    # Join words in the list back into strings and assign to a variable.
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords

###############################


def prep_repo_data(df, column, extra_words=[], exclude_words=[]):
    '''
    This function take in a df and the string name for a text column with 
    option to pass lists for extra_words and exclude_words and
    returns a df with the text article title, original text, stemmed text,
    lemmatized text, cleaned, tokenized, & lemmatized text with stopwords removed.
    '''
    df['clean'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)\
                            .apply(lemmatize)
    
    df['stemmed'] = df[column].apply(basic_clean).apply(stem)
    
    df['lemmatized'] = df[column].apply(basic_clean).apply(lemmatize)
    
    return df[['language', column, 'stemmed', 'lemmatized', 'clean']]


print("Wrangle functions loaded successfully.")