from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title' : "Data Engineer",
    'location' : 'Kampala, Uganda',
    'salary' : 'Ugx. 2M'
  },
  {
    'id': 1,
    'title' : "Data Analyst",
    'location' : 'Kampala, Uganda',
    'salary' : 'Ugx. 1M'
  },
  {
    'id': 1,
    'title' : "Backend Engineer",
    'location' : 'Remote',
    
  },
  {
    'id': 4,
    'title' : "Frontend Engineer",
    'location' : 'Mbarara, Uganda',
    'salary' : 'Ugx. 2.3M'
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='ASU')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
