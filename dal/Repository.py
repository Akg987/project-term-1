from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from be.consetting import Setting
from be.server import M_Hazine

class Repository:
    def __init__(self):
        conn = Setting().GetConectionString()
        self.engine = create_engine(str(conn))
        self.Session = sessionmaker(bind=self.engine)
        
    def insert(self, obj):
        session = self.Session()
        try:
            session.add(obj)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(f"Error inserting object: {e}")
            return str(e)
        finally:
            session.close()


    def Read(self,obj):
        session = self.Session()
        return session.query(obj).all()



    def Update(self, obj, id):
        session = self.Session()
        try:
            existing_obj = self.ReadById(id)
            if existing_obj:
                session.query(M_Hazine).filter(M_Hazine.id == id).update({
                    M_Hazine.title: obj.title,
                    M_Hazine.hazine: obj.hazine,
                    M_Hazine.place: obj.place,
                    M_Hazine.hazinebarayechechizi: obj.hazinebarayechechizi,
                    M_Hazine.time: obj.time
                })
                session.commit()
                return True
            else:
                print(f"No object found with ID: {id}")
                return False
        except Exception as e:
            session.rollback()
            print(f"Error updating object: {e}")
            return str(e)
        finally:
            session.close()

    def Delete(self, id):
        session = self.Session()
        try:
            obj = session.query(M_Hazine).filter(M_Hazine.id == id).first()
            if obj:
                session.delete(obj)
                session.commit()
                return True
            else:
                print(f"No object found with ID: {id}")
                return False
        except Exception as e:
            session.rollback()
            print(f"Error deleting object: {e}")
            return str(e)
        finally:
            session.close()
    def ReadById(self, id):
        session = self.Session()
        return session.query(M_Hazine).filter(M_Hazine.id == id).first()
    def ReadAllHazine(self):
        session = self.Session()
        return session.query(M_Hazine).all()
