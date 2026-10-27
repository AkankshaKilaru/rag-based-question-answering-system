def detect_persona(message):
    """
    Detect customer persona based on keywords.
    Returns:
    - Technical Expert
    - Frustrated User
    - Business Executive
    """

    message = message.lower()

    technical_keywords = [
        "api",
        "error",
        "authentication",
        "configuration",
        "logs",
        "debug",
        "server",
        "token",
        "integration",
        "endpoint"
    ]

    frustrated_keywords = [
        "frustrated",
        "angry",
        "nothing works",
        "terrible",
        "urgent",
        "annoyed",
        "fed up",
        "worst",
        "issue again",
        "still not working"
    ]

    executive_keywords = [
        "business",
        "impact",
        "operations",
        "revenue",
        "customers",
        "downtime",
        "productivity",
        "timeline",
        "resolution",
        "executive"
    ]

    for keyword in technical_keywords:
        if keyword in message:
            return "Technical Expert"

    for keyword in frustrated_keywords:
        if keyword in message:
            return "Frustrated User"

    for keyword in executive_keywords:
        if keyword in message:
            return "Business Executive"

    return "Business Executive"

def get_sentiment(message):

    message = message.lower()

    negative_words = [
        "frustrated",
        "angry",
        "annoyed",
        "terrible",
        "worst",
        "upset",
        "frustrating",
        "still not working",
        "nothing works",
        "fed up",
            ]

    positive_words = [
        "good",
        "great",
        "happy",
        "excellent",
        "thanks"
    ]

    for word in negative_words:
        if word in message:
            return "Negative"

    for word in positive_words:
        if word in message:
            return "Positive"

    return "Neutral"