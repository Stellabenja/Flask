from flask import Flask, render_template, request, session, url_for, redirect
app = Flask(__name__)




@app.route('/')
def index():
 return render_template('base.html')

@app.route('/home', methods=['GET', 'POST'])
def home_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('base'))

    # show the form, it wasn't submitted
    return render_template('home.html') 




#run    

if __name__ == "__main__":
    app.run(debug=True)