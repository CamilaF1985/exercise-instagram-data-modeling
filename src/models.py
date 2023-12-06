import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

# Definición de la base de datos declarativa
Base = declarative_base()

# Entidad User: Representa a un usuario en la plataforma
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    username = Column(String(250), unique=True, nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)  # Columna de email añadida directamente

# Entidad Follower: Representa la relación de seguimiento entre usuarios
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)

# Entidad Post: Representa un post creado por un usuario
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

# Entidad Comment: Representa un comentario en un post
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

# Entidad Media: Representa los medios asociados a un post (imágenes o videos)
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    type = Column(Enum('image', 'video', name='media_type'), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

# Renderizar el diagrama UML
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e





