from flask_login import UserMixin
from App.app import db 

class User(db.Model, UserMixin):
	__tablename__ = "user"
	
	uid = db.Column(db.Integer, primary_key= True)
	name = db.Column(db.Text, nullable=False)
	uninum = db.Column(db.Integer, nullable=False)
	email = db.Column(db.Text, nullable=False)
	password = db.Column(db.Text, nullable=False)
	
	def __repr__(self, *args):
		return f"hi {self.email} your password is {self.password}"
		
	def get_id(self):
		return self.uid