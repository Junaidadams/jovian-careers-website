from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Cape Town, South Africa",
        "salary": "R15,000",
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Delhi, India",
        "salary": "Rs 16,00,000",
    },
    {
        "id": 3,
        "title": "Frontend Engineer",
        "location": "Remote",
    },
    {   "id": 4,
        "title": "Backend Engineer",
        "location": "San Fransisco, USA",
        "salary": "$14,000",
    }
    
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS,
                           company_name="Jovian")
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run("0.0.0.0", debug = True)

# mailto:hello@jovian.ai?subject=Application for {{jobs['title']}}