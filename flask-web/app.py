from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask("app")

    from route import hello_route
    app.register_blueprint(hello_route.hello_bp)

    return app


app = create_app()
# api = Api(app)
# api.add_resource(app_route, '/')
# app.register_blueprint(hello_route)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
