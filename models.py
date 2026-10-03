from datetime import datetime, timezone
from database import base
import sqlalchemy as sql
import sqlalchemy.orm as orm


class RAM(base):
    __tablename__ = "ram"
    id=sql.Column(sql.Integer,primary_key=True,index=True)
    agent_id=sql.Column(sql.String, index=True)
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
     agent_id=sql.Column(sql.String, index=True)
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
     agent_id=sql.Column(sql.String, index=True)
     percent= sql.Column(sql.Float,index=True)
     coures_logical= sql.Column(sql.Integer , index=True )
     coures_pysical= sql.Column(sql.Integer, index=True )
     date = sql.Column(
             sql.DateTime(timezone=True),
             default=lambda: datetime.now(timezone.utc)
         )


class Processes(base):
     __tablename__= "processes"
     id= sql.Column(sql.Integer,primary_key=True,index=True)
     agent_id=sql.Column(sql.String, index=True)
     pid= sql.Column(sql.Integer,index=True)
     name= sql.Column(sql.String ,index=True)
     cpu_percent= sql.Column(sql.Float ,index=True)
     ram_percent= sql.Column(sql.Float ,index=True)
     status= sql.Column(sql.String ,index=True)
     date = sql.Column(
                  sql.DateTime(timezone=True),
                  default=lambda: datetime.now(timezone.utc)
              )
     
     

class TcpPing(base):
    __tablename__ = "tcp_ping"

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True ,index=True)
    agent_id=sql.Column(sql.String, index=True)
    host = sql.Column(sql.String, nullable=False ,index=True)
    port = sql.Column(sql.Integer , nullable=False ,index=True)
    connected = sql.Column(sql.Boolean, nullable=False ,index=True)
    date = sql.Column(
                    sql.DateTime(timezone=True),
                    default=lambda: datetime.now(timezone.utc)
                       )

     
