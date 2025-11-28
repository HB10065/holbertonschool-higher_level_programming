#!/usr/bin/python3
'''
Module Doc
'''
import MySQLdb
import sys


if __name__ == '__main__':
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_user,
        passwd=mysql_pass,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute('''
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    ''', (state_name,))

    results = cursor.fetchall()

    city_names = [row[0] for row in results]
    print(', '.join(city_names))

    cursor.close()
    db.close()
