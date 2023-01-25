import requests


url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
all_inf = response.json()
heroes_list = ['Hulk', 'Captain America', 'Thanos']
energy = {}
for i in all_inf:
    if i['name'] in heroes_list:
            energy[i['name']] = i['powerstats']['intelligence']
a = ''
for k, v in energy.items():
    a = max(energy, key=(lambda k: energy[k]))
print(a)





