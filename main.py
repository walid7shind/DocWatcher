from memory.conversational_memory import get_conversational_chain_for_code

def ask(chain, question):
    result = chain({
        "question": question,
        "chat_history": []  # Managed internally by Qdrant memory
    })

    print(" Answer:", result["answer"])
    return result["answer"]

if __name__ == "__main__":
    chain = get_conversational_chain_for_code()

    while True:
        q = input("\n❓ Ask a question ('q' to quit):\n> ")
        if q.lower() in ["q", "quit", "exit"]:
            break
        ask(chain, q)
