activate env 

select interpretor

signin to neon and add project 

connect string  and add in database.py

run this in env python shell
->
from database import Base, engine
from models import ChatHistory
Base.metadata.create_all(bind=engine)
exit()


then in env run 
-> python app.py
