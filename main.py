# main.py

import json
from dijkstra import dijkstra, get_path

with open("graph_data.json") as f:
    graph = json.load(f)