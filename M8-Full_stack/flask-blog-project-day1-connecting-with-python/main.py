from db.connect import connect_to_db
from slugify import slugify



connection = connect_to_db()

cursor = connection.cursor()


# get blogs

# get_blog_query = "SELECT * FROM blogs;"

# cursor.execute(get_blog_query)

# result = cursor.fetchall()

# print(len(result))




def insert_blog(title,content,cover_url,category):
    try:
        cursor.execute("""INSERT INTO
	blogs(
		title,
        slug,
		content,
		cover_url,
		category
	)
	VALUES(
		%s,
		%s,
		%s,
		%s,
        %s
        )""",(title,slugify(title),content,cover_url,category))
        connection.commit()
    except Exception as e:
        print(e)



insert_blog("My Github",'Github page','https://github.com/SivareddyBodapati','webpage')