#!/usr/bin/env python3

import psycopg2

con = psycopg2.connect(database='news')

select_stmt_1 = """
    SELECT articles.title, COUNT(*) AS num
    FROM articles, log
    WHERE log.path = '/article/' || articles.slug
        AND log.status like '%200%'
    GROUP BY  articles.title
    ORDER BY num DESC
    LIMIT 3;
"""

select_stmt_2 = """
    SELECT authors.name, COUNT(*) AS num
    FROM authors, articles, log
    WHERE log.path = '/article/' || articles.slug
        AND log.status LIKE '%200%'
        AND articles.author = authors.id
    GROUP BY authors.name
    ORDER BY num DESC
"""

select_stmt_3 = """
    SELECT to_char(date_trunc('day', time), 'FMMonth DD, YYYY') AS day, ROUND(((COUNT(CASE WHEN status = '404 NOT FOUND' THEN status END)::numeric / COUNT(status)::numeric) * 100), 2) AS errorPerc
    FROM log
    GROUP BY day
    HAVING (ROUND(((COUNT(CASE WHEN status = '404 NOT FOUND' THEN status END)::numeric / COUNT(status)::numeric) * 100), 2)) > 1.00
"""

with con:

    cur = con.cursor()
    cur.execute(select_stmt_1)

    rows = cur.fetchall()

    print('\n1. What are the most popular three articles of all time?\n ')
    for row in rows:
        print('    - "' + row[0] + '" - ' + str(row[1]) + " views")
    
    cur.close()

    cur = con.cursor()
    cur.execute(select_stmt_2)

    rows = cur.fetchall()

    print('\n2. Who are the most popular article authors of all time?\n ')
    for row in rows:
        print('    - ' + row[0] + ' - ' + str(row[1]) + " views")

    cur.close()

    cur = con.cursor()
    cur.execute(select_stmt_3)

    rows = cur.fetchall()

    print('\n3. On which days did more than 1% of requests lead to errors?\n ')
    for row in rows:
        print('    - ' + row[0] + ' - ' + str(row[1]) + "% errors")




