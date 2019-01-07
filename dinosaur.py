
from flask import Flask
app = Flask(__name__)
print(app)
print("eggnog")

@app.route("/")
def hello():
    print("always kill hitler")
    return "Hello World!"

@app.route("/dinosaur")
def dinosaur():
    return "Pteradactyls will rule the world"

if __name__ == '__main__':
    app.run()
