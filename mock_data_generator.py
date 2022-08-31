import string
import numpy as np
import pandas as pd
from scipy.stats import geom, planck

pass_num = 8000
np.random.seed(42)


def generate_mock_data(cities_api):
    """Generates random passenger data"""
    passengers_dict = {}
    for i in range(len(cities_api)):
        if i % 3 == 0:
            city_count = abs(geom.rvs(0.5, size=pass_num))
        elif i % 3 == 1:
            city_count = abs(planck.rvs(0.5, size=pass_num))
        else:
            city_count = abs(geom.rvs(1/(1+i), size=pass_num))//10

        passengers_dict['{}'.format(cities_api[i])] = city_count
        if i == 0:
            continue
        for j in range(pass_num//10):
            first = np.random.randint(0, len(passengers_dict))
            sec = np.random.randint(0, pass_num)
            passengers_dict[cities_api[first]][sec//2:sec] = 0
    passengers = pd.DataFrame(passengers_dict)
    return passengers


def generate_random_name():
    start = np.random.randint(0, 4)
    fin = np.random.randint(5, 9)
    name = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [*string.ascii_lowercase]
    for vowel in vowels:
        consonants.remove(vowel)

    for i in range(start, fin+1):
        if i % 2 == 0:
            name += np.random.choice(vowels)
        else:
            name += np.random.choice(consonants)
        if len(name) == 1:
            name = name.upper()
    return name


def generate_mock_passenger(cities_api, name):
    keys = abs(planck.rvs(0.5, size=len(cities_api)))
    passenger = pd.DataFrame(columns=cities_api, index=[name])
    passenger.iloc[0] = keys
    return passenger
