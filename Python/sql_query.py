import psycopg2

connection = psycopg2.connect(host="cool.db.com", database="dbname",
		user="username", password="password", port="5432")
cursor = connection.cursor()

cursor.execute("SELECT t.* FROM things t WHERE t.id=1;")

result = cursor.fetchone()
print(result)