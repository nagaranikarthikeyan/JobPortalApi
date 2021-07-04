from sqlalchemy.orm import Session
import models, schemas

def get_jobs(db:Session):
    return db.query(models.Jobs).all()

def create_job(db:Session,jobs:schemas.JobCreate):
    db_job = models.Jobs(**jobs.dict() )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_cand(db:Session):
    return db.query(models.Candidates).all()

def create_cadidate(db:Session,cand:schemas.Candidate):
    db_cand = models.Candidates(**cand.dict() )
    db.add(db_cand)
    db.commit()
    db.refresh(db_cand)
    return db_cand

def get_job_by_id(db: Session, id: int):
    return db.query(models.Jobs).filter(models.Jobs.id == id).first()

def update_job_by_id(db: Session, id: int , job = schemas.Job):
    db_job = db.query(models.Jobs).filter(models.Jobs.id == id).one_or_none()
    if db_job is None:
        return None
    for var, value in vars(job).items():
        setattr(db_job, var, value) if value else None

    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def delete_job_by_id(db: Session, id: int):
    db_job = db.query(models.Jobs).filter(models.Jobs.id == id).one_or_none()
    print("dele")
    print(db_job.jobtitle)
    db.delete(db_job)
    db.commit()
    return db_job

def apply_job(db: Session, jobs : schemas.JobapplicationCreate, job_id: int,cand_id:int,status='Open'):
    db_item = models.Jobapplication(**jobs.dict(), job_id=job_id,candidate_id=cand_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_jobsapplied_by_candid(db: Session, id: int):
    #db_job = db.query(models.Jobapplication).filter(models.Jobapplication.candidate_id == id).all()
    return db.query(models.Jobapplication).filter(models.Jobapplication.candidate_id == id).all()
    