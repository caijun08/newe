import time
from application import app


class UrlManager():

    @staticmethod
    def buildStaticUrl(path):
        release_version = '0.0.1'
        ver = '%s' % int(time.time()) if not release_version else release_version
        path = '/static%s?ver=%s' % (path, ver)
        return UrlManager.buildUrl(path)

    @staticmethod
    def buildUrl(path):
        prepath = app.config['LOCATION'] if 'LOCATION' in app.config else ''
        return '%s%s' % (prepath, path)