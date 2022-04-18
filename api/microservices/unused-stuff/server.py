#!/usr/bin/env python3

import connexion

import encoder


app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Steam Reviews API'})
app.run(port=3200)



# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """


if __name__ == "__main__":
    app.run(debug=True)
