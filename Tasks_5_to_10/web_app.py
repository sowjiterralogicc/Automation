from flask import Flask, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key

# Simulated user data (for demonstration purposes)
users = {
    'user1': {'username': 'sowji', 'password': 'Ammu1998@17'},
    'user2': {'username': 'Sowji1', 'password': 'sowjanya@26'},
}

# Simulated user authentication function
def is_user_authenticated():
    return 'user_id' in session

from flask import render_template

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user['password'] == password:
            session['user_id'] = username
            return redirect(url_for('dashboard'))

    return render_template('login.html')


# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return 'Logged out successfully.'


# Dashboard route (requires authentication)
@app.route('/dashboard')
def dashboard():
    if is_user_authenticated():
        username = session['user_id']
        return render_template('dashboard.html', is_authenticated=True, username=username)
    else:
        return render_template('dashboard.html', is_authenticated=False)

# Decorator for authentication
def login_required(func):
    def decorated_function(*args, **kwargs):
        if not is_user_authenticated():
            return redirect(url_for('login'))
        return func(*args, **kwargs)

    return decorated_function
# Protected route (requires authentication)
@app.route('/protected')
@login_required
def protected():
    return 'This is a protected route. Only authenticated users can access it.'
@app.route('/')
def home():
    return 'Welcome to the home page!'
if __name__ == '__main__':
    app.run(debug=True)
