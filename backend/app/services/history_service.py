from app.core.supabase_client import supabase


def save_research(
    question: str,
    answer: str
):
    supabase.table(
        "research_history"
    ).insert({
        "question": question,
        "answer": answer
    }).execute()


def get_research_history():

    response = (
        supabase.table(
            "research_history"
        )
        .select("*")
        .order(
            "created_at",
            desc=True
        )
        .execute()
    )

    return response.data