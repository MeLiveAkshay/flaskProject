from flask import Flask, render_template

app = Flask(__name__)

@app.route('/blog')
def blog():
    posts = [
        {
            'title': 'How to Learn Python',
            'author': 'Akshay Prajapati',
            'content': 'Start with basics, then move to projects.',
            'date': '2025-04-07'
        },
        {
            'title': 'Understanding Flask and Jinja2',
            'author': 'Ravi Sharma',
            'content': 'A quick intro to Flask and how templating works.',
            'date': '2025-04-06'
        },
        {
            'title': 'Final Year Project Ideas',
            'author': 'Priya Gupta',
            'content': 'Top real-world project ideas for CS students.',
            'date': '2025-04-05'
        }
    ]
    return render_template('blog.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
