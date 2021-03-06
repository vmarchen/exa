# -*- coding: utf-8 -*-
'''
Project
===============================================
'''
from sqlalchemy import String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from exa.utils import gen_uid
from exa.relational.base import datetime, Base, Column, Integer


ProjectJob = Table(
    'projectjob',
    Base.metadata,
    Column('project_pkid', Integer, ForeignKey('project.pkid', onupdate='CASCADE', ondelete='CASCADE')),
    Column('job_pkid', Integer, ForeignKey('job.pkid', onupdate='CASCADE', ondelete='CASCADE'))
)
ProjectContainer = Table(
    'projectcontainer',
    Base.metadata,
    Column('project_pkid', Integer, ForeignKey('project.pkid', onupdate='CASCADE', ondelete='CASCADE')),
    Column('container_pkid', Integer, ForeignKey('container.pkid', onupdate='CASCADE', ondelete='CASCADE'))
)
ProjectFile = Table(
    'projectfile',
    Base.metadata,
    Column('project_pkid', Integer, ForeignKey('project.pkid', onupdate='CASCADE', ondelete='CASCADE')),
    Column('file_pkid', Integer, ForeignKey('file.pkid', onupdate='CASCADE', ondelete='CASCADE'))
)


class Project(Base):
    '''
    Carefully planned enterprise to achieve a specific aim.
    '''
    name = Column(String)
    description = Column(String)
    created = Column(DateTime, default=datetime.now)
    modified = Column(DateTime, default=datetime.now)
    accessed = Column(DateTime, default=datetime.now)
    size = Column(Integer)
    file_count = Column(Integer)
    jobs = relationship('Job', secondary=ProjectJob, backref='projects', cascade='all, delete')
    containers = relationship('Container', secondary=ProjectContainer, backref='projects', cascade='all, delete')
    files = relationship('File', secondary=ProjectFile, backref='projects', cascade='all, delete')
