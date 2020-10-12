# A Python Box-Office Movie Takings Web Scraper

Scrape raw box-office data from [boxofficemojo.com](https://www.boxofficemojo.com/year/world/) and extract, transform and load in _Jupyter Notebooks_ using Requests-HTML and Pandas for CSV conversion.

## How to use:

Extract historical data from [boxofficemojo.com](https://www.boxofficemojo.com/year/world/) with `scrape.py`. Run `python -i scrape.py` followed by your arguments (no arguments will default to the current year only), e.g:

To scrape data from a specific year in the terminal:

```shell
python -i scrape.py <start_year>
```

e.g.

```shell
python -i scrape.py 2020
```

Or a specific number or years in the past

```shell
python -i scrape.py <start_year> <years_ago>
```

e.g.

```shell
python -i scrape.py 2019 10
```

Each iteration will produce a CSV file for a given year.

### Transform Data in Jupyter

1. Run notebook **1 - Load Data** .
2. Run notebook **2 - Combine Data** to combine data from each selected year into the cache.
3. Run notebook **3 - Transform Data** to output cleaned data to `CACHE_DIR, 'box-office-ranking-cleaned-dataset.csv'`.
