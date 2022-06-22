#!/usr/bin/python3
"""TestScore model
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class TestScore(BaseModel, Base):
	"""TestScore class for score"""
	__tablename__  = "test_scores"
	user_id = Column(String(128), ForeignKey("users.id"), nullable=False)
	subject = Column(String(128), nullable=False)
	score = Colume(Integer, nullable=False)
	
	def __init__(self, *args, **kwargs):
        """initializes TestScores"""
        super().__init__(*args, **kwargs)
