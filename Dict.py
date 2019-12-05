import os
import sys

name_power_map = {"diwen" : 100,
                "miemie" : 10000,
                "meili": 999}

print(name_power_map)

print(name_power_map['diwen'])  # 100

del name_power_map['diwen']

name_power_map['miemie'] = 888
print(name_power_map['miemie'])

print(len(name_power_map))  # 2

print(name_power_map.get('miemie'))

print(name_power_map.keys())    # print all keys
print(name_power_map.values())  # print all values