'''
Created on Sep 25, 2013

@author: kpaskov
'''

from model_perf_schema import Base, EqualityByIDMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, CLOB

class BindingSiteDetails(Base, EqualityByIDMixin):
    __tablename__ = 'binding_site_details'
    
    bioentity_id = Column('bioentity_id', Integer, primary_key=True)
    json = Column('json', CLOB)
            
    def __init__(self, bioentity_id, json):
        self.bioentity_id = bioentity_id
        self.json = json
        
    @hybrid_property
    def id(self):
        return self.bioentity_id
            
    def unique_key(self):
        return self.bioentity_id