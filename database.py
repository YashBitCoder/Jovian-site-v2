from sqlalchemy import create_engine

db_conn_str = "mysql+pymysql://9l6bdnj488yxc52t5k9b:pscale_pw_2snn41nY1E3E0U3jVOKBXnB5H98AMV5wJkmYJigbZoI@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(db_conn_str,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})
