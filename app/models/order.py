import datetime
# import classes
from app.models.base_model import BaseModel
from app.models.referal import Referal  # noqa
from app.models import db


class Order(db.Model, BaseModel):
	# table name
	__tablename__ = 'orders'
	# displayed fields
	visible = ['id', 'user_id', 'referal_id', 'status', 'banned', 'created_at', 'updated_at']

	# columns definitions
	id = db.Column(db.String, primary_key=True)
	user_id = db.Column(
		db.Integer,
		db.ForeignKey('users.id'),
		nullable=False
	)
	user = db.relationship('User')
	referal_id = db.Column(
		db.Integer,
		db.ForeignKey('referals.id'),
		nullable=False
	)
	banned = db.Column(db.Boolean())
	referal = db.relationship('Referal')
	status = db.Column(db.String)
	created_at = db.Column(db.DateTime)
	updated_at = db.Column(db.DateTime)

	def __init__(self):
		self.id = 'ds-' + datetime.datetime.now().strftime("%Y%m%d.%H%M%S%f")
		self.created_at = datetime.datetime.now()
		self.updated_at = datetime.datetime.now()
