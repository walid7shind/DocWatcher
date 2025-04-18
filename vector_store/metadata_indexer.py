import re

def extract_metadata_from_text(text):
    classes = re.findall(r'class (\w+)', text)
    functions = re.findall(r'def (\w+)', text)
    return {
        "classes": classes,
        "functions": functions
    }

def enrich_chunks_with_metadata(chunks):
    for chunk in chunks:
        content = chunk.page_content
        metadata = extract_metadata_from_text(content)
        chunk.metadata.update(metadata)
    return chunks
 
