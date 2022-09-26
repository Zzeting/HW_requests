from apikey import QAuth_TOKEN
import YaDisc
import SuperHero
from SuperHero import comparison_by_characteristics
import easygui
from pprint import pprint

if __name__ == '__main__':
    # hulk = SuperHero.SuperHero('Hulk')
    # captain_america = SuperHero.SuperHero('Captain America')
    # thanos = SuperHero.SuperHero('Thanos')
    #
    # powerful = comparison_by_characteristics([hulk, captain_america, thanos], 'intelligence')
    # print(powerful)

    ya = YaDisc.YandexDisc(QAuth_TOKEN)
    YaDisc.uploads_file_disk(ya)  # функция загрузки файла
