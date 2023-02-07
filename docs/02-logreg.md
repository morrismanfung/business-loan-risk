Statistical Inference: Logistic Regression
================
Morris M. F. Chan

-   <a href="#statistical-inference-logistic-regression"
    id="toc-statistical-inference-logistic-regression">Statistical
    Inference: Logistic Regression</a>

# Statistical Inference: Logistic Regression

Logistic regression is first performed on the selected variables from
the data set to provide insight for possible machine learning algorithms
(if any).

``` r
library( tidyverse)
```

    ## ── Attaching packages ─────────────────────────────────────── tidyverse 1.3.2 ──
    ## ✔ ggplot2 3.4.0     ✔ purrr   1.0.1
    ## ✔ tibble  3.1.8     ✔ dplyr   1.1.0
    ## ✔ tidyr   1.3.0     ✔ stringr 1.5.0
    ## ✔ readr   2.1.3     ✔ forcats 1.0.0
    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## ✖ dplyr::filter() masks stats::filter()
    ## ✖ dplyr::lag()    masks stats::lag()

``` r
df <- read_csv( '../data/train_processed.csv')
```

    ## New names:
    ## Rows: 13744 Columns: 24
    ## ── Column specification
    ## ──────────────────────────────────────────────────────── Delimiter: "," chr
    ## (13): BorrCity, BorrState, CDC_State, ThirdPartyLender_State, DeliveryMe... dbl
    ## (9): ...1, Unnamed: 0, ApprovalFiscalYear, NaicsCode, ThirdPartyDollars... lgl
    ## (2): Franchise, ChargedOff
    ## ℹ Use `spec()` to retrieve the full column specification for this data. ℹ
    ## Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## • `` -> `...1`

``` r
model <- glm( as.factor( ChargedOff) ~ BorrState + DeliveryMethod + NasicsSector + Franchise + BusinessAge + ThirdPartyDollars + TermInMonths + JobsSupported, data = df, family = 'binomial')

summary( model)
```

    ## 
    ## Call:
    ## glm(formula = as.factor(ChargedOff) ~ BorrState + DeliveryMethod + 
    ##     NasicsSector + Franchise + BusinessAge + ThirdPartyDollars + 
    ##     TermInMonths + JobsSupported, family = "binomial", data = df)
    ## 
    ## Deviance Residuals: 
    ##    Min      1Q  Median      3Q     Max  
    ## -1.284   0.000   0.000   0.000   2.724  
    ## 
    ## Coefficients:
    ##                                                     Estimate Std. Error z value
    ## (Intercept)                                       -6.350e+01  1.224e+05  -0.001
    ## BorrStateAL                                        2.140e+01  6.516e+04   0.000
    ## BorrStateAZ                                       -2.336e+01  2.650e+04  -0.001
    ## BorrStateCA                                       -4.109e+00  2.735e+00  -1.502
    ## BorrStateCO                                       -2.469e+01  2.864e+04  -0.001
    ## BorrStateCT                                       -2.511e+01  8.259e+04   0.000
    ## BorrStateFL                                       -2.931e+00  2.537e+00  -1.156
    ## BorrStateGA                                       -2.353e+01  2.999e+04  -0.001
    ## BorrStateHI                                        5.110e+01  1.420e+05   0.000
    ## BorrStateIA                                       -2.240e+01  5.731e+04   0.000
    ## BorrStateID                                       -2.680e+01  4.293e+04  -0.001
    ## BorrStateIL                                       -2.508e+01  3.041e+04  -0.001
    ## BorrStateIN                                       -2.233e+01  4.760e+04   0.000
    ## BorrStateKS                                       -1.945e+01  5.725e+04   0.000
    ## BorrStateKY                                       -2.900e+00  8.064e+04   0.000
    ## BorrStateLA                                       -2.565e+01  1.059e+05   0.000
    ## BorrStateMA                                       -2.331e+01  2.774e+04  -0.001
    ## BorrStateMD                                       -1.893e+00  1.318e+05   0.000
    ## BorrStateME                                       -8.824e+00  7.120e+04   0.000
    ## BorrStateMI                                       -2.231e+01  3.492e+04  -0.001
    ## BorrStateMN                                       -2.239e+01  2.395e+04  -0.001
    ## BorrStateMO                                       -2.202e+01  4.611e+04   0.000
    ## BorrStateMS                                       -2.754e+00  2.168e+05   0.000
    ## BorrStateMT                                       -2.372e+01  1.264e+05   0.000
    ## BorrStateNC                                       -2.862e+01  5.048e+04  -0.001
    ## BorrStateND                                       -2.285e+01  7.149e+04   0.000
    ## BorrStateNE                                        1.487e+01  8.335e+04   0.000
    ## BorrStateNH                                       -2.442e+01  5.669e+04   0.000
    ## BorrStateNJ                                       -2.052e+01  4.759e+04   0.000
    ## BorrStateNM                                       -2.477e+01  5.998e+04   0.000
    ## BorrStateNV                                       -2.426e+01  3.687e+04  -0.001
    ## BorrStateNY                                       -1.061e+00  2.388e+00  -0.444
    ## BorrStateOH                                       -2.259e+01  3.935e+04  -0.001
    ## BorrStateOK                                        9.308e+00  6.348e+04   0.000
    ## BorrStateOR                                       -2.381e+01  5.759e+04   0.000
    ## BorrStatePA                                       -3.083e+00  6.728e+04   0.000
    ## BorrStatePR                                       -1.433e+00  1.416e+05   0.000
    ## BorrStateRI                                        1.775e+01  6.010e+03   0.003
    ## BorrStateSC                                       -4.282e+00  4.594e+04   0.000
    ## BorrStateSD                                       -9.898e-01  2.889e+00  -0.343
    ## BorrStateTN                                       -1.785e+00  6.752e+04   0.000
    ## BorrStateTX                                        6.299e-01  2.742e+00   0.230
    ## BorrStateUT                                       -2.455e+01  2.520e+04  -0.001
    ## BorrStateVA                                       -2.089e+01  4.221e+04   0.000
    ## BorrStateWA                                       -2.249e+01  4.062e+04  -0.001
    ## BorrStateWI                                       -2.575e+01  3.635e+04  -0.001
    ## DeliveryMethod504 Refinance                        1.289e+01  2.562e+04   0.001
    ## DeliveryMethodALP                                  3.635e+01  9.637e+03   0.004
    ## DeliveryMethodPCLP                                 2.233e+01  4.226e+04   0.001
    ## NasicsSector21                                     2.245e+01  1.518e+05   0.000
    ## NasicsSector22                                     4.072e+01  1.470e+05   0.000
    ## NasicsSector23                                     1.628e+00  1.053e+05   0.000
    ## NasicsSector31                                     5.816e+00  1.110e+05   0.000
    ## NasicsSector32                                     3.525e+00  1.092e+05   0.000
    ## NasicsSector33                                     2.433e+01  1.037e+05   0.000
    ## NasicsSector42                                     2.532e+00  1.061e+05   0.000
    ## NasicsSector44                                     2.773e+00  1.058e+05   0.000
    ## NasicsSector45                                    -1.543e+01  1.069e+05   0.000
    ## NasicsSector48                                     4.454e+00  1.084e+05   0.000
    ## NasicsSector49                                     4.229e+00  1.158e+05   0.000
    ## NasicsSector51                                     1.944e+00  1.172e+05   0.000
    ## NasicsSector52                                     3.022e+00  1.100e+05   0.000
    ## NasicsSector53                                     4.779e-01  1.060e+05   0.000
    ## NasicsSector54                                    -1.581e+01  1.051e+05   0.000
    ## NasicsSector55                                     2.939e+01  2.504e+05   0.000
    ## NasicsSector56                                     2.119e+01  1.037e+05   0.000
    ## NasicsSector61                                     8.339e+00  1.233e+05   0.000
    ## NasicsSector62                                     2.236e+01  1.037e+05   0.000
    ## NasicsSector71                                     2.655e+01  1.037e+05   0.000
    ## NasicsSector72                                     8.126e+00  1.039e+05   0.000
    ## NasicsSector81                                     2.285e+01  1.037e+05   0.000
    ## FranchiseTRUE                                     -1.571e+01  1.550e+04  -0.001
    ## BusinessAgeExisting or more than 2 years old       5.792e-01  6.435e+04   0.000
    ## BusinessAgeExisting, 5 or more years              -2.060e+01  6.602e+04   0.000
    ## BusinessAgeLess than 3 years old but at least 2   -1.799e+01  9.145e+04   0.000
    ## BusinessAgeLess than 4 years old but at least 3   -1.824e+01  9.742e+04   0.000
    ## BusinessAgeLess than 5 years old but at least 4   -8.851e+00  1.012e+05   0.000
    ## BusinessAgeNew Business or 2 years or less         2.538e+01  1.097e+05   0.000
    ## BusinessAgeNew, Less than 1 Year old               4.621e+00  6.435e+04   0.000
    ## BusinessAgeStartup, Loan Funds will Open Business -2.275e+01  6.585e+04   0.000
    ## BusinessAgeUnanswered                              1.941e+00  6.435e+04   0.000
    ## ThirdPartyDollars                                 -8.876e-07  1.782e-06  -0.498
    ## TermInMonths                                       1.514e-02  2.069e-02   0.732
    ## JobsSupported                                     -9.844e-02  2.163e-01  -0.455
    ##                                                   Pr(>|z|)
    ## (Intercept)                                          1.000
    ## BorrStateAL                                          1.000
    ## BorrStateAZ                                          0.999
    ## BorrStateCA                                          0.133
    ## BorrStateCO                                          0.999
    ## BorrStateCT                                          1.000
    ## BorrStateFL                                          0.248
    ## BorrStateGA                                          0.999
    ## BorrStateHI                                          1.000
    ## BorrStateIA                                          1.000
    ## BorrStateID                                          1.000
    ## BorrStateIL                                          0.999
    ## BorrStateIN                                          1.000
    ## BorrStateKS                                          1.000
    ## BorrStateKY                                          1.000
    ## BorrStateLA                                          1.000
    ## BorrStateMA                                          0.999
    ## BorrStateMD                                          1.000
    ## BorrStateME                                          1.000
    ## BorrStateMI                                          0.999
    ## BorrStateMN                                          0.999
    ## BorrStateMO                                          1.000
    ## BorrStateMS                                          1.000
    ## BorrStateMT                                          1.000
    ## BorrStateNC                                          1.000
    ## BorrStateND                                          1.000
    ## BorrStateNE                                          1.000
    ## BorrStateNH                                          1.000
    ## BorrStateNJ                                          1.000
    ## BorrStateNM                                          1.000
    ## BorrStateNV                                          0.999
    ## BorrStateNY                                          0.657
    ## BorrStateOH                                          1.000
    ## BorrStateOK                                          1.000
    ## BorrStateOR                                          1.000
    ## BorrStatePA                                          1.000
    ## BorrStatePR                                          1.000
    ## BorrStateRI                                          0.998
    ## BorrStateSC                                          1.000
    ## BorrStateSD                                          0.732
    ## BorrStateTN                                          1.000
    ## BorrStateTX                                          0.818
    ## BorrStateUT                                          0.999
    ## BorrStateVA                                          1.000
    ## BorrStateWA                                          1.000
    ## BorrStateWI                                          0.999
    ## DeliveryMethod504 Refinance                          1.000
    ## DeliveryMethodALP                                    0.997
    ## DeliveryMethodPCLP                                   1.000
    ## NasicsSector21                                       1.000
    ## NasicsSector22                                       1.000
    ## NasicsSector23                                       1.000
    ## NasicsSector31                                       1.000
    ## NasicsSector32                                       1.000
    ## NasicsSector33                                       1.000
    ## NasicsSector42                                       1.000
    ## NasicsSector44                                       1.000
    ## NasicsSector45                                       1.000
    ## NasicsSector48                                       1.000
    ## NasicsSector49                                       1.000
    ## NasicsSector51                                       1.000
    ## NasicsSector52                                       1.000
    ## NasicsSector53                                       1.000
    ## NasicsSector54                                       1.000
    ## NasicsSector55                                       1.000
    ## NasicsSector56                                       1.000
    ## NasicsSector61                                       1.000
    ## NasicsSector62                                       1.000
    ## NasicsSector71                                       1.000
    ## NasicsSector72                                       1.000
    ## NasicsSector81                                       1.000
    ## FranchiseTRUE                                        0.999
    ## BusinessAgeExisting or more than 2 years old         1.000
    ## BusinessAgeExisting, 5 or more years                 1.000
    ## BusinessAgeLess than 3 years old but at least 2      1.000
    ## BusinessAgeLess than 4 years old but at least 3      1.000
    ## BusinessAgeLess than 5 years old but at least 4      1.000
    ## BusinessAgeNew Business or 2 years or less           1.000
    ## BusinessAgeNew, Less than 1 Year old                 1.000
    ## BusinessAgeStartup, Loan Funds will Open Business    1.000
    ## BusinessAgeUnanswered                                1.000
    ## ThirdPartyDollars                                    0.618
    ## TermInMonths                                         0.464
    ## JobsSupported                                        0.649
    ## 
    ## (Dispersion parameter for binomial family taken to be 1)
    ## 
    ##     Null deviance: 82.577  on 941  degrees of freedom
    ## Residual deviance: 27.582  on 858  degrees of freedom
    ##   (12802 observations deleted due to missingness)
    ## AIC: 195.58
    ## 
    ## Number of Fisher Scoring iterations: 24

It can be seen that none of the coefficients are statistically
significant with the likelihood of a loan being charged-off. Given the
large sample size, small standard scores suggest there are only
neglectable associations between the selected features and the risk of a
loan being charged-off. Unfortunately, it is deemed meaningless to
continue the project using more advanced models or algorithms. A close
inspection on the original
[article](https://www.tandfonline.com/doi/full/10.1080/10691898.2018.1434342)
will reveal that the high accuracy observed in the suggested workflow is
only significant because of variables manually added by the authors for
the sake of the project as a school assignment.
