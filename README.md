# Web_scraping_classification_Indeed

Scrape, preprocess, gridsearch, votingclassifer, train model, predict.

indeed.com scraping full job description to use variouls classification models. Also provides prediction script to test job descriptions to predict job title

---- file desc ----
chromedriver: driver to interact with web through chromebrowser
fit_counter.joblib: fitting counter X train (job desc)
trained_model.joblib: VT trained model
test_set.csv: data to perform prediction (will show 100% accuracy because it is made from scraped data for code test) / changeable
new_test_set_prediciton: prediction outcome

---- script desc ----
## 01_Scraping

This script scrapes full job description and job title from indeed.com using selenium.
The steps of scraping is:
- open html of list of jobs in specific location
- iterate through job cards to get job url
- find desc element
- add it into a row of csv

## 02_Preprocessing

Preprocessing steps:
1. Merge job data collected from various locations
2. train test split (test = 0.2)
3. Vectorize job desc(X var) with count vectorizer
4. Vectorize job title(Y var) with int
5. Save vectors in 'filedir/data/vecdata'

## 03_Classification

1. Import stored vectors
2. find best params and score from gridsearchCV
3. feed best parameter into models
4. voting classifier to find best fit
5. export trained model joblib.dump
6. Get results (accuracy, cm, prediction csv), store in local dir

## 04_Prediction_with_new_data

1. import X_test (job desc), convert to df
2. vectorize by fitting into x_train fitting counter
3. predict by VT stored model
4. return vectorized results and store it as csv
