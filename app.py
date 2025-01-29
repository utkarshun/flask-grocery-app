import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "abcdegfg123"
app.config['SESSION_COOKIE_NAME'] = "myCOOKIE_MONster528"


@app.route("/",methods=["POST","GET"])
def index():
    # Store items in session if not already set
    if 'all_items' not in session or 'shopping_items' not in session:
        session['all_items'], session['shopping_items'] = get_db()
    
    return render_template('index.html', all_items=session['all_items'], shopping_items=session['shopping_items'])


@app.route('/add_items', methods=["POST"])
def add_items():
    # Add selected item to shopping list
    shopping_list = session.get('shopping_items', [])
    item_to_add = request.form.get("select_items")
    
    if item_to_add and item_to_add not in shopping_list:
        shopping_list.append(item_to_add)
        session['shopping_items'] = shopping_list  # Save back to session
    
    return render_template('index.html', all_items=session['all_items'], shopping_items=session['shopping_items'])


@app.route('/remove_items', methods=["POST"])
def remove_items():
    checked_boxes = request.form.getlist("check")
    shopping_list = session.get('shopping_items', [])
    
    for item in checked_boxes:
        if item in shopping_list:
            shopping_list.remove(item)
    
    session['shopping_items'] = shopping_list  # Save updated list to session
    return render_template('index.html', all_items=session['all_items'], shopping_items=session['shopping_items'])


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('grocery_list.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM groceries')
        all_data = cursor.fetchall()

        # Extract only grocery names
        all_items = [val[1] for val in all_data]

        # Randomly select 5 shopping items
        shopping_list = all_items.copy()
        random.shuffle(shopping_list)
        shopping_list = shopping_list[:5]

    return all_items, shopping_list  # Return both lists


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
