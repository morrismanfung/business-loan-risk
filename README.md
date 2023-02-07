# Business Loan Risk Predictor

Author: Morris M. F. Chan

Inspired by the journal article [“Should This Loan be Approved or Denied?”: A Large Dataset with Class Assignment Guidelines](https://www.tandfonline.com/doi/full/10.1080/10691898.2018.1434342), this project aims to study factors affecting risks of loans being charged-off. We are currently using machine learning algorithms to study the associations of interest. We are currently using a public data set by U.S. Small Business Administration. The data set can be found [here](https://data.sba.gov/en/dataset/7-a-504-foia).

## Methodology

### Feature Selection

Exploratory data analysis (EDA) is done by visually inspecting the associations between each variable and the status loans. The full EDA report can be found [here](https://github.com/morrismanfung/business-loan-risk/blob/main/docs/01-eda.ipynb). By visualizing the distribution of each variables in the data set, the variables below are selected for machine learning:

- `LoanStatus` (as the target variable)
- `BorrState`
- `DeliveryMethod`
- `NaicsCode` (with NAICS sectors extracted)
- `FranchiseCode` (as a binary variable of whether the loan is associated with a franchise)
- `BusinessAge`
- `ThirdPartyDollar`
- `TermInMonths`
- `JobsSupported`

### Machine Learning Algorithm

Given the large proportion of categorical features and the large number of dummy variables created by one-hot encoding, distance-based method (e.g., K nearest neighbor) is not used.

Potentially useful algorithms include a support vector claissifier (SVC), a random forest claissifier (RFC), a Gaussian naive Bayes classifier, a logistic regression classifier, and a linear support vector classifer (LinearSVC).

### Data Splitting

Stratified splitting was done with a test size of 50%. All observations are randomly mixed ignoring when the loans are applied. It ignores situational factors associated with the global economic situations.

### Preliminary Statistical Inference

Before spending more effort on modelling, we decided to use basic logistic regression to identify potentially useful features in the data set. Unfortunately, all features are not statistically significantly associated with the risk of the loan being charged-off. Given the small standard scores and the large sample size, it is believed that all features are not potentially associated with the likelihood of interest. It is concluded that the given features in the data set are not sufficient to predict the likelihood of a small business loan being charged-off. The project is, thus, closed.

### Potential Future Work

The conclusion made currently is based on traditional null hypothesis significance testing. However, statistically speaking, large p-values and small standard scores are not statistically evident to the claim that all features are not associated with the risk of interst. Thus, it is suggested that a Bayesian approach can be adopted to further confirm the conclusion of this project.
