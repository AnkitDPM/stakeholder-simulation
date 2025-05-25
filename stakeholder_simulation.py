import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Stakeholder Simulation", layout="wide")

# --- Roles, Phases, Behaviors ---
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
role_colors = {
    "Client": "#e3f2fd",
    "Project Manager": "#c8e6c9",
    "Project Team": "#fff9c4"
}

st.title("🌈 Role-based Stakeholder Simulation")

# --- Sidebar for Simulation Settings ---
st.sidebar.header("Simulation Settings")
num_projects = st.sidebar.select_slider(
    "Number of Simulation Runs (multiples of 100)", options=[100,200,300,400,500,600,700,800,900,1000], value=300)
st.sidebar.markdown("---")

# --- Input for Each Role ---
st.header("Configure Stakeholder Behaviors")
profiles = []
for role in roles_behaviors:
    with st.expander(f"{role}", expanded=True):
        for phase in roles_behaviors[role]["phases"]:
            st.subheader(f"{role} - {phase} Phase")
            for behavior in roles_behaviors[role]["behaviors"]:
                val = st.selectbox(
                    f"{role} - {phase} - {behavior}",
                    ordinal_levels,
                    key=f"{role}-{phase}-{behavior}",
                    index=1
                )
                profiles.append({"Role": role, "Phase": phase, "Behavior": behavior, "Value": val})

profiles_df = pd.DataFrame(profiles)

# --- Run Simulation Button ---
if st.button("Run Simulation 🚀"):
    # --- Simulate ---
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
        # Assign random weights per role/behavior
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
    projects_df = pd.DataFrame(projects)

    st.success("Simulation complete! See results below:")

    # --- Plots ---
    col1, col2, col3 = st.columns(3)
    for kpi, col in zip(['CostCat','DurationCat','QualityCat'], [col1, col2, col3]):
        fig = px.histogram(projects_df, x=kpi, color='Phase', barmode='group',
                           category_orders={kpi: ['Low','Medium','High']},
                           title=f"{kpi.replace('Cat','')} by Phase",
                           color_discrete_sequence=px.colors.sequential.Plasma_r)
        fig.update_layout(bargap=0.2)
        col.plotly_chart(fig, use_container_width=True)

    # --- Heatmap ---
    st.subheader("Heatmap of Quality Category by Phase")
    quality_pivot = pd.crosstab(projects_df['Phase'], projects_df['QualityCat'])
    fig = px.imshow(quality_pivot.values, labels=dict(x="Quality Category", y="Phase", color="Count"),
                    x=quality_pivot.columns, y=quality_pivot.index,
                    color_continuous_scale='Viridis', text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

    # --- Show Dataframe (optional) ---
    with st.expander("See Raw Simulation Data"):
        st.dataframe(projects_df)

else:
    st.info("Configure behaviors above, then click 'Run Simulation 🚀' to see results.")
