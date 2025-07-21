# streamlit_app.py
import streamlit as st
import random
from typing import Dict, List, Tuple
import json

# Configure page
st.set_page_config(
    page_title="Interview Practice App",
    page_icon="💼",
    layout="wide"
)

# Question bank with answers and keywords
QUESTION_BANK = {
    "Scrum Master": {
        "questions": [
            {
                "question": "What are the three pillars of Scrum?",
                "keywords": ["transparency", "inspection", "adaptation"],
                "answer": "The three pillars of Scrum are Transparency (making work visible), Inspection (regularly examining artifacts and progress), and Adaptation (adjusting based on inspection results)."
            },
            {
                "question": "How do you handle impediments in a sprint?",
                "keywords": ["identify", "escalate", "remove", "track", "prioritize"],
                "answer": "Identify impediments early, work to remove them directly if possible, escalate to management when needed, track them visually, and prioritize based on impact to the team."
            },
            {
                "question": "What is the difference between velocity and capacity?",
                "keywords": ["velocity", "historical", "capacity", "availability", "planning"],
                "answer": "Velocity is a historical measure of how much work a team completes per sprint, while capacity is the amount of work a team can take on in an upcoming sprint based on availability and other factors."
            },
            {
                "question": "How do you facilitate a retrospective meeting?",
                "keywords": ["safe space", "what went well", "improvement", "action items", "follow up"],
                "answer": "Create a safe space for open discussion, review what went well and what didn't, identify improvement opportunities, define concrete action items, and follow up on previous retrospective actions."
            }
        ]
    },
    "Product Owner": {
        "questions": [
            {
                "question": "How do you prioritize items in a product backlog?",
                "keywords": ["value", "business", "user", "dependencies", "effort", "roi"],
                "answer": "Prioritize based on business value, user impact, dependencies between items, implementation effort, and return on investment (ROI). Consider urgent vs important factors."
            },
            {
                "question": "What makes a good user story?",
                "keywords": ["invest", "independent", "negotiable", "valuable", "estimable", "small", "testable"],
                "answer": "A good user story follows the INVEST criteria: Independent, Negotiable, Valuable, Estimable, Small, and Testable. It should clearly define who, what, and why."
            },
            {
                "question": "How do you handle changing requirements from stakeholders?",
                "keywords": ["communicate", "prioritize", "impact", "backlog", "stakeholder", "value"],
                "answer": "Communicate the impact of changes, work with stakeholders to understand the value and urgency, reprioritize the backlog accordingly, and ensure transparency about trade-offs."
            },
            {
                "question": "What is the Definition of Done and why is it important?",
                "keywords": ["criteria", "quality", "complete", "shared understanding", "consistent"],
                "answer": "The Definition of Done is a shared understanding of what criteria must be met for work to be considered complete. It ensures quality and consistency across deliverables."
            }
        ]
    },
    "Project Manager": {
        "questions": [
            {
                "question": "How do you manage project scope creep?",
                "keywords": ["change control", "document", "impact", "stakeholder", "approval", "baseline"],
                "answer": "Implement change control processes, document all changes, assess impact on timeline/budget/resources, get stakeholder approval, and maintain a clear project baseline."
            },
            {
                "question": "What are the key components of a project plan?",
                "keywords": ["scope", "timeline", "resources", "budget", "risks", "milestones", "deliverables"],
                "answer": "Key components include project scope, timeline/schedule, resource allocation, budget, risk management plan, milestones, and deliverables definition."
            },
            {
                "question": "How do you handle conflicting priorities between stakeholders?",
                "keywords": ["communication", "negotiate", "prioritize", "document", "escalate", "consensus"],
                "answer": "Facilitate communication between stakeholders, help negotiate priorities based on business value, document decisions, escalate when needed, and work toward consensus."
            },
            {
                "question": "What project management methodologies are you familiar with?",
                "keywords": ["waterfall", "agile", "scrum", "kanban", "hybrid", "pmbok"],
                "answer": "Common methodologies include Waterfall (sequential phases), Agile (iterative), Scrum (sprints), Kanban (continuous flow), and hybrid approaches. Choice depends on project needs."
            }
        ]
    },
    "Data Analyst": {
        "questions": [
            {
                "question": "How do you ensure data quality in your analysis?",
                "keywords": ["validation", "cleaning", "completeness", "accuracy", "consistency", "source"],
                "answer": "Validate data sources, clean and preprocess data, check for completeness and accuracy, ensure consistency across datasets, and document data quality issues and resolutions."
            },
            {
                "question": "Explain the difference between correlation and causation.",
                "keywords": ["correlation", "causation", "relationship", "cause", "effect", "confounding"],
                "answer": "Correlation shows a statistical relationship between variables, while causation means one variable directly causes changes in another. Correlation doesn't imply causation due to potential confounding factors."
            },
            {
                "question": "How do you choose the right visualization for your data?",
                "keywords": ["audience", "data type", "story", "trends", "comparisons", "purpose"],
                "answer": "Consider your audience, data types, the story you want to tell, whether showing trends or comparisons, and the purpose of the visualization. Match chart type to data and message."
            },
            {
                "question": "What steps do you take in a typical data analysis project?",
                "keywords": ["define", "collect", "clean", "explore", "analyze", "visualize", "communicate"],
                "answer": "Define the problem, collect relevant data, clean and preprocess, explore data patterns, conduct analysis, create visualizations, and communicate findings to stakeholders."
            }
        ]
    },
    "Cybersecurity": {
        "questions": [
            {
                "question": "What is the CIA triad in cybersecurity?",
                "keywords": ["confidentiality", "integrity", "availability", "security", "principles"],
                "answer": "The CIA triad consists of Confidentiality (protecting data from unauthorized access), Integrity (ensuring data accuracy and trustworthiness), and Availability (ensuring systems and data are accessible when needed)."
            },
            {
                "question": "How do you respond to a security incident?",
                "keywords": ["identify", "contain", "assess", "eradicate", "recover", "lessons learned"],
                "answer": "Follow incident response steps: Identify the incident, contain the threat, assess the damage, eradicate the threat, recover systems, and conduct lessons learned review."
            },
            {
                "question": "What is the principle of least privilege?",
                "keywords": ["minimum", "access", "necessary", "permissions", "role-based", "security"],
                "answer": "The principle of least privilege means giving users only the minimum access rights necessary to perform their job functions, reducing security risks and potential damage from compromised accounts."
            },
            {
                "question": "Explain different types of authentication factors.",
                "keywords": ["something you know", "something you have", "something you are", "multi-factor", "password", "biometric"],
                "answer": "Three types: Something you know (passwords), something you have (tokens, phones), and something you are (biometrics). Multi-factor authentication combines multiple types for stronger security."
            }
        ]
    },
    "Software Engineer": {
        "questions": [
            {
                "question": "What is the difference between SQL and NoSQL databases?",
                "keywords": ["structured", "relational", "schema", "acid", "scalability", "flexibility"],
                "answer": "SQL databases are structured, relational with fixed schemas and ACID compliance. NoSQL databases are more flexible, schema-less, and designed for scalability and handling unstructured data."
            },
            {
                "question": "Explain the concept of version control and Git.",
                "keywords": ["tracking", "history", "branches", "merge", "collaboration", "repository"],
                "answer": "Version control tracks changes to code over time. Git is a distributed system allowing multiple developers to work on projects with branching, merging, and maintaining complete history."
            },
            {
                "question": "What are the principles of object-oriented programming?",
                "keywords": ["encapsulation", "inheritance", "polymorphism", "abstraction"],
                "answer": "The four main principles are: Encapsulation (bundling data and methods), Inheritance (deriving new classes), Polymorphism (multiple forms of methods), and Abstraction (hiding complexity)."
            },
            {
                "question": "How do you ensure code quality and maintainability?",
                "keywords": ["code review", "testing", "documentation", "standards", "refactoring", "clean code"],
                "answer": "Use code reviews, write comprehensive tests, maintain documentation, follow coding standards, regularly refactor code, and apply clean code principles for readability and maintainability."
            }
        ]
    }
}

def initialize_session_state():
    """Initialize session state variables"""
    if 'selected_job' not in st.session_state:
        st.session_state.selected_job = None
    if 'current_questions' not in st.session_state:
        st.session_state.current_questions = []
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}
    if 'incorrect_questions' not in st.session_state:
        st.session_state.incorrect_questions = []
    if 'quiz_completed' not in st.session_state:
        st.session_state.quiz_completed = False
    if 'show_answer_key' not in st.session_state:
        st.session_state.show_answer_key = False
    if 'current_round' not in st.session_state:
        st.session_state.current_round = 1

def check_answer(question_data: Dict, user_answer: str) -> Tuple[bool, List[str]]:
    """Check if user answer contains required keywords"""
    user_answer_lower = user_answer.lower()
    found_keywords = []
    
    for keyword in question_data['keywords']:
        if keyword.lower() in user_answer_lower:
            found_keywords.append(keyword)
    
    # Consider answer correct if at least 60% of keywords are found
    threshold = max(1, len(question_data['keywords']) * 0.6)
    is_correct = len(found_keywords) >= threshold
    
    return is_correct, found_keywords

def reset_quiz():
    """Reset all quiz-related session state"""
    for key in ['current_questions', 'user_answers', 'incorrect_questions', 
                'quiz_completed', 'show_answer_key', 'current_round']:
        if key in st.session_state:
            del st.session_state[key]
    initialize_session_state()

def main():
    st.title("💼 Interview Practice App")
    st.write("Practice interview questions for different job roles and get instant feedback!")
    
    initialize_session_state()
    
    # Sidebar for job selection
    st.sidebar.title("Job Selection")
    job_titles = list(QUESTION_BANK.keys())
    selected_job = st.sidebar.selectbox("Select a job title:", [""] + job_titles)
    
    if selected_job and selected_job != st.session_state.selected_job:
        st.session_state.selected_job = selected_job
        reset_quiz()
    
    if not selected_job:
        st.info("👈 Please select a job title from the sidebar to begin!")
        return
    
    # Display current job and round
    col1, col2 = st.columns([3, 1])
    with col1:
        st.header(f"Interview Questions: {selected_job}")
    with col2:
        if st.session_state.current_round > 1:
            st.info(f"Round {st.session_state.current_round} (Retry)")
    
    # Start new quiz button
    if not st.session_state.current_questions:
        if st.button("Start Quiz", type="primary"):
            st.session_state.current_questions = QUESTION_BANK[selected_job]['questions'].copy()
            random.shuffle(st.session_state.current_questions)
            st.rerun()
        return
    
    # Quiz interface
    if st.session_state.current_questions and not st.session_state.quiz_completed:
        display_quiz()
    
    # Show results and answer key
    if st.session_state.quiz_completed:
        display_results()

def display_quiz():
    """Display the quiz questions"""
    st.write(f"**Answer all {len(st.session_state.current_questions)} questions below:**")
    
    with st.form("quiz_form"):
        answers = {}
        
        for i, question_data in enumerate(st.session_state.current_questions):
            st.write(f"**Question {i+1}:**")
            st.write(question_data['question'])
            
            # Pre-fill with previous answer if retrying
            previous_answer = st.session_state.user_answers.get(question_data['question'], "")
            answers[question_data['question']] = st.text_area(
                f"Your answer for question {i+1}:",
                value=previous_answer,
                height=100,
                key=f"answer_{i}"
            )
            st.write("---")
        
        submitted = st.form_submit_button("Submit Answers", type="primary")
        
        if submitted:
            process_answers(answers)

def process_answers(answers: Dict[str, str]):
    """Process submitted answers and determine incorrect ones"""
    st.session_state.user_answers.update(answers)
    incorrect = []
    
    for question_data in st.session_state.current_questions:
        user_answer = answers.get(question_data['question'], "")
        if not user_answer.strip():
            incorrect.append(question_data)
        else:
            is_correct, _ = check_answer(question_data, user_answer)
            if not is_correct:
                incorrect.append(question_data)
    
    if incorrect:
        st.session_state.incorrect_questions = incorrect
        st.session_state.current_questions = incorrect
        st.session_state.current_round += 1
        st.warning(f"You got {len(incorrect)} question(s) wrong. Please retry those questions.")
        st.rerun()
    else:
        st.session_state.quiz_completed = True
        st.rerun()

def display_results():
    """Display quiz results and answer key"""
    st.success("🎉 Congratulations! You've answered all questions correctly!")
    
    total_questions = len(QUESTION_BANK[st.session_state.selected_job]['questions'])
    st.metric("Questions Completed", f"{total_questions}/{total_questions}")
    st.metric("Rounds Taken", st.session_state.current_round)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Start New Quiz", type="primary"):
            reset_quiz()
            st.rerun()
    
    with col2:
        if st.button("Show Answer Key"):
            st.session_state.show_answer_key = True
            st.rerun()
    
    # Display answer key
    if st.session_state.show_answer_key:
        st.write("## 📋 Answer Key")
        
        for i, question_data in enumerate(QUESTION_BANK[st.session_state.selected_job]['questions']):
            with st.expander(f"Question {i+1}: {question_data['question'][:50]}..."):
                st.write("**Question:**")
                st.write(question_data['question'])
                
                st.write("**Your Answer:**")
                user_answer = st.session_state.user_answers.get(question_data['question'], "Not answered")
                st.write(user_answer)
                
                st.write("**Sample Answer:**")
                st.write(question_data['answer'])
                
                st.write("**Key Keywords:**")
                st.write(", ".join(question_data['keywords']))

if __name__ == "__main__":
    main()


# requirements.txt
streamlit==1.29.0


# README.md
# Interview Practice App

A Streamlit application that helps users practice interview questions for different job roles including Scrum Master, Product Owner, Project Manager, Data Analyst, Cybersecurity, and Software Engineer.

## Features

- **Multiple Job Roles**: Choose from 6 different job titles, each with tailored interview questions
- **Intelligent Scoring**: Answers are evaluated based on relevant keywords and concepts
- **Retry Mechanism**: Continue practicing questions you got wrong until you master them all
- **Answer Key**: Review sample answers and key concepts after completing the quiz
- **Progress Tracking**: See how many rounds it takes to master all questions

## How to Use

1. Select a job title from the sidebar
2. Click "Start Quiz" to begin
3. Answer all questions in the form
4. Submit your answers for evaluation
5. If you get questions wrong, you'll retry only those questions
6. Once all questions are correct, view the answer key for reference

## Installation

1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Run the app: `streamlit run streamlit_app.py`

## Question Evaluation

The app evaluates answers by checking for relevant keywords and concepts. You need to demonstrate understanding of at least 60% of the key concepts for each question to pass.

## Job Roles & Topics

- **Scrum Master**: Agile methodology, sprint management, team facilitation
- **Product Owner**: Backlog management, user stories, stakeholder communication
- **Project Manager**: Project planning, scope management, stakeholder coordination
- **Data Analyst**: Data quality, visualization, analysis methodology
- **Cybersecurity**: Security principles, incident response, authentication
- **Software Engineer**: Programming concepts, databases, code quality

## Contributing

Feel free to contribute additional questions or job roles by modifying the `QUESTION_BANK` dictionary in the main application file.


# .gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Streamlit
.streamlit/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
