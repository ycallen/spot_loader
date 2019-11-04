from rdflib.plugins.sparql.parser import parseQuery, parseUpdate
from rdflib.plugins.sparql.algebra import translateQuery, translateUpdate
from pprint import  pprint

queryString = '''select ?edu ?eduLabel
        where
        {
            Q567 wdt:P69 ?edu.
            ?edu wdt:P31 wd:Q3918         	
        }'''
parsed = parseQuery(queryString)
pprint(parsed)