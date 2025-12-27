# Automobile Dataset

## Source

- [Let us do Data Analysis with Python](https://medium.com/@sriramselvank/let-us-do-data-analysis-with-python-db2cb6eca43f)
- [Automobile](https://archive.ics.uci.edu/dataset/10/automobile)


## Dataset Information

### Additional Information

This data set consists of three types of entities: (a) the specification of an auto in terms of various characteristics, 
(b) its assigned insurance risk rating, (c) its normalized losses in use as compared to other cars.  The second rating 
corresponds to the degree to which the auto is more risky than its price indicates. Cars are initially assigned a risk 
factor symbol associated with its price.   Then, if it is more risky (or less), this symbol is adjusted by moving it up 
(or down) the scale.  Actuarians call this process "symboling".  A value of +3 indicates that the auto is risky, -3 that 
it is probably pretty safe.

The third factor is the relative average loss payment per insured vehicle year.  This value is normalized for all autos 
within a particular size classification (two-door small, station wagons, sports/speciality, etc...), and represents the 
average loss per car per year.

Note: Several of the attributes in the database could be used as a "class" attribute.

### Variables Table

| #  | Attribute         | Type        | Range / Categories                                                                                                                                                                             |
|----|-------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | symboling         | Categorical | -3, -2, -1, 0, 1, 2, 3                                                                                                                                                                         |
| 2  | normalized-losses | Continuous  | 65 – 256                                                                                                                                                                                       |
| 3  | make              | Categorical | alfa-romero, audi, bmw, chevrolet, dodge, honda, isuzu, jaguar, mazda, mercedes-benz, mercury, mitsubishi, nissan, peugot, plymouth, porsche, renault, saab, subaru, toyota, volkswagen, volvo |
| 4  | fuel-type         | Categorical | diesel, gas                                                                                                                                                                                    |
| 5  | aspiration        | Categorical | std, turbo                                                                                                                                                                                     |
| 6  | num-of-doors      | Categorical | four, two                                                                                                                                                                                      |
| 7  | body-style        | Categorical | hardtop, wagon, sedan, hatchback, convertible                                                                                                                                                  |
| 8  | drive-wheels      | Categorical | 4wd, fwd, rwd                                                                                                                                                                                  |
| 9  | engine-location   | Categorical | front, rear                                                                                                                                                                                    |
| 10 | wheel-base        | Continuous  | 86.6 – 120.9                                                                                                                                                                                   |
| 11 | length            | Continuous  | 141.1 – 208.1                                                                                                                                                                                  |
| 12 | width             | Continuous  | 60.3 – 72.3                                                                                                                                                                                    |
| 13 | height            | Continuous  | 47.8 – 59.8                                                                                                                                                                                    |
| 14 | curb-weight       | Continuous  | 1488 – 4066                                                                                                                                                                                    |
| 15 | engine-type       | Categorical | dohc, dohcv, l, ohc, ohcf, ohcv, rotor                                                                                                                                                         |
| 16 | num-of-cylinders  | Categorical | eight, five, four, six, three, twelve, two                                                                                                                                                     |
| 17 | engine-size       | Continuous  | 61 – 326                                                                                                                                                                                       |
| 18 | fuel-system       | Categorical | 1bbl, 2bbl, 4bbl, idi, mfi, mpfi, spdi, spfi                                                                                                                                                   |
| 19 | bore              | Continuous  | 2.54 – 3.94                                                                                                                                                                                    |
| 20 | stroke            | Continuous  | 2.07 – 4.17                                                                                                                                                                                    |
| 21 | compression-ratio | Continuous  | 7 – 23                                                                                                                                                                                         |
| 22 | horsepower        | Continuous  | 48 – 288                                                                                                                                                                                       |
| 23 | peak-rpm          | Continuous  | 4150 – 6600                                                                                                                                                                                    |
| 24 | city-mpg          | Continuous  | 13 – 49                                                                                                                                                                                        |
| 25 | highway-mpg       | Continuous  | 16 – 54                                                                                                                                                                                        |
| 26 | price             | Continuous  | 5118 – 45400                                                                                                                                                                                   |


