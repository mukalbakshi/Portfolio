from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')  # <username>/<int:post_id>
def my_home():  # username=None, post_id=None
    return render_template('index.html')  # name=username, post_id=post_id


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["subject"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')
# CSV - Comma separated values


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        try:
            # if valid_login(request.form['username'],
            #                request.form['password']):
            #     return log_the_user_in(request.form['username'])
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to Database'    
    else:
        return print('error')
        # error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)
