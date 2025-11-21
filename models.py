from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
import random
# dessa forma importamos o que foi criado de antemão em database.py
from database import Base

def generate_random_id():
    return random.randint(1, 99999999999)

class valor(Base):
    __tablename__ = "valores"

    id = Column(Integer, primary_key=True, index=True, default=generate_random_id)
    nome = Column(String, index=True, nullable=False)

