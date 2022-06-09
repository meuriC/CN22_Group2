import connexion
from yaml import Loader, load
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
import json
from flask import jsonify
from flask import redirect

# create the application instance
options = {
    "swagger_ui_config": {
        #"oauth2RedirectUrl": "http://localhost:5000/ui/oauth2-redirect.html",
        "oauth2RedirectUrl": "http://steamreviews.sytes.net/ui/oauth2-redirect.html",
    }
}
app = connexion.App(__name__, specification_dir="./", options=options)
swagger_yml = load(open("swagger.yaml", 'r'), Loader=Loader)

swaggerui_blueprint = get_swaggerui_blueprint(
    "/ui",
    "swagger.yaml",
    config={
        #'spec': swagger_yml, 'oauth2RedirectUrl': "http://localhost:5000/ui/oauth2-redirect.html"},
        'spec': swagger_yml, 'oauth2RedirectUrl': "http://steamreviews.sytes.net/ui/oauth2-redirect.html"},
    oauth_config={
        'clientId': "sUnKWfmlaywQm64EtEZpioz5uRK5GAzc",
        "usePkceWithAuthorizationCodeGrant": True}
)
app.app.register_blueprint(swaggerui_blueprint)

CORS(app.app)
app.app.config['SESSION_TYPE'] = 'memcached'
app.app.config['SECRET_KEY'] = 'secretKey safe'
oauth = OAuth(app.app)
auth0 = oauth.register(
    'auth0',
    client_id='sUnKWfmlaywQm64EtEZpioz5uRK5GAzc',
    client_secret='AbC4iHv7TlkNvKXpxEv88dRBmcYu6MykpyN8SBsIKIC7G5pOegcySMEgTDW7vDLd',
    api_base_url='https://dev-p3dnwrxe.us.auth0.com',
    access_token_url='https://dev-p3dnwrxe.us.auth0.com/oauth/token',
    authorize_url='https://dev-p3dnwrxe.us.auth0.com/authorize',
    response_type='code',
    client_kwargs={
        'scope': 'admin user'
    },
)

# swagger.yml file to configure the endpoints
app.add_api("swagger.yaml")


@app.app.route('/login')
def call():
    #return auth0.authorize_redirect(redirect_uri="http://localhost:5000/ui/callback",  audience='https://cn22group2/')
    return auth0.authorize_redirect(redirect_uri="http://steamreviews.sytes.net/ui/callback",  audience='https://cn22group2/')


@app.app.route('/callback')
def callback_handling():
    return jsonify(auth0.authorize_access_token())


@app.app.route('/health')
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(debug=True)
