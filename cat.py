from py2neo import Graph, Node, Relationship

# Connect to the Neo4j database
graph = Graph(password="123456789")

query = """
MERGE (s:Entity {name: 'Simpa'})
MERGE (c:Category {name: 'Cat'})
MERGE (s)-[:IS_A]->(c)
MERGE (milk:Item {name: 'Milk'})
MERGE (salmon:Item {name: 'Salmon fish'})
MERGE (c)-[:LIKES]->(milk)
MERGE (c)-[:LIKES]->(salmon)
MERGE (c)-[:SITS_ON]->(:Furniture {name: 'carpet'});
"""

quer2="""
MERGE (simpa:Entity {name: 'Simpa'})
MERGE (birdAnimal:Animal {name: 'Killdeer', fur: true})
MERGE (simpa)-[:CAUGHT]->(birdAnimal)
MERGE (c:Category {name: 'Cat'})
MERGE (birdCategory:Category {name: 'Bird'})
MERGE (mammalCategory:Category {name: 'Mammal'})
MERGE (c)-[:IS_A]->(mammalCategory)
MERGE (birdCategory)-[:IS_A]->(mammalCategory)
MERGE (birdAnimal)-[:IS_A]->(birdCategory)
MERGE (birdAnimal)-[:HAS]->(beak:Feature {name: 'Long and thin beak'})
MERGE (birdAnimal)-[:HIDING]->(curtain:Location {name: 'Curtain'})
MERGE (birdAnimal)-[:HIDING]->(window:Location {name: 'Window'});

"""
graph.run(quer2)