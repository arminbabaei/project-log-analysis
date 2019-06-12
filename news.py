#!/usr/bin/env python3

import psycopg2

def db_connect():
    con = psycopg2.connect(database='news')
    cur = con.cursor()
    return con, cur

def execute_query(query, cur):
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def print_top_articles(cur):
    query = """
    SELECT articles.title, COUNT(*) AS num
    FROM articles, log
    WHERE log.path = '/article/' || articles.slug
        AND log.status like '%200%'
    GROUP BY  articles.title
    ORDER BY num DESC
    LIMIT 3;
    """
    results = execute_query(query, cur)

    print('\n1. What are the most popular three articles of all time?\n ')
    for result in results:
        print('    - "' + result[0] + '" - ' + str(result[1]) + " views")  

def print_top_authors(cur): 
    query = """
    SELECT authors.name, COUNT(*) AS num
    FROM authors, articles, log
    WHERE log.path = '/article/' || articles.slug
        AND log.status LIKE '%200%'
        AND articles.author = authors.id
    GROUP BY authors.name
    ORDER BY num DESC
    """
    results = execute_query(query, cur)

    print('\n2. Who are the most popular article authors of all time?\n ')
    for result in results:
        print('    - ' + result[0] + ' - ' + str(result[1]) + " views")

def print_errors_over_one(cur):
    query = """
    SELECT to_char(date_trunc('day', time), 'FMMonth DD, YYYY') AS day, ROUND(((COUNT(CASE WHEN status = '404 NOT FOUND' THEN status END)::numeric / COUNT(status)::numeric) * 100), 2) AS errorPerc
    FROM log
    GROUP BY day
    HAVING (ROUND(((COUNT(CASE WHEN status = '404 NOT FOUND' THEN status END)::numeric / COUNT(status)::numeric) * 100), 2)) > 1.00
    """
    results = execute_query(query, cur)

    print('\n3. On which days did more than 1% of requests lead to errors?\n ')
    for result in results:
        print('    - ' + result[0] + ' - ' + str(result[1]) + "% errors")


if __name__ == '__main__':
    cur = None
    con = None
    try:
        con, cur = db_connect()
        print_top_articles(cur)
        print_top_authors(cur)
        print_errors_over_one(cur)
    finally:
        if cur is not None:
            cur.close()
        if con is not None:
            con.close()

