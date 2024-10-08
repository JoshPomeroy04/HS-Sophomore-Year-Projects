import xml.etree.ElementTree as ET
data = ET.parse('info.xml')
root = data.getroot()

# Variable for looping while statement
looping = True

# Main function that reads through xml file
def listinfo(cont, cont2, cont3, cont4, cont5, cont6):

    # Variables needed for storing data
    countrylist = []
    capitallist = []
    arealist = []
    populationlist = []
    territorylist = []
    continentTlist = []
    countryTlist = []
    capitalTlist = []
    areaTlist = []
    populationTlist = []
    totalCarea = 0
    totalCpop = 0
    totalTarea = 0
    totalTpop = 0

    # Parent for loop which loops through all the continents
    for item in root.findall('continen' + cont2):
        continent = item.get('name')
        print("""




Countries in """ + continent + ''':
        ''')

        # Parent loop which reads the country and information about the country
        for stuff in root.iter('countr' + cont6):
            country = stuff.attrib['name']
            countrylist.append(country)

            # Loop to read through capitals
            for things in root.iter('capita' + cont3):
                capital = things.attrib['name']
                capitallist.append(capital)

            # Loop to read through area
            for items in root.iter('are' + cont4):
                area = items.attrib['name']
                arealist.append(area)

            # Loop to read through population
            for thing in root.iter('populatio' + cont5):
                population = thing.attrib['name']
                populationlist.append(population)
        
        # Counts how many countries are in the continent
        loop = len(countrylist)

        # Loop that prints out all information regarding countries in a specific continent
        for stuff in range(1, loop + 1):
            # Adds up all the areas and populations to get a total value
            totalCarea += int(arealist[0].split()[0].replace(',', ''))
            totalCpop += int(populationlist[0].split()[0].replace(',', ''))
            print(countrylist[0] + """:
                Capital: """ + capitallist[0] + """
                Area: """ + arealist[0] + """
                Population: """ + populationlist[0] + """
                """)
            # Removes the country and the info regarding it from the lists
            countrylist.pop(0)
            capitallist.pop(0)
            arealist.pop(0)
            populationlist.pop(0)

        # Parent loop to read through territories
        for stuff in root.iter('territor' + cont6):
            territory = stuff.attrib['name']
            territorylist.append(territory)

            # Loop that reads through what continent the territory is on
            for things in root.iter('continentT' + cont):
                continentT = things.attrib['name']
                continentTlist.append(continentT)

            # Loop that reads through what country has control over the territory
            for items in root.iter('countryT' + cont):
                countryT = items.attrib['name']
                countryTlist.append(countryT)

            # Loop that reads through what the capital of the territory is
            for thing in root.iter('capitalT' + cont):
                capitalT = thing.attrib['name']
                capitalTlist.append(capitalT)

            # Loop that reads through what the area of the territory is
            for objects in root.iter('areaT' + cont):
                areaT = objects.attrib['name']
                areaTlist.append(areaT)

            # Loop that reads through the population of the territory
            for info in root.iter('populationT' + cont):
                populationT = info.attrib['name']
                populationTlist.append(populationT)
    
        # Counts how many territories there are
        loopT = len(territorylist)
    
        print("""


Territories in """ + continentTlist[0] + """:
   """)
        # Loop that prints out information on the territories
        for stuff in range(1, loopT + 1):

            # Adds up all the areas and populations to get a total value
            totalTarea += int(arealist[0].split()[0].replace(',', ''))
            totalTpop += int(populationlist[0].split()[0].replace(',', ''))
            print(territorylist[0] + """:
                Continent located on: """ + continentTlist[0] + """
                Ruling country: """ + countryTlist[0] + """
                Capital: """ + capitalTlist[0] + """
                Area: """ + areaTlist[0] + """
                Population: """ + populationTlist[0])
            territorylist.pop(0)
            continentTlist.pop(0)
            countryTlist.pop(0)
            capitalTlist.pop(0)
            areaTlist.pop(0)
            populationTlist.pop(0)
        print('''
        
Totals in ''' + continent + ''':
                Countries: ''' + str(loop) + '''
                    Area: ''' + str(totalCarea) + ' sq mi' + '''
                    Population: ''' + str(totalCpop) + '''
                
                Territories: ''' + str(loopT) + '''
                    Area: ''' + str(totalTarea) + ' sq mi' + '''
                    Population: ''' + str(totalTpop) + '''
                
                Countries and Territories: ''' + str(loop + loopT) + '''
                    Area: ''' + str(totalCarea + totalTarea) + ' sq mi' + '''
                    Population: ''' + str(totalCpop + totalTpop))

# Loop that allows the user to pick what to look at
while looping == True:
    choice = input('Which continent would you like to look at? Enter NA for North America, SA for South America, or ALL to view all. If you would like to quit type "exit". ')
    if choice == 'NA' or choice == 'na':
        listinfo('N', 't', 'l', 'a', 'n', 'y')
    elif choice == 'SA' or choice == 'sa':
        listinfo('S', 'tS', 'lS', 'aS', 'nS', 'yS')
    elif choice == 'ALL' or choice == 'All' or choice == 'all':
        listinfo('N', 't', 'l', 'a', 'n', 'y')
        listinfo('S', 'tS', 'lS', 'aS', 'nS', 'yS')
    elif choice == 'exit' or choice == 'Exit':
        looping = False
