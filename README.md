# Armin Babaei
# armin.babaei@gmail.com

# Logs Analysis Project


1. What are the most popular three articles of all time? 

    Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:
```sh
	"Princess Shellfish Marries Prince Handsome" — 1201 views
	"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
	"Political Scandal Ends In Political Scandal" — 553 views
```

2. Who are the most popular article authors of all time? 

    That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

```sh
	Ursula La Multa — 2304 views
	Rudolf von Treppenwitz — 1985 views
	Markoff Chaney — 1723 views
	Anonymous Contributor — 1023 views
```

3. On which days did more than 1% of requests lead to errors? 

    The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson 	for more information about the idea of HTTP status codes.)

	Example:

```sh
	July 29, 2016 — 2.5% errors
```

# Installation


```sh
$ psql -d news -f newsdata.sql
```

```sh
$ pthon new.py
```

```sh
vagrant@vagrant:/vagrant/news$ python news.py

1. What are the most popular three articles of all time?
 
    - "Candidate is jerk, alleges rival" - 338647 views
    - "Bears love berries, alleges bear" - 253801 views
    - "Bad things gone, say good people" - 170098 views

2. Who are the most popular article authors of all time?
 
    - Ursula La Multa - 507594 views
    - Rudolf von Treppenwitz - 423457 views
    - Anonymous Contributor - 170098 views
    - Markoff Chaney - 84557 views

3. On which days did more than 1% of requests lead to errors?
 
    - 17 July     , 2016 - 2.26% errors
```

### Todos

 - Improve SQL queries

License
----

MIT
