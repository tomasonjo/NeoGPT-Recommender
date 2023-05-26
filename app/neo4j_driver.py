import os
from neo4j import GraphDatabase
import streamlit as st

host = st.secrets.db_credentials.NEO4J_URL
user = st.secrets.db_credentials.NEO4J_USER
password = st.secrets.db_credentials.NEO4J_PASS
driver = GraphDatabase.driver(host, auth=(user, password))


def run_query(query, params={}):
    with driver.session() as session:
        result = session.run(query, params)
        return [r.values()[0] for r in result][:50]
        

# if __name__ == '__main__':
#     print(run_query("""
#     MATCH (m:Movie {title:"Copycat"})<-[:ACTED_IN]-(a)
#     RETURN {actor: a.name} AS result;
#     """))
