from typing import List, Optional
from pydantic import BaseModel


class JobapplicationBase(BaseModel):
    status : str

class JobapplicationCreate(JobapplicationBase):
    pass
    
class Jobapplication(JobapplicationBase):
    id : int
    candidate_id : int
    job_id: int

    class Config:
        orm_mode = True


class CandidateBase(BaseModel):
    id : int
    candname : str
    candcity : str
    candmail : str
    contact : str
    candexperience : str
    willingtorelocate : str
    
class CandidateCreate(CandidateBase):
    pass
    
class Candidate(CandidateBase):
    id : int
    is_active : bool
    jobs_applied :List[Jobapplication] = []

    class Config:
        orm_mode = True

class JobBase(BaseModel):
    jobtitle : str
    jobdesc : str
    requirements : str
    skills : str
    experience :str
    locations :str
    salary : str
    companyname : str

class JobCreate(JobBase):
    pass
    
class Job(JobBase):
    id : int
    is_active : bool
    class Config:
        orm_mode = True

