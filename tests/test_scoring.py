import pytest

from scan.questions import QUESTIONS
from scan.report import build_report
from scan.scoring import score


def all_answers(value):
    return {q["id"]: value for q in QUESTIONS}


def test_all_ones_is_beginner():
    result = score(all_answers(1))
    assert result.overall == 1.0
    assert result.level == "Beginner"


def test_all_fives_is_advanced():
    result = score(all_answers(5))
    assert result.overall == 5.0
    assert result.level == "Advanced"


def test_level_thresholds():
    assert score(all_answers(2)).level == "Exploring"
    assert score(all_answers(3)).level == "Developing"
    assert score(all_answers(4)).level == "Advanced"


def test_gaps_are_weakest_dimensions():
    answers = all_answers(4)
    for q in QUESTIONS:
        if q["dimension"] == "data":
            answers[q["id"]] = 1
        if q["dimension"] == "governance":
            answers[q["id"]] = 2
    result = score(answers)
    assert result.gaps == ["data", "governance"]
    assert "data" not in result.strengths


def test_missing_answer_raises():
    answers = all_answers(3)
    answers.pop("s1")
    with pytest.raises(ValueError):
        score(answers)


def test_out_of_range_raises():
    answers = all_answers(3)
    answers["s1"] = 7
    with pytest.raises(ValueError):
        score(answers)


def test_report_contains_key_sections():
    result = score(all_answers(3))
    report = build_report("Test Gym", "Fitness / sports studio", result)
    assert "AI Readiness Report: Test Gym" in report
    assert "Priority gaps and next steps" in report
    assert "no-show" in report
