from sqlalchemy.orm import Session,sessionmaker
from  sqlalchemy import create_engine,Column,Integer,String,DateTime
from be.consetting import Setting
from sqlalchemy.ext.declarative import declarative_base

conn=Setting().GetConectionString()
engine=create_engine(str(conn))
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()

class M_Hazine(Base):
    __tablename__="ModiriatHazine"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    hazine=Column(Integer)
    place=Column(String)
    hazinebarayechechizi=Column(String)
    time=Column(DateTime)

    def __init__(self,title="",hazine=0,place="",hazinebarayechechizi="",time=None):
        self.title=title
        self.hazine=hazine
        self.place=place
        self.hazinebarayechechizi=hazinebarayechechizi
        self.time=time

Base.metadata.create_all(engine)

