import imp
from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

#all db tables will share this
#for common attrs
@as_declarative()
class Base:
    id: Any
    __name__ : str

    #to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()