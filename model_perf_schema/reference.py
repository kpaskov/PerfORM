'''
Created on Jul 24, 2013

@author: kpaskov
'''
from model_perf_schema import Base, EqualityByIDMixin
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, CLOB

class Reference(Base, EqualityByIDMixin):
    __tablename__ = 'reference'
    
    id = Column('reference_id', Integer, primary_key=True)
    json = Column('json', String)
            
    def __init__(self, reference_id, json):
        self.id = reference_id
        self.json = json
        
    def unique_key(self):
        return self.id
    
class Bibentry(Base, EqualityByIDMixin):
    __tablename__ = 'reference_bibentry'
    
    id = Column('reference_id', Integer, primary_key=True)
    json = Column('json', CLOB)
            
    def __init__(self, reference_id, json):
        self.id = reference_id
        self.json = json
        
    def unique_key(self):
        return self.id