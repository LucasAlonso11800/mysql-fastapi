from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Pulqui123*@localhost:3306/fastapi")

meta = MetaData()

conn = engine.connect()

