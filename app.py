from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def start(name=None):
    return render_template('start.html', name=name)

@app.route('/')
def about():
	images = ['LZ1.png', 'LZ2.png']
	return render_template('content-body.html', images=images)

@app.route('/resume/<focus>')
def resume_page(focus):
    return "Hire me as a {}".format(focus)

if __name__ == '__main__':
    app.run()

