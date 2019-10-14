from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/confirmation", methods=['POST', 'GET'])

def validation():
   # gets user input data from form
    # gets user input data from form
    user = request.form['username']
    password = request.form['password']
    password_verify = request.form['verify']
    email = request.form['email']

    # these variables store error messages if there are any errors
    error_username = ""
    error_password = ""
    error_verify = ""
    error_email = ""

   # checks for proper username length
    if len(user) < 3 or len(user) > 20 or " " in user :
        error_username = "Invalid username."

     # checks for proper password length
    if len(password) < 3 or len(password) > 20 or " " in password:
        error_password = "Invalid password."

      # checks for proper password length
    if len(password_verify) < 3 or len(password_verify) > 20 or " " in password_verify:
        error_verify = "Invalid verfication password."

        # Checks if password and verify password match

    if  password_verify != password:
          error_verify = "Passwords don't match"

           # Gets '@' and '.' count in email string
    at_symbol_count = email.count('@')
    period_count = email.count('.')

          # Checks for the correct length of email
    if len(email) > 0:      
        if len(email) < 3 or len(email) > 20:
            error_email = "Invalid email: too short or too long" 

            # checks for 'space' in email        
    if " " in email:
        error_email = "Invalid email: spaces not accepted"

         # checks for more than one '@' or '.' in email
    if at_symbol_count > 1 or period_count > 1:
        error_email = "Invalid email: extra character"

          # checks for empty email string and missing characters
    if email != "":
        if '@' not in email or '.' not in email:
            error_email = "Invalid email: missing character"     

    # returns confirmation page if no errors found
    if  error_username == "" and  error_password  == "" and  error_verify == "":
        return render_template('confirmation.html', user=user)
    
    # returns home page with error messages if errors found
    else:
        return render_template('signup.html', error_username=error_username, error_password=error_password, error_verify=error_verify, error_email=error_email)

@app.route("/")
def index():

    '''
    home page that displays user signup form
    '''

    return render_template('signup.html')


if __name__ == '__main__':
    app.run()
