import os
import sys
import re
sys.path.append(os.path.realpath('.'))
from pprint import pprint

import inquirer
import random

mp = ['Cache', 'Dust II', 'Nuke', 'Mirage', 'Inferno', 'Insertion II', 'Basalt', 'Train', 'Vertigo', 'Overpass', 'Ancient', 'Premier']

veto = [
    inquirer.Checkbox('user_select', message="Vetar:", choices = mp),
]

answers = inquirer.prompt(veto)

#pprint(answers['user_select'])
selection = mp

for x in answers['user_select']:
    selection.remove(x)

print("Mapas vetados: ",answers['user_select'])
print("Mapas selecionados: ", selection)

print("Buscando partida em ",random.choice(selection))