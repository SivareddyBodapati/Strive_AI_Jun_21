-- create a blog table

CREATE TABLE IF NOT EXISTS
	blogs(
		blog_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
		title VARCHAR(150) NOT NULL,
		slug  VARCHAR(200) NOT NULL UNIQUE,
		content TEXT NOT NULL,
		cover_url TEXT NOT NULL,
		category VARCHAR(100) NOT NULL,
		is_published BOOLEAN DEFAULT FALSE,
		created_at TIMESTAMPTZ DEFAULT NOW(),
		published_at TIMESTAMPTZ DEFAULT NOW(),
		updated_at TIMESTAMPTZ DEFAULT NOW()
	);



-- insert a record to table


INSERT INTO
	blogs(
		title,
		slug,
		content,
		cover_url,
		category
	)
	VALUES(
		'How to serve a website with flask?',
		'how-to-serve-a-website',
		'Use flask',
		'cover_url.png',
		'python'
	);


-- get all records from a table.
SELECT *
	FROM blogs;


-- get records and change column name on the fly with ALIAS

SELECT
	blog_id AS id,
	title
FROM blogs;


	-- get single record from a table. (returns still array)
SELECT *
	FROM blogs WHERE blog_id=3;

-- get records matching with where clause from a table. (returns still array)
SELECT *
	FROM blogs WHERE is_published=true;


	-- you can chain with AND OR
SELECT *
	FROM blogs WHERE is_published=true AND category ='python';

-- PARTIAL MATCHING with LIKE OPERATOR (includes)
SELECT *
	FROM blogs WHERE title LIKE '%conn%';

-- PARTIAL MATCHING with LIKE OPERATOR (starts with)
SELECT *
	FROM blogs WHERE title LIKE 'H%';

-- PARTIAL MATCHING with LIKE OPERATOR (ends with)

SELECT *
	FROM blogs WHERE category LIKE '%k';

-- update multiple column in a table for a single record

UPDATE
	blogs
		SET 
			content='Use flask to serve a website with python.',
			slug='how-to-serve-a-website-with-flask'
		WHERE blog_id=3;


-- delete singel record from a table.""

DELETE
	FROM
		blogs
	WHERE 
		blog_id=2;