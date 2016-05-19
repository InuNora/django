bind = "0.0.0.0:8080"
workers = 1
pythonpath = "/home/box/web"
errorlog = "/home/box/web/etc/error.log"
loglevel = "debug"
def wsgi_application(environ, start_response):
    #
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = 'Hello, world!'
    start_response(status, headers )
    return [ body ]
