class Graph(object):

    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for j in range(size)])
        self.size = size

    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        # self.adjMatrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        # self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def print_matrix(self):
        for row in self.adjMatrix:
            print(row)
        print()

    def transpose(self):
        for i in range(self.size):
            for j in range(self.size):
                (self.adjMatrix[i][j], self.adjMatrix[j][i]) = (self.adjMatrix[j][i], self.adjMatrix[i][j])


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()
    g.transpose()
    g.print_matrix()
