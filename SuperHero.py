import requests


class SuperHero:
    super_hero = []

    def __init__(self, name):
        self.name = name
        self.super_hero.append(self)

    def _get_all_info_superhero(self):
        url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
        response = requests.get(url)
        if 100 < response.status_code < 300:
            result = [info for info in response.json() if info['name'] == self.name]
            return result[0]
        else:
            print('Error')

    def get_values_characteristic(self):
        hero_info = self._get_all_info_superhero()['powerstats']
        return hero_info


def comparison_by_characteristics(list_hero, power):
    powers_hero = []
    for hero in list_hero:
        powers = hero.get_values_characteristic()
        if power in powers:
            powers_hero.append([hero.name, powers[power]])
        else:
            print('Error')
            return
    powers_hero.sort(key=lambda x: x[1], reverse=True)
    return f'Из полученного списка, герой с именем {powers_hero[0][0]} самый мощный по принятому показателю силы'