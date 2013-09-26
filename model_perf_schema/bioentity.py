'''
Created on Jul 24, 2013

@author: kpaskov
'''
from model_perf_schema import Base, EqualityByIDMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, CLOB
import json as json_loader

class Bioentity(Base, EqualityByIDMixin):
    __tablename__ = 'bioentity'
    
    id = Column('bioentity_id', Integer, primary_key=True)
    json = Column('json', CLOB)
            
    def __init__(self, bioent_id, json):
        self.id = bioent_id
        self.json = json
        
    @hybrid_property
    def format_name(self):
        return json_loader.loads(self.json)['format_name']
        
    @hybrid_property
    def class_type(self):
        return json_loader.loads(self.json)['bioent_type']
            
    def unique_key(self):
        return (self.format_name, self.class_type)