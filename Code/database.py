import sqlalchemy as db
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

bulk_data = api.get_bulk_data()
