import fetcher
import html_editor
import mock_data_generator as mdg
import city_selector_model as csm
from os import startfile
import os.path
import sys

if __name__ == '__main__':
    print('Database exist:', os.path.exists('sample.db'))
    if not os.path.exists('sample.db'):
        print('Crawling started...')
        sys.path.append('.')
        fetcher.run_crawler()
        sys.path.remove('.')
        print('Database created!')
    city_dict = fetcher.fetch_api(True)
    cities_api = fetcher.fetch_database('sample.db')
    print('Database connected')
    trimmed_data, trimmed_cities = csm.trim_data(mdg.generate_mock_data(cities_api))
    labelled_data, model = csm.train_model(trimmed_data)
    print('Model has been trained')
    key = ''
    while key != 'q':
        print('Generating...')
        pass_name = mdg.generate_random_name()
        target_passenger = mdg.generate_mock_passenger(trimmed_cities, pass_name)
        cities = csm.get_cities(labelled_data, model, target_passenger, 5)
        flight_list = fetcher.fetch_flight(cities, city_dict, 'IST')
        html_editor.create_guide(cities, 'sample.db', pass_name, flight_list)
        startfile(f'site_template\\{pass_name}.html')
        key = input('Press any key to continue\nPress q to exit: ')
