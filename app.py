from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/buildings")
def get_buildings():
    with open("static/buildings.json", "r") as buildings:
        return buildings.read()


if __name__ == '__main__':
    app.run()
