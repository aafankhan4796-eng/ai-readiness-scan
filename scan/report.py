"""Builds the readiness report.

A template-based Markdown report always works. If an Anthropic API key is set,
an optional AI-written executive summary is added on top.
"""

import os
from datetime import date

from .questions import DIMENSIONS, SECTORS
from .recommendations import recommendations_for
from .scoring import ScanResult

DEFAULT_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5")


def build_report(business_name: str, sector: str, result: ScanResult) -> str:
    """Return the full report as Markdown."""
    name = business_name.strip() or "Your business"
    lines = [
        f"# AI Readiness Report: {name}",
        f"*Sector: {sector} | Date: {date.today().isoformat()}*",
        "",
        f"## Overall readiness: {result.overall:.1f} / 5 ({result.level})",
        result.level_description,
        "",
        "## Scores by dimension",
        "| Dimension | Score (1-5) |",
        "|---|---|",
    ]
    for key, label in DIMENSIONS.items():
        lines.append(f"| {label} | {result.dimension_scores[key]:.1f} |")

    lines += ["", "## Strengths"]
    lines += [f"- **{DIMENSIONS[d]}** ({result.dimension_scores[d]:.1f})" for d in result.strengths]

    lines += ["", "## Priority gaps and next steps"]
    for dim, recs in recommendations_for(result.gaps).items():
        lines.append(f"### {DIMENSIONS[dim]} ({result.dimension_scores[dim]:.1f})")
        lines += [f"- {r}" for r in recs]

    lines += ["", f"## AI use cases to explore ({sector})"]
    lines += [f"- {u}" for u in SECTORS.get(sector, SECTORS["General small business"])]

    lines += [
        "",
        "## Suggested 30-day plan",
        "1. **Week 1:** Pick one use case above and define one success metric.",
        f"2. **Week 2:** Fix the basics in your weakest area: {DIMENSIONS[result.gaps[0]]}.",
        "3. **Week 3:** Run a small pilot with one team or process.",
        "4. **Week 4:** Measure the result and decide to stop, adjust or scale.",
    ]
    return "\n".join(lines)


def ai_summary(business_name: str, sector: str, result: ScanResult, api_key: str | None = None) -> str | None:
    """Optional: ask Claude for a short executive summary. Returns None if unavailable."""
    api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    try:
        import anthropic
    except ImportError:
        return None

    scores = ", ".join(f"{DIMENSIONS[k]}: {v:.1f}" for k, v in result.dimension_scores.items())
    prompt = (
        "You are a management consultant advising a small business on AI adoption. "
        f"Business: {business_name or 'a small business'} (sector: {sector}). "
        f"AI readiness scores out of 5: {scores}. Overall {result.overall:.1f} ({result.level}). "
        "Write a 120-word executive summary in plain English: where they stand, the single most "
        "important next step, and one concrete AI use case for their sector. No bullet points."
    )
    try:
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model=DEFAULT_MODEL,
            max_tokens=400,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text.strip()
    except Exception:
        return None
