from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_docs(docs, chunk_size=1000, overlap=150):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    return splitter.split_documents(docs)
 
