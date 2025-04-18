from qdrant_client import QdrantClient
from langchain_qdrant import Qdrant

from ingestion.embedder import get_embedder
from config import settings

def upload_to_qdrant(chunks):
    embedder = get_embedder()

    return Qdrant.from_documents(
        documents=chunks,
        embedding=embedder,
        url=settings.QDRANT_URL,
        api_key=settings.QDRANT_API_KEY,
        collection_name=settings.QDRANT_COLLECTION
    )
def get_qdrant_vectorstore(embedding, collection_name):
    client = QdrantClient(
        url=settings.QDRANT_URL,
        api_key=settings.QDRANT_API_KEY
    )
    return Qdrant(
    client=client,
    collection_name=collection_name,
    embeddings=embedding  # <- plural and correct name
)

