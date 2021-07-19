from flask import Flask, jsonify, request
from project.models import User, db


app = Flask(__name__)
app.config.from_object("project.config.Config")
db.init_app(app)


@app.route("/add", methods=["POST"])
def add_user():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    email = request.args.get('email')
    phone_number = request.args.get('phone')
    try:
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
        )
        db.session.add(user)
        db.session.commit()
        return "User {} added".format(user.id)
    except Exception as e:
        return str(e)


@app.route("/users", methods=["GET"])
def get_all_users():
    try:
        users = User.query.all()
        return jsonify([u.serialize() for u in users])
    except Exception as e:
        return str(e)


@app.route("/users/<id_>", methods=["PUT"])
def update_user_by_id(id_):

    user = User.query.filter_by(id=id_).first()
    if user:
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        email = request.args.get('email')
        phone_number = request.args.get('phone')
        try:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone_number = phone_number
            db.session.commit()
            return "User {} was updated".format(user.id)
        except Exception as e:
            raise e
    else:
        raise FileNotFoundError


@app.route("/users/<id_>")
def get_user_by_id(id_):

    user = User.query.filter_by(id=id_).first()
    if user:
        return jsonify(user.serialize())
    else:
        raise FileNotFoundError


@app.route("/users/<id_>", methods=["DELETE"])
def delete_user_by_id(id_):

    user = User.query.filter_by(id=id_).first()
    id = user.id
    if user:
        db.session.delete(user)
        db.session.commit()
        return "User {} was deleted".format(id)
    else:
        raise FileNotFoundError
