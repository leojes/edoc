from app import db

class User(db.Model):
	"""docstring for User"""
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64),index=True, unique=True)
	email=db.Column(db.String(120),index=True, unique=True)
	pass_hash=db.Column(db.String(128))
	project=db.relationship('Project', backref='user', lazy='dynamic')

	def __init__(self, username, email):
		super(User, self).__init__()
		self.arg = arg


class Project(object):
	"""docstring for Project"""
	id=db.Column(db.Integer,primary_key=True)
	project_name =db.Column(db.Text)
	pro_specification= db.Column(db.Text)
	pro_domain=db.relationship('Domains', backref='pro', lazy='dynamic')
	pro_submition=db.Column(db.String(200))
	pro_cost=db.Column(db.Integer)
	references=db.Column(db.Text)
	user_id= db.Column(db.Integer, db.ForeignKey('user.id'))

	def __init__(self, arg):
		super(Project, self).__init__()
		self.arg = arg
	
class Domains(object):
	"""docstring for Domains"""
	id=db.Column(db.Integer,primary_key=True)
	tags=db.Column(db.Text, unique=True)
	usage=db.Column(db.Integer)
	
	def __init__(self, arg):
		super(Domains, self).__init__()
		self.arg = arg
		