from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Text , Date
from sqlalchemy.orm import relationship
from database import Base


class Jobs(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    jobtitle = Column(String)
    requirements = Column(Text)
    jobdesc = Column(Text)
    skills = Column(String)
    experience = Column(String)
    locations = Column(String)
    salary = Column(String)
    companyname = Column(String)
    is_active = Column(Boolean, default=True)

class Jobapplication(Base):
    __tablename__ = "jobapplication"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    candidate = relationship("Candidates", back_populates="jobs_applied")

class Candidates(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    candname = Column(String)
    candcity = Column(String)
    candmail = Column(String)
    contact = Column(String)
    candexperience = Column(String)
    willingtorelocate = Column(String)
    is_active = Column(Boolean, default=True)
    jobs_applied = relationship("Jobapplication", back_populates="candidate")


    
    
