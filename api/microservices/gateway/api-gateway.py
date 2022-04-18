import connexion
from yaml import Loader, load
from flask_swagger_ui import get_swaggerui_blueprint

# create the application instance
app = connexion.App(__name__, specification_dir="./")
swagger_yml = load(open("swagger.yaml", 'r'), Loader = Loader)

swaggerui_blueprint = get_swaggerui_blueprint("/ui", "swagger.yaml", config = {'spec': swagger_yml})
app.app.register_blueprint(swaggerui_blueprint)

# swagger.yml file to configure the endpoints
app.add_api("swagger.yaml")

if __name__ == "__main__":
    app.run(debug=True)
	
