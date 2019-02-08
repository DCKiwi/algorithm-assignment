# David Cockerill
# 16163090
# Assignment 3
# Problem 3

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def build_graph(self, file):
        first_line_bool = True
        file_lines = 0
        line_number = 0

        for line in file:

            if not line.strip():
                continue

            elif first_line_bool:
                first_line_bool = False
                line_number = line

                if int(line_number) < 1:
                    raise SystemExit("Incorrect input - line count must be 1 or greater")

                continue

            else:
                l = line.strip().split(" ")
                l = list(map(int, l))
                self.add_edge(l[0], l[1])
                file_lines += 1

        if file_lines != int(line_number):
            raise SystemExit("Incorrect input - first line number does not match line count")

    def test_cyclic(self):
        values = []

        for key, value in self.graph.items():
            for char in value:
                values.append(char)

        if len(values) > len(set(values)):
            self.write_file("This is not a tree \n")

        else:
            self.write_file("This is a tree \n")

    @staticmethod
    def write_file(output):
        output_file = open("prob3.out", "w")
        output_file.write(output)
        output_file.close()


f = open("prob3.in")
g = Graph()
g.build_graph(f)
g.test_cyclic()
