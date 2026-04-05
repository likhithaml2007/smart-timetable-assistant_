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
        conflict = False
        
        for e in st.session_state.events:
            if e[1] == str(date) and e[2] == str(time):
                conflict = True
                break

        if conflict:
            st.error("⚠️ Time conflict! Another event already exists at this time.")
        else:
            st.session_state.events.append((event, str(date), str(time), category))
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
time = st.time_input("Select Time")
category = st.selectbox("Event Type", ["Class", "Exam", "Assignment"])
