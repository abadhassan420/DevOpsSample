from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello World</title>
        <script>
            function showMessage() {
                alert("Hello, World!");
            }
        </script>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <button onclick="showMessage()">Click me</button>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
