from datetime import date
from flask import render_template
from app import db, application
from users.Trainer import Trainer
from users.Trainee import Trainee



@application.route("/")
def landing():
    db.session.add(Trainer(55, 'Shay Levi', 'Barre', date(2021, 5, 22), '10-154-850274', 'shaked201098@gmail.com' , '052- 5843564', 'ShayLevi55', '70.00', 1111))
    db.session.commit()
    return render_template("test.html")


if __name__ == '__main__':
    with application.app_context():
        # Create the database tables 
        db.create_all()
    application.run()