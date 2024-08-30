from flask import render_template,request,redirect,url_for,Blueprint
from flask_login import current_user

core = Blueprint("core",__name__, template_folder="templates")

@core.route("/", methods=["GET","POST"])
def index():
	if current_user.is_authenticated:
		return redirect(url_for("auth.dashboard"))
	else:
		return render_template("core/index.html")
		
@core.route("/about")
def about():
	return render_template("core/about.html")
	