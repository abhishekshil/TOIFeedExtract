from flask import Flask, render_template, flash, redirect, url_for, request
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
    # Create cursor
    #cur = mysql.connection.cursor()

    # Get articles
    #result = cur.execute("SELECT * FROM articles")

    #articles = cur.fetchall()

    #if result > 0:
        return render_template('articles.html', articles=articles)
    #else:
        #msg = 'No Articles Found'
        #return render_template('articles.html', msg=msg)
    # Close connection
    #cur.close()


#Single Article
@app.route('/article/<string:id>/')
def article(id):
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone()

    return render_template('article.html', article=article)




if __name__ == '__main__':
    app.run(debug=True)
