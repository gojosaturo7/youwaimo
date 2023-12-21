from py2neo import *

# Open connection
graph = Graph("bolt://localhost:7687",auth=("neo4j", "password"))

# Create nodes
person1 = Node("Person", name="John Doe", age=30)
person2 = Node("Person", name="Jane Smith", age=25)
person3 = Node("Person", name="Bob Tabor", age=22)

# Read nodes
cypher_query = "MATCH (p:Person) RETURN p"
people = graph.run(cypher_query)

# Use the match function to find relationships of type "KNOWS"
relationships = graph.match(r_type="KNOWS")
for r in relationships:
    print(r)

# Create a relationship label
KNOWS = Relationship.type("KNOWS")

# Use relationship label
ab = KNOWS(person1, person2)
bc = KNOWS(person2, person3)

# Create relationship in graph
graph.create(ab)
graph.create(bc)

# Deleting a node
node_to_delete = graph.nodes.get(5)
graph.delete(node_to_delete)

# Delete all nodes
delete_query = "MATCH (n) DETACH DELETE n;"
graph.run(delete_query)
