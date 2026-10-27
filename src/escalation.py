def should_escalate(query, confidence, history=None):
    query = query.lower().strip()

    if confidence < 60:
        return True

    sensitive_keywords = [
        "refund",
        "billing",
        "charged twice",
        "legal",
        "lawsuit",
        "manager",
        "human support",
        "account compromised",
        "unauthorized access",
    ]

    if any(word in query for word in sensitive_keywords):
        return True

    dissatisfaction_keywords = [
        "still not working",
        "again",
        "nothing works",
        "tried everything",
        "fed up",
        "very frustrated",
        "extremely angry",
        "worst experience",
    ]

    if any(word in query for word in dissatisfaction_keywords):
        return True

    history = history or []
    unsuccessful_turns = 0

    for item in history:
        previous_query = item.get("query", "").lower()
        previous_response = item.get("response", "").lower()
        previous_feedback = item.get("feedback", "").lower()

        if (
            any(word in previous_query for word in dissatisfaction_keywords)
            or previous_feedback in ["no", "👎 no", "not helpful"]
            or "error generating response" in previous_response
        ):
            unsuccessful_turns += 1

    return unsuccessful_turns >= 2
