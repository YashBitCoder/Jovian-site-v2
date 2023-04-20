from flask import Flask, render_template, jsonify

app = Flask(__name__)

main_jobs_ls = [
  {
    'id': 1,
    'Position': 'Data Engineer',
    'Salary': 'INR 45,00,000',
    'Location': 'Delhi, India',
    'Experience': '5yrs'
  },
  
  {
    'id': 2,
    'Position': 'ML Engineer',
    'Location': 'Mumbai, India',
    'Experience': '3yrs'
  },
 
  {
    'id': 3,
    'Position': 'Data Analyst',
    'Salary': 'INR 25,00,000',
    'Location': 'Karnataka, India',
    'Experience': '2yrs'
  },
 
  {
    'id': 4,
    'Position': 'Full Stack Developer',
    'Salary': 'INR 30,00,000',
    'Location': 'Mumbai, India',
    'Experience': '2yrs'
  }
]

@app.route('/')
def Main_fun():
  return render_template('home.html', jobs=main_jobs_ls, company_name='Main Singh')

@app.route('/api/jobs')
def ls_jobs():
  return jsonify(main_jobs_ls) 

if __name__ == '__main__':
  app.run(debug=True)