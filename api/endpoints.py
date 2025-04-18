from fastapi import APIRouter, Query
from vector_store.qdrant_client import get_qdrant_vectorstore
from ingestion.embedder import get_embedder
from config import settings
from retrieval.qa_chain import get_qa_chain
from utils.question_rewriter import get_question_rewriter

router = APIRouter()

embedder = get_embedder()
vectorstore = get_qdrant_vectorstore(
    embedding=embedder,
    collection_name=settings.QDRANT_COLLECTION
)
qa_chain   = get_qa_chain(vectorstore)
rewriter   = get_question_rewriter()

@router.get("/ask")
def ask_question(q: str = Query(...)):
    # ── rewrite the question ───────────────────────────────
    rewritten_msg = rewriter.invoke({"question": q})   # AIMessage
    rewritten     = getattr(rewritten_msg, "content", str(rewritten_msg))

    print(f"📝 Rewritten Question: {rewritten}")

    # ── run the RAG chain (string only!) ───────────────────
    result = qa_chain.invoke({"query": rewritten})     # use .invoke → future‑safe

    return {
        "original":   q,
        "rewritten":  rewritten,
        "answer":     result
    }
