from datetime import datetime, timezone
from database import base
import sqlalchemy as sql
import sqlalchemy.orm as orm

class RAM(base):
    __tablename__ = "ram"
    id=sql.Column(sql.Integer,primary_key=True,index=True)
    ram_used=sql.Column(sql.Float , index=True)
    ram_total=sql.Column(sql.Float,index=True)
    from datetime import datetime, timezone
    date = sql.Column(
    sql.DateTime(timezone=True),
    default=lambda: datetime.now(timezone.utc)
)

class Disk(base):
     __tablename__ = "disk"
     id=sql.Column(sql.Integer,primary_key=True,index=True)
     disk_total=sql.Column(sql.Float , index=True )
     disk_used=sql.Column(sql.Float , index=True )
     disk_free=sql.Column(sql.Float , index=True )
     date = sql.Column(
         sql.DateTime(timezone=True),
         default=lambda: datetime.now(timezone.utc)
     )


class CPU(base):
     __tablename__ = "cpu"
     id= sql.Column(sql.Integer,primary_key=True,index=True)
     percent= sql.Column(sql.Float,index=True)
     coures_logical= sql.Column(sql.Integer , index=True )
     coures_pysical= sql.Column(sql.Integer, index=True )
     date = sql.Column(
             sql.DateTime(timezone=True),
             default=lambda: datetime.now(timezone.utc)
         )



     
