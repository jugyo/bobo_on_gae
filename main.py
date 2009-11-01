import bobo
import wsgiref.handlers

bobo_app_name='project'

def main():
    application = bobo.Application(bobo_resources=bobo_app_name)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
