from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # demo only: pretend we created the user
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/subject')
def subject():
    # placeholder "your subject page" -> reuse index grid
    return render_template('index.html')

@app.route('/feed')
def feed():
    # demo content for feed
    posts = [
        {
            "user": "UNAME",
            "title": "วิชา sdlfgmdiofhjdiojfgdljjgosdlmfsfd",
            "file": {"name": "ไฟล์สรุปว่าเขาไม่รัก.pdf", "type": "pdf"}
        },
        {
            "user": "UNAME",
            "title": "วิชา sdlfgmdiofhjdiojfgdljjgosdlmfsfd",
            "file": None
        }
    ]
    return render_template('feed.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
