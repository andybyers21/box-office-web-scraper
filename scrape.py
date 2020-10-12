import datetime
import os
import pandas as pd
import requests
import sys
from requests_html import HTML


BASE_DIR = os.path.dirname(__file__)

url = 'https://www.boxofficemojo.com/year/world/'


def url_to_txt(url):
    """ Get data from boxofficemojo.com using requests.

    Check for status code 200.
    Retrieve data for defined year.
    """
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        return html_text
    return None


def parse_and_extract(url, name='2020'):
    """ Parse data from url and extract relevant info.

    Loop through rows & cols to verify that r_table is a list.
    Parse HTML & CSS.
    Return raw data as CSV.
    """
    html_text = url_to_txt(url)

    if html_text == None:
        return False

    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table"
    r_table = r_html.find(table_class)
    table_data = []
    header_names = []

    if len(r_table) == 0:
        return False

    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]                # assume first row is header
    header_cols = header_row.find("th")
    header_names = [x.text for x in header_cols]

    for row in rows[1:]:
        cols = row.find("td")
        row_data = []
        for i, col in enumerate(cols):
            row_data.append(col.text)
        table_data.append(row_data)

    df = pd.DataFrame(table_data, columns=header_names)
    path = os.path.join(BASE_DIR, 'data')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(f'data/{name}_boxofficemojo_rankings.csv')
    df.to_csv(filepath, index=False)
    return True


def run(start_year=None, years_ago=1):
    """ Run the scraper.

    Assert start year & number of years ago
    scrape multiple iterations of... 
    """
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year

    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f"{start_year}") == 4

    for i in range(0, years_ago + 1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        finished = parse_and_extract(url, name=start_year)
        if finished:
            print(f"finished {start_year}")
        else:
            print(f"{start_year} does data not exist")
        start_year -= 1


if __name__ == "__main__":
    try:
        start = int(sys.argv[1])
    except:
        start = None
    try:
        count = int(sys.argv[2])
    except:
        count = 0
    run(start_year=start, years_ago=count)
