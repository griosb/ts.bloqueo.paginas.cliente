from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import engine, meta_data


#table of pages with the domain
pageTable = Table("UrlPages", meta_data,
             Column("id", Integer, primary_key=True, autoincrement=True),
             Column("Domain", String(255), nullable=False)
             )

meta_data.create_all(engine) #create the table