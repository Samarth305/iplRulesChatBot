from typing import List, Dict
from interface.base_response_generator import BaseResponseGenerator
from util.invoke_ai import invoke_ai


SYSTEM_PROMPT = """
Use the provided context to provide a concise answer to the user's question.
If you cannot find the answer in the context, say so. Do not make up information.
"""


class ResponseGenerator(BaseResponseGenerator):
    def rewrite_query(self, query: str, history: List[Dict]) -> str:
        """Rewrite the query to make it standalone using chat history."""
        if not history:
            return query
            
        history_text = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in history[-5:]])
        system_message = "You are a query rewriter. Given a chat history and a follow-up query, rewrite the follow-up query to be a standalone question that can be understood without the chat history. Do not answer the question, just rewrite it. If the query is already standalone, return it exactly as is."
        user_message = f"<chat_history>\n{history_text}\n</chat_history>\n<follow_up_query>\n{query}\n</follow_up_query>"
        
        rewritten_query = invoke_ai(system_message=system_message, user_message=user_message)
        print(f"🔄 Rewrote query: '{query}' -> '{rewritten_query}'")
        return rewritten_query

    def generate_response(self, query: str, context: List[str], history: List[Dict] = None) -> str:
        """Generate a response using the AI model."""
        context_text = "\n".join(context)
        
        history_text = ""
        if history:
            history_text = "<chat_history>\n" + "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in history[-5:]]) + "\n</chat_history>\n"
            
        user_message = (
            f"{history_text}"
            f"<context>\n{context_text}\n</context>\n"
            f"<question>\n{query}\n</question>"
        )

        return invoke_ai(system_message=SYSTEM_PROMPT, user_message=user_message)
