def clean_docs(docs):
  #gotta add some sick ahh cleaning logic right here
    for doc in docs:
        doc.metadata["source"] = doc.metadata.get("source", "unknown")
    return docs
 
