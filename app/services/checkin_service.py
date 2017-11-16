import datetime
from app.models import db
from app.models.check_in import CheckIn
from app.models.user_ticket import UserTicket
from app.models.user import User
from app.models.base_model import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from app.builders.response_builder import ResponseBuilder


class CheckinService():
     
    def checkin_list(self, request):
        response = ResponseBuilder()
        checkins = db.session.query(CheckIn).all()
        _results = []
        # if checkins is not None:
        for checkin in checkins:
            data = checkin.as_dict()
            user_ticket = db.session.query(UserTicket).filter_by(id = checkin.user_ticket_id).first()
            data['user_tickets'] = user_ticket.as_dict()
            data['user_tickets']['user'] = db.session.query(User).filter_by(id = user_ticket.user_id).first().as_dict()

            _results.append(data)

        return response.set_data(_results).build()
