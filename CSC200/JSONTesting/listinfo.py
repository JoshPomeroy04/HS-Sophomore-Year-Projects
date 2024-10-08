import json
myJson = open('info.json', 'r')
data = json.load(myJson)
myJson.close()

for thing in data['continents']:
    print('Countries in: ' + thing['continent'])
    for things in thing['countries']:
        print('''---------------------------------
''' + things['name'] + ''':
    Capital: ''' + things['capital'] + '''
    Area: ''' + things['area'] + '''
    Population: ''' + things['population'])


