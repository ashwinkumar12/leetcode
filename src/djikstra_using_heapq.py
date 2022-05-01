import heapq
from collections import defaultdict
import sys
import pprint

class Solution(object):
    def __init__(self):
        self.graph = defaultdict(dict)
        
    def construct_graph(self, times):
        for u,v,w in times:
            self.graph[u].update({v:w})
        #pprint.pprint(self.graph)
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        self.construct_graph(times)
        distances = self.calculate_distances(N, K)
        print distances
        distances = distances.values()
        if [False for i in distances if i==sys.maxint]:
            return -1
        return max(distances)

    def add_all(self, dict_val, set_val):
        for k,v in dict_val.iteritems():
            set_val.add(k)
            for k1,v1 in v.iteritems():
                set_val.add(k1)
        return set_val

    def calculate_distances(self, N, K):
        print self.graph
        hq = list()
        distances = defaultdict(int)
        vertex_set = set()
        vertex_set = self.add_all(self.graph,vertex_set)
        print vertex_set
        for vertex in vertex_set:
            distances[vertex] = sys.maxint
        distances[K] = 0

        print distances
        entry_lookup = dict()
        for vertex, distance in distances.iteritems():
            entry = [distance, vertex]
            entry_lookup[vertex] = entry
            heapq.heappush(hq, entry)
        print hq   
        print entry_lookup 
        while len(hq) > 0:
            print hq
            print '\n',distances
            current_distance,current_vertex = heapq.heappop(hq)
            print 'current_vertex,current_distance --- ',current_vertex,current_distance            
            for neighbors, neighbors_distance in self.graph[current_vertex].iteritems():
                dist = neighbors_distance + distances[current_vertex]
                print 'neighbors,neighbors_distance --- ',neighbors, neighbors_distance
                print 'dist,distances --- ',dist, distances[neighbors]
                if dist < distances[neighbors]:
                    distances[neighbors] = dist
                    entry_lookup[neighbors][0] = dist
        
        return distances

if __name__ == "__main__":
    a = Solution()
    """
    times = [   [15,8,1],[7,10,41],[7,9,34],[9,4,31],
                [12,13,50],[14,3,52],[4,11,99],[4,7,86],
                [10,13,57],[9,6,10],[1,7,51],[7,15,38],
                [1,9,11],[12,7,94],[9,13,34],[11,7,79],
                [7,6,28],[5,3,34],[2,6,97],[14,1,97],
                [6,10,90],[12,10,37],[13,3,73],[11,14,7],
                [15,1,39],[6,5,90],[13,6,43],[6,9,32],
                [4,6,45],[11,10,2],[2,13,4],[14,15,29],
                [1,14,88],[14,6,19],[6,2,29],[3,14,72],
                [1,15,4],[11,5,2],[6,7,56],[8,7,88],
                [13,14,70],[14,12,58],[14,2,86],[11,3,57],
                [5,2,56],[3,10,26],[2,11,21],[14,5,54],
                [5,12,40],[14,4,81],[15,2,99],[5,7,57],
                [13,12,5],[4,9,60],[12,15,48],[6,14,1],
                [9,7,44],[13,7,69],[5,13,42],[4,1,7],
                [11,9,76],[8,1,76],[5,14,29],[2,3,69],
                [7,3,23],[12,14,28],[11,4,85],[10,1,10],
                [15,12,36],[1,11,69],[15,10,96],[11,13,69],
                [7,12,49],[1,2,95],[6,4,46],[8,12,94],
                [12,4,93],[13,5,31],[12,2,60],[6,1,87],
                [4,14,20],[5,11,89],[4,15,88],[4,10,21],
                [1,6,5],[10,8,26],[8,2,51],[3,15,23],
                [7,2,12],[11,1,47],[2,1,75],[3,8,63],
                [8,10,19],[6,8,18],[4,2,55],[14,11,80],
                [10,3,73],[3,5,22],[12,3,61],[1,13,33],
                [9,3,98],[9,12,69],[15,9,6],[7,13,76],
                [11,12,22],[11,15,51],[13,15,46],[5,10,58],
                [1,10,26],[13,4,85],[7,14,58],[5,8,46],
                [11,6,32],[10,9,41],[9,14,35],[14,13,60],
                [3,9,97],[2,5,39],[7,11,19],[1,12,27],
                [7,5,13],[8,4,34],[9,15,25],[5,1,93],
                [15,13,97],[14,9,35],[8,6,67],[9,5,39],
                [13,11,35],[7,4,21],[12,9,64],[14,8,8],
                [10,12,94],[8,9,76],[8,5,71],[2,9,64],
                [10,14,59],[1,4,74],[7,1,69],[15,5,55],
                [6,15,80],[13,8,84],[8,13,63],[8,3,91],
                [10,4,87],[1,5,39],[8,11,0],[1,3,79],
                [4,5,82],[4,12,87],[3,11,29],[7,8,92],
                [10,7,77],[6,12,42],[13,2,40],[9,10,13],
                [4,13,65],[2,4,34],[3,13,44],[2,14,69],
                [3,4,42],[5,15,98],[14,7,6],[15,3,94],
                [10,2,37],[15,11,7],[9,2,15],[13,9,66],
                [4,8,83],[8,15,23],[13,1,50],[6,13,57],
                [2,10,37],[10,6,38],[2,7,45],[9,8,8],
                [3,12,28],[3,2,83],[2,12,75],[1,8,91],
                [4,3,70],[12,6,48],[3,1,13],[5,6,42],
                [6,11,96],[3,6,22],[15,6,34],[11,8,43],
                [15,7,40],[9,11,57],[11,2,11],[2,8,22],
                [9,1,73],[2,15,40],[12,11,10],[15,4,78],
                [12,8,75],[10,15,37],[13,10,44],[8,14,33],
                [3,7,82],[5,4,46],[12,5,79],[15,14,43],
                [10,5,65],[5,9,34],[12,1,54],[6,3,16],
                [14,10,83],[10,11,67]
            ]
    """
    times = [('U','V',2), ('U','W',5), ('U','X',1),
             ('V','U',2), ('V','X',2), ('V','W',3), 
             ('W','V',3), ('W','U',5), ('W','X',3), ('W','Y',1), ('W','Z',5), 
             ('X','U',1), ('X','V',2), ('X','W',3), ('X','Y',1), 
             ('Y','X',1), ('Y','W',1), ('Y','Z',1), 
             ('Z','W',5), ('Z','Y',1)
            ]
    print a.networkDelayTime(times,15,'X')