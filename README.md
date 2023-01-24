# CSV Combiner
## Description
Command line program that takes several CSV files as arguments. Each CSV file (found in the fixtures directory of this repo) will have the same columns. Outputs a new CSV file to stdout that contains the rows from each of the inputs along with an additional column that has the filename from which the row came. Requires 2 or more input CSV files.

## Example
``python csvcombiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv``

Given two input files named `clothing.csv` and `accessories.csv`.

|email_hash|category|
|----------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|

|email_hash|category|
|----------|--------|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|

Output (combined.csv)

|email_hash|category|filename|
|----------|--------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|clothing.csv|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|clothing.csv|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|clothing.csv|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|accessories.csv|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|accessories.csv|

## Unit Testing
Included unit tests that check the functionality of the program
