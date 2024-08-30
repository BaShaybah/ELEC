""" CREATE APP"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from flask_login import LoginManager
from flask_bcrypt import Bcrypt 

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
	app = Flask(__name__, 
				template_folder="templates", 
				static_folder="static",
				static_url_path="/")
	app.secret_key = "hsjoeo8392nskwln3io2kso20"
	app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./base.db"
	
	db.init_app(app)
	log_manager = LoginManager()
	log_manager.init_app(app)
	
	from App.blueprints.auth.models import User
	@log_manager.user_loader
	def load_user(uid):
		return User.query.get(uid)
	
	bcrypt.init_app(app)
	
	from App.blueprints.core.routes import core
	from App.blueprints.auth.routes import auth
	app.register_blueprint(core, url_prefix="/")
	app.register_blueprint(auth, url_prefix="/auth")
	
	migrate = Migrate(app, db)
	return app
	
	