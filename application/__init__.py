from flask  import Flask 
from flask_pymongo import PyMongo  


app = Flask(__name__)
app.config["SECRET_KEY"] = "187e3dce86547678f312969d769bb26e7db71afd"
app.config["MONGO_URI"] = "mongodb+srv://cheikhibrambengue90:cheikhibrambengue90@cluster0.qgcf0mz.mongodb.net/etudiant_flask?retryWrites=true&w=majority"


#Setup MongoDB
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes  