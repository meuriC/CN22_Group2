import os
import re


import json
from six.moves.urllib.request import urlopen

from jose import jwt

from flask import Flask, jsonify, request, url_for, abort, g
from flask import redirect
from six.moves.urllib.parse import urlencode

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from users_pb2_grpc import UsersStub
from users_pb2 import *

AUTH0_DOMAIN = 'dev-p3dnwrxe.us.auth0.com'
API_AUDIENCE = 'https://cn22group2/'
ALGORITHMS = ["RS256"]

users_host = os.getenv("USERS_HOST", "localhost")
users_channel = grpc.insecure_channel(f"{users_host}:50052")
users_client = UsersStub(users_channel)
jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
jwks = json.loads(jsonurl.read())


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


def verify_token(access_token) -> dict:

    unverified_header = jwt.get_unverified_header(access_token)
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                access_token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer="https://"+AUTH0_DOMAIN+"/"
            )
        except jwt.ExpiredSignatureError:
            handle_auth_error(AuthError({"code": "token_expired",
                                         "description": "token is expired"}, 401))
        except jwt.JWTClaimsError:
            handle_auth_error(AuthError({"code": "invalid_claims",
                                         "description":
                                         "incorrect claims,"
                                         "please check the audience and issuer"}, 401))
        except Exception:
            handle_auth_error(AuthError({"code": "invalid_header",
                                         "description":
                                         "Unable to parse authentication"
                                         " token."}, 401))
    unverified_claims = jwt.get_unverified_claims(access_token)
    if unverified_claims.get("scope") and unverified_claims.get("sub"):
        token_scopes = unverified_claims["scope"].split()
        return {'sub': unverified_claims.get("sub"), 'scope': token_scopes}
    handle_auth_error(AuthError({"code": "invalid_header",
                                 "description":
                                     "Unable to parse authentication"
                                     " token."}, 401))


def logoutUser():
    return redirect('https://dev-p3dnwrxe.us.auth0.com/v2/logout')


def loginUser():
    s = request.url_root + "login"
    return redirect(s)


def createUser(UserItem):
    request = CreateUserRequest(
        user_language=UserItem["language"], user_name=UserItem["username"])
    response = users_client.CreateUser(request)
    return {"user_name": response.user_name, "user_id": response.user_id}


def getUser(user_id):
    request = IdRequest(user_id=user_id)
    response = users_client.GetUserById(request)
    return {"user_name": response.user_name, "user_id": response.user_id, "user_language": response.user_language, "user_num_reviews": response.user_num_reviews, "user_num_games_owned": response.user_num_games_owned}


def deleteUserAccount(user_id):
    request = IdRequest(user_id=user_id)
    return users_client.DeleteUserById(request).deleted


def createReview(user_id, app_id, ReviewsItem):
    request = CreateReviewRequest(
        app_id=app_id, review=ReviewsItem["review"], recommended=ReviewsItem["recommended"], user_id=user_id)
    response = users_client.PostReview(request)
    return {"user_id": response.author_steam_id, "app_id": response.app_id, "review": response.review, "recommended": response.recommended}
