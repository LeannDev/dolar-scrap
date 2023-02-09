import os
from dotenv import load_dotenv
import psycopg2

# load dotenv
load_dotenv()

# DATABASE ENV
DATABASE = {
    'NAME': os.getenv('NAME_DB'),
    'USER': os.getenv('USER_DB'),
    'PASSWORD': os.getenv('PASSWORD_DB'),
    'HOST': os.getenv('HOST_DB'),
    'PORT': os.getenv('PORT_DB')
}

# connect database
con = psycopg2.connect(
    host=DATABASE["HOST"],
    port=DATABASE["PORT"],
    user=DATABASE["USER"],
    password=DATABASE["PASSWORD"],
    database=DATABASE["NAME"],
)