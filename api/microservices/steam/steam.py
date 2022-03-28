"""
Main module of the server file
"""

# 3rd party moudles
from re import template
from flask import render_template
import connexion
from microservices.reviews.reviews import review_by_id

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

import users_pb2
from users_pb2_grpc import UsersStub


#from ..reviews import reviews_pb2

import reviews



# Create the Steam application instance?
app = connexion.App(__name__, specification_dir="./")

# read the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")

class SteamService():

    def Steam():

    def getReviewByID(id):
        return review_by_id(id)
    
    
    
# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


if __name__ == "__main__":
    getReviewByID(883710)
    app.run()
