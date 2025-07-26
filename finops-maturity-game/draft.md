To create the Streamlit code for the "FinOps Journey Simulation" game, Cursor will need a detailed prompt covering the UI elements and basic logic. Here's a prompt broken down into sections for clarity:

---

# Streamlit FinOps Game: Scenario Presentation Module

**Objective:** Create the Streamlit code for the "Scenario Presentation" module of a FinOps maturity game. This module will display a fictional company scenario, ask the user to identify the maturity stage and challenges, and provide initial feedback.

---

## 1. Core Application Setup

* **Import Streamlit:** Start with the standard `import streamlit as st`.
* **Page Configuration:** Set the page title to "FinOps Journey Simulation" and use a wide layout.

---

## 2. Global Game State (Placeholder)

* Initialize `st.session_state.current_scenario_index` to `0` (for the first scenario).
* Initialize `st.session_state.feedback_message` to an empty string.
* **Define Scenarios:** Create a Python list of dictionaries called `scenarios`. Each dictionary should represent a scenario and contain:
    * `title`: A string for the scenario's heading (e.g., "Acme Corp's Cloud Chaos").
    * `description`: A multi-line string for the scenario's narrative.
    * `correct_maturity_stage`: A string indicating the correct maturity stage ("Crawl", "Walk", or "Run").
    * `correct_challenges`: A list of strings representing the correct challenges for that scenario.
    * `maturity_options`: A list of all possible maturity stage options (e.g., ["Crawl", "Walk", "Run", "Unsure"]).
    * `challenge_options`: A comprehensive list of potential FinOps challenges that the user can select from (e.g., "Lack of cost visibility", "No central governance", "Engineers not involved in cost discussions", "Inefficient resource utilization", "Manual reporting processes").

    *Provide at least **three distinct scenarios** representing Crawl, Walk, and Run stages respectively.*

---

## 3. User Interface Layout

* **Main Title:** Display "FinOps Journey Simulation" using `st.title()`.
* **Instructions:** Add a brief explanatory text using `st.write()`: "Read the scenario below and answer the questions to help the company improve its FinOps maturity."

---

## 4. Scenario Display Logic

* **Current Scenario Retrieval:** Get the current scenario dictionary using `scenarios[st.session_state.current_scenario_index]`.
* **Scenario Heading:** Display the `scenario['title']` using `st.header()`.
* **Scenario Description:** Display the `scenario['description']` within an `st.info()` block to make it stand out.
* **Visual Separator:** Use `st.divider()` for visual separation.

---

## 5. User Input Widgets

* **Maturity Stage Question:**
    * Prompt: "What FinOps maturity stage does Acme Corp seem to be in?" (or appropriate company name).
    * Widget: `st.radio()` with options from `scenario['maturity_options']`. Store the selection in a variable, e.g., `user_maturity_choice`.
* **Challenges/Opportunities Question:**
    * Prompt: "What are the key FinOps challenges or opportunities present in this scenario? (Select all that apply)"
    * Widget: `st.multiselect()` with options from `scenario['challenge_options']`. Store the selections in a variable, e.g., `user_challenge_choices`.

---

## 6. Submission and Feedback

* **Submit Button:** Create an `st.button()` labeled "Analyze Scenario".
* **Evaluation Logic (inside the button's `if` block):**
    * **Maturity Check:**
        * If `user_maturity_choice` matches `scenario['correct_maturity_stage']`, set a positive message for maturity feedback.
        * Else, set a negative/hint message for maturity feedback, explaining why their choice might be incorrect.
    * **Challenges Check:**
        * Compare `set(user_challenge_choices)` with `set(scenario['correct_challenges'])`.
        * If they are identical, set a positive message for challenges feedback.
        * Else, set a message indicating what was missed or incorrectly selected.
    * **Combine Feedback:** Concatenate the maturity and challenges feedback into `st.session_state.feedback_message`.
    * **Advance Scenario (Placeholder):** For now, you can add a simple `st.write("Ready to move to the next step!")` or increment `st.session_state.current_scenario_index` (with bounds checking) to demonstrate progression for future development.
* **Display Feedback:** After the button logic, display `st.session_state.feedback_message` using `st.write()` or `st.success()/st.warning()/st.error()` based on correctness.

---

## 7. Initial State (When app loads or refreshes)

* Ensure that `st.session_state` variables are initialized only once using `if 'key' not in st.session_state:`.

---

## 8. Requirements for Cursor

* Generate the complete, runnable Streamlit Python code (`.py` file).
* Include comments where necessary to explain key parts of the code.
* Ensure the code is clean, readable, and follows Python best practices.
* Do not include any external dependencies beyond Streamlit itself.

---