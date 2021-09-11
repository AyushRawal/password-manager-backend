from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)

class Record(db.Model):
    id = db.Column(db.String, nullable=False, primary_key=True)
    username = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=True)
    notes = db.Column(db.String, nullable=True)

#  db.create_all()

record_put_args = reqparse.RequestParser()
record_put_args.add_argument('title', type=str, help='Please provide title', required=True)
record_put_args.add_argument('password', type=str, help='Please provide password', required=True)
record_put_args.add_argument('url', type=str, help='URL', required=False)
record_put_args.add_argument('notes', type=str, help='Notes', required=False)

record_update_args = reqparse.RequestParser()
record_update_args.add_argument('id', type=str, help='Please provide id', required=True)
record_update_args.add_argument('title', type=str, help='Title', required=False)
record_update_args.add_argument('password', type=str, help='Password', required=False)
record_update_args.add_argument('url', type=str, help='URL', required=False)
record_update_args.add_argument('notes', type=str, help='Notes', required=False)

record_delete_args = reqparse.RequestParser()
record_delete_args.add_argument('id', type=str, help='Please provide id', required=True)

resource_fields = {
    'id': fields.String,
    'title': fields.String,
    'password': fields.String,
    'url': fields.String,
    'notes': fields.String,
}

resource_list_fields = {
    'records' : fields.List(fields.Nested(resource_fields), attribute='records')
}

class User(Resource):
    @marshal_with(resource_list_fields)
    def get(self, Username):
        records = Record.query.filter_by(username=Username)
        if not records.first():
            abort(404, message="Username not found")
        return {'records': records}

    @marshal_with(resource_fields)
    def post(self, Username):
        args = record_put_args.parse_args()
        record = Record(id=str(uuid4()), username=Username, title=args['title'], password=args['password'], url=args['url'], notes=args['notes'])
        db.session.add(record)
        db.session.commit()
        return record

    @marshal_with(resource_fields)
    def patch(self, Username):
        args = record_update_args.parse_args()
        record = Record.query.filter_by(id=args['id']).first()
        if not record:
            abort(404, message="Record does not exist")
        if args['title']:
            record.title = args['title']
        if args['password']:
            record.password = args['password']
        if args['url']:
            record.url = args['url']
        if args['notes']:
            record.notes = args['notes']

        db.session.commit()
        return record

    def delete(self, Username):
        args = record_delete_args.parse_args()
        record = Record.query.filter_by(id=args['id']).first()
        if not record:
            abort(404, message="Record does not exist")
        db.session.delete(record)
        db.session.commit()
    
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE')
    return response

api.add_resource(User, "/user/<string:Username>")

if (__name__ == "__main__"):
    app.run(debug=True)
