from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/candidate/", response_model=List[schemas.Candidate])
def read_candidate( db: Session = Depends(get_db)):
    cands = crud.get_cand(db)
    print("hi")
    print(cands)
    return cands
    
@app.get("/jobs/", response_model=List[schemas.Job])
def read_jobs( db: Session = Depends(get_db)):
    jobs = crud.get_jobs(db)
    print("hi")
    print(jobs)
    return jobs

@app.get("/jobs/{job_id}", response_model=schemas.Job)
def read_job_by_id(job_id: int, db: Session = Depends(get_db)):
    db_job = crud.get_job_by_id(db, id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

@app.post("/jobs/update/{job_id}", response_model=schemas.Job)
def update_job_by_id(job_id: int,jobs: schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = crud.update_job_by_id(db=db, id=job_id,job=jobs)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job


@app.delete("/jobs/delete/{job_id}", response_model=schemas.Job)
def delete_job_by_id(job_id: int, db: Session = Depends(get_db)):
    db_job = crud.delete_job_by_id(db=db, id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

@app.post("/jobs/", response_model=schemas.Job)
def create_jobs(jobs: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db=db, jobs=jobs)

@app.post("/jobs/{job_id}/apply", response_model=schemas.Jobapplication)
def apply_jobs(job_id: int, jobs: schemas.JobapplicationCreate, db: Session = Depends(get_db)):
    return crud.apply_job(db=db, jobs=jobs,job_id=job_id,cand_id=101)

@app.get("/jobsapplied/{cand_id}",response_model=List[schemas.Jobapplication])
def read_job_by_id(cand_id: int, db: Session = Depends(get_db)):
    db_job = crud.get_jobsapplied_by_candid(db, id=cand_id)
    return db_job
