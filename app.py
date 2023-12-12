from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="12345678",
        database="AstronomyAppDB"
    )
    return conn

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()  # Cambiado de 'episodes' a 'users'
    cursor.close()
    conn.close()

    users_list = []
    for user in users:
        user_data = {
            'UserID': user[0],
            'Username': user[1],
            'Email': user[2],
            'VerificationStatus': user[3],
            'NASA_API_Key': user[4],
            'CreatedAt': user[5],
            'UpdatedAt': user[6]
        }
        users_list.append(user_data)

    return render_template('users.html', users=users_list)

@app.route('/preferences', methods=['GET'])
def get_preferences():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM UserPreferences")
    preferences = cursor.fetchall()
    cursor.close()
    conn.close()

    preferences_list = []
    for preference in preferences:
        preference_data = {
            'PreferenceID': preference[0],
            'UserID': preference[1],
            'FrequencyPreference': preference[2],
            'TimingPreference': preference[3],
            'ReceiveEmailAlerts': preference[4],
            'CreatedAt': preference[5],
            'UpdatedAt': preference[6]
        }
        preferences_list.append(preference_data)

    return render_template('preferences.html', preferences=preferences_list)

if __name__ == '__main__':
    app.run(debug=True)
