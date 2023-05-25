from neo4j import GraphDatabase
host = "neo4j+s://80a5f8b8.databases.neo4j.io"
username = "neo4j"
password = "N9Jhybir-NaFEsvGXS53X7SthV5wheHDEg7ua7yY-3E"
driver = GraphDatabase.driver(host, auth=(username, password))
try:
    with driver.session() as session:
        # Perform a simple query to test the connection
        result = session.run("RETURN 1")
        print("Connection successful!")
except Exception as e:
    print("Connection failed:", str(e))