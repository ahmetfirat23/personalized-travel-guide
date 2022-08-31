import bs4
import sqlite3


def query(cities, db):
    dbfile = db
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    cities_table = {}
    for city in cities:
        names = [names for names in
                 cur.execute("SELECT attraction_name FROM products WHERE city_name = '{}'".format(city))]
        photos = [photo for photo in cur.execute("SELECT image_url FROM products WHERE city_name = '{}'".format(city))]
        ratings = [rating for rating in cur.execute("SELECT rating FROM products WHERE city_name = '{}'".format(city))]
        reviews = [review for review in cur.execute("SELECT reviews FROM products WHERE city_name = '{}'".format(city))]
        abouts = [about for about in cur.execute("SELECT about FROM products WHERE city_name = '{}'".format(city))]
        city_table = {'names': names, 'photos': photos, 'ratings': ratings, 'reviews': reviews,'abouts':abouts}
        cities_table.update({city: city_table})
    con.close()
    return cities_table


def create_guide(cities, db, pass_name, flight_list):
    with open('site_template\\template.html') as index:
        txt = index.read()
        soup = bs4.BeautifulSoup(txt, features="html.parser")
    script = open('site_template\\script.js', 'w+')

    cities_table = query(cities, db)

    pass_name_h2 = soup.find(id='intro').find('h2')
    pass_name_h2.append(pass_name + '!')

    for i in range(len(cities)):
        city = cities[i]
        city_data = cities_table[city]
        city_name_h2 = soup.find(id='city-{}'.format(i)).find('h2', {'class': 'city-name'})
        city_name_h2.append(city.capitalize())

        str_template = ''
        for j in range(len(city_data['names'])):
            spot_template = ''
            if j % 2 == 0:
                spot_template += '''<div class="text-on-left"><div class="left-text"><h3 class="dest-name">{}
                </h3><span class="rating">Rating: {}/5</span><h4 class="comment-h">What people think?</h4>'''.format(
                    city_data['names'][j][0], city_data['ratings'][j][0])
            else:
                spot_template += '''<div class="text-on-right"><img class="left-image" src="{}"/><div 
                class="right-text"><h3 class="dest-name">{}</h3><span class="rating">Rating {}/5</span><h4 
                class="comment-h">What people think?</h4>'''.format(
                    city_data['photos'][j][0], city_data['names'][j][0], city_data['ratings'][j][0])

            review_list = city_data['reviews'][j][0].split('%&break')
            for review in review_list:
                if len(review) > 500:
                    hashed = str(abs(hash(review)))
                    script.write( '''function readMore{0}(){{let dots = document.getElementById('dots-{0}');let more = document.getElementById('more-{0}');let btnText = document.getElementById('more-btn-{0}');'''.format(hashed)+\
                    '''if(dots.style.display ==='none'){dots.style.display ='inline';btnText.innerHTML = 'Read more';more.style.display='none';} else{dots.style.display = 'none';btnText.innerHTML = 'Read less';more.style.display ='inline';}}\n''')
                    review = review[:500] + "<span id='dots-{0}' style='display:inline'>...</span><span id='more-{0}' ".format(hashed) + "style='display:none'>" + review[500:] + "</span>" + \
                             '''<button id="more-btn-{0}" onclick="readMore{0}()">Read more</button>'''.format(hashed)
                spot_template += "<p> <span class='inline'> {} </span> </p>".format(review)

            spot_template += '</div>'

            if j % 2 == 0:
                spot_template += '<img class="right-image"src="{}"/>'''.format(city_data['photos'][j][0])
            else:
                spot_template += '''</div></div>'''
            if city_data['abouts'][j][0] is not None:
                spot_template += '''</div><div class='break'''
                if j % 2 == 1:
                    spot_template += ''' gray'''
                spot_template += ''''><span class='about-h'>About</span><br> <span class='about'>{}</span>'''.format(city_data['abouts'][j][0])
            spot_template += '</div>'
            str_template += spot_template

        if flight_list[i] != -1 and flight_list[i] is not None:
            flight_template = '<div class="flight"><div class="about-h">Flight list</div>'
            for flight in flight_list[i]:
                flight_template += '<div class="flight-row'
                if i % 2 == 1:
                    flight_template += ' gray'
                flight_template += '"><span class="f_info">Departure: {}<br>Arrival: {}</span><a class="f_code" href="https://www.google.com/search?q={}">Flight code: {}</a></div>'.format(flight[0], flight[1], flight[2], flight[2])
            flight_template += '</div>'
            str_template += flight_template

        template = bs4.BeautifulSoup(str_template, features='html.parser')
        city_name_h2.insert_after(template)
    with open(f"site_template\\{pass_name}.html", "w", encoding='utf-8') as outf:
        outf.write(str(soup))
