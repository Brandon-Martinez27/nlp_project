import numpy as np
import pandas as pd

from requests import get
from bs4 import BeautifulSoup
from time import sleep
import os

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
    This function scrapes the GH search results for most starred 
    pages from each of 4 languages for the first 10 pages of each 
    and returns a list of urls.
    '''
    # create empty list to hold urls
    urls = []
    # create list of languages to search for
    languages = ['JavaScript', 'Python']
    # loop through the languages
    for language in languages:
        # loop throught the page numbers
        for i in range(1,16):
            # each page for most starred repos on GH
            url = f'https://github.com/search?l={language}&p={i}&q=stars%3A%3E0&s=stars&type=Repositories'
            # append the url to the urls list
            urls.append(url)
    return urls

def get_all_urls(urls):
    '''
    This function scrapes all of the urls from
    the GH search results pages and returns a complete list of urls.
    '''
    # create empty list
    repo_urls = []
    n=0
    # loop through each url in urls list
    for url in urls:
        # Make request and soup object using helper function
        soup = make_soup(url)
        # delay 1 second between fetch
        sleep(8)
        n = n + 1
        print(f"Scraping loop number {n}")
        # Create a list of the anchor elements that hold the urls.
        urls_list = soup.find_all('a', class_='v-align-middle')
        # I'm using a set comprehension to return only unique urls.
        urls_set = {'https://github.com' + link.get('href') for link in urls_list}
        # I'm converting my set to a list of urls.
        urls_set = list(urls_set)
        # extend the list with a new url as an element
        repo_urls.extend(urls_set)        
    return repo_urls

def get_repo_content(urls, cached=False):
    '''
    This function takes in a list of Github urls and a parameter
    with default cached == False which scrapes the language and  
    readme text for each url, creates a list of dictionaries with 
    the title and text for each blog, converts list to df, and returns 
    df. If cached == True, the function returns a df from a json file.
    '''
    if cached == True:
        df = pd.read_json('github_repos.json')
        
    # cached == False completes a fresh scrape for df     
    else:

        # Create an empty list to hold dictionaries
        articles = []
        n=0
        # Loop through each url in our list of urls
        for url in urls:

            # Make request and soup object using helper
            soup = make_soup(url)
            sleep(8)
            n = n + 1
            print(f"Scraping loop number {n}")
            # Save the programming language of each repo in variable language
            language = soup.find('span', class_='text-gray-dark text-bold mr-1').text

            # Save the text in each repo to variable content
            content = soup.find('article', class_="markdown-body entry-content container-lg").text

            # Create a dictionary holding the title and content for each blog
            article = {'language': language, 'content': content}

            # Add each dictionary to the articles list of dictionaries
            articles.append(article)
            
        # convert our list of dictionaries to a df
        df = pd.DataFrame(articles)

        # Write df to a json file for faster access
        df.to_json('github_repos.json')
    
    return df



##### This is the key function that returns 6 dataframes #####
def train_validate_test(df):
    '''
    this function takes in a dataframe and splits it into 3 samples, 
    a test, which is 20% of the entire dataframe, 
    a validate, which is 24% of the entire dataframe,
    and a train, which is 56% of the entire dataframe. 
    It then splits each of the 3 samples into a dataframe with independent variables
    and a series with the dependent, or target variable. 
    The function returns 3 dataframes and 3 series:
    X_train (df) & y_train (series), X_validate & y_validate, X_test & y_test. 
    '''
    # split df into test (20%) and train_validate (80%)
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)

    # split train_validate off into train (70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

        
    # split train into X (dataframe, drop target) & y (series, keep target only)
    X_train = train.drop(columns= ['target_var'])
    X_validate = validate.drop(columns= ['target_var'])
    X_test = test.drop(columns= ['target_var'])

    y_train = train[['target_var']]
    y_validate = validate[['target_var']]
    y_test = test[['target_var']]

    train_explore = train.copy()
    df_explore = df.copy()

    return X_train, y_train, X_validate, y_validate, X_test, y_test, train_explore, df_explore

print("Wrangle functions loaded successfully.")