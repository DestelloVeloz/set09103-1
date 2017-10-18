from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('chords.html'), 200

@app.route('/C/')
def C():
  return render_template('cpage.html'), 200

@app.route('/D/')
def D():
  return render_template('dpage.html'), 200

@app.route('/E/')
def E():
  return render_template('epage.html'), 200

@app.route('/F/')
def F():
  return render_template('fpage.html'), 200

@app.route('/G/')
def G():
  return render_template('gpage.html'), 200

@app.route('/A/')
def A():
  return render_template('apage.html'), 200

@app.route('/B/')
def B():
  return render_template('bpage.html'), 200


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
