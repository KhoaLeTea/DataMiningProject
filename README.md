# Yelp Me Yelp You
Using the Yelp dataset provided by the [Yelp Dataset Challenge](https://www.yelp.com/dataset_challenge),
we analyze the sentiment and related statistics of user reviews. We look at how the sentiment rating of a user's review is correlated to the business. Specifically, we looked for relationships between the attributes associated with each business (does it have free wifi? a parking garage?) and reviews given by over 1 million users in 11 cities worldwide.

### Team Members
* Michael Barlow
* Madeleine Crouch 
* Khoa Le
* Dalton Morrow

## Prerequisites:
Python 2.7 with Pandas, [Plotly](https://plot.ly/python/), [NLTK](http://www.nltk.org/install.html) with vader_lexicon and stopwords. To install NLTK corpora and models from the terminal, type

```
python
import nltk
nltk.download()
```

then choose the necessary materials from the GUI.

[RapidMiner](https://rapidminer.com/) (requires educational license to use full featureset); [Jupyter](http://jupyter.org/) or [Anaconda](https://www.continuum.io/downloads) or your preferred method of running .ipynb files also required for running all analyses and files.

## Questions
* What are the most common issues in a poorly-reviewed business?
  * No universal problems were identified in the review text of reviews with low star ratings, but the 'issue distribution' of each business can be analyzed over time within the categories of problems about service, food, price, or other. This distribution was obtained by counting keywords relating to trauma within each review. 
* Are certain business attributes indicative of the performance of a business?
  * Whether the business is open or permanently closed was one of the best indications of business category. Latitude and longitude were also important, but less so than whether the business was open at the time the review was written. This analysis was performed with a decision tree.
* What changes can a business make to improve their reviews?
  * By using the results from the first two questions, a fledgling business can make important decisions relating to prospective location, service and waitstaff, or even products and services offered. This analysis is most pertinent for restaurants and related businesses, since these types of establishments made up the bulk of our data.
  
### Applications

[Video Demonstration Link](http://www.screencast.com/t/35vgNv7uF)

[Final Paper Link](https://github.com/Amerterasu/DataMiningProject/blob/master/10_YelpMeYelpYou_Part4.pdf)
