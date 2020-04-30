from flask import Flask, redirect, url_for, request ,render_template
#from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
#from models import User, Project, Domains

############################################

basedir = os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
Migrate(app,db)

############################################

class User(db.Model):
	"""docstring for User"""
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64),index=True, unique=True)
	email=db.Column(db.String(120),index=True, unique=True)
	pass_hash=db.Column(db.String(128))
	project=db.relationship('Project', backref='user', lazy='dynamic')

	def __init__(self, username, email):
		#super(User, self).__init__()
		self.username = username
		self.email = email
		self.pass_hash = pass_hash
class Project(db.Model):
	__tablename__="project"
	"""docstring for Project"""
	id=db.Column(db.Integer,primary_key=True)
	project_name =db.Column(db.Text)
	pro_specification= db.Column(db.Text)
	pro_domain=db.Column(db.String(120))
	#pro_domain=db.relationship('Domains', backref='pro', lazy='dynamic')
	pro_submition=db.Column(db.String(200))
	pro_cost=db.Column(db.Integer)
	references=db.Column(db.Text)
	user_id= db.Column(db.Integer, db.ForeignKey('user.id'))

	def __init__(self, project_name, pro_specification, pro_domain, pro_submition, pro_cost, references):
		#super(Project, self).__init__()
		self.project_name = project_name
		self.pro_specification = pro_specification
		self.pro_domain = pro_domain
		self.pro_submition = pro_submition
		self.pro_cost = pro_cost
		self.references = references



class Domains(db.Model):
	"""docstring for Domains"""
	id=db.Column(db.Integer,primary_key=True)
	tags=db.Column(db.Text, unique=True)
	usage=db.Column(db.Integer)

	def __init__(self, arg):
		super(Domains, self).__init__()
		self.tags = arg
		self.usage = usage

############################################

@app.route('/home') 
def success(): 
   return render_template('home_page.html')

@app.route('/projects/<name>')
def index(name):
	#print(name)

	sample=Project("The amazing superman", "needs a life", "FT", "12-31-56", 14500, "{'_sa_instance_state': <sqlalchemy.orm.state.I")
	db.session.add(sample)
	db.session.commit()

	result=Project.query.filter_by(pro_domain=str(name))
	#print(result[])
	result_dict = [u.__dict__ for u in result]
	print(type(result_dict))
	print(result_dict)
	return render_template('project.html',title='Projects', result_dict=result_dict)
@app.route('/About_us')
def about_us():
	pass

@app.route("/add_project",methods=["GET","POST"])
def form():
	if (request.method=='POST'):
		print(request.form['name'])
		return render_template("output.html", title="Sucess")
	return render_template('form.html', title='Add Project')


if __name__ == '__main__': 
   app.run(debug = True) 