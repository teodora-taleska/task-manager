from models import Users, Session

session = Session()


def signup(name, surname, email, password):
    if Users.email_exists(session, email):
        print("User already exists!")
        return False
    else:
        new_user = Users(name, surname, email, password)
        session.add(new_user)
        session.commit()
        print("User has been successfully created!")
        return True


def login(email, password):
    user = session.query(Users).filter_by(email=email).first()

    if user is None:
        print("User does not exist!")
        return user
    elif user.check_pass(password):
        return {"uid": user.uid, "name": user.name, "surname": user.surname, "email": user.email}
    else:
        print("Passwords do not match!")
        return user
