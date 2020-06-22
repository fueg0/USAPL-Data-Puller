import requests
from bs4 import BeautifulSoup
###
# PUT THE LIFTER ID NUMBER INTO 'ID' TO FETCH THE PROPER PAGE
###
ID = ''

URL = 'https://usapl.liftingdatabase.com/lifters-view?id=' + ID
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="content")

tabs = results.find_all('table', id='')
name = results.find('h2', id='')

print(name.text)

for t in tabs:
    tbod = t.find('tbody', id='')
    tr = tbod.find_all('tr', id='')
    # variables to catch undesired elements
    bday = tbod.find('tr', string='').text
    rec = tbod.find('tr', string='').text
    oldrec = tbod.find_all('tr', id="showoldbutton")

    # conditional to print nothing in the case that an undesired element is targeted
    if "Records" in rec or "Birth" in bday or len(oldrec) > 0:
        print('')

    # prints the desirable elements
    else:

        # loop to print <th> Lift Type, and move through each <td> tag to only select lifts and totals
        for td in tr:
            print(td.find('th').text.strip())

            td_class = td.find('td', id='').text

            # conditional  to
            if len(td_class) > 10 or "/" in td_class:
                   print('')

            else:
                   print(td_class.strip())
        print('\n')