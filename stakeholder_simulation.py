import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Stakeholder Simulation", layout="wide")

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

st.title("🌈 Role-based Stakeholder Simulation")

st.sidebar.header("Simulation Settings")
num_projects = st.sidebar.select_slider(
    "Number of Simulation Runs (multiples of 100)", options=[100,200,300,400,500,600,700,800,900,1000], value=300)
st.sidebar.markdown("---")

st.header("Configure Stakeholder Behaviors (by Phase)")
profiles = []
for phase in phases:
    with st.expander(f"{phase} Phase", expanded=True):
        for role in roles_behaviors:
            if phase in roles_behaviors[role]["phases"]:
                st.subheader(f"{role}")
                for behavior in roles_behaviors[role]["behaviors"]:
                    val = st.selectbox(
                        f"{phase} - {role} - {behavior}",
                        ordinal_levels,
                        key=f"{phase}-{role}-{behavior}",
                        index=1
                    )
                    profiles.append({"Phase": phase, "Role": role, "Behavior": behavior, "Value": val})

profiles_df = pd.DataFrame(profiles)

def simulate_projects(num_projects, profiles_df):
    projects = []
    for _ in range(num_projects):
        phase = np.random.choice(phases)
        cost = 50
        duration = 50
        quality = 50
        for _, row in profiles_df[profiles_df["Phase"] == phase].iterrows():
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

if st.button("Run Simulation 🚀"):
    projects_df = simulate_projects(num_projects, profiles_df)
    st.success("Simulation complete! See results below:")

    col1, col2, col3 = st.columns(3)
    for kpi, col in zip(['CostCat','DurationCat','QualityCat'], [col1, col2, col3]):
        fig = px.histogram(projects_df, x=kpi, color='Phase', barmode='group',
                           category_orders={kpi: ['Low','Medium','High']},
                           title=f"{kpi.replace('Cat','')} by Phase",
                           color_discrete_sequence=px.colors.sequential.Plasma_r)
        fig.update_layout(bargap=0.2)
        col.plotly_chart(fig, use_container_width=True)

    st.subheader("Heatmap of Quality Category by Phase")
    quality_pivot = pd.crosstab(projects_df['Phase'], projects_df['QualityCat'])
    fig = px.imshow(quality_pivot.values, labels=dict(x="Quality Category", y="Phase", color="Count"),
                    x=quality_pivot.columns, y=quality_pivot.index,
                    color_continuous_scale='Viridis', text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("See Raw Simulation Data"):
        st.dataframe(projects_df)

    st.header("🔎 Insights from Simulation")
    st.markdown(f"""
    - **High cost or duration**: If you observe many projects in the 'High' category, review which behaviors are set to 'High' for negative factors (e.g., Ego, Delays, ScopeCreep). Lowering these will improve outcomes.
    - **High quality**: High levels of positive behaviors (e.g., Stakeholder Engagement, Collaborative Planning) lead to more 'High' quality projects.
    - **Phase differences**: If certain phases show worse outcomes, focus improvement efforts on behaviors in those phases.
    - **Tip**: Use this simulation to test how changing stakeholder behaviors impacts project KPIs.
    """)
else:
    st.info("Configure behaviors above, then click 'Run Simulation 🚀' to see results.")
