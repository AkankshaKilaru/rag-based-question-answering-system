from src.persona import detect_persona

print(
    detect_persona(
        "Can you explain API authentication failure?"
    )
)

print(
    detect_persona(
        "I am frustrated. Nothing works."
    )
)

print(
    detect_persona(
        "What is the business impact of this issue?"
    )
)