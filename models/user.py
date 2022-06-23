#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5
from flask_login import UserMixin


class User(BaseModel, UserMixin, Base):
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
	def get(cls, email=None, user_id=None):
		"""get user by email, id"""
		if user_id:
			users_dict = models.storage.all(cls)
			if users_dict:
				for key, value in users_dict.items():
					if value.id == user_id:
						return value
		
		if email:
			users_dict = models.storage.all(cls)
			if users_dict:
				for key, value in users_dict.items():
					if value.email == email:
						return value
						
		return None
		
		
	def check_password(self, password=None):
		"""password checker"""
		if self.password == md5(password.encode()).hexdigest():
			return True
		return False
