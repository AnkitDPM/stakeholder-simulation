import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Sensitivity Analysis - Stakeholder Simulation", layout="wide")

phases = ['Initiation', 'Planning', 'Execution', 'Closure']
roles_behaviors = {
    "Client": {
        "phases": ['Initiation', 'Planning', 'Closure'],
        "behaviors": ["Ego", "RiskAversion", "StakeholderEngagement", "Delays", "ScopeCreep"]
    },
    "Project Manager": {
        "phases": ['Initiation', 'Planning', 'Execution', 'Closure'],
        "behaviors": ["Adaptability", "CollaborativePlanning", "ConstructiveFeedback", "ProactiveComms", "ConflictResolution", "Miscommunication"]
    },
    "Project Team": {
        "phases": ['Planning', 'Execution', 'Closure'],
        "behaviors": ["Adaptability", "CollaborativePlanning", "ConstructiveFeedback", "Delays", "Miscommunication"]
    }
}
ordinal_levels = ['Low', 'Medium', 'High']
ordinal_map = {'Low': 1, 'Medium': 2, 'High': 3}

behavior_weights = {
    "Ego": {"cost": 2, "duration": 1, "quality": -2},
    "RiskAversion": {"cost": 1, "duration": 2, "quality": -1},
    "Delays": {"cost": 2, "duration": 3, "quality": -2},
    "ScopeCreep": {"cost": 3, "duration": 2, "quality": -2},
    "Miscommunication": {"cost": 1, "duration": 2, "quality": -2},
    "StakeholderEngagement": {"cost": -2, "duration": -1, "quality": 3},
    "Adaptability": {"cost": -1, "duration": -1, "quality": 2},
    "CollaborativePlanning": {"cost": -2, "duration": -2, "quality": 3},
    "ConstructiveFeedback": {"cost": -1, "duration": -1, "quality": 2},
    "ProactiveComms": {"cost": -1, "duration": -1, "quality": 2},
    "ConflictResolution": {"cost": -1, "duration": -1, "quality": 2},
}

st.title("📈 Sensitivity Analysis - Stakeholder Simulation")

st.sidebar.header("Simulation Settings")
num_projects = st.sidebar.select_slider(
    "Number of Simulation Runs", options=[100,200,300,400,500,600,700,800,900,1000], value=300)
st.sidebar.markdown("---")

all_behaviors = []
for role in roles_behaviors:
    for phase in roles_behaviors[role]["phases"]:
        for behavior in roles_behaviors[role]["behaviors"]:
            all_behaviors.append((role, phase, behavior))
behavior_options = [f"{role} - {phase} - {behavior}" for (role, phase, behavior) in all_behaviors]
selected_behavior = st.sidebar.selectbox("Select Behavior for Sensitivity Analysis", behavior_options)

# Set all behaviors to Medium by default
base_profiles = []
for role in roles_behaviors:
    for phase in roles_behaviors[role]["phases"]:
        for behavior in roles_behaviors[role]["behaviors"]:
            base_profiles.append({"Role": role, "Phase": phase, "Behavior": behavior, "Value": "Medium"})

def simulate_projects(num_projects, profiles_df):
    projects = []
    for _ in range(num_projects):
        phase = np.random.choice(phases)
        cost = 50
        duration = 50
        quality = 50
        for _, row in profiles_df.iterrows():
            if row["Phase"] == phase:
                level = ordinal_map[row["Value"]]
                w = behavior_weights[row["Behavior"]]
                cost += w["cost"] * (level - 2)
                duration += w["duration"] * (level - 2)
                quality += w["quality"] * (level - 2)
        cost += np.random.normal(0, 2)
        duration += np.random.normal(0, 2)
        quality += np.random.normal(0, 2)
        cost_cat = 'High' if cost > 55 else 'Medium' if cost > 45 else 'Low'
        duration_cat = 'High' if duration > 55 else 'Medium' if duration > 45 else 'Low'
        quality_cat = 'High' if quality > 55 else 'Medium' if quality > 45 else 'Low'
        projects.append({
            'Phase': phase,
            'Cost': cost, 'Duration': duration, 'Quality': quality,
            'CostCat': cost_cat, 'DurationCat': duration_cat, 'QualityCat': quality_cat
        })
    return pd.DataFrame(projects)

if st.button("Run Sensitivity Analysis 🚀"):
    results = {}
    for level in ordinal_levels:
        profiles = [dict(profile) for profile in base_profiles]
        sel_role, sel_phase, sel_behavior = all_behaviors[behavior_options.index(selected_behavior)]
        for profile in profiles:
            if profile["Role"] == sel_role and profile["Phase"] == sel_phase and profile["Behavior"] == sel_behavior:
                profile["Value"] = level
        profiles_df = pd.DataFrame(profiles)
        results[level] = simulate_projects(num_projects, profiles_df)
    st.success("Sensitivity analysis complete! See results below:")

    for kpi in ['CostCat','DurationCat','QualityCat']:
        st.subheader(f"{kpi.replace('Cat','')} Distribution by {selected_behavior}")
        fig = px.histogram(
            pd.concat([
                df.assign(Level=level)
                for level, df in results.items()
            ]),
            x=kpi, color='Level', barmode='group',
            category_orders={kpi: ['Low','Medium','High'], 'Level': ordinal_levels},
            title=f"{kpi.replace('Cat','')} Distribution by {selected_behavior}",
            color_discrete_sequence=px.colors.qualitative.Set1
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Heatmap of Quality Category by Phase (per Level)")
    for level, df in results.items():
        st.markdown(f"**{selected_behavior} = {level}**")
        quality_pivot = pd.crosstab(df['Phase'], df['QualityCat'])
        fig = px.imshow(quality_pivot.values, labels=dict(x="Quality Category", y="Phase", color="Count"),
                        x=quality_pivot.columns, y=quality_pivot.index,
                        color_continuous_scale='Viridis', text_auto=True)
        st.plotly_chart(fig, use_container_width=True)

    # Insights
    st.header("🔎 Insights from Sensitivity Analysis")
    st.markdown(f"""
    - **Impact of {selected_behavior}:** Observe how changing this behavior from Low to High shifts the distribution of cost, duration, and quality.
    - If increasing this behavior improves quality and reduces cost/duration, it is a key leverage point for project success.
    - Use this analysis to prioritize training or interventions for the most sensitive behaviors.
    """)
else:
    st.info("Select a behavior and click 'Run Sensitivity Analysis 🚀' to see results.")
