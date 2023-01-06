def city_type(country, city, population=''):
    if population:
        city_string = country.title() + ', ' + city.title() + ' - population ' + population
    else:
        city_string = country.title() + ', ' + city.title()
    return city_string