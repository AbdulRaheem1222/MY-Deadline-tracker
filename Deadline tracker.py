import streamlit as st
from datetime import datetime

# 👉 Page settings
st.set_page_config(page_title="Deadline Tracker", page_icon="📅", layout="centered")

# 👉 Title and subtitle
st.markdown(
    """
    <h1 style='text-align: center;'>📅 Smart Deadline Tracker</h1>
    <p style='text-align: center; color: gray;'>Track your important tasks and never miss a deadline again!</p>
    <hr style='border: 1px solid #eee;' />
    """,
    unsafe_allow_html=True
)

# 👉 Add task section in sidebar
st.sidebar.header("➕ Naya Task Add Karein")

task_name = st.sidebar.text_input("📝 Task ka Naam")
deadline_date = st.sidebar.date_input("📆 Deadline ki Tareekh")

if st.sidebar.button("✅ Add Task"):
    if "tasks" not in st.session_state:
        st.session_state.tasks = []
    if task_name:
        st.session_state.tasks.append({"task": task_name, "deadline": deadline_date})
        st.sidebar.success(f"✅ Task '{task_name}' add ho gaya!")
    else:
        st.sidebar.warning("⚠️ Task ka naam likhna zaroori hai.")

# 👉 Display tasks
st.subheader("📋 Aapke Tasks")

if "tasks" in st.session_state and st.session_state.tasks:
    tasks_sorted = sorted(st.session_state.tasks, key=lambda x: x["deadline"])
    
    for task in tasks_sorted:
        days_left = (task["deadline"] - datetime.now().date()).days
        if days_left < 0:
            status = "❌ Deadline guzar chuki hai"
            color = "red"
        elif days_left == 0:
            status = "🚨 Aaj Deadline hai!"
            color = "orange"
        elif days_left <= 3:
            status = f"⚠️ {days_left} din baaqi hain"
            color = "orange"
        else:
            status = f"✅ {days_left} din baaqi hain"
            color = "green"

        st.markdown(
            f"""
            <div style="padding: 10px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid {color}; background-color: #f9f9f9;">
                <strong>{task['task']}</strong><br>
                📅 <i>{task['deadline']}</i><br>
                <span style="color: {color};">{status}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info("⚠️ Koi task add nahi hua hai.")

# 👉 Footer
st.markdown(
    "<hr><p style='text-align: center; font-size: 12px;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
