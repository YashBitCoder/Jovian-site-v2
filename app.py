from flask import Flask, render_template, jsonify
from sqlalchemy import text
# from database import engine

app = Flask(
  __name__,
  template_folder='templates',  # Name of html file folder
  static_folder='static')

main_jobs_ls = [{
  'id': 1,
  'Position': 'Data Engineer',
  'Salary': 'INR 45,00,000',
  'Location': 'Delhi, India',
  'Experience': '5yrs'
}, {
  'id': 2,
  'Position': 'ML Engineer',
  'Salary': '45,00,000',
  'Location': 'Mumbai, India',
  'Experience': '3yrs'
}, {
  'id': 3,
  'Position': 'Data Analyst',
  'Salary': 'INR 25,00,000',
  'Location': 'Karnataka, India',
  'Experience': '2yrs'
}, {
  'id': 4,
  'Position': 'Full Stack Developer',
  'Salary': 'INR 30,00,000',
  'Location': 'Mumbai, India',
  'Experience': '2yrs'
}]


def load_main_jobs():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))

    jobs = []

    for row in result.fetchall():
      row_dict = dict(zip(result.keys(), row))
      jobs.append(row_dict)

    return jobs


@app.route('/')
def Main_fun():
  jobs = load_main_jobs()
  return render_template('home.html', jobs=jobs, company_name='Jovian')


@app.route('/api/jobs')
def ls_jobs():
  return jsonify(main_jobs_ls)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port='8080', debug=True)
