# -*- coding: utf-8 -*-
import json
from pprint import pprint

#loads the data from an existing .json into a dictiorary
data = json.load(open('input_example.json'))
pprint(data['projects'])