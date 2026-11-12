#working with SWAPI data
from os.path import exists
import requests

planet_num = ''

def getPlanets():
    url = "https://swapi.dev/api/planets/"  # URL of API
    response = requests.get(url) # Gets all data from url
    data =  response.json()
    global planet_num
    try:
        print("please enter a number between 1 - 60")
        planet_num = input("Enter a planet's number: ")
        url += planet_num
        response = requests.get(url)
        data = response.json()
        saveData(data)
    except:
        print("invalid planet number")
        getPlanets()

def saveData(data):
    file_exists = exists('planets.txt')
    if(file_exists):
        with open('planets.txt', 'a') as f:
            f.write('Planet Number: ' + str(planet_num))
            f.write('\n')
            f.write('Planet Name: ' + data['name'])
            f.write('\n')
            f.write('Planet Terrain: '  + data['terrain'])
            f.write('\n')
            f.write('Planet Climate: ' + data['climate'])
            f.write('\n')
            f.write('Planet Orbital Period: ' + data['orbital_period'])
            f.write('\n')
            f.write('Planet Rotation Period: ' + data['rotation_period'])
            f.write('\n''\n')
    else:
        with open("planets.txt", 'w')as f:
            f.write('Planet Number: ' + str(planet_num))
            f.write('\n')
            f.write('Planet Name: ' + data['name'])
            f.write('\n')
            f.write('Planet Terrain: '  + data['terrain'])
            f.write('\n')
            f.write('Planet Climate: ' + data['climate'])
            f.write('\n')
            f.write('Planet Orbital Period: ' + data['orbital_period'])
            f.write('\n')
            f.write('Planet Rotation Period: ' + data['rotation_period'])
            f.write('\n''\n')

getPlanets()
