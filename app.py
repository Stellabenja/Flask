from flask import Flask, render_template, request, session, url_for, redirect
app = Flask(__name__)




@app.route('/')
def index():
 return render_template('base.html')



@app.route('/home', methods=['GET', 'POST'])
def home_form():
    if request.method == 'POST':
       
        return redirect(url_for('base'))

    
    return render_template('home.html') 

@app.route('/login', methods=['GET', 'POST'])
def login_form():
    if request.method == 'POST':
        
        return redirect(url_for('base'))

    
    return render_template('login.html') 


#run    

if __name__ == "__main__":
    app.run(debug=True)