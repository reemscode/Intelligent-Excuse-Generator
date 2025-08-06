import streamlit as st
import random

st.set_page_config(page_title="Intelligent Excuse Generator")

st.title("🤖 Intelligent Excuse Generator")
st.markdown("Feeling stuck? Need a quick excuse? This tool has your back!")

def generate_excuse(context, tone):
    excuses = {
        "Work": {
            "Neutral": [
                "I had an urgent client call.",
                "There was a technical glitch in my system.",
                "My internet was unstable today.",
                "A scheduled software update restarted my system.",
                "I lost track of time while preparing a different report.",
                "I had overlapping tasks and missed the meeting window.",
                "My VPN refused to connect to the office servers.",
            ],
            "Guilt-Tripping": [
                "I tried my best to join, but my mother fell sick and I had to take care of her.",
                "I was overwhelmed due to a family emergency and couldn't concentrate.",
                "I had a panic attack and needed a moment to breathe.",
                "A close friend called me in distress, and I had to be there for them.",
                "I’m going through a rough patch mentally and didn’t want to affect anyone else.",
            ]
        },
        "School": {
            "Neutral": [
                "There was a power outage during class time.",
                "I wasn’t feeling well and took rest.",
                "My system crashed just before class started.",
                "I accidentally joined the wrong meeting link.",
                "My schedule app glitched and showed the wrong time.",
                "I was doing another subject’s assignment and lost track of time.",
                "There was a fire drill in our building.",
            ],
            "Guilt-Tripping": [
                "My younger sibling got hurt and I had to rush to help.",
                "I was mentally not in the right place due to personal issues.",
                "We had a sudden medical emergency at home.",
                "I cried all morning because of exam stress and couldn’t attend class.",
                "A relative passed away and I was helping with arrangements.",
            ]
        },
        "Personal": {
            "Neutral": [
                "Something urgent came up suddenly at home.",
                "I had unexpected guests.",
                "I lost track of time while doing chores.",
                "My phone was on silent and I missed the message.",
                "I went out for groceries and it took longer than expected.",
                "There was loud construction work and I couldn’t focus.",
            ],
            "Guilt-Tripping": [
                "I was struggling with anxiety and couldn’t bring myself to respond.",
                "I didn’t mean to ignore you — I just wasn’t in the right headspace.",
                "My pet was sick and I couldn’t leave it unattended.",
                "I had a breakdown after a fight at home.",
                "I was mentally exhausted and needed to shut off completely.",
            ]
        }
    }

    return random.choice(excuses.get(context, {}).get(tone, ["No excuse found."]))

context = st.selectbox("Select the context:", ["Work", "School", "Personal"])
tone = st.selectbox("Choose the tone of your excuse:", ["Neutral", "Guilt-Tripping"])

if st.button("Generate Excuse"):
    excuse = generate_excuse(context, tone)
    st.success(f"📝 {excuse}")
