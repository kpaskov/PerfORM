'''
Created on Jul 24, 2013

@author: kpaskov
'''
from model_perf_schema import Base, EqualityByIDMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, CLOB
import json as json_loader

class Reference(Base, EqualityByIDMixin):
    __tablename__ = 'reference'
    
    id = Column('reference_id', Integer, primary_key=True)
    json = Column('json', CLOB)
            
    def __init__(self, reference_id, json):
        self.id = reference_id
        self.json = json
        
    @hybrid_property
    def format_name(self):
        return json_loader.loads(self.json)['format_name']
            
    def unique_key(self):
        return self.format_name
    
class ReferenceBib(Base, EqualityByIDMixin):
    __tablename__ = 'reference_bib'
    
    id = Column('reference_id', Integer, primary_key=True)
    json = Column('json', CLOB)
            
    def __init__(self, reference_id, json):
        self.id = reference_id
        self.json = json
        
    @hybrid_property
    def format_name(self):
        return json_loader.loads(self.json)['format_name']
            
    def unique_key(self):
        return self.format_name