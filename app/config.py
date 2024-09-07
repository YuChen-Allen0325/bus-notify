import os
from dotenv import load_dotenv
load_dotenv()


class PostgresConfig:
    URL = os.environ.get("PG_URL")
    DB_NAME = os.environ.get("PG_DB_NAME")
    PORT = os.environ.get("PG_PORT")
    USERNAME = os.environ.get("PG_USERNAME")
    PASSWORD = os.environ.get("PG_PASSWORD")


class BusConfig:
    Route_URL = os.environ.get("Bus_Route_URL")
    Stop_URL = os.environ.get("Bus_Stop_URL")
    Event_URL = os.environ.get("Bus_Event_URL")


class GmailServiceConfig:
    Sender_eamil = os.environ.get("Gmail_Service_Sender_eamil")
    App_Password = os.environ.get("Gmail_Service_App_Password")
    Smtp_Server = os.environ.get("Gmail_Service_Smtp_Server")
    Port = os.environ.get("Gmail_Service_Port")