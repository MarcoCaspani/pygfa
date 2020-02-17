# ADAPTATION FROM https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/

# A union by rank and path compression

class Subset:

    def __init__(self, id, parent, rank):
        self.id = id
        self.parent = parent
        self.rank = rank
        self.descendants = set([id])

    def print(self):
        print("id:\t" + str(self.id) + \
              "\tparent: " + str(self.parent) + \
              "\trank: " + str(self.rank) + \
              "\tdescendants: " + str(self.descendants))

# returns a new collection of disjoint sets
def new_collection(vertices=None) -> dict:
    collection = dict()
    for v in vertices:
        collection.update({v: Subset(v, v, 0)})
    return collection

# A utility function to find set of an element
# node(uses path compression technique)
def find_set(collection, node) -> str:
    if collection[node].parent != node:
        rep = find_set(collection, collection[node].parent)
        node_descendants = collection[node].descendants

        # path compression
        collection[node].parent = rep
        collection[rep].descendants = collection[rep].descendants.union(node_descendants)
        collection[node].descendants = {}
    return collection[node].parent

# A function that does union of two sets
# of u and v(uses union by rank)
def union(collection, u, v) -> dict:
    u_descendants = collection[u].descendants
    v_descendants = collection[v].descendants

    # Attach smaller rank tree under root
    # of high rank tree(union by Rank)
    if collection[u].rank > collection[v].rank:
        collection[v].parent = u
        collection[u].descendants = collection[u].descendants.union(v_descendants)
        collection[v].descendants = {}
    elif collection[v].rank > collection[u].rank:
        collection[u].parent = v
        collection[v].descendants = collection[v].descendants.union(u_descendants)
        collection[u].descendants = {}
    # If ranks are same, then make one as
    # root and increment its rank by one
    else:
        collection[v].parent = u
        collection[u].rank += 1
        collection[u].descendants = collection[u].descendants.union(v_descendants)
    return collection
