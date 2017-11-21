import datetime
from app.models import db
from sqlalchemy import or_
from app.models.check_in import CheckIn
from app.models.user_ticket import UserTicket
from app.models.user import User
from app.models.base_model import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from app.configs.settings import LOCAL_TIME_ZONE
from app.builders.response_builder import ResponseBuilder
from app.services.base_service import BaseService



class CheckinService(BaseService):
    def __init__(self, perpage):
        self.perpage = perpage

    def checkin_list(self, request, page):
        self.total_items = CheckIn.query.count()
        if page is not None:
            self.page = request.args.get('page')
			# self.page = page
        else:
            self.perpage = 10
            self.page = 1
        self.base_url = request.base_url

		# paginate
        checkins = super().paginate(db.session.query(CheckIn).order_by(CheckIn.created_at.desc()))
        response = ResponseBuilder()
        # checkins = db.session.query(CheckIn).all()
        _results = []
        # if checkins is not None:
        for checkin in checkins['data']:
            data = checkin.as_dict()
            data = self.transformTimeZone(data)
            user_ticket = db.session.query(UserTicket).filter_by(id = checkin.user_ticket_id).first()
            data['user_tickets'] = user_ticket.as_dict()
            data['user_tickets']['user'] = db.session.query(User).filter_by(id = user_ticket.user_id).first().as_dict()

            _results.append(data)

        return response.set_data(_results).set_links(checkins['links']).build()

    def search_checkins(self, keyword):
        response = ResponseBuilder()
        _results = []
        results = db.session.query(CheckIn, UserTicket).join(UserTicket, User).filter(or_(
            UserTicket.ticket_code.contains(keyword),
            UserTicket.id.contains(keyword),
            User.username.contains(keyword),
            User.first_name.contains(keyword),
            User.last_name.contains(keyword),
            User.email.contains(keyword))).limit(20).all()
        for checkin, userticket in results:
            data = checkin.as_dict()
            data = self.transformTimeZone(data)
            data['user_tickets'] = userticket.as_dict()
            data['user_tickets']['user'] = userticket.user.include_photos().as_dict()
            _results.append(data)
        return response.set_data(_results).set_message('search account results').build()

    def transformTimeZone(self, obj):
        entry = obj
        created_at_timezoned = datetime.datetime.strptime(entry['created_at'], "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=LOCAL_TIME_ZONE)
        entry['created_at'] = str(created_at_timezoned).rsplit('.', maxsplit=1)[0] + " WIB"
        updated_at_timezoned = datetime.datetime.strptime(entry['updated_at'], "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=LOCAL_TIME_ZONE)
        entry['updated_at'] = str(updated_at_timezoned).rsplit('.', maxsplit=1)[0] + " WIB"
        return entry