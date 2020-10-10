Extract box office takings for a defined timeframe from [boxofficemojo.com](https://www.boxofficemojo.com/year/world/) to CSV.

Using Requests-HTML and Pandas for CSV conversion.

How to use:
run `python -i scrape.py` followed by your arguments (no arguments will default to the current year only), e.g:

To scrape data from a specific year:

```shell
python -i scrape.py <start_year>
```

e.g.

```shell
python -i scrape.py 2020
```

Or a specific number or years in the past

```shell
python -i scrape.py <start_year> <years to go back>
```

e.g.

```shell
python -i scrape.py 2019 10
```

Each iteration will produce a CSV file for each year.
