'''
Created on Jul 24, 2013

@author: kpaskov
'''
from model_perf_schema import Base, EqualityByIDMixin
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

class Bioentity(Base, EqualityByIDMixin):
    __tablename__ = 'bioentity'
    
    id = Column('bioentity_id', Integer, primary_key=True)
    format_name = Column('format_name', String)
    display_name = Column('display_name', String)
    class_type = Column('class', String)
    json = Column('json', String)
            
    def __init__(self, bioent_id, format_name, display_name, class_type, json):
        self.id = bioent_id
        self.format_name = format_name
        self.display_name = display_name
        self.class_type = class_type
        self.json = json

    def unique_key(self):
        return (self.format_name, self.class_type)