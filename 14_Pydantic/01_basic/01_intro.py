# Pydantic is a python library that provides certain things that are helpful in web dev as well as ML
# Data Validation, Setting Mangement, Data parsing, API development, Data Serilization/deserilaization

# Always import BaseModel
# Always give type annotations
# Always use an unpacked dictionary, at the time of model init or model initiation
# Pydantic will always try to convert the given value into the decided type, The model ensures that 
# the data integrity is, uh, at the point of creation.

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id': '101a', 'name': "Chaicode", 'is_active': True}

user = User(**input_data)
print(user)


# If I would have written this in pure CPython it wouldn't have given me 
# class User:
#     def __init__(self, id, name, is_active):
#         self.id = id
#         self.name = name
#         self.is_active = is_active

# input_data = {'id': '101a', 'name': "Chaicode", 'is_active': True}

# user = User(**input_data)
# print(user.__dict__)