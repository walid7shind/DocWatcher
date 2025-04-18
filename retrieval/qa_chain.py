from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

def get_qa_chain(vectorstore):
    llm = ChatOpenAI(temperature=0)

    prompt = PromptTemplate.from_template("""
You are a helpful assistant that answers questions about a codebase. Be concise, cite file names, and do not guess if unsure.

Context:
{context}

Question:
{question}

Answer:
""")

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )
