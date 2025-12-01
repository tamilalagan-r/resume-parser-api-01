from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "API Running Successfully"}

@app.route("/resume", methods=["POST"])
def parse_resume():
    return {"status": "resume parsing working"}

if __name__ == "__main__":
    app.run(debug=True)
