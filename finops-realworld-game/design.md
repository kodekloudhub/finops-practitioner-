## Streamlit App Design: Azure Cost Optimization Puzzle Game

### Overview
This Streamlit app is an interactive educational game based on a FinOps use case. The scenario involves an Engineering Manager in a mid-size company dealing with skyrocketing Azure bills, who must also act as a FinOps manager. The app presents **7 jumbled steps** for solving Azure cost issues. Users (students) rearrange them into the correct order, submit their arrangement, receive feedback on errors, see the correct sequence, and have a reset option.

The app emphasizes learning through trial and error, promoting best practices in cloud cost management. It uses Streamlit for a simple, web-based interface without complex backend needs.

**Key Goals**:
- Educate on logical order of Azure cost optimization.
- Provide interactive rearrangement with feedback.
- Keep it engaging with emojis (e.g., ✅ for correct, ❌ for incorrect) and minimal UI.

**Tech Stack**:
- Python with Streamlit library.
- No external databases or APIs needed; all logic is in-memory.
- Use Streamlit's session state for tracking user arrangements and game state.

### Requirements
- **Total Steps**: Exactly 7, jumbled on initial load.
- **Correct Order of Steps** (hardcoded in the app for validation):
  1. **Gather Data**: Review current Azure bills and usage reports to understand where costs are coming from.
  2. **Identify Cost Drivers**: Analyze the data to pinpoint the services and resources driving the high costs.
  3. **Set Budgets and Alerts**: Establish budgets for different departments or projects and set up alerts for when costs approach limits.
  4. **Optimize Resources**: Rightsize over-provisioned resources, delete unused ones, and switch to cost-effective alternatives.
  5. **Implement Reservations and Savings Plans**: Purchase reserved instances or savings plans for predictable workloads.
  6. **Enforce Tagging and Governance**: Mandate resource tagging for better cost allocation and implement policies to prevent wasteful spending.
  7. **Monitor and Iterate**: Continuously monitor costs, review optimizations, and adjust strategies as needed.

- **Jumbling**: On app load or reset, shuffle the 7 steps randomly.
- **User Interaction**:
  - Display jumbled steps as a draggable list or numbered selectors (use Streamlit's `st.multiselect` or custom components for reordering).
  - "Submit" button to check the arrangement.
  - Post-submit: Show feedback on what's wrong (e.g., list misplaced steps with positions), display the correct order, and provide a "Reset" button to shuffle and start over.
- **Feedback Mechanism**:
  - Compare user's ordered list to the correct order.
  - Highlight correct positions (✅) and incorrect ones (❌) with explanations (e.g., "Step X should be after Step Y because...").
  - If fully correct, show a success message like "Great job! You've optimized the costs efficiently 🎉".
- **Edge Cases**:
  - Handle incomplete arrangements (e.g., prompt user to arrange all 7).
  - Ensure reset clears session state and reshuffles.
- **UI/UX**:
  - Simple, clean design with headers, lists, and buttons.
  - Use emojis for engagement.
  - Responsive for desktop/mobile.

---

### UI Flow
1. **Landing Page/Introduction**:
   - Display the use case scenario in a blockquote.
   - > You are an Engineering Manager in a mid-size company with skyrocketing Azure bills. You've been asked to also handle FinOps. In which order will you solve the Azure cost issues?
   - Brief instructions: "Rearrange the jumbled steps below into the correct logical order, then submit."

2. **Jumbled Steps Section**:
   - Show the 7 steps in a random order as a bulleted list.
   - Provide a way to rearrange: Use Streamlit's `st.expander` or a custom widget for drag-and-drop (if possible; fallback to numbered selectboxes where user assigns positions 1-7 to steps).

3. **Submission and Feedback**:
   - "Submit" button.
   - On submit: Validate and display:
     - User's arrangement.
     - Feedback table (see below).
     - Correct order as a numbered list.
   - "Reset" button to restart.

4. **Game Loop**:
   - Users can submit multiple times, but reset shuffles anew.

---

### Components and Logic
#### Core Data Structures
- **Steps List** (hardcoded):
  ```python
  correct_steps = [
      "Gather Data: Review current Azure bills and usage reports to understand where costs are coming from.",
      "Identify Cost Drivers: Analyze the data to pinpoint the services and resources driving the high costs.",
      "Set Budgets and Alerts: Establish budgets for different departments or projects and set up alerts for when costs approach limits.",
      "Optimize Resources: Rightsize over-provisioned resources, delete unused ones, and switch to cost-effective alternatives.",
      "Implement Reservations and Savings Plans: Purchase reserved instances or savings plans for predictable workloads.",
      "Enforce Tagging and Governance: Mandate resource tagging for better cost allocation and implement policies to prevent wasteful spending.",
      "Monitor and Iterate: Continuously monitor costs, review optimizations, and adjust strategies as needed."
  ]
  ```

- **Session State**:
  - Use `st.session_state` to store:
    - `jumbled_steps`: Shuffled list on init/reset.
    - `user_order`: User's arranged list.

#### Key Functions
1. **Shuffle Steps**:
   - On app start or reset: `random.shuffle(correct_steps)` to create `jumbled_steps`.

2. **Rearrangement UI**:
   - Option 1 (Simple): Use 7 `st.selectbox` for positions 1-7, ensuring no duplicates.
   - Option 2 (Advanced): Implement a sortable list using Streamlit components (e.g., via `streamlit-sortables` if installed, or custom JavaScript).

3. **Validation Logic**:
   - Compare `user_order` to `correct_steps`.
   - Generate feedback: For each position, check if match; if not, explain why (e.g., "This step should come after identifying drivers because optimization requires data insights.").

4. **Feedback Display**:
   - Use a table to show results:

     | Position | User's Step | Status | Explanation |
     |----------|------------|--------|-------------|
     | 1 | [User's choice] | ✅ or ❌ | [Brief reason if wrong] |
     - Followed by the correct order in a numbered list.

5. **Buttons**:
   - `if st.button("Submit"): # validation code`
   - `if st.button("Reset"): # reshuffle and clear state`

---

### Implementation Notes
- **Dependencies**: Install `streamlit` via pip. For advanced sorting, consider adding `streamlit-sortables` or similar.
- **File Structure**:
  - `app.py`: Main Streamlit script with all logic.
  - No additional files needed.
- **Best Practices**:
  - Keep code modular with functions for shuffle, validate, and display.
  - Use Markdown for formatting (e.g., **bold** for emphasis, emojis like 🔄 for reset).
  - Test for usability: Ensure rearrangement is intuitive and feedback is educational.
- **Potential Enhancements** (Optional):
  - Add hints button to reveal one correct step.
  - Track attempts and show score.
