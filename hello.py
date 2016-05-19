
def wsgi_application(environ, start_response):
    mas = environ['QUERY_STRING'].split("&")
    body = "\n".join(mas)
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers )
    return [ body ]
