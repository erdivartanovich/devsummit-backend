from app.services import hackatonproposalservice
from app.controllers.base_controller import BaseController


class HackatonProposalController(BaseController):
	
	@staticmethod
	def index(status):
		result = hackatonproposalservice.get(status)
		if result['error']:
			return BaseController.send_error_api(result['data'], result['message'])
		return BaseController.send_response_api(result['data'], result['message'])

	@staticmethod
	def deny(order_id):
		if order_id is None:
			return BaseController.send_error_api(None, 'invalid payload')
		payloads = {
			'order_id': order_id
		}
		result = hackatonproposalservice.deny(payloads)
		if result['error']:
			return BaseController.send_error_api(result['data'], result['message'])
		return BaseController.send_response_api(result['data'], result['message'])

	@staticmethod
	def verify(order_id):
		if order_id is None:
			return BaseController.send_error_api(None, 'invalid payload')
		payloads = {
			'order_id': order_id
		}
		result = hackatonproposalservice.verify(payloads)
		if result['error']:
			return BaseController.send_error_api(result['data'], result['message'])
		return BaseController.send_response_api(result['data'], result['message'])

	@staticmethod
	def resend_email(order_id):
		if order_id is None:
			return BaseController.send_error_api(None, 'invalid payload')
		payloads = {
			'order_id': order_id
		}
		result = hackatonproposalservice.resend_email(payloads)
		if result['error']:
			return BaseController.send_error_api(result['data'], result['message'])
		return BaseController.send_response_api(result['data'], result['message'])

	@staticmethod
	def resend_certificate(user_id):
		if user_id is None:
			return BaseController.send_error_api(None, 'invalid payload')
		payloads = {
			'user_id': user_id
		}
		result = hackatonproposalservice.resend_certificate(payloads)
		if result['error']:
			return BaseController.send_error_api(result['data'], result['message'])
		return BaseController.send_response_api(result['data'], result['message'])

	@staticmethod
	def send_certificate():
		result = hackatonproposalservice.send_certificate()
		if result['error']:
			return BaseController.send_error_api(result['data'], result['message'])
		return BaseController.send_response_api(result['data'], result['message'])

	@staticmethod
	def email_certificate(request):
		email = request.json['email'] if 'email' in request.json else None
		name = request.json['name'] if 'name' in request.json else None
		if email and name:
			payload = {
				'email': email,
				'name': name
			}
		else:
			return BaseController.send_error_api(None, 'invalid payload')

		result = hackatonproposalservice.email_certificate(payload)
		if result['error']:
			return BaseController.send_error_api(result['data'], result['message'])
		return BaseController.send_response_api(result['data'], result['message'])
