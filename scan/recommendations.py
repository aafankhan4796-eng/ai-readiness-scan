"""Rule-based recommendations per dimension, so the tool works without an API key."""

RECOMMENDATIONS = {
    "strategy": [
        "List your three most time-consuming tasks and rank them by how much an AI tool could save.",
        "Set a small, fixed budget (time or money) for one 4-week AI pilot.",
        "Agree on one success metric for the pilot, such as hours saved per week.",
    ],
    "data": [
        "Move customer, booking and financial records into one digital system.",
        "Clean up duplicates and missing fields in your main customer list.",
        "Write down who has access to which data and remove access that isn't needed.",
    ],
    "processes": [
        "Document your top three workflows step by step; AI can only improve what is clear.",
        "Track how long repetitive tasks take for two weeks to find the biggest time sinks.",
        "Start measuring 2-3 simple KPIs, such as no-show rate or response time.",
    ],
    "people": [
        "Appoint one 'AI champion' to test tools and share what works.",
        "Run a one-hour hands-on session where staff try an AI assistant on real tasks.",
        "Share early wins openly to build trust and reduce resistance to change.",
    ],
    "technology": [
        "Check whether your current software already has built-in AI features you are not using.",
        "Prefer cloud tools that can export data or connect to other systems.",
        "Give the team access to one approved AI assistant instead of many personal accounts.",
    ],
    "governance": [
        "Write a one-page AI policy: what data may never go into AI tools, and who reviews outputs.",
        "Check that any AI vendor complies with GDPR and stores data in the EU where possible.",
        "Keep a human review step for anything AI writes that customers will see.",
    ],
}


def recommendations_for(gaps: list, per_gap: int = 3) -> dict:
    """Return recommendations for the weakest dimensions."""
    return {dim: RECOMMENDATIONS[dim][:per_gap] for dim in gaps}
