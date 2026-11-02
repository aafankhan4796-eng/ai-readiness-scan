"""Scoring logic: turns answers into dimension scores and a readiness level."""

from dataclasses import dataclass

from .questions import DIMENSIONS, QUESTIONS

LEVELS = [
    (1.0, "Beginner", "AI is not yet on the radar. Start with basics: digital data and one small experiment."),
    (2.0, "Exploring", "There is interest, but foundations are missing. Fix data and pick one clear use case."),
    (3.0, "Developing", "Foundations are in place. You are ready for a focused AI pilot."),
    (4.0, "Advanced", "You can scale AI across teams. Focus on governance and measuring impact."),
]


@dataclass
class ScanResult:
    dimension_scores: dict  # dimension key -> average score (1-5)
    overall: float          # average of dimension scores (1-5)
    level: str
    level_description: str
    strengths: list         # dimension keys, strongest first
    gaps: list              # dimension keys, weakest first


def score(answers: dict) -> ScanResult:
    """Score a completed questionnaire.

    answers: question id -> integer 1..5. Every question must be answered.
    """
    missing = [q["id"] for q in QUESTIONS if q["id"] not in answers]
    if missing:
        raise ValueError(f"Missing answers for: {', '.join(missing)}")
    for qid, value in answers.items():
        if not isinstance(value, int) or not 1 <= value <= 5:
            raise ValueError(f"Answer for {qid} must be an integer from 1 to 5, got {value!r}")

    totals = {key: [] for key in DIMENSIONS}
    for q in QUESTIONS:
        totals[q["dimension"]].append(answers[q["id"]])
    dimension_scores = {k: round(sum(v) / len(v), 2) for k, v in totals.items()}

    overall = round(sum(dimension_scores.values()) / len(dimension_scores), 2)

    level, description = LEVELS[0][1], LEVELS[0][2]
    for threshold, name, desc in LEVELS:
        if overall >= threshold:
            level, description = name, desc

    ranked = sorted(dimension_scores, key=dimension_scores.get, reverse=True)
    return ScanResult(
        dimension_scores=dimension_scores,
        overall=overall,
        level=level,
        level_description=description,
        strengths=ranked[:2],
        gaps=list(reversed(ranked))[:2],
    )
