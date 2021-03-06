from app.controllers.base_controller import BaseController
from app.models.base_model import BaseModel
from app.services import questionerservice


class QuestionerController(BaseController):

	@staticmethod
	def index(request):
		booth_id = request.args.get('booth_id', '')
		questioners = questionerservice.get(booth_id)
		return BaseController.send_response_api(questioners, 'questioners retrieved successfully')

	@staticmethod
	def show(id):
		questioner = questionerservice.show(id)
		return BaseController.send_response_api(questioner)
	
	@staticmethod
	def patch(id, request):
		# pyload should have keys: booth_id and questions 
		if ('questions' in request.json) and ('booth_id' in request.json):
			payload = {
				'booth_id': request.json['booth_id'],
				'questions': request.json['questions']
			}
			questioner = questionerservice.patch(id, payload)
			if questioner['error']:
				return BaseController.send_error_api(None, questioner['message'])
			return BaseController.send_response_api(questioner['data'], questioner['message'])
		else:
			return BaseController.send_error_api(None, 'payload not valid!')

	@staticmethod
	def post_answer(id, user, request):
		user_id = user.id
		answers = request.json['answers']
		if answers:
			payload = {
				'answers': answers
			}
			result = questionerservice.post_answer(id, user_id, payload)
			if result['error']:
				return BaseController.send_error_api(result['data'], 'error post answer')
			return BaseController.send_response_api(result, "answer successfully posted")
		else:
			return BaseController.send_error_api('payload not valid')

	@staticmethod
	def delete(id):
		questioner = questionerservice.delete(id)
		if questioner['error']:
			return BaseController.send_error_api(None, questioner['message'])
		return BaseController.send_response_api(questioner, questioner['message'])
