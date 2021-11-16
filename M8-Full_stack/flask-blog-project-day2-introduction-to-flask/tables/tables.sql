-- create a blog table
CREATE TABLE IF NOT EXISTS
	author(
		id INTEGER PRIMARY KEY  GENERATED ALWAYS AS IDENTITY,
		name VARCHAR(200) NOT NULL,
		last_name VARCHAR(200) NOT NULL,
		avatar TEXT NOT NULL,
		bio TEXT NOT NULL,
		linkedin_link TEXT,
		twitter_link TEXT,
		github_link TEXT
	);
CREATE TABLE IF NOT EXISTS
	blogs(
		blog_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
		title VARCHAR(150) NOT NULL,
		slug  VARCHAR(200) NOT NULL UNIQUE,
		content TEXT NOT NULL,
		cover_url TEXT NOT NULL,
		category VARCHAR(100) NOT NULL,
		author_id INTEGER REFERENCES author(id) NOT NULL,
		is_published BOOLEAN DEFAULT FALSE,
		created_at TIMESTAMPTZ DEFAULT NOW(),
		published_at TIMESTAMPTZ DEFAULT NOW(),
		updated_at TIMESTAMPTZ DEFAULT NOW()
	);

INSERT INTO author(name,
				  last_name,
				   avatar,
				   bio)
VALUES('NishithReddy',
	   'Cherukuru',
	   'Nissy.png',
		'Student @ Strive School')
RETURNING *;

INSERT INTO
		blogs(
			title,
			slug,
			content,
			cover_url,
			category,
			author_id,
			is_published)
VALUES(
		'useEFFECT VS useLayoutEffect',
		'useeffect-vs-uselayouteffect',
		'I also a big extreme sports enthusiast. When Im not hanging out with my family or at the computer you can find me cruising around on my onewheel or hitting the slopes on my snowboard when its cold.',
		'https://kentcdodds.com/',
		'REACT',
		1,
		true)


select blogs.id as blog_id,
		blogs.title,
		blogs.cover_url,
		a.last_name,
		a.name,
		a.avatar
from blogs
	INNER JOIN author a
		on a.id =blogs.author_id  WHERE a.id=1; -- whenever author.id is equal to blog.author_id merge them and get it together
		