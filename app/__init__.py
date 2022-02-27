from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
def create_app(config_name):
  app = Flask(__name__)
  #create app config
  app.config.from_object(config_options[config_name])
  #initialize flask exts
  bootstrap.init_app(app)
  #return views
  return app