# AI-Powered-Test-Case-Generator-with-CrewAI-and-Gemini

## AI Test Case Generator using CrewAI + Gemini

A modular Flask web application that uses **CrewAI agents** and **Google Gemini 2.0 Flash LLM** to automatically generate **structured test cases** based on user requirements.

## Architecture Design Flow

  ![Image](https://github.com/user-attachments/assets/2cc1b826-34bf-4f48-b2ba-ccca38db82b3)

## 🌐 Live Demo

https://github.com/user-attachments/assets/a12e4ad7-ff75-487b-b8dd-8c2dda2625b6

## Project Objective

This application simplifies the QA process by automating the generation of:

1) Functional test cases  
2) Edge case scenarios  
3) Input validations  
4) Positive and negative test scenarios  

It uses a **multi-agent system** built with [CrewAI](https://docs.crewai.com/) and is backed by **Gemini 2.0 Flash LLM** for high-performance language understanding and reasoning.

---

## 🏗️ Project Structure

    test_case_generator_app/
    ├── app.py # Main Flask app
    ├── config/
    │ └── llm_config.py # Gemini LLM configuration
    ├── agents/
    │ ├── requirement_analyst.py # Agent to analyze user requirements
    │ └── test_case_generator.py # Agent to generate test cases
    ├── tasks/
    │ ├── requirement_analysis_task.py # Task for requirement breakdown
    │ └── test_case_generation_task.py # Task for generating test cases
    ├── crew/
    │ └── crew_manager.py # Coordinates agents and tasks
    ├── utils/
    │ └── formatter.py # Formats raw text into readable HTML
    ├── templates/
    │ └── index.html # Frontend UI
    ├── .env # Environment variables
    └── requirements.txt # Python dependencies


---

## 🧪 How It Works

    1. User inputs a plain English requirement via a web form.
    2. Flask sends this to the backend.
    3. CrewManager sets up:
       a) Agent 1: Requirement Analyst
       b) Agent 2: Test Case Generator
       c) Task 1: Break down requirement
       d) Task 2: Generate test cases
    4. CrewAI uses Gemini LLM to reason and complete both tasks.
    5. Output is formatted and returned as a clean HTML preview.

---

## 📦 Installation

    ### 🧱 Prerequisites
    
    - Python 3.10+
    - Google API Key (for Gemini)
    - `virtualenv` or `conda` environment

    ### 🔧 Steps

    # 1. Clone the repo
        git clone https://github.com/gurmeet289/AI-Powered-Test-Case-Generator-with-CrewAI-and-Gemini.git
        cd ai-test-case-generator
    
    # 2. Create environment and activate it
        python -m venv venv
        source venv/bin/activate  # or venv\Scripts\activate on Windows
    
    # 3. Install dependencies
        pip install -r requirements.txt
    
    # 4. Set up environment variables
        .env

  ## Inside .env file:

    GEMINI_API_KEY=your_google_api_key_here

    ### Note - You must have a valid Google Cloud key to use Gemini models.

## Run the App

    python app.py
    Navigate to http://127.0.0.1:5000 in your browser.

## 📚 Technologies Used

    1) Flask – Web framework
    
    2) CrewAI – Multi-agent orchestration
    
    3) Gemini Flash 2.0 – Large language model for reasoning
    
    4) HTML/CSS – Frontend
    
    5) Python – Backend logic

## Agents Breakdown
    
    1) Agent Role
    2) Requirement Analyst	Understand and break user requirement into features and edge cases
    3) Test Case Generator	Generate structured and actionable test cases

## Example Use Case

    Input:
    
    "As a user, I want to log in with email and password, and reset password if I forget it."
    
    Output:

    Functional test cases for login, password reset
    
    Edge cases like empty fields, invalid formats
    
    Validations for email format, password strength
    
    Negative test scenarios (wrong password, user not found)


## Thank You! Keep Learning!

