import networkx as nx
import matplotlib.pyplot as plt
import json


G = nx.DiGraph()
s = """
{
    "info": "0xa",
    "children": [
        {
            "info": "0xaa",
            "children": [
                {
                    "info": "0xaaa",
                    "children": []
                },
                {
                    "info": "0xaaa1",
                    "children": []
                }
            ]
        },
        {
            "info": "0xbb",
            "children": [
                {
                    "info": "0xbbb",
                    "children": []
                }
            ]
        }
    ]
}
"""


def get_plot(node_obj, children):
    if children is None:
        return

    for child in children:
        info = child["info"]
        nodes.append(info)
        pair_obj = (node_obj, info)
        edges.append(pair_obj)

        get_plot(child["info"], child["children"])

    return


tree = json.loads(s)
root = tree["info"]
nodes = []
edges = []
nodes.append(root)
get_plot(root, tree["children"])

G.add_edges_from(edges)
G.add_nodes_from(nodes)

nx.draw(G, with_labels=True)
plt.savefig("foo.png")
