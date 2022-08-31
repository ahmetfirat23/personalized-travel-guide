import requests
import sqlite3
from datetime import datetime, timedelta
import os


def fetch_api(with_airports=False):
    url = 'https://api.turkishairlines.com/test/getPortList'
    # This val is just a Client_test so may cause problems during comp.
    values = """{                                              
    	"requestHeader": {
    		"clientUsername": "OPENAPI",
    		"clientTransactionId": "CLIENT_TEST_1",
    		"channel": "WEB",
    		"languageCode":"EN",
    		"airlineCode":"TK"
    	}
    }
    """
    headers = {'apisecret': '885c340e96ac4c7a9638c021ccbe8a01', 'Content-Type': 'application/json',
               'apikey': 'l7xxf90f2f436d3b48bba2a0d0ef5aec7008'}

    request = requests.request(url=url, data=values, headers=headers, method='POST')
    r_dict = request.json()

    return extract_cities(r_dict, with_airports)


def extract_cities(r_dict, with_airports):
    correct_num = 0
    err_num = 0
    r_dict = r_dict['data']['Port']
    city_list = set()
    airport_table = {}
    trans_table = str.maketrans("ğıöüşç", "giousc")
    # 3 different formats ==> 3 try/except ==> More common one on the outer shell
    for i in range(len(r_dict)):
        try:
            city = r_dict[i]['City']['LanguageInfo']['Language']['Name'].lower().translate(trans_table)
            correct_num += 1
        except:
            try:
                city = r_dict[i]['City']['LanguageInfo']['Language'][0]['Name'].lower().translate(trans_table)
                correct_num += 1
            except:
                try:
                    city = r_dict[i]['City']['LanguageInfo'].lower().translate(trans_table)
                    correct_num += 1
                except:
                    err_num += 1
                    continue
        if city == '':
            correct_num -= 1
            continue
        if not with_airports:
            city_list.add(city)
        else:
            airport_table.update({city: r_dict[i]['City']['Code']})

    return list(city_list) if not with_airports else airport_table


def fetch_database(db):
    dbfile = db
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    city_list = [name[0] for name in cur.execute("SELECT city_name FROM products")]
    return city_list


def fetch_flight(cities, city_dict, origin):
    flight_list = []
    for city in cities:
        try:
            flight_list.append(time_table_(origin, city_dict[city]))
        except:
            flight_list.append(-1)
    return flight_list


def time_table_(origin, target):
    info_list = []

    def timeTable(originCode, destinationCode, count=3, date=datetime.now()):
        if (len(info_list) == 3):
            return info_list

        url = 'https://api.turkishairlines.com/test/getTimeTable'

        values = f"""

    {{
       "requestHeader": {{
        "clientUsername": "OPENAPI",
        "clientTransactionId": "CLIENT_TEST_1",
        "channel": "WEB",
        "languageCode":"EN",
        "airlineCode":"TK"
      }},
      "OTA_AirScheduleRQ":{{
        "OriginDestinationInformation":{{
          "DepartureDateTime":{{
            "WindowAfter":"P0D",                                        
            "WindowBefore":"P0D",
            "Date": "{str(date).split()[0]}"  
          }},
          "OriginLocation":{{
            "LocationCode": "{originCode}",   
            "MultiAirportCityInd":true
          }},
          "DestinationLocation":{{
            "LocationCode": "{destinationCode}",
            "MultiAirportCityInd":false
          }}
        }},
        "AirlineCode":"TK",
        "FlightTypePref":{{
          "DirectAndNonStopOnlyInd":true
        }}
      }},
      "scheduleType":"W",
      "tripType":"O"
    }}
        """
        headers = {'apisecret': '885c340e96ac4c7a9638c021ccbe8a01', 'Content-Type': 'application/json',
                   'apikey': 'l7xxf90f2f436d3b48bba2a0d0ef5aec7008'}

        request = requests.request(url=url, data=values, headers=headers, method='POST')
        r_dict = request.json()
        try:
            # print(r_dict['data']['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
            #           'OriginDestinationOptions']['OriginDestinationOption'])

            if type(r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
                        'OriginDestinationOptions']['OriginDestinationOption']) is list:
                for i in range(len(
                        r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
                            'OriginDestinationOptions']['OriginDestinationOption'])):
                    if (datetime.strptime(
                            r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
                                'OriginDestinationOptions']['OriginDestinationOption'][i]['FlightSegment'][
                                'DepartureDateTime'].split('T')[0], '%Y-%m-%d') > datetime.now() and [dateConverter(
                        r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
                            'OriginDestinationOptions']['OriginDestinationOption'][i]['FlightSegment'][
                            'DepartureDateTime']), dateConverter(
                        r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
                            'OriginDestinationOptions']['OriginDestinationOption'][i]['FlightSegment'][
                            'ArrivalDateTime']), r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS'][
                        'OTA_AirScheduleRS'][
                        'OriginDestinationOptions'][
                        'OriginDestinationOption'][
                        i][
                        'FlightSegment'][
                        'FlightNumber']] not in info_list):
                        info_list.append([dateConverter(
                            r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
                                'OriginDestinationOptions']['OriginDestinationOption'][i]['FlightSegment'][
                                'DepartureDateTime']), dateConverter(
                            r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
                                'OriginDestinationOptions']['OriginDestinationOption'][i]['FlightSegment'][
                                'ArrivalDateTime']), r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS'][
                            'OTA_AirScheduleRS']['OriginDestinationOptions'][
                            'OriginDestinationOption'][i]['FlightSegment']['FlightNumber']])
                        count -= 1
                        if (len(info_list) == 3):
                            info_list.sort(key=lambda x: dateSortingFormat(x[0]))
                            return info_list
                    else:
                        pass
                return timeTable(originCode, destinationCode, count, date + timedelta(1))
            else:
                if (datetime.strptime(
                        r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
                            'OriginDestinationOptions']['OriginDestinationOption']['FlightSegment'][
                            'DepartureDateTime'].split('T')[0], '%Y-%m-%d') > datetime.now() and [dateConverter(
                    r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
                        'OriginDestinationOptions']['OriginDestinationOption']['FlightSegment'][
                        'DepartureDateTime']), dateConverter(
                    r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
                        'OriginDestinationOptions']['OriginDestinationOption']['FlightSegment']['ArrivalDateTime']),
                    r_dict["data"][
                        'timeTableOTAResponse'][
                        'extendedOTAAirScheduleRS'][
                        'OTA_AirScheduleRS'][
                        'OriginDestinationOptions'][
                        'OriginDestinationOption'][
                        'FlightSegment'][
                        'FlightNumber']] not in info_list):
                    info_list.append([dateConverter(
                        r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
                            'OriginDestinationOptions']['OriginDestinationOption']['FlightSegment'][
                            'DepartureDateTime']), dateConverter(
                        r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS']['OTA_AirScheduleRS'][
                            'OriginDestinationOptions']['OriginDestinationOption']['FlightSegment']['ArrivalDateTime']),
                        r_dict["data"]['timeTableOTAResponse']['extendedOTAAirScheduleRS'][
                            'OTA_AirScheduleRS']['OriginDestinationOptions']['OriginDestinationOption'][
                            'FlightSegment']['FlightNumber']])
                    count -= 1
                    if (len(info_list) == 3):
                        info_list.sort(key=lambda x: dateSortingFormat(x[0]))
                        return info_list
                return timeTable(originCode, destinationCode, count, date + timedelta(1))

        except:
            return -1

    def dateConverter(date):

        temp = date.split("T")
        first = temp[0].split("-")
        first.reverse()
        return ".".join(first) + "-" + date.split("T")[1][:-3]

    def dateSortingFormat(date):
        return datetime.strptime(date, '%d.%m.%Y-%H:%M')

    return timeTable(origin, target)


def run_crawler():
    os.chdir(r"where_to_visit")
    os.system("scrapy crawl attraction")