import datetime
from app.models import db
from sqlalchemy.exc import SQLAlchemyError
# import model class
from app.models.referal import Referal
from app.models.user import User
from app.builders.response_builder import ResponseBuilder
from app.services.user_ticket_service import UserTicketService


class ReferalService():

	def get(self):
		referals = db.session.query(Referal).all()
		return referals

	def show(self, id):
		referal = db.session.query(Referal).filter_by(id=id).first()
		return referal

	def create(self, payloads):
		response = ResponseBuilder()
		self.model_referal = Referal()
		self.model_referal.owner = payloads['owner']
		self.model_referal.discount_amount = payloads['discount_amount']
		self.model_referal.referal_code = payloads['referal_code']
		self.model_referal.quota = payloads['quota']
		db.session.add(self.model_referal)
		try:
			db.session.commit()
			data = self.model_referal.as_dict()
			return response.set_data(data).set_message('referal created successfully').build()
		except SQLAlchemyError as e:
			data = e.orig.args
			return response.set_data({'sql_error': True}).set_error(True).set_message(data).build()


	# should be placed in another class as should not be related to referal (should be user referal)
	def reward_referal(self, user):
		response = ResponseBuilder()
		if user['referal_count'] < 10:
			return response.set_data(None).set_message('Not sufficient referal count').set_error(True).build()
		if user['referal_count'] > 10:
			return response.set_data(None).set_message('You have taken your reward').set_error(True).build()
		payload = {}
		payload['user_id'] = user['id']
		payload['ticket_id'] = 1
		update_user = db.session.query(User).filter_by(id=user['id'])
		update_user.update({
			'referal_count': 11
		})
		db.session.commit()
		UserTicketService().create(payload)
		return response.set_data(None).set_message('You have successfully redeemed your reward').build()


	def update(self, payloads, id):
		response = ResponseBuilder()
		try:
			self.model_referal = db.session.query(Referal).filter_by(id=id)
			self.model_referal.update({
				'owner': payloads['owner'],
				'discount_amount': payloads['discount_amount'],
				'referal_code': payloads['referal_code'],
				'quota': payloads['quota'],
				'updated_at': datetime.datetime.now()
			})
			db.session.commit()
			data = self.model_referal.first().as_dict()
			return response.set_data(data).set_message('referal updated successfully').build()
		except SQLAlchemyError as e:
			data = e.orig.args
			return response.set_error(True).set_data({'sql_error': True}).set_message(data).build()

	def delete(self, id):
		response = ResponseBuilder()
		self.model_referal = db.session.query(Referal).filter_by(id=id)
		if self.model_referal.first() is not None:
			# delete row
			self.model_referal.delete()
			db.session.commit()
			return response.set_data(None).set_message('referal deleted successfully').build()
		else:
			return response.set_data(None).set_error(True).set_message('deletion failed').build()

	def check_referal_code(self, referal_code):
		response = ResponseBuilder()
		referal = db.session.query(Referal).filter_by(referal_code=referal_code).first()
		if referal:
			# return referal data
			return response.set_data(referal.as_dict()).set_message('referal code successfully retrieved').build()
		return response.set_error(True).set_data({'code_invalid': True}).set_message('referal code is not valid').build()
