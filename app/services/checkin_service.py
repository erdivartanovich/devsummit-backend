import datetime
from app.models import db
from app.models.check_in import CheckIn
from app.models.user_ticket import UserTicket
from app.models.user import User
from app.models.base_model import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from app.configs.settings import LOCAL_TIME_ZONE
from app.builders.response_builder import ResponseBuilder


class CheckinService():
     
    def checkin_list(self, request):
        response = ResponseBuilder()
        checkins = db.session.query(CheckIn).all()
        _results = []
        # if checkins is not None:
        for checkin in checkins:
            data = checkin.as_dict()
            data = self.transformTimeZone(data)
            user_ticket = db.session.query(UserTicket).filter_by(id = checkin.user_ticket_id).first()
            data['user_tickets'] = user_ticket.as_dict()
            data['user_tickets']['user'] = db.session.query(User).filter_by(id = user_ticket.user_id).first().as_dict()

            _results.append(data)

        return response.set_data(_results).build()

    def transformTimeZone(self, obj):
        entry = obj
        created_at_timezoned = datetime.datetime.strptime(entry['created_at'], "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=LOCAL_TIME_ZONE)
        entry['created_at'] = str(created_at_timezoned).rsplit('.', maxsplit=1)[0] + " WIB"
        updated_at_timezoned = datetime.datetime.strptime(entry['updated_at'], "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=LOCAL_TIME_ZONE)
        entry['updated_at'] = str(updated_at_timezoned).rsplit('.', maxsplit=1)[0] + " WIB"
        return entry