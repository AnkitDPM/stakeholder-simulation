import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Scenario Analysis - Stakeholder Simulation", layout="wide")

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

st.title("📊 Scenario Analysis - Stakeholder Simulation")

st.sidebar.header("Simulation Settings")
num_projects = st.sidebar.select_slider(
    "Number of Simulation Runs", options=[100,200,300,400,500,600,700,800,900,1000], value=300)

st.sidebar.markdown("---")
scenario_names = st.sidebar.text_input("Scenario Names (comma separated)", value="Pessimistic,Base,Optimistic")
scenario_list = [s.strip() for s in scenario_names.split(",") if s.strip()]

scenarios = {}
for scenario in scenario_list:
    st.header(f"Configure: {scenario}")
    profiles = []
    for role in roles_behaviors:
        with st.expander(f"{role} ({scenario})", expanded=(scenario=="Base")):
            for phase in roles_behaviors[role]["phases"]:
                st.subheader(f"{role} - {phase} Phase")
                for behavior in roles_behaviors[role]["behaviors"]:
                    val = st.selectbox(
                        f"{role} - {phase} - {behavior} ({scenario})",
                        ordinal_levels,
                        key=f"{scenario}-{role}-{phase}-{behavior}",
                        index=1 if scenario=="Base" else 0
                    )
                    profiles.append({"Role": role, "Phase": phase, "Behavior": behavior, "Value": val})
    scenarios[scenario] = pd.DataFrame(profiles)

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

if st.button("Run Scenario Analysis 🚀"):
    results = {}
    for scenario, profiles_df in scenarios.items():
        results[scenario] = simulate_projects(num_projects, profiles_df)
    st.success("Scenario analysis complete! See results below:")

    for kpi in ['CostCat','DurationCat','QualityCat']:
        st.subheader(f"{kpi.replace('Cat','')} Distribution by Scenario")
        fig = px.histogram(
            pd.concat([
                df.assign(Scenario=scenario)
                for scenario, df in results.items()
            ]),
            x=kpi, color='Scenario', barmode='group',
            category_orders={kpi: ['Low','Medium','High'], 'Scenario': scenario_list},
            title=f"{kpi.replace('Cat','')} Distribution by Scenario",
            color_discrete_sequence=px.colors.qualitative.Set1
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Heatmap of Quality Category by Phase (per Scenario)")
    for scenario, df in results.items():
        st.markdown(f"**{scenario}**")
        quality_pivot = pd.crosstab(df['Phase'], df['QualityCat'])
        fig = px.imshow(quality_pivot.values, labels=dict(x="Quality Category", y="Phase", color="Count"),
                        x=quality_pivot.columns, y=quality_pivot.index,
                        color_continuous_scale='Viridis', text_auto=True)
        st.plotly_chart(fig, use_container_width=True)

    # Insights
    st.header("🔎 Insights from Scenario Analysis")
    st.markdown("""
    - **Compare scenarios:** See how changing stakeholder behaviors in each scenario shifts project outcomes.
    - **Pessimistic scenarios** (more negative behaviors) will show higher cost/duration and lower quality.
    - **Optimistic scenarios** (more positive behaviors) will show lower cost/duration and higher quality.
    - **Action:** Use this to stress-test your project plans and identify critical behaviors to focus on.
    """)
else:
    st.info("Configure each scenario above, then click 'Run Scenario Analysis 🚀' to compare results.")
