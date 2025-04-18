from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from ingestion.embedder import get_embedder
from config import settings

client = QdrantClient(url=settings.QDRANT_URL, api_key=settings.QDRANT_API_KEY)

client.recreate_collection(
    collection_name="chat_history",
    vectors_config=VectorParams(
        size=get_embedder().embed_query("test").__len__(),
        distance=Distance.COSINE
    )
)

print("✅ 'chat_history' collection created.")
 
