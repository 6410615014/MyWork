from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users_database = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone_num = request.form.get('phone_num')
        email = request.form.get('email')
        username = request.form.get('username')
        users_database[username] = {'First name':first_name,'Last name':last_name,'Phone number':phone_num,"E-mail":email}
        return redirect(url_for('user_home', username=username))
    return render_template('register.html')

@app.route('/user/<username>')
def user_home(username):
    user_data = users_database.get(username, {})
    return render_template('user_home.html', username=username, user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)
