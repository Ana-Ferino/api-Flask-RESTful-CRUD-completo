from collections import namedtuple
from graphene import ObjectType, String, Int


class User(ObjectType):
    id = Int()  
    token = String()