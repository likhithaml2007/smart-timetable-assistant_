import streamlit as st

st.set_page_config(page_title="Smart Timetable", layout="centered")

st.title("📅 Smart Timetable Assistant")

# Initialize session state
if "events" not in st.session_state:
    st.session_state.events = []

# Input fields
event = st.text_input("Enter Event (Class / Exam / Assignment)")
date = st.date_input("Select Date")

# Add event
if st.button("Add Event"):
    if event:
        st.session_state.events.append((event, str(date)))
        st.success("Event added successfully!")
    else:
        st.warning("Please enter event name")

# Display events
st.write("## 📌 Your Schedule")
if st.session_state.events:
    for i, e in enumerate(st.session_state.events):
        st.write(f"{i+1}. {e[0]} on {e[1]}")
else:
    st.info("No events added yet")

# Clear events
if st.button("Clear All Events"):
    st.session_state.events = []
    st.success("All events cleared!")
