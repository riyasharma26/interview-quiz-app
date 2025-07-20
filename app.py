import streamlit as st
from question_bank import QuestionBank
import re

# Initialize session state
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'current_questions' not in st.session_state:
    st.session_state.current_questions = []
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'quiz_complete' not in st.session_state:
    st.session_state.quiz_complete = False
if 'missed_questions' not in st.session_state:
    st.session_state.missed_questions = []
if 'quiz_round' not in st.session_state:
    st.session_state.quiz_round = 1
if 'show_answer_key' not in st.session_state:
    st.session_state.show_answer_key = False

def evaluate_answer(user_answer, keywords, min_keywords=2):
    """Evaluate user answer based on keyword matching"""
    if not user_answer.strip():
        return False, 0
    
    user_answer_lower = user_answer.lower()
    matched_keywords = []
    
    for keyword in keywords:
        # Check for exact matches and partial matches
        if keyword.lower() in user_answer_lower:
            matched_keywords.append(keyword)
    
    score = len(matched_keywords)
    passed = score >= min_keywords
    
    return passed, score

def reset_quiz():
    """Reset all quiz-related session state"""
    st.session_state.quiz_started = False
    st.session_state.current_questions = []
    st.session_state.user_answers = {}
    st.session_state.quiz_complete = False
    st.session_state.missed_questions = []
    st.session_state.quiz_round = 1
    st.session_state.show_answer_key = False

# App header
st.title("🎯 Interview Quiz App")
st.write("Practice interview questions for your target job role!")

# Initialize question bank
question_bank = QuestionBank()

# Job title selection
if not st.session_state.quiz_started:
    st.header("Select Your Target Job Title")
    
    job_titles = list(question_bank.questions.keys())
    selected_job = st.selectbox("Choose a job title:", job_titles)
    
    if st.button("Start Quiz"):
        st.session_state.quiz_started = True
        st.session_state.selected_job = selected_job
        st.session_state.current_questions = question_bank.get_questions(selected_job)
        st.session_state.user_answers = {}
        st.session_state.quiz_round = 1
        st.rerun()

# Quiz interface
elif st.session_state.quiz_started and not st.session_state.quiz_complete:
    st.header(f"Interview Quiz - {st.session_state.selected_job}")
    
    if st.session_state.quiz_round > 1:
        st.subheader(f"Round {st.session_state.quiz_round} - Practice Missed Questions")
        st.write("Focus on the questions you missed in the previous round.")
    else:
        st.subheader("Answer the following interview questions:")
    
    # Display current questions
    questions_to_show = st.session_state.current_questions
    
    with st.form("quiz_form"):
        answers = {}
        
        for i, question_data in enumerate(questions_to_show):
            st.write(f"**Question {i+1}:** {question_data['question']}")
            answers[i] = st.text_area(
                f"Your answer for Question {i+1}:",
                key=f"answer_{st.session_state.quiz_round}_{i}",
                height=100
            )
            st.write("---")
        
        submitted = st.form_submit_button("Submit Answers")
        
        if submitted:
            # Evaluate answers
            correct_count = 0
            total_questions = len(questions_to_show)
            missed_questions = []
            
            for i, question_data in enumerate(questions_to_show):
                user_answer = answers[i]
                passed, score = evaluate_answer(user_answer, question_data['keywords'])
                
                if passed:
                    correct_count += 1
                else:
                    missed_questions.append(question_data)
                
                # Store the answer for later reference
                st.session_state.user_answers[f"round_{st.session_state.quiz_round}_q_{i}"] = {
                    'question': question_data['question'],
                    'user_answer': user_answer,
                    'correct': passed,
                    'score': score,
                    'keywords': question_data['keywords'],
                    'sample_answer': question_data['sample_answer']
                }
            
            # Show results
            st.success(f"Quiz Round {st.session_state.quiz_round} Complete!")
            st.write(f"Score: {correct_count}/{total_questions}")
            
            if missed_questions:
                st.warning(f"You missed {len(missed_questions)} questions. Let's practice those!")
                st.session_state.current_questions = missed_questions
                st.session_state.quiz_round += 1
                
                if st.button("Continue to Next Round"):
                    st.rerun()
            else:
                st.balloons()
                st.success("🎉 Congratulations! You've mastered all questions!")
                st.session_state.quiz_complete = True
                st.session_state.show_answer_key = True
                st.rerun()

# Quiz complete - show answer key
elif st.session_state.quiz_complete and st.session_state.show_answer_key:
    st.header("🎓 Quiz Complete - Answer Key")
    st.success("Great job! You've successfully answered all questions correctly.")
    
    st.subheader("Review Your Journey:")
    
    # Show all rounds and answers
    for round_num in range(1, st.session_state.quiz_round):
        st.write(f"### Round {round_num}")
        
        round_answers = {k: v for k, v in st.session_state.user_answers.items() 
                        if k.startswith(f"round_{round_num}_")}
        
        for key, answer_data in round_answers.items():
            status = "✅ Correct" if answer_data['correct'] else "❌ Incorrect"
            st.write(f"**Q:** {answer_data['question']}")
            st.write(f"**Your Answer:** {answer_data['user_answer']}")
            st.write(f"**Status:** {status}")
            st.write(f"**Sample Answer:** {answer_data['sample_answer']}")
            st.write(f"**Key Concepts:** {', '.join(answer_data['keywords'])}")
            st.write("---")
    
    # Final statistics
    total_rounds = st.session_state.quiz_round - 1
    st.write(f"**Total Rounds Completed:** {total_rounds}")
    st.write(f"**Job Title:** {st.session_state.selected_job}")
    
    if st.button("Start New Quiz"):
        reset_quiz()
        st.rerun()

# Sidebar with instructions
with st.sidebar:
    st.header("How to Use")
    st.write("""
    1. **Select Job Title**: Choose your target role
    2. **Answer Questions**: Provide detailed responses
    3. **Get Feedback**: See which questions need work
    4. **Practice More**: Focus on missed questions
    5. **Master All**: Complete when you get 100%
    6. **Review**: Check the answer key
    """)
    
    st.header("Tips for Success")
    st.write("""
    - Be specific in your answers
    - Use technical terms when appropriate
    - Include examples from your experience
    - Cover multiple aspects of each question
    """)
    
    if st.session_state.quiz_started:
        st.header("Progress")
        st.write(f"**Job Title:** {st.session_state.selected_job}")
        st.write(f"**Current Round:** {st.session_state.quiz_round}")
        
        if st.button("Reset Quiz"):
            reset_quiz()
            st.rerun()
