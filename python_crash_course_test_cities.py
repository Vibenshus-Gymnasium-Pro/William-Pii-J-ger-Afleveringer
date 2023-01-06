from python_crash_course_city_functions import city_type

class test_class():
    def test_city_names(self):    
        print(city_type('santiage', 'chile'))

    def test_city_names_population(self):
        print(city_type('santiage', 'chile', '5000000'))


test = test_class()
test.test_city_names()
test.test_city_names_population()
