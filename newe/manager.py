from application import app
from common.libs.Helper import Helper
import www
from gevent.pywsgi import WSGIServer


if __name__ == '__main__':
    if app.config['RUN_ENVIRON'] == 'local':
        app.run(port=80, debug=True, host='127.0.0.1')
    else:
        http_server = WSGIServer(('0.0.0.0', 2020), app)
        http_server.serve_forever()
