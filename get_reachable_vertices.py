import pygfa
import argparse

# cli parser
parser = argparse.ArgumentParser(description="Get the set of reachable vertices starting from one vertex")
parser.add_argument('-f', '--file', metavar='file', type=str, nargs=1, required=True)
parser.add_argument('-v', '--vertex', metavar='vertex', type=str, nargs=1, required=True)
args = parser.parse_args()

# open and process gfa
mygfa = pygfa.gfa.GFA.from_file(args.file[0])

# use the new function to get reachable vertices
print(mygfa.get_reachable_vertices_from(args.vertex[0]))
