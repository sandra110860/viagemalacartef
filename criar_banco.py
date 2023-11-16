from viagemalacartef import database, app
from viagemalacartef.models import Usuario, Foto

with app.app_context():
    database.create_all()
