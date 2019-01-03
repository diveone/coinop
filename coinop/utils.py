import csv
import dateutil.parser as dateparser


def load_coins_from_csv(coin_name, file_path, factory=None):
    """Load file_path from csv and convert using factory

    :param file_path: string, csv path
    :param factory: fn, Factory for object to be created from csv
    """
    with open(file_path) as csv_file:
        coin_file = csv.DictReader(csv_file)
        for row in coin_file:
            if coin_file.line_num == 1:
                continue
            row['Date'] = dateparser.parse(row.get('Date'))
            factory(coin_name, row)


def format_str_int(s):
    if s == '-':
        return None
    else:
        update = s.replace(',', '')
        return int(update)
