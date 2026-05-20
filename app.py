import gradio as gr
from analyzer import analyze_job_description
from scraper import extract_text_from_url

# -------------------
# AI Job Description Analyzer - Version 1
#
# Thisi s the main Gradio app file.
#
# Current features:
# 1. User can paste a job posting URL
# 2. User can paste a job description manually
# 3. App returns strucrured analysis sectrions:
#       - short summary
#       - skill list
#       - tools / technologies
#       - experience level
#       - resume keywords
#       - suggested learning topics
# This is a basic prototype.
# Later will add:
# - real URL scraping
# - real keyword extraction
# - better seniority detection
# - resume matching

def analyze_job(url, pasted_text):
    """
    Analyze a job description and return structured career/job-search insights.

    Parameters:
        url (str): A job posting URL entered by the user.
        pasted_text (str): A job description pasted manually by the user.
    
    Returns:
        tuple: six text outputs:
            1. short summary
            2. skill list
            3. tools / technologies
            4. experience level
            5. resume keywords
            6. suggested learning topics
    """

    # clean up the pasted text by removing extra spaces at beginning / end.
    text = pasted_text.strip()
    source_note = ""

    # if the user pasted a JD, use it directly cuz it's more reliable than URL scraping
    if text:
        source_note = "Using pasted job description."
    # if no pasted text is provided, try to extract tedt from the URL
    elif url.strip():
        try:
            text = extract_text_from_url(url)
            source_note = "Using job description extracted from URL"
        except ValueError:
            return (
                "Could not extract the job description from this URL.\n\n"
                "Some job sites block automated text extraction or load content with JavaScript.\n\n"
                "Please paste the job description manually instead.",
                "",
                "",
                "",
                "",
                ""               
            )
    
    # if both fields are empty, ask the user to provide input
    else: 
        return (
            "Please enter a job URL or paste a job description",
            "",
            "",
            "",
            "",
            ""
        )
    
    result = analyze_job_description(text)

    summary = source_note + "\n\n" + result["summary"]
    skills = ", ".join(result["skills"]) if result["skills"] else "No specific technical skills detected yet."
    tools = ", ".join(result["tools"]) if result["tools"] else "No specific tools or technologies detected yet."
    experience_level = result["experience_level"]
    resume_keywords = ", ".join(result["resume_keywords"]) if result["resume_keywords"] else "No resume keywords detected yet."
    learning_topics = "\n".join(f"- {topic}" for topic in result["learning_topics"])

    return summary, skills, tools, experience_level, resume_keywords, learning_topics

# ------------------------------------------------------------
# Gradio Interface
#
# gr.Interface connects:
# - the Python function: analyze_job
# - the user inputs: URL box and job description box
# - the outputs: six analysis boxes
# ------------------------------------------------------------

demo = gr.Interface(
    fn=analyze_job,
    # User input components
    inputs=[
        gr.Textbox(
            label="Job Posting URL",
            placeholder="Paste a job posting URL here"
        ),
        gr.Textbox(
            label="Paste Job Description",
            lines=12,
            placeholder="Or paste the job description here"
        )
    ],
    # output components
    outputs=[
        gr.Textbox(label="Short summary"),
        gr.Textbox(label="Skills List"),
        gr.Textbox(label="Tools / Technologies"),
        gr.Textbox(label="Experience Level"),
        gr.Textbox(label="Resume Keywords"),
        gr.Textbox(label="Suggested Learning Topics"),
    ],
    title="AI Job Description Analyzer",

    description=(
        "Paste a job posting URL or job description text. "
        "The app will extract key skills, tools, experience level, "
        "resume keywords, and suggested learning topics."
    )
)

demo.launch()