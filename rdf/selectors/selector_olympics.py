from SPARQLWrapper import SPARQLWrapper, JSON
import pathlib
from urllib.request import urlopen

#sparql = SPARQLWrapper("https://linkeddata1.calcul.u-psud.fr/sparql")
#sparql = SPARQLWrapper("http://dbpedia.org/sparql")

#be patient it takes at least a minute to load dataset and then run the program

sparql = SPARQLWrapper("http://127.0.0.1:3030/ds")
sparql.setQuery("""
    PREFIX walls: <http://wallscope.co.uk/ontology/olympics/>
    PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
    SELECT DISTINCT ?instance ?name
    WHERE {
        ?instance walls:athlete ?athlete;
        walls:medal <http://wallscope.co.uk/resource/olympics/medal/Gold> .
        ?athlete rdfs:label ?name .
    } """)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

l = []

#print(results)
for result in results["results"]["bindings"]:
    #l.append(result["property"]["value"])
    print('%s : %s' % (result["instance"]["value"], result["name"]["value"]))

print("\ndistinct properties\n")
l = list(set(l))
print(*l, sep = "\n")