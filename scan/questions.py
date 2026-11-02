"""Questionnaire content for the AI Readiness Scan.

Six dimensions, each scored 1-5 from three questions. The dimensions follow
common AI-maturity frameworks used in consulting: strategy, data, processes,
people, technology and governance.
"""

DIMENSIONS = {
    "strategy": "Strategy & Leadership",
    "data": "Data",
    "processes": "Processes",
    "people": "People & Skills",
    "technology": "Technology",
    "governance": "Risk & Governance",
}

# Each answer option maps to a score from 1 (low readiness) to 5 (high).
SCALE = {
    1: "Not at all",
    2: "A little",
    3: "Partly",
    4: "Mostly",
    5: "Fully",
}

QUESTIONS = [
    # Strategy & Leadership
    {"id": "s1", "dimension": "strategy",
     "text": "Leadership has a clear view of what AI could do for the business."},
    {"id": "s2", "dimension": "strategy",
     "text": "There is budget or time set aside to try AI tools this year."},
    {"id": "s3", "dimension": "strategy",
     "text": "We have identified specific problems (e.g. admin, scheduling, customer questions) AI could help with."},
    # Data
    {"id": "d1", "dimension": "data",
     "text": "Key business data (customers, bookings, finances) is stored digitally, not on paper."},
    {"id": "d2", "dimension": "data",
     "text": "Our data is reasonably complete, up to date and in one or a few systems."},
    {"id": "d3", "dimension": "data",
     "text": "We know who can access which data and it is stored securely."},
    # Processes
    {"id": "p1", "dimension": "processes",
     "text": "Our main workflows (booking, invoicing, onboarding, reporting) are written down or standardised."},
    {"id": "p2", "dimension": "processes",
     "text": "We regularly spot repetitive manual tasks that take up staff time."},
    {"id": "p3", "dimension": "processes",
     "text": "We measure basic performance numbers (e.g. no-shows, response time, occupancy)."},
    # People & Skills
    {"id": "h1", "dimension": "people",
     "text": "Staff are comfortable using digital tools in their daily work."},
    {"id": "h2", "dimension": "people",
     "text": "At least one person could take ownership of an AI pilot."},
    {"id": "h3", "dimension": "people",
     "text": "Staff are open to changing how they work if it saves time."},
    # Technology
    {"id": "t1", "dimension": "technology",
     "text": "We use modern cloud software (e.g. booking system, CRM, accounting software)."},
    {"id": "t2", "dimension": "technology",
     "text": "Our systems can connect or export data to other tools."},
    {"id": "t3", "dimension": "technology",
     "text": "Someone already uses AI tools like ChatGPT, Copilot or Claude for work tasks."},
    # Risk & Governance
    {"id": "g1", "dimension": "governance",
     "text": "We understand the privacy rules (GDPR) that apply to our customer data."},
    {"id": "g2", "dimension": "governance",
     "text": "We have guidelines on what staff may and may not put into AI tools."},
    {"id": "g3", "dimension": "governance",
     "text": "A person checks important AI outputs before they reach customers."},
]

# Sector presets tailor the example use cases in the report.
SECTORS = {
    "General small business": [
        "Drafting customer emails and social media posts",
        "Summarising meetings and documents",
        "Answering common customer questions with a website chatbot",
    ],
    "Fitness / sports studio": [
        "Automated class reminders and no-show follow-ups",
        "Chatbot for membership, pricing and schedule questions",
        "Personalised workout or nutrition tips for members",
    ],
    "Daycare / childcare": [
        "Drafting daily parent updates from staff notes",
        "Smart staff rostering based on child-to-staff ratios",
        "Answering parent questions about policies and fees",
    ],
    "Elderly care home": [
        "Turning spoken care notes into written reports",
        "Planning staff shifts around resident care needs",
        "Family update messages drafted from care records (with review)",
    ],
}
