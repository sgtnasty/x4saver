#!/usr/bin/env python
"""
This file is part of the x4saver distribution (https://github.com/sgtnasty/x4saver).
Copyright (c) 2023 Ronaldo Nascimento

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, buT
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import xmltodict
import sys
import datetime
from gzip import GzipFile


filepath = sys.argv[1]
print(f"parse egosoft x4 savegame: {filepath}")
t1 = datetime.datetime.now()
print("PARSING")
xml = xmltodict.parse(GzipFile(filepath))
# savegame -> info -> player
# <player name="Val Selton" location="{20004,60011}" money="81920"></player>
print("SEARCHING")
player = xml['savegame']['info']['player']
player_name = player['@name']
player_money = player['@money']
print(f'PLAYER: {player_name} has ${player_money}')
# universe -> factions -> faction -> relations -> relation
for faction in xml['savegame']['universe']['factions']['faction']:
    faction_name = faction['@id']
    print(f'{faction_name}')
    try:    
        for relation in faction['relations']['relation']:
            relation_name = relation['@faction']
            relation_val = relation['@relation']
            print(f'\twith \'{relation_name}\': {relation_val}')
    except KeyError as key_err:
        print(f"KeyError: {key_err}")
        # sys.exit(1)
t2 = datetime.datetime.now()
td = t2 - t1
print(f'\t{td.seconds} second(s)')
