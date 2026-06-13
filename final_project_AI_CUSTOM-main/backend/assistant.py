from backend.cag import apply_context
from backend.knowledge import retrieve_snippets
from backend.store import context_store


def answer_question(user_id, question):
    snippets = retrieve_snippets(question)

    if not snippets:
        base_answer = "No encontre informacion suficiente en la base de conocimiento del curso."
        context_items = context_store.list_for_user(user_id)
        answer, context_used = apply_context(user_id, question, base_answer, context_items)
        return {
            "user_id": user_id,
            "answer": answer,
            "sources": [],
            "context_used": context_used,
        }

    source_text = " ".join(item["content"] for item in snippets)
    base_answer = f"Segun la base de conocimiento del curso: {source_text}"

    context_items = context_store.list_for_user(user_id)
    answer, context_used = apply_context(user_id, question, base_answer, context_items)

    return {
        "user_id": user_id,
        "answer": answer,
        "sources": [item["id"] for item in snippets],
        "context_used": context_used,
    }
