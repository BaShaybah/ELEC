from flask import render_template,request,redirect,url_for,Blueprint
from App.blueprints.auth.models import User
from App.app import db
from App.app import bcrypt

from flask_login import login_user,logout_user,current_user,login_required

auth = Blueprint("auth",__name__, template_folder="templates")


@auth.route("/", methods=["GET","POST"])
def signUp():
	if request.method == "GET":
		if current_user.is_authenticated:
			return redirect(url_for("dashboard"))
		return render_template("auth/index.html")
	elif request.method == "POST":
		name = request.form.get("name")
		uninum = int(request.form.get("uninum"))
		email = request.form.get("email")
		password = request.form.get("password")
		check = request.form.get("checkbox")
		if check:
			if not User.query.filter(User.email == email ).first():
				bpassword = bcrypt.generate_password_hash(password)
				user = User(name=name,uninum=uninum,email=email,password=bpassword)
				db.session.add(user)
				db.session.commit()
				current = User.query.filter(User.email == email).first()
				login_user(current)
				return redirect(url_for("auth.dashboard"))
			return render_template("auth/index.html",invalid=True)
		return render_template("auth/index.html",notchecked=True)
			
@auth.route("/dashboard")
@login_required
def dashboard():
	return render_template("auth/dashboard.html",user=current_user)
		
@auth.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		if current_user.is_authenticated:
			return redirect(url_for("auth.dashboard"))
		
		return render_template("auth/login.html",error=False)
	elif request.method == "POST":
		email = request.form.get("email")
		password = request.form.get("password")
		user = User.query.filter(User.email == email).first()
		if bcrypt.check_password_hash(user.password,password):
			login_user(user)
			return redirect(url_for("auth.dashboard"))
		else:
			return render_template("auth/login.html",error=True)
			
@auth.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("auth.signUp"))