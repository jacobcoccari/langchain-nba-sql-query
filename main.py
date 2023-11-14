# import load_dotenv()
from dotenv import load_dotenv
load_dotenv()

# Creating the connection to the model.
from langchain.chat_models import ChatOpenAI
model = ChatOpenAI()

# Now we need to create the connection to the database.
from langchain.utilities import SQLDatabase
db = SQLDatabase.from_uri("sqlite:///nba_roster.db")

string = db.get_table_names()

