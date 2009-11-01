import bobo

@bobo.query('/')
def hello(name='world'):
    return 'Hello %s!' % name
