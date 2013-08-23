'''
Created on Jul 24, 2013

@author: kpaskov
'''
from model_perf_schema import Base, EqualityByIDMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, CLOB

class GoReferences(Base, EqualityByIDMixin):
    __tablename__ = 'go_references'
    
    bioent_id = Column('bioent_id', Integer, primary_key=True)
    json = Column('json', CLOB)
            
    def __init__(self, bioent_id, json):
        self.bioent_id = bioent_id
        self.json = json
        
    @hybrid_property
    def id(self):
        return self.bioent_id
            
    def unique_key(self):
        return self.bioent_id