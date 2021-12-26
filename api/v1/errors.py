from flask import render_template
from . import v1


@v1.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
