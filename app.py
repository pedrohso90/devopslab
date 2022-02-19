from flask import Flask, request, render_template
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def my_index():
    return render_template('index.html')

@app.route("/soma")
def soma_valores():
    x=10+10
    return "Sua soma de 10+10="+str(x)

@app.route("/form", methods=['GET','POST'])
def insert_user():
    if request.method == "POST":
        user = request.form["user"]
        email = request.form["email"]
        processed_user = user.upper()
        processed_email = email.upper()

        connection = psycopg2.connect(user="user_heroku",
                                      password="pass_heroku",
                                      host="host_heroku",
                                      port="5432",
                                      database="name_heroku")
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO customers (username, email) VALUES (%s,%s)"""
        record_to_insert = (processed_user, processed_email)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

        if connection:
            cursor.close()
            connection.close()

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
