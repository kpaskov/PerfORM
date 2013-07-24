'''
Created on Jul 24, 2013

@author: kpaskov
'''
from model_perf_schema import Base, EqualityByIDMixin
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, CLOB

class BioentInteractionOverview(Base, EqualityByIDMixin):
    __tablename__ = 'bioent_interaction_overview'
    
    bioent_id = Column('bioent_id', Integer, primary_key=True)
    json = Column('json', CLOB)
            
    def __init__(self, bioent_id, json):
        self.bioent_id = bioent_id
        self.json = json
            
    def unique_key(self):
        return self.bioent_id
    
class BioentInteractionEvidence(Base, EqualityByIDMixin):
    __tablename__ = 'bioent_interaction_evidence'
    
    bioent_id = Column('bioent_id', Integer, primary_key=True)
    json = Column('json', CLOB)
            
    def __init__(self, bioent_id, json):
        self.bioent_id = bioent_id
        self.json = json
            
    def unique_key(self):
        return self.bioent_id
    
class BioentInteractionGraph(Base, EqualityByIDMixin):
    __tablename__ = 'bioent_interaction_graph'
    
    bioent_id = Column('bioent_id', Integer, primary_key=True)
    json = Column('json', CLOB)
            
    def __init__(self, bioent_id, json):
        self.bioent_id = bioent_id
        self.json = json
            
    def unique_key(self):
        return self.bioent_id
    
class BioentInteractionEvidenceResource(Base, EqualityByIDMixin):
    __tablename__ = 'bioent_interaction_ev_resource'
    
    bioent_id = Column('bioent_id', Integer, primary_key=True)
    json = Column('json', CLOB)
            
    def __init__(self, bioent_id, json):
        self.bioent_id = bioent_id
        self.json = json
            
    def unique_key(self):
        return self.bioent_id