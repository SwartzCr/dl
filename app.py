from flask import Flask, render_template, send_from_directory, request
app = Flask(__name__)

@app.route('/')
def base():
    passcode = request.cookies.get('passcode')
    if passcode == "happy birthday":
        response = app.make_response(render_template('base.html'))
    else:
        response = app.make_response(send_from_directory('static', 'seller.html'))
    return response

@app.route('/robots.txt')
def serve_static():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/spacer.gif')
def secret():
    response = app.make_response(send_from_directory(app.static_folder, 'spacer.gif'))
    response.set_cookie('passcode', value='happy birthday')
    return response
