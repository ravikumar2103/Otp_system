from flask import Flask, render_template, request, jsonify
from otp_generator import generate_otp
from otp_validator import store_otp, validate_otp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_otp', methods=['POST'])
def generate_otp_route():
    # In a real application, you would associate this OTP with a user
    # (e.g., based on their email or phone number from the form).
    identifier = "temp_user"  # Replace with actual user identification
    otp = generate_otp()
    store_otp(identifier, otp)
    # In a real application, you would send this OTP to the user
    # (e.g., via SMS or email).
    return jsonify({'message': f'OTP generated and stored. Please enter it on the verification page. (For this example, OTP is: {otp})', 'identifier': identifier})

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        identifier = request.form['identifier']
        entered_otp = request.form['otp']
        if validate_otp(identifier, entered_otp):
            return jsonify({'message': 'OTP Verified Successfully!'})
        else:
            return jsonify({'message': 'Invalid OTP.'})
    return render_template('verify.html')

if __name__ == '__main__':
    app.run(debug=True) 

'''print("Starting Flask app...")
from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from otp_generator import generate_otp
from otp_validator import store_otp, validate_otp

app = Flask(__name__)

# Mail configuration - **REPLACE WITH YOUR DETAILS**
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587  # Or your mail server's port (e.g., 465 for SSL) (e.g., 587 for TLS)
app.config['MAIL_USE_TLS'] = True  # Set to True if your server uses TLS
app.config['MAIL_USE_SSL'] = False  # Set to True if your server uses SSL
app.config['MAIL_USERNAME'] = 'ravikumar21032003@outlook.com'
app.config['MAIL_PASSWORD'] = '#Rk21MaRch'
app.config['MAIL_DEFAULT_SENDER'] = 'ravikumar21032003@outlook.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_otp', methods=['POST'])
def generate_otp_route():
    email = request.form.get('email')
    if not email:
        return jsonify({'error': 'Email address is required.'}), 400

    otp = generate_otp()
    store_otp(email, otp)  # Use email as the identifier

    msg = Message('Your OTP for Verification', recipients=[email])
    msg.body = f'Your OTP is: {otp}. Please use this to verify your identity.'

    try:
        mail.send(msg)
        return jsonify({'message': f'OTP has been sent to {email}. Please check your inbox.'})
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'error': 'Failed to send OTP via email.'}), 500

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        email = request.form['identifier']  # Now 'identifier' is the email
        entered_otp = request.form['otp']
        if validate_otp(email, entered_otp):
            return jsonify({'message': 'OTP Verified Successfully!'})
        else:
            return jsonify({'message': 'Invalid OTP.'})
    return render_template('verify.html')

if __name__ == '__main__':
    app.run(debug=True)'''
