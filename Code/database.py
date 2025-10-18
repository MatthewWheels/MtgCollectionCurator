import sqlalchemy as db
from io import StringIO
import json
import api


# Defining the Engine
engine = db.create_engine('sqlite:///cards_db.db', echo=True)

# Create the Metadata Object
metadata_obj = db.MetaData()

# Define the profile table

# database name
#profile = db.Table(
#    'profile',                                        
#    metadata_obj,                                    
#    db.Column('email', db.String, primary_key=True),  
#    db.Column('name', db.String),                    
#    db.Column('contact', db.Integer),                
#)

# Create the profile table
#metadata_obj.create_all(engine)
io = StringIO()
bulk_data = json.dump(api.get_bulk_data(), io)
json_data = json.loads(io.getvalue())

for i in json_data["data"]:
    print("Downloading " + i["name"] +  "...")
    download_uri = i["download_uri"]
    data = api.download_api_data(download_uri)
    print("Downloaded")
