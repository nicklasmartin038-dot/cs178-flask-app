# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

from dynamoCode import log_activity
from dbCode import (
    get_inventory,
    add_user as add_user_db,
    get_all_users,
    delete_user as delete_user_db,
    update_user as update_user_db,
    search_users_by_genre
)
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Extract form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        genre = request.form['genre']
        
        # Process the data (e.g., add it to a database)
        log_activity("add_user", user_name=name, genre=genre)
        add_user_db(first_name, last_name, genre)
        
        flash('User added successfully! Huzzah!', 'success')  # 'success' is a category; makes a green banner at the top
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('add_user.html')

@app.route('/delete-user',methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        # Extract form data
        first_name = request.form['first_name']
        last_name =request.form['last_name']
        
        # Process the data (e.g., add it to a database)
        # For now, let's just print it to the console
        delete_user_db(first_name, last_name)
        
        flash('User deleted successfully! Hoorah!', 'warning') 
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('delete_user.html')


@app.route('/display-users')
def display_users():
    # hard code a value to the users_list;
    # note that this could have been a result from an SQL query :) 
    users_list = get_all_users()
    return render_template('display_users.html', users=users_list)

@app.route('/inventory')
def inventory():
    items = get_inventory()
    return render_template('inventory.html', items=items)

@app.route('/update-user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        old_first_name = request.form['old_first_name']
        old_last_name = request.form['old_last_name']
        new_first_name = request.form['new_first_name']
        new_last_name = request.form['new_last_name']
        new_genre = request.form['new_genre']

        update_user_db(old_first_name, old_last_name, new_first_name, new_last_name, new_genre)

        flash('User updated successfully!', 'info')
        return redirect(url_for('home'))
    else:
        return render_template('update_user.html')

@app.route('/search-genre', methods=['GET', 'POST'])
def search_genre():
    if request.method == 'POST':
        genre = request.form['genre']
        users_list = search_users_by_genre(genre)
        return render_template('display_users.html', users=users_list)
    else:
        return render_template('search_genre.html')

# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
