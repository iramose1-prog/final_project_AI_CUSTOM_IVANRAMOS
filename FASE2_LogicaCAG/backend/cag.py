def apply_context(user_id, question, base_answer, context_items):
    if not context_items:
        return base_answer, []

    answer = base_answer
    keys_used = []

    for item in context_items:
        key = item["key"]
        value = item["value"]

        if key == "audience":
            answer = f"Explicado para {value}: {answer}"
            keys_used.append(key)
        elif key == "preferred_style":
            style_phrases = {
                "explicaciones con analogias": "Para explicarlo con una analogia: ",
            }
            prefix = style_phrases.get(value)
            if prefix:
                answer = f"{prefix}{answer}"
                keys_used.append(key)

    return answer, keys_used
