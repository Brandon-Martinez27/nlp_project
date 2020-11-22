<div style="position: relative; width: 100%; height: 0; padding-top: 38.0488%; padding-bottom: 48px; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden; border-radius: 8px; will-change: transform;">  <iframe style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"    src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAEOQcpqLGQ&#x2F;view?embed">  </iframe></div><a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAEOQcpqLGQ&#x2F;view?utm_content=DAEOQcpqLGQ&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener"></a>
# Natural Language Processing Project
## About the Project
### Goals
- Build a dataset of Github repositories' readme text
- Explore the text of the readme's and find connections to programming language
- Build a classification ML model that predicts the programming language used in a repo based on readme content. 

### Background

> "A readme file is a text file that is often included with software that contains general information or instructions about the software. The specific nature of 
> this information varies significantly from file to file...There is no general formula for writing a readme, however, and in the end the content depends on 
> the whims of the developer."

### Deliverables
The requirements for sharing your project. If possible, include links, such as the link to a presentation.

### Acknowledgments
Where you got the data, inspiration, etc. 
> My first inspiration for writing Readme files from Maggie Giust's Heart Failure repository [here](https://github.com/magsgiust/heart_failure).

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
First ideas about project while initially exploring the dataset.

### Hypotheses
A hypotheses that you test in your project. Feature x significantly increases with feature y.
```
Null hypothesis: Feature x does not correlate with feature y.
Alternative hypothesis: Feature x has a significant correlation with feature y.
```

A second hypotheses that you test in your project. Feature x significantly increases with feature y.
```
Null hypothesis: Feature x does not correlate with feature y.
Alternative hypothesis: Feature x has a significant correlation with feature y.
```

## Project Steps
### Acquire
Short description for each step of the process.
### Prepare
- Short
- Description
### Explore
Can use exandable text for large amounts of text.
<details>
  <summary> Click to Expand </summary>
  
  Text goes in here. Maybe an image.
  ### Headers Still Work
  If you add an empty line between the summary code and text.
</details>

### Model
- Short
  - Description
  
### Conclusions
Key insights from project.

## How to Reproduce
### Steps
What should the user viewing this project do to recreate the project?  
1. Fork or clone this repository.
2. Copy and paste the contents of 
    - <kbd> Copy_Pasta.md </kbd> for headers alone.
    - <kbd> README.md </kbd> for text with code used on different text, such as the expandable text.
3. View your final results.

<details>
  <summary> An Easy Way to Download </summary>
  
  To save the file straight in your project directory, follow these steps:
  1. Click the file in this repository you want to copy and paste. It should open to the page as shown below.
  2. Right click <kbd>raw</kbd>.
  3. Click <kbd>save as</kbd>.  
  
  ![1-3-steps](https://i.pinimg.com/originals/25/d3/7b/25d37bd84dd8508544b5f8fca9c442a4.png)  
  
  4. Click the folder you want to save the file in, such as your project directory.
  5. Rename the file as <kbd>README.md</kbd>.
  6. Make sure the file is saving as a markdown file before clicking save.  
  
  ![4-6-steps](https://i.pinimg.com/originals/14/b7/88/14b788b50562ea1fadac74cbd4963217.png)  
  
  7. You can now edit the file how you want within your project directory.
  
</details>

### Tools & Requirements
What tools did you use and what version were they?  
Python version 3.85

## License
Your permissions for users when reproducing your project.

## Creators
The names of all contributors for the project with contact information.
