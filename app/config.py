"""Base config."""
SECRET_KEY = 'GDtfDCFYjD'
# SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'
JSONIFY_PRETTYPRINT_REGULAR = True
# #!/usr/bin/python3
# """Flask configuration."""
# from os import environ, path
# # from dotenv import load_dotenv

# # basedir = path.abspath(path.dirname(__file__))
# # load_dotenv(path.join(basedir, '.env'))


# class Config:
#     """Base config."""
#     SECRET_KEY = environ.get('SECRET_KEY')
#     SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
#     STATIC_FOLDER = 'static'
#     TEMPLATES_FOLDER = 'templates'
#     JSONIFY_PRETTYPRINT_REGULAR = True


#     # FLASK_ENV = 'development'
#     # TESTING = True
#     # SECRET_KEY = environ.get('SECRET_KEY')
#     # STATIC_FOLDER = 'static'
#     # TEMPLATES_FOLDER = 'templates'

#     # # Database
#     # SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
#     # SQLALCHEMY_TRACK_MODIFICATIONS = False

#     # # AWS Secrets
#     # AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
#     # AWS_KEY_ID = environ.get('AWS_KEY_ID')


# # class ProdConfig(Config):
# #     FLASK_ENV = 'production'
# #     DEBUG = False
# #     TESTING = False


# # class DevConfig(Config):
# #     FLASK_ENV = 'development'
# #     DEBUG = True
# #     TESTING = True