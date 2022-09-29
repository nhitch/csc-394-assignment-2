from flask import Flask, render_template, url_for
from flask import request, redirect, session
import os
import psycopg2

hw3 = Flask(__name__)
conn = psycopg2.connect(
        host="db-hw3.co9ywatzeczd.us-east-2.rds.amazonaws.com",
        database="postgres",
        user="postgres",
        password="sickntired")

@hw3.route('/')
def main():
    conn = psycopg2.connect(
    host="db-hw3.co9ywatzeczd.us-east-2.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password="sickntired")
    cur = conn.cursor()
    cur.execute('SELECT VERSION();')
    stringA = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('hw3.html', data = stringA)

if(__name__ == "__main__"):
    hw3.run()
