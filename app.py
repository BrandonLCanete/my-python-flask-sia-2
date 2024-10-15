
from flask import Flask, render_template, request

app = Flask(__name__)


# Check if the email duplicate or not
def email_duplicate(email):
    try:
        # open the database text file
        with open('database.txt','r') as file:
            # read the database text file line
            lines = file.readlines()
            # loop through database text file 
            for line in lines:
                # check if Email : does exist
                if "Email:" in line:
                    # Split the email
                    theEmail = line.split("Email:")[1].strip()
                    # check if email does duplicate
                    if theEmail == email:
                        return True
    # check if file found
    except FileNotFoundError:
        return False

# Check if password exist or not   
def check_password(password):
    try:
        # open the database text file
        with open('database.txt','r') as file:
            # read the database text file line
            lines = file.readlines()
            # loop through database text file 
            for line in lines:
                # check if Password : does exist
                if "Password:" in line:
                    # Split the password
                    thePassword = line.split("Password:")[1].strip()
                    # check if password does exist
                    if thePassword == password:
                        return True
    # check if file found
    except FileNotFoundError:
        return False
    

# Check if the email exist or not
def check_email(email):
    try:
        # open the database text file
        with open('database.txt','r') as file:
            # read the database text file line
            lines = file.readlines()
            # loop through database text file 
            for line in lines:
                # check if Email : does exist
                if "Email:" in line:
                    # Split the email
                    theEmail = line.split("Email:")[1].strip()
                    # check if email does exist
                    if theEmail == email:
                        return True
    # check if file found
    except FileNotFoundError:
        return False


# Sign Up form
@app.route('/submit_signup', methods=['POST'])
def register():

    # variables
    user = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    cpassword = request.form.get('cpassword')

    # check if the user add all the needed data in th fields
    if(user != '' and email !='' and password !='' and cpassword !=''):
        # check if the password is same to confirm password
        if(password == cpassword):
             # check if the email is duplicate
             if(email_duplicate(email)):
                return "The email exist please try another one!"
             else:
                 # write the data inside database text file
                 with open('database.txt','w') as file:
                    file.write("Username: " +user + "\n")
                    file.write("Email: " +email + "\n")
                    file.write("Password: " +password + "\n")
                    file.close()
                    return "Sucessfully Register!"
        # password is not matched
        else:
            return "Password is not Matched!"
    # add all the needed data in the fields
    else:
        return "Please Add all the needed data in the fields!"
    
# Login form
@app.route('/submit_login', methods=['POST'])
def login():
     
     # variables
     email = request.form.get('email')
     password = request.form.get('password')
     
     # logic
     if(email!='' and password!=''):
        if check_email(email) and check_password(password):
            return "Login Sucessfully!"
        else:
            return "Incorrect Email or Password!"
     else:
         return "Please Add all the needed data in the fields!"


# Homepage
@app.route('/home')
def Home():
    return render_template('index.html', message="Welcome this is Homepage!")

# Login Page
@app.route('/login')
def Login():
    return render_template('index.html', message="Login Now!")

# Sign Up page
@app.route('/sign-up')
def sign_up():
    return render_template('index.html', message="Sign Up Now!")

# Root Page
@app.route('/')
def hello_world():
    return render_template('index.html', message="Hello, My Python Flask!")


if __name__ == '__main__':
    app.run(debug=True)


