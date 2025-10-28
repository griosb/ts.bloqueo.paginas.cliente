from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root123@localhost:3306/pagesblock") #access of the db

meta_data = MetaData()

