
def wsgi_application(environ, start_response):
    mas = environ['QUERY_STRING'].split("&")
    body = mas.join("\n")
    #input: 
    #/?a=1&a=2&b=3
    #Output:
    #a=1
    #a=2
    #b=3
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    #body = 'Hello, world!'
    start_response(status, headers )
    return [ body ]
