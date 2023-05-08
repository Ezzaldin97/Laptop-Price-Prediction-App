from app import app
from app.config_parser import Config

conf = Config()

if __name__=='__main__':
    app.run(host='0.0.0.0', port= conf.config["app_port"], debug=False)