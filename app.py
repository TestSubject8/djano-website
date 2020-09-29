from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def start(name=None):
    return render_template('start.html', name=name)

@app.route('/')
@app.route('/about/')
@app.route('/about/<focus>')
def about(focus='Default'):
	focus_list={'programmer': 'software', 'maker': 'builds'}
	return render_template('content-body.html', focus=focus, focus_title=focus_list.get(focus))

@app.route('/resume/<focus>')
def resume_page(focus):
    return "Hire me as a {}".format(focus)

if __name__ == '__main__':
    app.run()

