#!/usr/bin/python3
'''
Module Doc
'''
import MySQLdb
import sys


if __name__ == '__main__':

    s_con = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = s_con.cursor()
    cursor.execute('SELECT id, name,  FROM cities'
                   ' ORDER BY cities.id ASC')
    for row in cursor.fetchall():
        print(row)
    cursor.close
    s_con.close
