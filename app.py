from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<body>
    <h2>Upload File</h2>
    <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML_FORM

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    return f"File '{file.filename}' uploaded successfully!"
    
app.run(debug=True)
