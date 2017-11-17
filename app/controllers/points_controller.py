from app.controllers.base_controller import BaseController
from app.services import pointtransactionservice
from app.models.base_model import BaseModel


class PointsController(BaseController):

	@staticmethod
	def transfer_point(request, sender_id):
		receiver_id = request.json['receiver_id'] if 'receiver_id' in request.json else None
		points = request.json['points'] if 'points' in request.json else None
		result = pointtransactionservice.transfer_points(receiver_id, sender_id, points)
		if result['error']:
			return BaseController.send_error_api(None, result['data'])
		return BaseController.send_response_api(None, result['data'])

	@staticmethod
	def transfer_point_log(request, user):
		if user['role_id'] == 1:
			# admin
			result = pointtransactionservice.get_admin_log()
		elif user['role_id'] == 7:
			# attendee
			result = pointtransactionservice.get_user_log(user['id'])
		elif user['role_id'] == 3:
			# booth
			result = pointtransactionservice.get_booth_log(user['id'])

		return BaseController.send_response_api(BaseModel.as_list(result), 'logs retrieved succesfully')

	@staticmethod
	def reward_point(request, user):
		major = request.json['major'] if 'major' in request.json else None
		minor = request.json['minor'] if 'minor' in request.json else None

		if major and minor:
			payloads = {
				'major': major,
				'minor': minor
			}
		else:
			return BaseController.send_error_api(None, 'invalid payload')
		result = pointtransactionservice.reward_point(payloads, user)
		if result['error']:
			return BaseController.send_response_api(result['data'], result['message'])
		return BaseController.send_error_api(result['data'], result['message'])