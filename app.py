import os
from flask import Flask, render_template , jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'Juba, South Sudan',
        'salary':  'SSP. 40,00,000'
    },

    {
        'id':2,
        'title':  'Desktop Support',
        'location':  'Torit, South Sudan',
       
    },

    {
        'id':3,
        'title':  'B2B engineer',
        'location':  'ZainTelecom, South Sudan',
        'salary':  'SSP. 150,00,000'
    },

    {
        'id':4,
        'title':  'Frontend Development',
        'location':  'Wfp, South Sudan',
       
    }
]
@app.route("/")
def hello_world():
    return render_template('home.html', 
                            jobs=JOBS,
                            company_name='Ojok') # return "Hello, World!"
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    # return jsonify(JOBS)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's port, default 5000 locally
    app.run(host="0.0.0.0", port=port, debug=True)