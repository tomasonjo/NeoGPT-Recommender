examples = """
# I have already watched Top Gun
MATCH (u:User {id: $userId}), (m:Movie {title:"Top Gun"})
MERGE (u)-[:WATCHED]->(m)
RETURN distinct {answer: 'noted'} AS result
# I like Top Gun
MATCH (u:User {id: $userId}), (m:Movie {title:"Top Gun"})
MERGE (u)-[:LIKE_MOVIE]->(m)
RETURN distinct {answer: 'noted'} AS result
# What is a good comedy?
MATCH (u:User {id:$userId}), (m:Movie)-[:IN_GENRE]->(:Genre {name:"Comedy"})
WHERE NOT EXISTS {(u)-[:WATCHED]->(m)}
RETURN {movie: m.title} AS result
ORDER BY m.imdbRating DESC LIMIT 1
# Who played in Top Gun?
MATCH (m:Movie)<-[r:ACTED_IN]-(a)
RETURN {actor: a.name, role: r.role} AS result
# What is the plot of the Copycat movie?
MATCH (m:Movie {title: "Copycat"})
RETURN {plot: m.plot} AS result
# Did Luis Guzmán appear in any other movies?
MATCH (p:Person {name:"Luis Guzmán"})-[r:ACTED_IN]->(movie)
RETURN {movie: movie.title, role: r.role} AS result
# Do you know of any matrix movies?
MATCH (m:Movie)
WHERE toLower(m.title) CONTAINS toLower("matrix")
RETURN {movie:m.title} AS result
# Which movies do I like?
MATCH (u:User {id: $userId})-[:LIKE_MOVIE]->(m:Movie)
RETURN {movie:m.title} AS result
# Recommend a movie
MATCH (u:User {id: $userId})-[:LIKE_MOVIE]->(m:Movie)
MATCH (m)<-[r1:RATED]-()-[r2:RATED]->(otherMovie)
WHERE r1.rating > 3 AND r2.rating > 3 AND NOT EXISTS {(u)-[:WATCHED|LIKE_MOVIE|DISLIKE_MOVIE]->(otherMovie)}
WITH otherMovie, count(*) AS count
ORDER BY count DESC
LIMIT 1
RETURN {recommended_movie:otherMovie.title} AS result
"""
