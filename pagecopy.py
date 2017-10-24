from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('page.html'), 200

@app.route('/guitars/')
def guitars():
  data = {}
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass

  return render_template('guitars.html',data=data), 200

@app.route('/guitars/add', methods=['POST','GET'])
def add():
  data = {}
  import json
  try:
    with open('static/data.json', 'r') as f:
      data = json.load(f)
  except:
    pass
  if request.method == 'POST':
    f = request.files['photo']
    print request.form
    brand = request.form['brand']
    model = request.form['model']
    desc = request.form['desc']
    id = 1;
    try:
      id = len(data['guitars']) + 1
    except:
      pass
    photo = '%s.jpg' % id
    f.save('static/uploads/guitars/%s.jpg' % id)
    newguitar = { 'id' : id, 'brand' : brand, 'model' : model, 'desc' : desc,
      'photo' : photo }

    data['guitars'].append(newguitar)
    with open('static/data.json', 'w') as outfile:
      json.dump(data, outfile)

    return render_template('guitars.html', data=data), 200
  else:
    return render_template('guitaradd.html'), 200

@app.route('/amps/')
def amps():
  
  return render_template('amps.html'), 200

@app.route('/effects/')
def effects():
  return render_template('effects.html'), 200

@app.route('/about/')
def about():
  return render_template('about.html'), 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
