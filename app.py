import streamlit as st

st.set_page_config(
    page_title="Mainuok",
    page_icon="🧡",
    layout="wide"
)

# -----------------------------
# Session state
# -----------------------------
if "activities" not in st.session_state:
    st.session_state.activities = [
        {"title": "Study Session", "host": "Matas", "location": "Vilnius", "category": "Study", "joined": 3},
        {"title": "Gallery Visit", "host": "Egle", "location": "Old Town", "category": "Culture", "joined": 2},
    ]

if "form_error" not in st.session_state:
    st.session_state.form_error = ""

# -----------------------------
# Callback
# -----------------------------
def post_activity():
    title = st.session_state.activity_title.strip()
    host = st.session_state.host_name.strip()
    location = st.session_state.location_name.strip()
    category = st.session_state.category_name

    if not title:
        st.session_state.form_error = "Please enter an activity."
        return

    if not host:
        st.session_state.form_error = "Please enter your name."
        return

    st.session_state.activities.append({
        "title": title,
        "host": host,
        "location": location if location else "Vilnius",
        "category": category,
        "joined": 0
    })

    st.session_state.activity_title = ""
    st.session_state.host_name = ""
    st.session_state.location_name = ""
    st.session_state.category_name = "Study"
    st.session_state.form_error = ""

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: #f7f2ec;
    }

    html, body, [class*="css"] {
        font-family: "Segoe UI", sans-serif;
        color: #2d1f1a;
    }

    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }

    .main-title {
        font-size: 4.2rem;
        font-weight: 800;
        line-height: 1.05;
        color: #2b1d18;
        margin-bottom: 0.6rem;
    }

    .accent {
        color: #c65a36;
    }

    .subtitle {
        font-size: 1.25rem;
        color: #5d4f49;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }

    .badge {
        display: inline-block;
        background: #dfead8;
        color: #495843;
        padding: 0.55rem 1rem;
        border-radius: 999px;
        font-size: 0.95rem;
        margin-bottom: 1.2rem;
        font-weight: 600;
    }

    .top-brand {
        font-size: 2rem;
        font-weight: 800;
        color: #2b1d18;
        margin-bottom: 1rem;
    }

    .soft-card {
        background: #fffaf6;
        border: 1px solid rgba(0,0,0,0.05);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.05);
    }

    .hero-panel {
        background: linear-gradient(180deg, #f1ddd4, #f8efea);
        border-radius: 28px;
        min-height: 480px;
        padding: 28px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    }

    .floating-card {
        background: white;
        border-radius: 18px;
        padding: 14px 18px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        margin-bottom: 18px;
    }

    .floating-title {
        font-weight: 700;
        font-size: 1rem;
        color: #2b1d18;
    }

    .floating-sub {
        color: #6b5b54;
        font-size: 0.92rem;
    }

    .center-emoji {
        font-size: 5rem;
        text-align: center;
        margin-top: 3.5rem;
        margin-bottom: 1rem;
    }

    .center-text {
        text-align: center;
        color: #5e4e47;
        font-size: 1.25rem;
        font-weight: 600;
    }

    .section-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #2b1d18;
        margin-bottom: 1rem;
    }

    .activity-card {
        background: white;
        border-radius: 20px;
        padding: 18px;
        border: 1px solid rgba(0,0,0,0.05);
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        margin-bottom: 14px;
    }

    .activity-title {
        font-size: 1.2rem;
        font-weight: 800;
        color: #2b1d18;
        margin-bottom: 4px;
    }

    .activity-meta {
        color: #65554f;
        font-size: 0.98rem;
        margin-bottom: 4px;
    }

    .joined-pill {
        display: inline-block;
        background: #f7dfd4;
        color: #a14d31;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.9rem;
        margin-top: 6px;
    }

    div.stButton > button {
        border-radius: 14px;
        font-weight: 700;
        padding: 0.7rem 1rem;
        border: none;
    }

    .footer-note {
        text-align: center;
        color: #6b5b54;
        margin-top: 2rem;
        margin-bottom: 1rem;
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Top brand
# -----------------------------
st.markdown('<div class="top-brand">🧡 Mainuok</div>', unsafe_allow_html=True)

# -----------------------------
# Hero
# -----------------------------
left, right = st.columns([1.1, 0.95], gap="large")

with left:
    st.markdown('<div class="badge">✨ AI-Powered Matching in Vilnius</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="main-title">Never do things <span class="accent">alone</span> again</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="subtitle">Find friendly companions for study sessions, art exhibitions, cultural events, and social plans in Vilnius. Real connections with real people who share your interests.</div>',
        unsafe_allow_html=True
    )

    b1, b2 = st.columns(2)
    with b1:
        st.button("Find Your Match", use_container_width=True)
    with b2:
        st.button("Learn More", use_container_width=True)

    s1, s2 = st.columns(2)
    with s1:
        st.metric("Active Users", "500+")
    with s2:
        st.metric("Happy Matches", "98%")

with right:
    st.markdown('<div class="hero-panel">', unsafe_allow_html=True)

    st.markdown("""
    <div class="floating-card">
        <div class="floating-title">Study Session</div>
        <div class="floating-sub">with Matas</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="center-emoji">👥</div>', unsafe_allow_html=True)
    st.markdown('<div class="center-text">Connecting people in Vilnius</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="floating-card">
        <div class="floating-title">Gallery Visit</div>
        <div class="floating-sub">with Egle</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Main content
# -----------------------------
st.write("")
st.write("")

form_col, live_col = st.columns([0.95, 1.05], gap="large")

with form_col:
    st.markdown('<div class="section-title">Create your own plan</div>', unsafe_allow_html=True)
    st.markdown('<div class="soft-card">', unsafe_allow_html=True)

    st.text_input(
        "What do you want to do?",
        key="activity_title",
        placeholder="e.g. Study session at 5pm"
    )

    st.text_input(
        "Your name",
        key="host_name",
        placeholder="e.g. Mighty"
    )

    st.text_input(
        "Location",
        key="location_name",
        placeholder="e.g. Vilnius Tech campus"
    )

    st.selectbox(
        "Category",
        ["Study", "Culture", "Sports", "Walk", "Games", "Music", "Other"],
        key="category_name"
    )

    st.button("🚀 Create Activity", on_click=post_activity, use_container_width=True)

    if st.session_state.form_error:
        st.warning(st.session_state.form_error)
        st.session_state.form_error = ""

    st.markdown('</div>', unsafe_allow_html=True)

with live_col:
    st.markdown('<div class="section-title">Live opportunities</div>', unsafe_allow_html=True)

    if len(st.session_state.activities) == 0:
        st.info("No opportunities yet. Create the first one.")
    else:
        for i, act in enumerate(st.session_state.activities):
            st.markdown(f"""
            <div class="activity-card">
                <div class="activity-title">{act['title']}</div>
                <div class="activity-meta">👤 with {act['host']}</div>
                <div class="activity-meta">📍 {act['location']}</div>
                <div class="activity-meta">🏷️ {act['category']}</div>
                <div class="joined-pill">🙌 {act['joined']} joined</div>
            </div>
            """, unsafe_allow_html=True)

            c1, c2 = st.columns(2)
            with c1:
                if st.button("Join this plan", key=f"join_{i}", use_container_width=True):
                    st.session_state.activities[i]["joined"] += 1
                    st.rerun()
            with c2:
                st.button("Save for later", key=f"save_{i}", use_container_width=True)

st.markdown('<div class="footer-note">Mainuok • Helping people find companionship in Vilnius</div>', unsafe_allow_html=True)