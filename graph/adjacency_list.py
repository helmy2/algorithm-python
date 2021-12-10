class Node:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    def add_edge(self, s, d):
        node = Node(d)
        node.next = self.graph[s]
        self.graph[s] = node

        # node = Node(s)
        # node.next = self.graph[d]
        # self.graph[d] = node

    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    def transpose(self):
        g = Graph(4)
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                g.add_edge(temp.vertex, i)
                temp = temp.next
        self.V = g.V
        self.graph = g.graph


if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)

    graph.print_agraph()
    # 0 1 1 1
    # 0 0 0 0
    # 0 0 0 0
    # 0 0 0 0

    graph.transpose()
    graph.print_agraph()

    # 0 0 0 0
    # 1 0 0 0
    # 1 0 0 0
    # 1 0 0 0
