from dotenv import load_dotenv
import os 

load_dotenv()
AGENT_ID=os.getenv("AGENT_ID")
DATABASE_URL=os.getenv("DATABASE_URL")

print(AGENT_ID)
print(DATABASE_URL)