def summarize_text(text):
    cleaned = text.strip()

    if len(cleaned) < 30:
        return "Text too short to summarize."

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Summarize the following text clearly."
                },
                {
                    "role": "user",
                    "content": cleaned[:4000]
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        # IMPORTANT: never crash the app
        return "AI summary is temporarily unavailable (API quota limit)."
