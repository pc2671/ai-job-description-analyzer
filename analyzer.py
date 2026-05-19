# analyzer.py
# This file contains the main job description analysis logic.

from skills import TECHNICAL_SKILLS, TOOLS_TECHNOLOGIES, SOFT_SKILLS

def find_matches(text, keywords):
    """
    Find keywords that appear in the job description text.

    A simple Version 1 keyword matcher.
    It ignores capitalization by converting both the job text
    and keyword to lowercase.
    """
    text_lower = text.lower()
    matches = []

    for keyword in keywords:
        if keyword.lower() in text_lower:
            matches.append(keyword)
    return sorted(set(matches))

def estimate_experience_level(text):
    """
    Estimate the experience level based on words and phrases commonly 
    found in job descriptions.
    """
    text_lower = text.lower()

    senior_terms = [
        "senior", "staff", "principal", "lead",
        "5+ years", "6+ years", "7+ years", "8+ years", "9+ years", "10+ years"
    ]

    mid_terms = [
        "mid-level", "3+ years", "4+ years", "experienced", "professional experience"
    ]

    entry_terms = [
        "new grad", "entry-level", "new graduate", "junior", "0-1 years", "0-2 years"
        "1+ years", "internship"
    ]

    internship_terms = [
        "intern", "internship", "interns", "student", "students"
    ]

    
    if any(term in text_lower for term in senior_terms):
        return "Senior-level estimate"

    if any(term in text_lower for term in mid_terms):
        return "Mid-level estimate"
    
    if any(term in text_lower for term in entry_terms):
        return "Entry-level / junior estimate"
        
    if any(term in text_lower for term in internship_terms):
        return "Internship / entry-level estimate"
    
    return "Not clearly stated"


def create_summary(text, technical_skills, tools):
    """
    Create a simple summary based on detected skills and tools.
    """
    skill_part = ", ".join(technical_skills[:5]) if technical_skills else "general technical skills"
    tool_part = ", ".join(tools[:5]) if tools else "common development tools"

    return (
        "This job posting appears to be for a technical role. "
        f"It mentions skills such as {skill_part} and tools/technologies such as {tool_part}. "
        "The role likely requires problem solving, communication, and the ability to work with technical systems."
    )

def suggest_learning_topics(technical_skills, tools):
    """
    Suggest learning topics based on missing or detected skills
    """
    all_items = set(technical_skills + tools)
    topics = []

    if "Angular" in all_items or "TypeScript" in all_items:
        topics.append("Learn Angular and TypeScript frontend development")

    if ".NET Core" in all_items or "C#" in all_items:
        topics.append("Review .NET Core and C# backend development")

    if "Azure" in all_items:
        topics.append("Practice Azure cloud fundamentals")

    if "Azure Cosmos DB" in all_items or "Azure Blob Storage" in all_items:
        topics.append("Review Azure storage services: Cosmos DB and Blob Storage")

    if "Docker" in all_items or "CI/CD" in all_items or "Azure DevOps" in all_items:
        topics.append("Learn Docker, CI/CD pipelines, and Azure DevOps basics")

    if "Jasmine" in all_items or "Karma" in all_items or "Protractor" in all_items:
        topics.append("Review frontend testing with Jasmine, Karma, and Protractor")

    if "React" in all_items or "Vue" in all_items:
        topics.append("Review modern frontend frameworks such as React and Vue")

    if "Full-stack" in all_items:
        topics.append("Understand how frontend, backend, database, and cloud services work together")
    
    if not topics:
        topics = [
            "Review Python fundamentals",
            "Practice SQL basics",
            "Learn Git and GitHub workflow",
            "Review common software engineering interview topics"
        ]

    return topics


def analyze_job_description(text):
    """
    Main function that analyzes a job description.

    Returns a dictionary with all analysis results.
    """
    technical_skills = find_matches(text, TECHNICAL_SKILLS)
    tools = find_matches(text, TOOLS_TECHNOLOGIES)
    soft_skills = find_matches(text, SOFT_SKILLS)

    experience_level = estimate_experience_level(text)
    summary = create_summary(text, technical_skills, tools)

    resume_keywords = technical_skills + tools + soft_skills
    learning_topics = suggest_learning_topics(technical_skills, tools)

    return {
        "summary": summary,
        "skills": technical_skills,
        "tools": tools,
        "experience_level": experience_level,
        "resume_keywords": resume_keywords,
        "learning_topics": learning_topics,
    }