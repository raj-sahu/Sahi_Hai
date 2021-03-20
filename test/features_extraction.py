from dotenv import load_dotenv
import os
load_dotenv()
LOCALHOST_PATH = os.getenv("LOCALHOST_PATH")
DIRECTORY_NAME = os.getenv("DIRECTORY_NAME")
print(LOCALHOST_PATH)
