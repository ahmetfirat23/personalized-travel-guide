import scrapy
from scrapy_splash import SplashRequest
from ..items import WhereToVisitItem
from fetcher import fetch_api

# Created By  : Ali Tarik Sahin and Ceyhun Sonyurek
# Created Date: 6/08/2022
# Creator Team: Optimize Isler
# Created for: THY Hackathon

class AttractionSpider(scrapy.Spider):
    name = 'attraction'

    cities = fetch_api()
        #['santiago de compostela', 'ottawa', 'bilbao', 'ki̇li̇manjaro', 'syktyvkar', 'honolulu', 'wellington', 'dallas', 'louisville', 'sendai', 'sundsvall', 'karlsruhe,baden-baden', 'holguin', 'santo domingo', 'bacolod', 'lviv', 'rio de janeiro', 'johnstown', 'quebec', 'barcelona', 'seattle', 'windsor', 'red deer', 'houston', 'quito', 'regina', 'grande prairie', 'thunder bay', 'hamilton', 'sydney(nova scotia)', 'gander', 'fort lauderdale', 'white plains', 'florianopolis', 'seychelles', 'santorini island', 'bandung', '', 'juba', 'san francisco', 'skelleftea', 'longyearbyen', '', 'lyon', 'belem', 'munster', 'sudbury', 'surgut', 'berlin', 'saint john', 'springfield', 'diyarbakir', 'beirut', 'freetown', 'funchal', 'ho chi̇ mi̇nh ci̇ty (sai̇gon)', 'hurghada', 'st. george', 'kharkiv', 'harlingen', 'bakersfield', 'staunton/waynesboro/harrisonburg', 'sharjah', 'ulaanbaatar', 'turkistan', 'timmins', 'bucaramanga', 'toronto', 'shreveport', 'bingol', 'ulyanovsk', 'bridgetown', 'fortaleza', 'binghamton', 'dakar', 'huntsville', 'bergen', 'umea', 'sal', 'yuma', 'montreal', 'baghdad', 'milan', 'douala', 'singapore', 'rouyn', 'dalaman (mugla)', 'birmingham', 'hatay', 'san josé del cabo', 'san jose', 'sarajevo', "val d'or", 'birmingham', 'vancouver', 'wroclaw', 'são josé do rio preto', 'san jose', 'san juan', 'billings', 'dammam', 'winnipeg', 'bilbao', 'biarritz/anglet/bayonne', 'semerkand', 'bismarck', 'thessaloni̇ki̇', 'frankfurt', 'skopje', 'banjul', 'saskatoon', 'bishkek', 'fort st.john', 'salt lake city', 'bodrum (mugla)', 'denizli', 'silao', 'london', 'abbotsford', 'whitehorse', 'doha', 'odessa', 'são luís', 'kota kinabalu', 'calgary', 'bangkok', 'north bay', 'charlottetown', 'bamako', 'victoria', 'chennai', 'sacramento', 'madrid', 'little rock', 'st johns', 'el calafate ', 'majuro atoll', 'mont-joli', 'santa marta', 'manaus', 'manchester', 'toronto', 'santa maria', 'maracaibo', 'batna', 'dipolog', 'billund', 'denpasar(bali)', 'bologna', 'urumqi', 'santa ana', 'bangalore', 'mombasa', 'sarnia', 'hyannis', 'blantyre', 'hyderabad', 'sept iles', 'montego bay', 'santa clara', 'fukuoka', 'saginaw', 'sofia', 'usinsk', 'ko samui', 'kahului', 'kansas city', 'nashville', 'brisbane', 'orlando', 'ordu-giresun', 'muscat', 'durango', 'makhachkala', 'maceio', 'del rio', 'darwin', 'springfield', 'medellin', 'fort wayne', 'mandalay', 'bordeaux', 'spli̇t', 'bogota', 'harrisburg', 'boise', 'des moines', 'kralendjik', 'mumbai', '', 'bodo', 'dakar', 'boston', 'medinah', 'memphis', 'melbourne', 'kano', 'mexico city', 'vieux fort', 'porto seguro', 'detroit', 'beaumont-port arthur', 'mc allen', 'dublin', 'sarasota bradenton', 'kabul', 'kiev', 'medford', 'kota bahru', 'krabi', 'aguadilla', 'durban', 'salvador', 'dusseldorf', 'oki̇nawa', 'malabo', 'oklahoma city', 'managua', 'sharm el-shei̇kh', 'kuching', 'bremen', 'kahramanmaras', 'kocaeli', 'mogadi̇shu', 'bari', 'davao ', 'zadar', 'brownsville', 'zagreb', 'bristol', 'brussels', 'olbia', 'mashad', 'santiago', 'london', 'lago sul', 'stuttgart', 'charlotte amalie', 'stavropol', 'manchester', 'basel', 'bathurst', 'basra', 'surabaya', 'omaha', 'miami', 'urumiyeh', 'washington dc', 'reykjavík', 'dubai', 'houston', 'omsk', 'baton rouge', 'batu licin-borneo island', 'burlington', 'stavanger', 'ibague', 'budapest', 'buffalo', 'zonguldak', 'ekaterinburg', 'ontario', 'kastamonu', 'burbank', 'ibiza', 'batumi (international)', 'dushanbe', 'new york', 'milwaukee', 'kaliningrad', 'gold coast', 'boa vista', 'kigali', 'seoul', 'wichita', 'strasbourg', 'malta', 'chapecó', 'malé', 'idaho falls', 'saint martin', 'kherson', 'moline', 'karachi', 'porto', 'si̇i̇rt', 'washington dc', 'monroe', 'malatya', 'bandar seri begawan', 'sydney', 'washington dc', 'mammoth lakes', 'murmansk', 'syracuse', 'kingston', 'shi̇raz', 'chisinau', 'malmo', 'kuala lumpur', 'osaka', 'samsun', 'chicago', 'salzburg', 'norfolk', 'krasnoyarsk', 'worcester', 'oran', 'manila', 'isfahan', 'ostersund', 'mobile', 'modesto', 'igdir', 'oslo', 'molde', 'belize city', 'osh', 'kirkenes', 'georgetown', 'puerto iguazu', 'foz do iguacu', 'bozeman', 'van', 'north bend', 'malay', 'varna', 'montpellier/mediterranee', 'sivas', 'bucharest', 'maputo', 'guadalajara', 'kalibo', 'kalmar', 'gdansk', 'ouagadougou', 'oujda', 'magnitogorsk', 'mardin', 'spokane', 'visby', 'georgetown', 'eau claire', 'venice', 'novosi̇bi̇rsk', 'campinas', 'entebbe', 'victoria', 'medan', 'erbil', 'marseille', 'mineralnye vody', 'mauritius (port louis)', 'monterey', 'kona', 'tehran', 'artvi̇n-hopa', 'missoula', 'madison', 'minsk', 'minneapolis', 'mus', 'lefkosa', 'new orleans', 'irkutsk', 'george town', 'tagbilaran', 'montrose', 'tashkent', 'xian', 'montería', 'edinburgh', 'iloilo', 'balikesir-edremit', 'monterrey', 'munich', 'tbilisi', 'rio de janeiro', 'columbia', 'zanzibar', 'cagliari', 'cairo', 'akron', 'tabriz', 'imperatriz', 'guangzhou', 'montevideo', 'zaporizhzhia', 'indianapolis', 'krakow', 'kiruna', 'kurgan', 'krasnodar', 'khartoum', 'kristiansand', 'grand junction', 'cotabato', "martha's vineyard", 'canberra', 'kosice', 'kermanshah', 'cayo coco', 'eagle', 'belgorod', 'kristiansund', ' ilhéus', 'kars', 'caracas', 'vienna', 'kolkata', 'xiamen', 'praia', 'marrakech', 'rapid city', 'ribeirão preto', 'milan', 'imperial', 'vitória', 'kathmandu', 'paris', 'fayetteville/springdale', 'zurich', 'samara', 'teneri̇fe', 'crescent city', 'cebu', 'kuala lumpur', 'rio branco', 'kaunas', 'annaba', 'chiang rai', 'myrtle beach', 'chelyabinsk', 'san salvador', 'marysville', 'aalborg', 'miri', 'iquitos', 'podgorica', 'anapa', 'aarhus', 'kuala terengganu', 'riohacha', 'amasya / merzifon', 'moscow', "saint george's", 'barrancabermeja', 'manizales', '', 'tegucigalpa', 'allentown', 'abi̇djan', 'valenci̇a', 'albuquerque', 'sanliurfa', 'redding', 'genoa', 'valensiya', 'aberdeen', 'islamabad', 'isparta', 'redmond', 'kuwait', 'sukhothai', '', 'akra', 'raleigh durham', 'williston', 'jakarta', 'nantucket', 'sulaymaniyah', 'cologne', 'istanbul', 'gothenburg', 'tirana', 'campo grande', 'tai̇f', 'recife', 'waco', 'cagayan de oro', 'arcata-eureka', 'paducah', 'ithaca', 'adana', 'port-au-prince', 'christchurch', 'izmir', 'addi̇s ababa', 'aden', 'adiyaman', 'osaka', 'hilo', 'el paso', 'adeliade', 'gulfport', 'al qassim', 'charlottesville', 'souda', 'charleston', 'konya', 'tokat', 'tyumen', 'west palm beach', 'vilnius', 'san andrés', 'chico', 'cedar rapids', 'buenos aires', 'sochi', 'alesund', 'volgograd', 'alexandria', 'green bay', 'yangon', 'kazan', 'turku', 'fort hood/killeen', 'kutahya', 'grand rapids', 'sao paulo', 'graz', 'tlemcen', 'tallinn', 'valparaiso', 'ponta delgada (azores)', 'toulouse', 'agadir', 'tel aviv', 'greensboro', 'ängelholm', 'portland', 'greenville', 'malaga', 'richmond', 'ciudad del este', 'aguascalientes', 'conakry', 'perm', 'canakkale', 'pereira', 'nakhichevan', 'tampere / pirkkala', 'beijing', 'great falls', 'penang', 'nadi', 'naples', 'perth', 'cleveland', 'riga', 'natal', 'cluj', 'nassau', 'nevsehir', 'college station', 'varadero', 'cali', 'charlotte', 'tangier', 'passo fundo', 'naberevnye chelny', 'gunnison', 'colombo', 'antananarivo', 'nairobi', 'inyokern', 'hagåtña, guam', 'columbus', 'casablanca', '', 'tomsk', 'hancock', 'nice', 'geneva', 'newcastle', 'erzincan', 'constanta', 'tromso', 'belo horizonte', 'erie', 'agri', 'tampa', 'taipei', 'cairns', 'erzurum', 'chiang mai', 'aracaju', 'ankara', 'philadelphia', "n'djamena", 'cody', 'cochin', 'phoenix', 'auckland', 'cotonou', 'colorado springs', 'cordoba', 'peoria', 'luanda', 'valledupar', 'almaty', 'albany', 'lansing', 'copenhagen', 'pittsburgh', 'alta', 'algiers', 'las vegas', 'los angeles', 'casper', 'cape town', 'trondheim', 'ronneby', 'santa cruz de la sierra', 'lubbock', 'turi̇n(tori̇no)', 'guayaquil', 'reno', 'baku', 'amarillo', 'eugene', 'ahmedabad', 'thiruvananthapuram', 'tiruchirappalli', 'goiania', 'amman', 'libreville', 'monrovia', 'roanoke', 'amsterdam', 'rochester', 'nur-sultan', 'sint eustatius', 'lake charles', 'babelthuap island', 'evenes', 'anchorage', 'nagoya', 'rosario', 'rostov', 'townsville', 'alanya', 'gaziantep', 'corpus christi', 'sao vicente', 'evansville', 'st. george', 'charleston', 'londrina', 'port lincoln', 'palanga', 'providenciales island', 'new york', 'alor satar', 'st.petersburg', 'tulsa', 'tunis', 'palma de mallorca', 'jackson', 'leipzig', 'catania', 'niamey', 'palermo', 'tucson', 'jackson', 'cartagena', 'las palmas de gran canaria', 'lexington', 'jacksonville', 'traverse city', 'sapporo', 'nizhnevartovsk', 'pohnpei island', 'najaf', 'phnom penh', 'cúcuta', 'pensacola', 'pointe-noire', 'aqaba', 'lafayette', 'lome', 'cancun', 'el yopal', 'willemstad', 'porto alegre', 'long beach', 'nouakchott', 'new york', 'puerto plata', 'buenos aires', 'langkawi', 'cincinnati', 'port of spain', 'sirnak', 'arkhangelsk', 'fort myers', 'poznan', 'stockholm', 'london', 'elazig', 'ndola', 'sault ste. marie', 'lahore', 'rotterdam', 'mosinee', 'curitiba', 'popayán', 'ashgabat', 'puerto princesa', 'aspen', 'astrakhan', 'juazeiro do norte', 'london', '', 'asmara', 'bagotville', 'kayseri', 'asunción', 'riyadh', 'jeddah', 'lihue', 'tyler', 'moroni', 'knoxville', 'hannover', 'milan', 'lima', 'hanoi', 'liberia', 'hamburg', 'athens', 'little rock', 'lisbon', 'atlanta', 'havana', 'haugesund', 'amritsar', 'prague', 'rostov', 'appleton', 'hobart', 'alexandria', 'rovaniemi', 'oranjestad', 'prishtina', 'new york', 'trabzon', 'abu dhabi', 'ljubljana', 'deer lake', 'pisa', 'austin', 'pasco', 'ponce', 'palm springs ', 'pasto', 'si̇nop', 'constantin', 'cozumel', 'asheville', 'edmonton', 'bursa ', 'lulea', 'senai', 'warsaw', 'roxas', 'pointe-à-pitre le raizet', 'hayden', 'panama city', 'fredericton int.', 'djibouti', 'punta cana', 'ahwaz', 'helsinki ', 'busan', 'klamath falls', 'faro', 'pula', 'armenia', 'fargo', 'nur-sultan', 'fresno', 'kingston', 'providence', 'fayetteville', 'shanghai', 'iles de la madeleine', 'lincoln', 'puerto vallarta', 'rize', 'tokyo', 'linz', 'windhoek ', 'antalya', 'toronto', 'longana', 'yaounde', 'portland', 'halifax', 'lagos', 'rome', 'kalamazoo', 'samana', 'las palmas (canary islands)', 'la paz / el alto', 'porto santo (madeira)', 'fort-de-france', 'friedrichshafen', 'lampang', 'alicante', 'nurnberg', 'daytona beach', 'da nang', 'dhaka', 'hiroshima', 'mykonos island', 'fergana', 'dallas', 'kamloops', 'dar es salaam', 'neiva', 'david', 'fez', 'hakkari', 'dayton', 'johannesburg', 'laredo', 'la romana', 'navegantes', 'dubrovnik', 'hong kong', 'joinville', 'kelowna', 'yoshkar ola', 'phuket', 'saba', 'fort mcmurray', 'joão pessoa', 'santa clara', 'carlsbad', 'san pedro sula&#x9;', 'san antonio', 'istanbul', 'savannah', 'yanbu', 'ufa', 'santa barbara', 'khanty-mansiysk', 'south bend', 'san luis obispo', 'kinshasa', 'lusaka', 'bahrain', 'delhi( new delhi )', 'denver', 'batman', 'luxembourg', 'barranquilla', 'state college', 'santiago', 'aktau', 'tokyo']

    city_id_match = dict()
    number_of_attractions = 4

    def start_requests(self):
        """In this section, for every city, the spider goes to the webpage where the name of the city is searched"""
        for city in AttractionSpider.cities:
            yield SplashRequest("https://www.tripadvisor.com/Search?q=" + city, self.parse, args={'wait': 5})
            # wait argument waits for 5 second for javascript in the webpage to load (the value here is an exaggerated number
            # normally a number between 1-2 should be enough, but in any case it is set to 5 seconds)

    def parse(self, response):
        """After getting response from the webpage, the spider takes the city name searched and encode it in a dictionary
        with the particular geographical code (e.g. "g243786"). The reason is that when scrapping through these webpages with
        a number of cities, it gets difficult to follow city names. Afterwards, the spider uses that geographical code to
        jump to "activities to do" page.
        """
        city_name = response.css("#page-title+ .ajax-content .title-query::text").extract_first()

        onclick_data = response.xpath("//div[@class='ui_columns is-mobile result-content-columns']").xpath("./@onclick").extract()
        for elem in onclick_data:
            selected_id = self.find_selected_id(elem)
            city_id = self.find_city_id(elem)
            # this checkpoint is made for the spider to find accurate city in the search page
            if city_id == selected_id:
                AttractionSpider.city_id_match[city_id] = city_name
                next_link = "https://www.tripadvisor.com/Attractions-" + city_id + "-Activities-a_allAttractions.true"
                yield response.follow(next_link, callback=self.parse_attractions)
                break
        else:
            yield None

    def parse_attractions(self, response):
        """ At this point, the spider loops through all attraction locations and gets links. It only selects the valid ones
        stops when desired number is reached, in this case it is 4. Validation is made by using the special geographical code.
        Afterwards, all the urls of the selected attraction places are followed.
        """
        links = response.xpath("//div[@class='alPVI eNNhq PgLKC tnGGX']").css("a::attr(href)").extract()
        city_id = self.find_city_id(response.xpath("//meta[@property='al:ios:url']/@content").extract_first())
        counter = 0
        for i in range(0, len(links), 2):
            if counter == AttractionSpider.number_of_attractions:
                break
            next_url = "https://www.tripadvisor.com" + links[i]
            attraction_city_id = self.find_city_id(next_url)
            if attraction_city_id != city_id:
                continue
            counter += 1
            yield response.follow(next_url, callback=self.get_info)

    def get_info(self, response):
        """This is where all the data are gathered for every single attraction location. In this section, validation is made
        by try-except blocks. At this point, it is essential to eliminate places without image or name or whatever critical
        for the database. The gathered data consists of city_name, attraction_name, rating, image_url, reviews and about parts"""
        items = WhereToVisitItem()
        try:
            attraction_name = response.css('.eIegw::text').extract_first()
            rating = response.css('#tab-data-qa-reviews-0 .uuBRH').css('::text').extract_first()
            image_url = response.xpath(
                    '//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div/div/span/section[2]/div/div/div/div[2]/span/div/div/div[1]/div/div/div/div[1]/div/div[1]/ul/li[1]/div/@style').extract_first()
            image_url = image_url[21:-1]
            about = ""
            try:
                about = response.css(".MJ .KxBGd::text").extract_first()
            except:
                pass
            comments = self.find_comments(response)

            city_id = self.find_city_id(response.xpath("//meta[@property='al:ios:url']/@content").extract_first())

            items['city_name'] = AttractionSpider.city_id_match[city_id]
            items['attraction_name'] = attraction_name
            items['rating'] = rating
            items['image_url'] = image_url
            items['reviews'] = comments
            items['about'] = about

            yield items
        except:
            pass

    def find_comments(self, response):
        """ This code extracts comments for the places and uses a special keyword ("%&break") between comments to make the
        common string look like a list. Moreover, this code only gets the comments whose owner rate the location more than
        or equal to 4 out of 5, which prevents negative comments to prevail
        """
        flag = False
        location_comment1 = ''
        location_comment2 = ''
        for comment_counter in range(1, 11):
            xpath_string = '// *[ @ id = "tab-data-qa-reviews-0"] / div / div[5] / div[' + str(
                comment_counter) + '] / span / div / div[2] / svg/@aria-label'
            try:
                location_comment_score = response.xpath(xpath_string).extract()[0]
                if (location_comment_score[0] == '5') or (location_comment_score[0] == '4'):
                    if location_comment1 == '':
                        location_comment1 = response.css('.KxBGd .yCeTE').extract()[comment_counter - 1].replace(
                            '<span class="yCeTE">', '').replace('<br>', '').replace('</span>', '')
                    else:
                        location_comment2 = response.css('.KxBGd .yCeTE').extract()[comment_counter - 1].replace(
                            '<span class="yCeTE">', '').replace('<br>', '').replace('</span>', '')
                        flag = True
            except:
                flag = True
            if flag:
                break
        return location_comment1 + ' %&break' + location_comment2

    def find_selected_id(self, onclick_data):
        """This code is used to make validation for cities. Thanks to this validation, the spider can differentiate a city
        from a restaurant with the same name"""
        id_index = onclick_data.index("selectedId")
        first_single_quote = onclick_data.index("'", id_index)
        last_single_quote = onclick_data.index("'", first_single_quote + 1)
        return "g" + onclick_data[first_single_quote + 1: last_single_quote]

    def find_city_id(self, onclick_data):
        """This is the code where the spider finds the geographical code that is spesific to a city"""
        id_index = onclick_data.index("-g")
        first_hyphen = id_index
        last_hyphen = onclick_data.index("-", first_hyphen + 1)
        return onclick_data[first_hyphen + 1: last_hyphen]


