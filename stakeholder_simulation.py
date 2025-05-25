import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Stakeholder Simulation", layout="wide")

phases = ['Initiation', 'Planning', 'Execution', 'Closure']
roles = ["Client", "Project Manager", "Project Team"]
traits = [
    "Ego", "RiskAversion", "StakeholderEngagement", "Delays", "ScopeCreep",
    "Adaptability", "CollaborativePlanning", "ConstructiveFeedback", "ProactiveComms",
    "ConflictResolution", "Miscommunication"
]
# For each trait, specify where it applies (role, phase)
trait_applicability = {
    "Ego": [("Client", "Initiation"), ("Client", "Planning"), ("Client", "Closure")],
    "RiskAversion": [("Client", "Initiation"), ("Client", "Planning"), ("Client", "Closure")],
    "StakeholderEngagement": [("Client", "Initiation"), ("Client", "Planning"), ("Client", "Closure")],
    "Delays": [("Client", "Initiation"), ("Client", "Planning"), ("Client", "Closure"),
               ("Project Team", "Planning"), ("Project Team", "Execution"), ("Project Team", "Closure")],
    "ScopeCreep": [("Client", "Initiation"), ("Client", "Planning"), ("Client", "Closure")],
    "Adaptability": [("Project Manager", "Initiation"), ("Project Manager", "Planning"), ("Project Manager", "Execution"), ("Project Manager", "Closure"),
                     ("Project Team", "Planning"), ("Project Team", "Execution"), ("Project Team", "Closure")],
    "CollaborativePlanning": [("Project Manager", "Initiation"), ("Project Manager", "Planning"), ("Project Manager", "Execution"), ("Project Manager", "Closure"),
                              ("Project Team", "Planning"), ("Project Team", "Execution"), ("Project Team", "Closure")],
    "ConstructiveFeedback": [("Project Manager", "Initiation"), ("Project Manager", "Planning"), ("Project Manager", "Execution"), ("Project Manager", "Closure"),
                             ("Project Team", "Planning"), ("Project Team", "Execution"), ("Project Team", "Closure")],
    "ProactiveComms": [("Project Manager", "Initiation"), ("Project Manager", "Planning"), ("Project Manager", "Execution"), ("Project Manager", "Closure")],
    "ConflictResolution": [("Project Manager", "Initiation"), ("Project Manager", "Planning"), ("Project Manager", "Execution"), ("Project Manager", "Closure")],
    "Miscommunication": [("Project Manager", "Initiation"), ("Project Manager", "Planning"), ("Project Manager", "Execution"), ("Project Manager", "Closure"),
                         ("Project Team", "Planning"), ("Project Team", "Execution"), ("Project Team", "Closure")]
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

import streamlit as st
import graphviz

# Color palettes
phase_colors = {
    "Initiation": "#AED6F1",
    "Planning": "#A9DFBF",
    "Execution": "#F9E79F",
    "Closure": "#F5B7B1"
}
role_colors = {
    "Client": "#2E86C1",
    "Project Manager": "#229954",
    "Project Team": "#B9770E"
}
behavior_colors = {
    "Ego": "#D35400", "RiskAversion": "#CA6F1E", "StakeholderEngagement": "#7D3C98", "Delays": "#A93226", "ScopeCreep": "#1F618D",
    "Adaptability": "#117A65", "CollaborativePlanning": "#196F3D", "ConstructiveFeedback": "#7B241C", "ProactiveComms": "#2471A3",
    "ConflictResolution": "#AF601A", "Miscommunication": "#616A6B"
}

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

# Create the graph
dot = graphviz.Digraph("StakeholderPhases", format="png")
dot.attr(rankdir="LR", size="8,3")
dot.attr('node', shape='box', style='rounded,filled', fontsize="10")

# Add phase nodes
for phase in phases:
    dot.node(f"phase_{phase}", phase, fillcolor=phase_colors[phase], fontcolor="#154360")

# Add stakeholder and behavior nodes per phase
for phase in phases:
    for role in roles_behaviors:
        if phase in roles_behaviors[role]["phases"]:
            role_id = f"role_{role}_{phase}"
            dot.node(role_id, role, fillcolor=role_colors[role], fontcolor="white", fontsize="10")
            dot.edge(f"phase_{phase}", role_id, color=role_colors[role])
            for behavior in roles_behaviors[role]["behaviors"]:
                beh_id = f"beh_{behavior}_{role}_{phase}"
                dot.node(beh_id, behavior, fillcolor=behavior_colors.get(behavior, "#ABB2B9"), fontcolor="white", fontsize="9", width="0.1")
                dot.edge(role_id, beh_id, color=behavior_colors.get(behavior, "#ABB2B9"))

st.subheader("📊 Horizontal, Compact, Colorful Phase–Stakeholder–Behavior Tree")
st.graphviz_chart(dot, use_container_width=True)


st.title("🌈 Stakeholder Simulation (by Trait)")

st.sidebar.header("Simulation Settings")
num_projects = st.sidebar.select_slider(
    "Number of Simulation Runs (multiples of 100)", options=[100,200,300,400,500,600,700,800,900,1000], value=300)
st.sidebar.markdown("---")

st.header("Configure Stakeholder Traits (by Trait)")
profiles = []
for trait in traits:
    with st.expander(f"Trait: {trait}", expanded=False):
        for (role, phase) in trait_applicability.get(trait, []):
            val = st.selectbox(
                f"{trait} for {role} in {phase}",
                ordinal_levels,
                key=f"{trait}-{role}-{phase}",
                index=1
            )
            profiles.append({"Trait": trait, "Role": role, "Phase": phase, "Value": val})

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
            w = behavior_weights[row["Trait"]]
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
    - **Trait-centric analysis**: Easily see which traits (behaviors) have the biggest impact in each phase and for each stakeholder.
    - **High cost/duration**: Traits like Ego, Delays, ScopeCreep, when set high for any stakeholder in any phase, will raise project risk.
    - **High quality**: Traits like Stakeholder Engagement and Collaborative Planning, when set high, improve outcomes.
    - **Action**: Use this to prioritize which traits to develop or mitigate for each stakeholder in each phase.
    """)
else:
    st.info("Configure traits above, then click 'Run Simulation 🚀' to see results.")
