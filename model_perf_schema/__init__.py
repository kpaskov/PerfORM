from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

class EqualityByIDMixin(object):
    def __eq__(self, other):
        if type(other) is type(self):
            return self.id == other.id
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
    
SCHEMA = None  
Base = None
metadata = None
    