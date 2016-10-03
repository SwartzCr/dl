from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def base():
    response = app.make_response(render_template('base.html'))
    return response

@app.route('/robots.txt')
def serve_static():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/spacer.gif')
def secret():
    response = app.make_response(send_from_directory(app.static_folder, 'spacer.gif'))
    response.set_cookie('passcode', value='bananas foster')
    return response
