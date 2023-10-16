from flask import Flask, render_template, send_from_directory, jsonify
import os
app = Flask(__name__)

jobs = [
  {
    'id':1,
    'title': "Data Analyst",
    'location': "New York",
    'salary': "$100,000"
  },
  {
    'id':2,
    'title': "Data Scientist",
    'location': "Delhi",
    'salary': "$150,000"
  },
  {
    'id':3,
    'title': "Data Engineer",
    'location': "San Francisco",
    'salary': "$200,000"
  },
  {
    'id':4,
    'title': "Full Stack Developer",
    'location': "Berlin",
    'salary': "$180,000"
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=jobs)

@app.route("/jobs")
def list_jobs():
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)