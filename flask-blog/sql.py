import sqlite3

with sqlite3.connect("blog.db") as connection:
	c = connection.cursor()

	c.execute("DROP TABLE if exists posts")
	c.execute("""CREATE TABLE posts(title text, post text)""")



	#dummy data
	posts = [
	("Russian currency falls in value", "We have been reporting for several months that falling oil prices would put pressure on russia's ability to maintain its balance of payments."),
	("UK Chancellor announces further cuts","George Osborne announced in his latest budget that the elderly would have to face pension cuts of up to 40%."),
	("Belfast economic growth set for boost","Reduction of corporation tax has resulted in significant inwards investment from global companies"),
	]

	for post in posts:
		c.executemany("INSERT INTO posts(title,post) VALUES(?,?)",(post,))

	c.close()