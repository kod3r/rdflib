"""

RDFLib Graphs (and Resources) can be "sliced" with [] syntax

This is a short-hand for iterating over triples

Combined with SPARQL paths (see foafpaths.py) - quite complex queries
can be realised

"""

from rdflib import Graph, RDF
from rdflib.namespace import FOAF

graph = Graph()

graph.load("foaf.rdf")

for person in graph[: RDF.type : FOAF.Person]:
    
    friends = list(graph[person:FOAF.knows * '+'/FOAF.name])
    if friends: 
        print "%s's circle of friends:"%graph.value(person, FOAF.name)
        for name in friends:
            print name
    
