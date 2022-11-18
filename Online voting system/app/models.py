from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, MetaData, Integer, String
# yauta browser open gara taaa
# tyoe aagi ko data pani aako ho its not a error hai 
# vote garna ko lagi location same hun
#face recognition window ma support gardaina hai error dina sakxa
# anilocation milo bhana matra vote garna apinxaa
# yauta valid user register gara hai ani check gara ta
# candidate pani register gara 
# qr code chai 127.0.0.1:8000/static/qrcodename
# tyo bhayo bhana I will explain block chain ko kura
# i will be back yakcin ma

Base = declarative_base()
metadata = MetaData()


class Voter(Base):
    __tablename__ = 'voter_tbl'
    voter_id = Column(Integer, primary_key = True, index = True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(String)
    location = Column(String)
    picture = Column(String)
    qr_code = Column(String)
    secret_key = Column(String)
    location = Column(Integer)
    citizenship_number = Column(String, unique = True)


class Candidate(Base):
    __tablename__ = 'candidate_tbl'
    candidate_id = Column(Integer, primary_key = True, index = True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(String)
    location = Column(String)
    picture = Column(String)
    location = Column(Integer)
    position = Column(Integer)
    citizenship_number = Column(String, unique = True)


class VoteStatus(Base):
    __tablename__ = 'votestatus'
    voted_status_id = Column(Integer, primary_key = True, index = True)
    voter_id = Column(Integer)
    candidate_id = Column(Integer)
    location = Column(Integer)
    position = Column(Integer)
