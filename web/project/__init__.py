from flask import Flask, jsonify, request
from project.models import User, db


app = Flask(__name__)
app.config.from_object("project.config.DevelopmentConfig")
db.init_app(app)


@app.route("/users/add", methods=["POST"])
def add_user():
    if request.form:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
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
    users = User.query.all()
    if users:
        return jsonify([u.serialize() for u in users])

    return jsonify([])


@app.route("/users/<id_>", methods=["GET"])
def get_user_by_id(id_):

    user = User.query.filter_by(id=id_).first()
    if user:
        return jsonify(user.serialize())
    else:
        raise FileNotFoundError


@app.route("/users/update/<id_>", methods=["PUT"])
def update_user_by_id(id_):

    user = User.query.filter_by(id=id_).first()
    if user:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
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


@app.route("/users/delete/<id_>", methods=["DELETE"])
def delete_user_by_id(id_):
    user = User.query.filter_by(id=id_).first()
    id = user.id
    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            return "User {} was deleted".format(id)
        except Exception as e:
            return str(e)
    else:
        raise FileNotFoundError
