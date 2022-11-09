from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from config import settings

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/loggin', methods=['POST'])
def initSession():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usersproject')
    data = cur.fetchall()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    for i in range(len(data)):
        if (email in data[i][2]) and (password in data[i][3]):
            return redirect(url_for('profile'))
    return "Error Session"



@app.route('/loggin')
def loggin():
        return render_template('loggin.html')

@app.route('/register', methods=['POST'])
def session():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()

        cur.execute('SELECT * FROM usersproject')
        data = cur.fetchall()
        for i in range(len(data)):
            if (email in data[i][2]):
                return "La cuenta ya existe!"

        cur.execute('INSERT INTO usersproject (fullname, email, password) VALUES (%s,%s,%s)',
        (fullname,email,password))
        mysql.connection.commit()
        return redirect(url_for('loggin'))

        

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.config.from_object(settings['development'])
    app.run()