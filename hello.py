def app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-type', 'text/plain')
    ]
    start_response(status, headers)
    return ["\n".join(environ["QUERY_STRING"].split("&")).encode()]