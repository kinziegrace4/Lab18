from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

my_info = {
    'title1': 'Blog 1',
    'content1': 'This is the content of blog 1.',
    'title2': 'Blog 2',
    'content2': 'This is the content of blog 2.',
}

@app.route('/')
def home():
    return render_template('template1.html')

@app.route('/blog1')
def p2():
    return render_template('blog1.html', my_list=my_info)

@app.route('/blog2')
def p3():
    return render_template('blog2.html', my_list=my_info)