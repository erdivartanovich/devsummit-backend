from app.models import db
from sqlalchemy.exc import SQLAlchemyError
from app.models.event import Event
from app.services.base_service import BaseService
from app.builders.response_builder import ResponseBuilder
from app.models.panel_event import PanelEvent


class EventService(BaseService):

    def __init__(self, perpage): 
        self.perpage = perpage

    def index(self, request):
        self.total_items = Event.query.count()
        if request.args.get('page'):
            self.page = request.args.get('page')
        else:
            self.perpage = self.total_items
            self.page = 1
        self.base_url = request.base_url
        paginate = super().paginate(db.session.query(Event))
        paginate = super().include_events()

        response = ResponseBuilder()
        result = response.set_data(paginate['data']).set_links(paginate['links']).build()
        return result

    def show(self, id):
        response = ResponseBuilder()
        self.events_model = db.session.query(Event).filter_by(id=id)
        if self.events_model.first() is None:
            return response.set_data(None).set_error(True).set_message('Event not found').build()

        data = self.events_model.first().as_dict()
        if data['type'] == "discuss panel":
            users = []
            panel_event = db.session.query(PanelEvent).filter_by(event_id=data['id']).all()
            for panel in panel_event:
                users.append(panel.user.include_photos().as_dict())
                data['user'] = users
        elif data['type'] != 'other':
            data['user'] = self.events_model.first().user.as_dict()
        return response.set_data(data).build()

    def create(self, payloads):
        response = ResponseBuilder()
        try:
            information = payloads['information'] if 'information' in payloads else None
            title = payloads['title'] if 'title' in payloads else None
            type = payloads['type'] if 'type' in payloads else None
            user_id = payloads['user_id'] if 'user_id' in payloads else None
            if type == 'discuss panel':
                # nullify user id, move to users and insert to panel_event instead
                user_id = None
                users = payloads['user_id'] if 'user_id' in payloads else None

            self.events_model = Event()
            self.events_model.information = information
            self.events_model.title = title
            self.events_model.type = type
            self.events_model.user_id = user_id

            db.session.add(self.events_model)
            db.session.commit()
            if type == 'discuss panel':
                # save the users to panel event
                for uid in users:
                    panel_event = PanelEvent()
                    panel_event.event_id = self.events_model.id
                    panel_event.user_id = uid 
                    db.session.add(panel_event)
                    
                db.session.commit()

            data = self.events_model.as_dict()

            return response.set_data(data).build()

        except SQLAlchemyError as e:
            data = e.orig.args
            response.set_data(data).set_error(True).build()

    def update(self, id, payloads):
        response = ResponseBuilder()
        try:
            self.events_model = db.session.query(Event).filter_by(id=id)
            information = payloads['information'] if 'information' in payloads else None
            title = payloads['title'] if 'title' in payloads else None
            type = payloads['type'] if 'type' in payloads else None
            user_id = payloads['user_id'] if 'user_id' in payloads else None
            new_event = {}
            if information:
                new_event['information'] = information
            if title:
                new_event['title'] = title
            
            new_event['type'] = type

            if type == 'discuss panel':
                # nullify user id, move to users and insert to panel_event instead
                user_id = None
                users = payloads['user_id'] if 'user_id' in payloads else None


            new_event['user_id'] = user_id

            self.events_model.update(new_event)

            db.session.commit()
            if type == 'discuss panel':
                # save the users to panel event
                deleted = db.session.query(PanelEvent).filter_by(event_id=id).delete()
                for uid in users:
                    panel_event = PanelEvent()
                    panel_event.event_id = id
                    panel_event.user_id = uid 
                    db.session.add(panel_event)
                db.session.commit()
            data = self.events_model.first().as_dict()
            return response.set_data(data).build()

        except SQLAlchemyError as e:
            data = e.orig.args
            return response.set_data(data).build()

    def delete(self, id):
        response = ResponseBuilder()
        self.events_model = db.session.query(Event).filter_by(id=id)
        if self.events_model.first() is not None:
            # delete row
            self.events_model.delete()
            db.session.commit()
            return response.set_data(None).build()
        else:
            return response.set_data(None).set_error(True).build()
