![Repo-Header](https://github.com/Darden-NLP-Project-Brandon-and-Luke/nlp_project/blob/main/nlp_project_banner.png?raw=true)
## About the Project
- For this project, you will be scraping data from GitHub repository README files. The goal will be to build a model that can predict what programming language a repository is, given the text of the README file.
- You will have to build a dataset yourself. Decide on a list of GitHub repositories to scrape, and write the python code necessary to extract the text of the README file for each page, and the primary language of the repository.
- Which repositories you use are up to you, but you should include at least 100 repositories in your data set.
- As an example of which repositories to use, here is a link to [GitHub's trending repositories](https://github.com/trending), the [most forked repositores](https://github.com/search?o=desc&q=stars:%3E1&s=forks&type=Repositories), and [the most starred repositories](https://github.com/search?q=stars%3A%3E0&s=stars&type=Repositories).
- Explore the data that you have scraped
- Transform your documents into a form that can be used in a machine learning model. You should use the programming language of the repository as the label to predict.
- Try fitting several different models and using several different representations of the text (e.g. a simple bag of words, then also the TF-IDF values for each).
- Build a function that will take in the text of a README file, and tries to predict the programming language.

### Goals
- Build a dataset of Github repositories' readme text
- Explore the text of the readme's and find connections to programming language
- Build a classification ML model that predicts the programming language used in a repo based on readme content. 

### Background
> "A readme file is a text file that is often included with software that contains general information or instructions about the software. The specific nature of this information varies significantly from file to file...There is no general formula for writing a readme, however, and in the end the content depends on the whims of the developer."

> "The content you are currently reading is what you will get for each repository you scrape.

> "This entire web page is the repository for this project"

### Deliverables
- A well-documented jupyter notebook that contains your analysis
- One or two google slides suitable for a general audience that summarize your findings. Include a well-labelled visualization in your slides.

### Acknowledgments
- [Codeup](https://codeup.com)'s Curriculum

- [GitHub](https://github.com/)

- [Canva](https://canva.com)

- [Readme Layout](https://github.com/ThompsonBethany01/Best-Practice/blob/main/README.md)

## Data Dictionary
| Feature Name    | Description                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| language        | The language of the repository. Scraped this data directly from each Github repository's home page.                                   |
| clean           | This is a string of characters (words) that have been cleaned through ACSII encoding, tokenizing, lemmatizing and removing stopwords. |
| words           | A list of cleaned words from the `clean` column.                                                                                      |
| doc_length      | Number of individual words in each document (row).                                                                                    |
| pred_bow        | Our Logistic Regression Model's prediction using Bag of Words as the feature generator.                                               |
| pred_tf         | Our Logistic Regression Model's prediction using TF-IDF as the feature generator.                                                     |
| pred_tfidf_tree | Our Decision Tree Model's prediction that used TF-IDF as the feature generator.                                                       |


## Initial Thoughts & Hypotheses
### Thoughts
> What's the proportion of each language in our data?

> What are the most common words in READMEs?

> Does the length of the README vary by programming language?

> What are the highest frequencies of word combinations? ie. ngrams

### Hypotheses
Is the average document length for **Python** READMEs longer or shorter than the overall average document length?

Two_tailed T-Test:
```
Null: The average `doc_length` of the python readmes are not statistically different from the overall population average `doc_length`
Alternative: The average `doc_length` of the python readmes **are** statistically different from the overall population average `doc_length`
```

Is the average document length for **JavaScript** READMEs longer or shorter than the overall average document length?

Two_tailed T-Test:
```
Null: The average `doc_length` of the JavaScript readmes are not statistically different from the overall population average `doc_length`
Alternative: The average `doc_length` of the JavaScript readmes **are** statistically different from the overall population average `doc_length`
```

## Project Steps
### Acquire
Data acquired using the BeautifulSoup library. Used helper functions to get requests to the first 30 search pages of most starred repos for Javascript and Python. Used helper function to parse HTML to find certain elements that contained the <i>programming language</i>, <i>repo-sub url</i>, and the <i>readme content</i> for each repo among said pages and saved to a DataFrame. Stored as a json file locally for reproduction.

### Prepare
Readme content is normalized, tokenized, stemmed, lemmatized, and stopwords are removed to produce "clean" content. Duplicate repos are removed and 2 columns are created The data is split into train, validate, and, test; stratifying on the programming language.

### Explore

<details>
  <summary> Summary </summary>
The distribution of JavaScript and Python data is nearly 1:1 Words counts with a distribution of between 40-60% are likely to be useless. Words on both ends of those tails will be more significant in classifying language in the modeling section. Word combinations may be more useful in classification since the combinations are more unique than individual words. 
</details>

<details>
  <summary> Hypothesis Testing </summary>

#### Hypothesis 1:
Two-Tailed T-Test: Is the average document length for Python READMEs longer or shorter than the overall average document length?

- $H_0$: The average `doc_length` of the python readmes are not statistically different from the overall population average `doc_length`
- $H_a$: The average `doc_length` of the python readmes **are** statistically different from the overall population average `doc_length`

<b>Result</b>: Null hypothesis was not rejected, meaning there is no statistically significant difference in the mean between the python average README doc lengths and the overall README average doc length.

-------

#### Hypothesis 2:
Two-Tailed T-Test: Is the average document length for JavaScript READMEs longer or shorter than the overall average document length?

- $H_0$: The average `doc_length` of the JavaScript readmes are not statistically different from the overall population average `doc_length`
- $H_a$: The average `doc_length` of the JavaScript readmes **are** statistically different from the overall population average `doc_length`

<b>Result</b>: Null hypothesis was not rejected, meaning there is no statistically significant difference in the mean between the JavaScript average README doc lengths and the overall README average doc length.

</details>

### Model
<details>
  <summary> Summary </summary>
  
- Baseline: It appears that JavaScript is the most often occuring result of the two languages represented, thus we will take as our baseline assuming that all README's are in JavaScript, which would mean our baseline model is accurately approximately 52% of the time.
- Feature Extraction: Using <b>Bag of Words</b> and <b>TF-IDF</b> to assign a numerical value to each word for modeling. Set X and y variables for computing. Used helper functions from <i>model.py</i> for cleaner documentation
- Models:
  - Logistic Regression Using Bag of Words
  - Logistic Regression Using TF-IDF
  - Decision Tree Using TF-IDF

</details>

<details>
  <summary> Evaluation </summary>
  
  Decision Tree model is most likely overfit, performed worse than others on validate. TF-IDF Logistic Regression Model performed best: <b>Model 2</b>. Moved forward with this model for testing on unseen data
</details>

### Conclusions
<details>
  <summary> Summary </summary>

- Repository languages classes:
    - JavaScript
    - Python

- We ran 3 different classification Models: 
    1. Logistic Regression Using Bag of Words
    2. Logistic Regression Using TF-IDF
    2. Decision Tree Using TF-IDF

- The results of the tests show that the model with the highest consistent accuracy is the **Logistic Regression model using TF-IDF** with an average of **90.5% accuracy** across all datasets.
    - We suspect that the high degree of accuracy is caused both by some overfitting (accounted for by adjusting the hyperparameters of the models) and only using binary classification. 
    - As shown in the exploration stage, we can see that there is enough distinctness in the words typically used in the Python and JavaScript repositories that allowed the models to determine the languages of the repository with relative ease. 
   
**Note**: *If additional languages had been added, i.e. adding Java or R into the mix, we expect that the overall accuracy and recall of the models would have gone down. We hypothesize this would've been due to the similarities of the purpose of those languages (not the syntax of those languages), thus the natural language surrounding those languages would have been harder for the model to decipher.*
</details>

<details>
  <summary> Next Steps </summary>

- As we continue to expand on the project, we would like to introduce additional languages into our repository scraping. That is the single biggest step we can make to improve the robustness of the model.

- We would have done more exploration related to which language introduced the most inaccuracy; i.e. was it more difficult for the model to decipher the Python repositories accurately, or was it the JavaScript repositories? This question would have extended to the additional languages under the expanded scraping mentioned above.
</details>

## How to Reproduce
### Steps
What should the user viewing this project do to recreate the project?  
1. Fork or clone this repository.
2. Copy and paste the contents of 
    - <kbd> nlp_final_notebook </kbd> for action steps
    - <kbd> wrangle_scratchpad </kbd> for acquiring and preparing multiple parts of repo data
    - <kbd> acquire.py </kbd> for helper functions
    - <kbd> prepare.py </kbd> for helper functions
    - <kbd> explore.py </kbd> for helper functions
    - <kbd> model.py </kbd> for helper functions

<details>
  <summary> An Easy Way to Download </summary>
  
  To save the file straight in your project directory, follow these steps:
  1. Click the file in this repository you want to copy and paste. It should open to the page as shown below.
  2. Right click <kbd>raw</kbd>.
  3. Click <kbd>save as</kbd>.    
  4. Click the folder you want to save the file in, such as your project directory.
  5. Rename the file as <kbd>file_name</kbd>.
  6. Make sure the file is saving as the proper file type file before clicking save.    
  7. You can now edit the file how you want within your project directory.
  
</details>

### Tools & Requirements
What tools did you use and what version were they?  
Python version 3.85 (all imports can be found in the import code block of each section)

## License
Anyone can use for reproduction and educational purposes.

## Creators
- Brandon Martinez
- Luke Becker
