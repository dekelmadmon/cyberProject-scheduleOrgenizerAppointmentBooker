import json
import datetime
from flask import Flask, render_template, request, make_response
import sqliteDBModule as DBM

app = Flask(__name__)

DB = DBM.Database()


@app.route('/main')
def main_page():
    return render_template('main.html')


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/login-page')
def login_page():
    return render_template("login.html")


@app.route('/sign-in-page')
def sign_in_page():
    return render_template("sign_in.html")


@app.route('/api/save-activity', methods=["POST"])
def post_new_activity():
    data = request.data.decode('utf-8')
    json_data = json.loads(data)
    return json_data, 200


@app.route('/api/sign-in', methods=["POST"])
def sign_in_info():
    data = request.data.decode('utf-8')
    json_data = json.loads(data)
    username = json_data["username"]
    email = json_data['email']
    password = json_data['password']
    if DB.sign_in(username, email, password):
        return '', 200
    else:
        return "Invalid credentials", 401


@app.route('/api/login', methods=["POST"])
def login_info():
    data = request.data.decode('utf-8')
    json_data = json.loads(data)
    email = json_data['email']
    password = json_data['password']

    if DB.login(email, password):
        return '', 200
    else:
        return "Invalid credentials", 401


@app.route('/update_schedule_dates', methods=["POST"])
def update_dates():
    try:
        data = request.data.decode('utf-8')
        json_data = json.loads(data)
        last_sunday = last_sunday_date()
        response_data = (str(last_sunday + datetime.timedelta(json_data['factor'] - 1)))
        this_date = json.dumps({"data": response_data})

        return make_response(this_date, 200)
    except json.JSONDecodeError:
        return make_response(json.dumps({"error": "Invalid JSON data"}), 400)
    except KeyError:
        return make_response(json.dumps({"error": "Missing key in JSON data"}), 400)


def last_sunday_date():
    today = datetime.date.today()
    days_since_sunday = 6 - today.weekday()
    last_sunday = today - datetime.timedelta(days=days_since_sunday)
    return last_sunday


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80, debug=True)