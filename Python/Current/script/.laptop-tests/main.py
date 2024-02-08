import time
import threading

from icecream import ic
from datetime import datetime
from flask import (
    render_template,
    request,
    Flask,
)

app = Flask( import_name = __name__ )
# app = Flask( import_name = 'DEV. Env. Tests' )


@app.route( rule = '/' )
def index() :
    return render_template( template_name_or_list = 'index.html' )


@app.route( rule = '/process_data', methods = [ 'POST' ] )
def process_data() :
    student_name = request.form[ 'student_name' ]
    ic( student_name )

    return render_template(
        debugger = student_name,
        template_name_or_list = 'handle.html'
    )














if __name__ == '__main__':
    app.run( debug = True )


    # ...



