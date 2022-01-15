from scraper import Scraper

def main() -> None:
    headers = {'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/41.0.2228.0 Safari/537.36'}
    filter = {'area':'surrey-bc',
              'type':'house',
              'max_price':1750000,
              'min_year_built':1980}

    scraper = Scraper(headers=headers, filter=filter)
    data = scraper.get_content()
    print(data)

if __name__ == '__main__':
    main()
