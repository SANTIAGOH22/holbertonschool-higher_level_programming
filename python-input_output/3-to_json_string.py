#!/usr/bin/python3
'''Function that return an object'''


import json


def to_json_string(my_obj):
    '''Return object of the json'''
    j_obj = json.dumps(my_obj)
    return j_obj
