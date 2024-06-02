import requests
from bs4 import BeautifulSoup


API_KEY = 'AIzaSyA9v64KpMrKie9JtFmgDYRPg8xbLJ7yMkQ'

def get_street_list(origin_address, destination_address):
    
    url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin_address}&destination={destination_address}&key={API_KEY}&mode=driving&optimize=true'
    response = requests.get(url)
    data = response.json()

    street_names_list = []

    street_names_list.append(origin_address)
    
    if data['status'] == 'OK':
        routes = data['routes']
        if routes:
            legs = routes[0]['legs']
            for leg in legs:
                steps = leg['steps']
                for step in steps:
                    soup = BeautifulSoup(step['html_instructions'], 'html.parser')
                    street_names = [elem.text for elem in soup.find_all('b')]
                    for street_name in street_names:
                        
                        if street_name.lower() not in ('left', 'right', 'north', 'south'):
                            street_names_list.append(street_name)
        
        else:
            print("No routes found.")
    else:
        print("Error:", data['status'])
    
    street_names_list.append(destination_address)
    
    print(street_names_list)
    return street_names_list