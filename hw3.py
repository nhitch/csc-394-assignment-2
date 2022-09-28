from flask import Flask, render_template
import psycopg2

hw3 = Flask(__name__)

@hw3.route('/')
def main():
    return render_template('hw3.html')

if(__name__ == "__main__"):
    hw3.run()