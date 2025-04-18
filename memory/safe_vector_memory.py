from langchain.memory import VectorStoreRetrieverMemory
from langchain_core.messages import BaseMessage

class SafeVectorStoreRetrieverMemory(VectorStoreRetrieverMemory):
    def _prep_inputs(self, inputs):
     
        inputs = super()._prep_inputs(inputs)

        if isinstance(inputs.get("chat_history"), list):
            inputs["chat_history"] = [
                msg.content if isinstance(msg, BaseMessage) else str(msg)
                for msg in inputs["chat_history"]
            ]

        return inputs
 
