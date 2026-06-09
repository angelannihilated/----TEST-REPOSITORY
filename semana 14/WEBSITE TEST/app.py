from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/Users/inmari/Documents/GitHub/[+] TEST REPOSITORY/semana 14/WEBSITE TEST/sand.html')  # ← Serves HTML + static files automatically!

if __name__ == '__main__':
    app.run(debug=True)  # Run locally at http://localhost:5000