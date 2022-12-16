import math
from typing import Dict

from utils import read_stripped_lines


class Graph:
    def __init__(self):
        self.flow_rates = {}
        self.tunnels = {}

    def add_node(self, name: str, flow_rate: int, tunnels: list[str]):
        self.flow_rates[name] = flow_rate
        self.tunnels[name] = tunnels

    def flow_rate(self, name: str):
        return self.flow_rates[name]

    def links(self, name: str):
        return self.tunnels[name]

    def nodes(self):
        return self.flow_rates.keys()


def day16_part1(filename: str) -> int:
    graph = parse_graph(filename)
    distances = find_shortest_distances(graph)
    flow_rates = {k: v for k, v in graph.flow_rates.items() if v > 0}
    return traverse(distances, flow_rates, 'AA', set(), remaining_time=30)


def parse_graph(filename):
    lines = read_stripped_lines(filename)
    graph = Graph()
    for line in lines:
        split = line.replace('Valve ', ''). \
            replace(' has flow rate=', ', '). \
            replace('; tunnels lead to valves ', ', '). \
            replace('; tunnel leads to valve ', ', ') \
            .split(', ')
        name = split[0]
        flow_rate = int(split[1])
        links = split[2:]
        graph.add_node(name, flow_rate, links)
    return graph


def find_shortest_distances(graph: Graph):
    nodes = graph.nodes()
    dist = {}
    for node in nodes:
        for other_node in graph.links(node):
            dist[(node, other_node)] = 1
    for node in nodes:
        dist[(node, node)] = 0
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist.get((i, j), math.inf) > dist.get((i, k), math.inf) + dist.get((k, j), math.inf):
                    dist[(i, j)] = dist.get((i, k), math.inf) + dist.get((k, j), math.inf)

    return dist


def traverse(distances: Dict[tuple[str, str], int], flow_rates: Dict[str, int], position: str, opened: set[str],
             remaining_time: int):
    if remaining_time <= 0:
        return 0
    if len(opened) == len(flow_rates):
        return 0

    potential_scores = []
    for valve, flow_rate in flow_rates.items():
        if valve not in opened:
            time_to_go_and_open = distances[(position, valve)] + 1
            pressure_release = (remaining_time - time_to_go_and_open) * flow_rate
            if pressure_release > 0:
                new_opened = opened.copy()
                new_opened.add(valve)
                potential_scores.append(pressure_release + traverse(distances, flow_rates, valve, new_opened,
                                                                    remaining_time - time_to_go_and_open))
    return max(potential_scores, default=0)


if __name__ == '__main__':
    assert day16_part1('res/day16_sample.txt') == 1651
    print(day16_part1('res/day16.txt'))
