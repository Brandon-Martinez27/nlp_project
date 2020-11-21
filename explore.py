from wordcloud import WordCloud
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import nltk

def word_string(df):
    # create variables to hold words that appear in each type of repo as a single string
    js_words = ' '.join(df[df.language=='JavaScript'].clean)
    py_words = ' '.join(df[df.language=='Python'].clean)
    all_words = ' '.join(df.clean)

    js_words = re.sub(r'\s.\s', '', js_words)
    py_words = re.sub(r'\s.\s', '', py_words)
    all_words = re.sub(r'\s.\s', '', all_words)
    return js_words, py_words, all_words

def word_freq(js_words, py_words, all_words):
    # how frequently each word appears
    js_freq = pd.Series(js_words.split()).value_counts()
    py_freq = pd.Series(py_words.split()).value_counts()
    all_freq = pd.Series(all_words.split()).value_counts()
    return js_freq, py_freq, all_freq

def word_counts(js_freq, py_freq):
    # word frequency dataframe
    word_counts = (pd.concat([js_freq, py_freq], axis=1, sort=True)
                .set_axis(['js', 'py'], axis=1, inplace=False)
                .fillna(0)
                .apply(lambda s: s.astype(int))
                )
    # all counts of the word
    word_counts['all'] = word_counts['js'] + word_counts['py']
    # proportion of each string that is javascript
    word_counts['prop_js'] = word_counts['js']/word_counts['all']
    return word_counts

def word_cloud(js_words, py_words):
    js_cloud = WordCloud(background_color='lightgray', 
                      height=800, width=800).generate(js_words)

    py_cloud = WordCloud(background_color='lightgray', 
                        height=800, width=800).generate(py_words)

    plt.figure(figsize=(10,10))
    axs = [plt.axes([.25, 1, .5, .5]), plt.axes([.8, 1, .5, .5])]

    # imshow => display data as an image
    axs[0].imshow(js_cloud)
    axs[1].imshow(py_cloud)

    axs[0].set_title('JavaScript')
    axs[1].set_title('Python')

    for ax in axs: ax.axis('off')

def ngrams(js_words, py_words, n):
    js_ngrams = pd.Series(list(nltk.ngrams(js_words.split(), n))).value_counts()
    py_ngrams = pd.Series(list(nltk.ngrams(py_words.split(), n))).value_counts()
    return js_ngrams, py_ngrams

def plot_ngrams(js_bigrams, py_bigrams, js_trigrams, py_trigrams):
    plt.subplot(221)
    js_bigrams.head(10).plot.barh(color='red', width=.9, figsize=(10, 10), alpha=.8)
    plt.title('10 most frequently occurring JavaScript bigrams')
    plt.ylabel('Bigram')
    plt.xlabel('Frequency')

    plt.subplot(222)
    py_bigrams.head(10).plot.barh(color='green', width=.9, figsize=(10, 10), alpha=.3)
    plt.title('10 most frequently occurring Python bigrams')
    plt.ylabel('Bigram')
    plt.xlabel('Frequency')

    plt.subplot(223)
    js_trigrams.head(10).plot.barh(color='orange', width=.9, figsize=(10, 10), alpha=.3)
    plt.title('10 most frequently occurring JavaScript trigrams')
    plt.ylabel('Trigram')
    plt.xlabel('Frequency')

    plt.subplot(224)
    py_trigrams.head(10).plot.barh(color='navy', width=.9, figsize=(10, 10), alpha=.3)
    plt.title('10 most frequently occurring Python trigrams')
    plt.ylabel('Trigram')
    plt.xlabel('Frequency')
    plt.tight_layout()
    plt.show()