'''
Created on Jul 24, 2013

@author: kpaskov
'''

from model_perf_schema import Base, EqualityByIDMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, CLOB

class RegulationOverview(Base, EqualityByIDMixin):
    __tablename__ = 'regulation_overview'
    
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
    
class RegulationDetails(Base, EqualityByIDMixin):
    __tablename__ = 'regulation_details'
    
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
    
class RegulationGraph(Base, EqualityByIDMixin):
    __tablename__ = 'regulation_graph'
    
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
    
class RegulationReferences(Base, EqualityByIDMixin):
    __tablename__ = 'regulation_references'
    
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
