'''
Created on Jul 24, 2013

@author: kpaskov
'''
from model_perf_schema import Base, EqualityByIDMixin
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, CLOB, String

class BioentMap(Base, EqualityByIDMixin):
    __tablename__ = 'bioent_map'
    
    id = Column('bioent_id', Integer, primary_key=True)
    format_name = Column('format_name', String)
    bioent_type = Column('bioent_type', String)
    json = Column('json', CLOB)
            
    def __init__(self, bioent_id, format_name, bioent_type, json):
        self.id = bioent_id
        self.format_name = format_name
        self.bioent_type = bioent_type
        self.json = json
            
    def unique_key(self):
        return (self.format_name, self.bioent_type)