import requests
from bs4 import BeautifulSoup

lift_id_list = [
"61095"
]

newlifter = "\n ---------------------------------------------------"

for lift_id in lift_id_list:
    URL = "https://usapl.liftingdatabase.com/lifters-view?id="+lift_id
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id="content")

    tables = results.find_all('table', id='')

    name = results.find('h2', id='').text
    print(name)

    for t in tables:
        tbody = t.find('tbody', id='')
        tr = tbody.find_all('tr', id='')

        bday = tbody.find('tr', string='').text
        rec = tbody.find('tr', string='').text
        oldrec = tbody.find_all('tr', id="showoldbutton")

        if "Records" in rec or "Birth" in bday or len(oldrec) > 0:
            print()

        else:
            for td in tr:
                print(td.find('th').text.strip())

                td_class = td.find('td', id='').text

                if len(td_class) > 10 or "/" in td_class:
                       print('')

                else:
                       print(td_class.strip())
            print(newlifter)