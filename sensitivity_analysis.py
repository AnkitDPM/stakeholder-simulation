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

st.title("📈 Sensitivity Analysis - Stakeholder Simulation")

st.sidebar.header("Simulation Settings")
num_projects = st.sidebar.select_slider(
    "Number of Simulation Runs", options=[100,200,300,400,500,600,700,800,900,1000], value=300)
st.sidebar.markdown("---")

# Select the behavior to analyze
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

def run_simulation(num_projects, profiles_df):
    projects = []
    for _ in range(num_projects):
        phase = np.random.choice(phases)
        role_means = {}
        for role in roles_behaviors:
            if phase in roles_behaviors[role]['phases']:
                subset = profiles_df[(profiles_df.Role == role) & (profiles_df.Phase == phase)]
                for behavior in roles_behaviors[role]['behaviors']:
                    v = subset[subset.Behavior == behavior]['Value'].values[0]
                    role_means[f"{role}_{behavior}"] = ordinal_map[v]
        cost_score = sum(v * np.random.uniform(-1, 1) for v in role_means.values())
        duration_score = sum(v * np.random.uniform(-1, 1) for v in role_means.values())
        quality_score = 10 - abs(cost_score) - abs(duration_score) + np.random.normal(0, 1)
        cost_cat = 'High' if cost_score > 2 else 'Medium' if cost_score > 0 else 'Low'
        duration_cat = 'High' if duration_score > 2 else 'Medium' if duration_score > 0 else 'Low'
        quality_cat = 'High' if quality_score > 7 else 'Medium' if quality_score > 4 else 'Low'
        projects.append({
            'Phase': phase,
            'CostScore': cost_score, 'DurationScore': duration_score, 'QualityScore': quality_score,
            'CostCat': cost_cat, 'DurationCat': duration_cat, 'QualityCat': quality_cat
        })
    return pd.DataFrame(projects)

if st.button("Run Sensitivity Analysis 🚀"):
    results = {}
    for level in ordinal_levels:
        # Copy base profiles and set selected behavior to the test level
        profiles = [dict(profile) for profile in base_profiles]
        sel_role, sel_phase, sel_behavior = all_behaviors[behavior_options.index(selected_behavior)]
        for profile in profiles:
            if profile["Role"] == sel_role and profile["Phase"] == sel_phase and profile["Behavior"] == sel_behavior:
                profile["Value"] = level
        profiles_df = pd.DataFrame(profiles)
        results[level] = run_simulation(num_projects, profiles_df)
    st.success("Sensitivity analysis complete! See results below:")

    # KPI plots comparison
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

    # Heatmap for Quality by Level
    st.subheader("Heatmap of Quality Category by Phase (per Level)")
    for level, df in results.items():
        st.markdown(f"**{selected_behavior} = {level}**")
        quality_pivot = pd.crosstab(df['Phase'], df['QualityCat'])
        fig = px.imshow(quality_pivot.values, labels=dict(x="Quality Category", y="Phase", color="Count"),
                        x=quality_pivot.columns, y=quality_pivot.index,
                        color_continuous_scale='Viridis', text_auto=True)
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Select a behavior and click 'Run Sensitivity Analysis 🚀' to see results.")
