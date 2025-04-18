from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

def get_question_rewriter():
    prompt = PromptTemplate.from_template("""
You are a senior developer assistant. Rewrite the following question to be more specific, grounded in JavaScript codebase terms (file names, routes, functions, variables), and optimized for internal code search.

Question: {question}

Rewritten:
""")

    llm = ChatOpenAI(temperature=0)

    chain = prompt | llm 
    return chain
