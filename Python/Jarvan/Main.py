#from neo4j import GraphDatabase
import tensorflow as tf
import numpy as np
from tensorflow import keras

"""
uri = "bolt://localhost:7687"  # URI do banco de dados Neo4j
user = "neo4j"  # Nome de usuário
password = "Oli81877"  # Senha

driver = GraphDatabase.driver(uri, auth=(user, password))

with driver.session() as session:
    result = session.run("MATCH (n) RETURN n")
    for record in result:
        print(record)
        
driver.close()

"""