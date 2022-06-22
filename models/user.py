#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
	"""Representation of a user"""
	__tablename__ = 'users'
	email = Column(String(128), nullable=False)
	password = Column(String(128), nullable=False)
	first_name = Column(String(128), nullable=True)
	last_name = Column(String(128), nullable=True)
	tests = relationship("TestScore", backref="user")


	def __init__(self, *args, **kwargs):
		"""initializes user"""
		super().__init__(*args, **kwargs)
        
        
	def __setattr__(self, name, value):
		"""sets attributes"""
		if name == "password":
			value = md5(value.encode()).hexdigest()
			
		super().__setattr__(name, value)

	@classmethod
	def get(cls, email=None):
		"""get user by email"""
		if email:
			users_dict = models.storage.all(cls)
			if users_dict:
				for user in users_dict:
					if user.email == email:
						return user
						
		return None
		
		
	def check_password(self, password=None):
		"""password checker"""
		if self.password == password:
			return True
		return False
