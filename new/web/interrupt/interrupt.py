from application import app
from flask import request,render_template
import re
@app.before_request
def check():
    path = request.path
    if path == '/':
        return

    if re.findall('(/static/.*|/newe/flow1.*|/newe/flow2.*|/newe/detail1|/newe/detail2|/newe/detail3|/favicon.ico)', path):
        return

    if request.method == 'GET':
        return render_template('common/error-404.html')
