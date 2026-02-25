from app import app
import datetime
from flask import render_template, request, redirect, url_for, flash


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Delmika Johnson")

@app.route('/profile/')
def profile():
    """Render the website's profile page."""
    date_joined = datetime.date(2020, 12, 12)
    formatted_date = format_date_joined(date_joined)
    return render_template('profile.html', 
                            name="Delmika Johnson", 
                            username="@delmika",
                            location = "Kingston, Jamaica",
                            date_joined=formatted_date,
                            bio = '''I am a student at UWI Mona, studying Electronics and Computer Science. 
	                        Outside of school, I enjoy reading, listening to music, trying different foods 
	                        and learning different languages.''',
                            posts=10,
                            followers=1500,
                            following=1000)

def format_date_joined(date):
    return date.strftime("%B, %Y")

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
