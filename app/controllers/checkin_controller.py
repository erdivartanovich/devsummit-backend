from app.controllers.base_controller import BaseController
from app.services import checkinservice


class CheckinController(BaseController):

    @staticmethod
    def index(request):
        checkin_list = checkinservice.checkin_list(request)
        if checkin_list is None:
            return BaseController.send_error_api(None, 'checkin list is empty')
        return BaseController.send_response_api(checkin_list['data'], 'checkin list retrieved successfully')
