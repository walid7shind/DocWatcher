import os
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from memory.safe_vector_memory import SafeVectorStoreRetrieverMemory

from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from config import settings

from ingestion.embedder import get_embedder

def get_conversational_chain_for_code():
    """
    Creates a ConversationalRetrievalChain that:
      - Uses a Qdrant collection for code retrieval (your codebase)
      - Stores conversation history in a separate Qdrant collection
    """
    client = QdrantClient(
        url=settings.QDRANT_URL,
        api_key=settings.QDRANT_API_KEY
    )
    embedding = get_embedder()

    code_vectorstore = QdrantVectorStore(
    client=client,
    collection_name=settings.QDRANT_COLLECTION,
    embedding=embedding
)

    chat_vectorstore = QdrantVectorStore.from_documents(
    documents=[],  
    embedding=embedding,
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY,
    collection_name="chat_history"
)



    
    memory = SafeVectorStoreRetrieverMemory(
    retriever=chat_vectorstore.as_retriever(),
    memory_key="chat_history",
    input_key="question",
    return_messages=False
)


    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(temperature=0, openai_api_key=settings.OPENAI_API_KEY),
        retriever=code_vectorstore.as_retriever(search_kwargs={"k": 4}),
        memory=memory
    )

    return chain
