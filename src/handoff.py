def create_handoff(
    persona,
    query,
    sources
):

    return {
        "persona": persona,
        "issue": query,
        "documents_used": sources,
        "recommendation":
        "Escalate to human support"
    }