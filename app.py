from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "API is Live"

@app.route("/parse-resume", methods=["POST"])
def parse_resume():
    uploaded_file = request.files.get("file")

    if not uploaded_file:
        return jsonify({"error": "No file sent"}), 400

    # Process file here...
    return jsonify({"status": "success", "filename": uploaded_file.filename})

if __name__ == "__main__":
    app.run()
