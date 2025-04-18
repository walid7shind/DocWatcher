from langchain_openai import OpenAIEmbeddings
from config import settings

def get_embedder():
    return OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
 
