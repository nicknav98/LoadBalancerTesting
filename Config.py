class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:password@pgBouncer:6432/WorkoutsDB'
    SQLALCHEMY_BINDS = {
        'gyms': 'postgresql+psycopg2://admin:password@pgBouncer:6432/GymsDB'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'super-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'

    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
