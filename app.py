from flask import Flask, render_template, url_for, json,request
import os
#from flask_mysqldb import MySQL
#from wtforms import Form, StringField, TextAreaField, PasswordField, validators
#from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

# Config MySQL
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = '123456'
#app.config['MYSQL_DB'] = 'myflaskapp'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
#mysql = MySQL(app)

#Articles = Articles()

# Index
@app.route('/')
def index():
    return render_template('home.html')


# About
@app.route('/about')
def about():
    return render_template('about.html')


# Articles
@app.route('/articles')
def articles():
    site_root=os.path.realpath(os.path.dirname(__file__))
    json_url=os.path.join(site_root,"temp1.json")
    data=json.loads(json_url)
    return render_template('articles.html',ctrsuccess=data)
    # Create cursor
    #cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")

    #articles = cur.fetchall()

    #if result > 0:
        #return render_template('articles.html', articles=articles)
    #else:
        #msg = 'No Articles Found'
        #return render_template('articles.html', msg=msg)
    # Close connection
    #cur.close()


#Single Article





if __name__ == '__main__':
    app.run(debug=True)
