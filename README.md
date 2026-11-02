# AI Readiness Scan

**A 5-minute diagnostic that tells a small business how ready it is to use AI, and what to do next.**

Small businesses hear a lot about AI but rarely know where to start. This tool asks 18 questions across six dimensions, scores the business from 1 to 5, and produces a practical report with priority gaps, sector-specific use cases and a 30-day plan.

![Radar chart of readiness scores](docs/radar.png)

## The business problem
- Owners of gyms, daycares and care homes want to save time with AI but lack the expertise to judge whether they are ready.
- Consultancies charge for AI maturity assessments; this tool brings a simplified version to businesses that cannot afford one.
- The goal: turn a vague "we should do something with AI" into one concrete, measurable first step.

## How it works
1. **Questionnaire:** 18 statements rated 1-5, grouped into six dimensions based on common AI-maturity frameworks:
   Strategy & Leadership, Data, Processes, People & Skills, Technology, Risk & Governance.
2. **Scoring:** dimension averages give an overall score and a readiness level (Beginner, Exploring, Developing, Advanced).
3. **Report:** the two weakest dimensions get targeted recommendations, plus use cases for the chosen sector (fitness studio, daycare, elderly care home or general small business) and a 30-day pilot plan.
4. **Optional AI summary:** with an Anthropic API key, Claude writes a short executive summary in consultant style. Without a key the tool still works fully.

See a full example: [sample_report.md](sample_report.md)

## Tech stack
- Python, Streamlit (web app), Plotly (radar chart)
- Anthropic Claude API (optional executive summary)
- pytest (unit tests for the scoring logic)

## Run it locally
```bash
git clone https://github.com/aafankhan4796-eng/ai-readiness-scan.git
cd ai-readiness-scan
pip install -r requirements.txt
streamlit run app.py
```
Optional AI summary: copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and add your API key.

Run the tests:
```bash
python -m pytest
```

## Project structure
```
app.py                  Streamlit interface
scan/questions.py       Questions, dimensions and sector use cases
scan/scoring.py         Scoring and readiness levels
scan/recommendations.py Recommendations per dimension
scan/report.py          Markdown report and optional AI summary
tests/                  Unit tests
```

## What I learned
- Structuring a fuzzy business question ("are we ready for AI?") into a clear framework, the same way consultants build diagnostics.
- Designing recommendations that are specific and actionable for non-technical owners.
- Building AI features that degrade gracefully: the tool is useful even without the AI part.

## Next steps
- Benchmark scores against other businesses in the same sector
- PDF export and email delivery of the report
- Validate the questionnaire with 10+ real business owners

---
Built by **Aafan Khan**, BSc Business Administration, University of Amsterdam · [LinkedIn](https://www.linkedin.com/in/aafan-khan)
