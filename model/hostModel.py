from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import engine, meta_data


hostTable = Table("information_host",meta_data,
             Column("id",Integer, primary_key=True, autoincrement=True),
             Column("name", String(255), nullable=False),
             Column("ip", String(255), nullable=False)
             )

#create the table by host
meta_data.create_all(engine)