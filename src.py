from scraper import Scrper

def main() -> None:
    headers = {'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/41.0.2228.0 Safari/537.36'}
    filter = {'area':'vancouver-bc',
              'type':'apartment-condo',
              'max_price':650000,
              'min_year_built':2015}

    scraper = Scrper(headers=headers, filter=filter)
    data = scraper.get_content()
    print(data)

if __name__ == '__main__':
    main()
