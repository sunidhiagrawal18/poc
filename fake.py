from flask import Flask, request, redirect, render_template_string, session, url_for

app = Flask(__name__)
app.secret_key = 'zap_poc_secret_key'

# Fake credentials
VALID_USERNAME = 'admin@fake.com'
VALID_PASSWORD = 'admin'

# Templates
login_page = '''
<!doctype html>
<title>Login</title>
<h2>Login Page</h2>
<form method="post">
  Email: <input type="text" name="username"><br>
  Password: <input type="password" name="password"><br>
  <input type="submit" value="Login">
</form>
'''  # no logout link on login page

home_page = '''
<!doctype html>
<title>Dashboard</title>
<h2>Welcome to the Dashboard</h2>
<p>You are logged in as {{ username }}</p>
<a href="{{ url_for('logout') }}">Logout</a>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == VALID_USERNAME and request.form['password'] == VALID_PASSWORD:
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))
    return render_template_string(login_page)

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template_string(home_page, username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
