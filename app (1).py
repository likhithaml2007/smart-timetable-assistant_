import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Smart Timetable", layout="centered")

st.title("📅 Smart Timetable Assistant")

# Initialize storage
if "events" not in st.session_state:
    st.session_state.events = []

# ----------- INPUT SECTION -----------
st.subheader("➕ Add New Event")

event = st.text_input("Enter Event Name")
date = st.date_input("Select Date")
time = st.time_input("Select Time")
category = st.selectbox("Event Type", ["Class", "Exam", "Assignment"])

# ----------- ADD EVENT WITH CONFLICT CHECK -----------
if st.button("Add Event"):
    if event:
        conflict = False
        
        for e in st.session_state.events:
            if e["date"] == str(date) and e["time"] == str(time):
                conflict = True
                break

        if conflict:
            st.error("⚠️ Time conflict! Another event exists at this time.")
        else:
            st.session_state.events.append({
                "event": event,
                "date": str(date),
                "time": str(time),
                "category": category
            })
            st.success("✅ Event added successfully!")
    else:
        st.warning("Please enter event name")

# ----------- DISPLAY EVENTS -----------
st.subheader("📌 Your Schedule")

if st.session_state.events:
    for i, e in enumerate(st.session_state.events):
        st.write(f"{i+1}. {e['event']} | {e['category']} | {e['date']} at {e['time']}")
else:
    st.info("No events added yet")

# ----------- FIND FREE TIME (SMART FEATURE) -----------
st.subheader("🔍 Find Free Time")

search_date = st.date_input("Check free time for date")

if st.button("Find Free Slots"):
    booked_times = []

    for e in st.session_state.events:
        if e["date"] == str(search_date):
            booked_times.append(e["time"])

    st.write("### 🕒 Available Slots:")

    found = False
    for hour in range(9, 18):  # 9 AM to 6 PM
        time_slot = f"{hour:02d}:00:00"
        if time_slot not in booked_times:
            st.write(f"✅ {hour}:00 is free")
            found = True

    if not found:
        st.warning("No free slots available!")

# ----------- CLEAR EVENTS -----------
if st.button("Clear All Events"):
    st.session_state.events = []
    st.success("All events cleared!")
