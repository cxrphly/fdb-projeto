from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
metadata = MetaData(schema='fdb')
db = SQLAlchemy(metadata=metadata)