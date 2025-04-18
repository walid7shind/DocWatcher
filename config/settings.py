import os
from dotenv import load_dotenv
load_dotenv()

QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
#might get an error here
REPO_URL = os.getenv("REPO_URL")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "code_chunks")
CHAT_COLLECTION = "chat_history"

