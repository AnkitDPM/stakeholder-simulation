import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import graphviz

st.set_page_config(page_title="Stakeholder Simulation", layout="wide")

# Literature-based mapping (see rationale table above)
phase_structure = {
    "Initiation": {
        "Client": ["RiskAversion", "StakeholderEngagement"],
        "Project Manager": ["Adaptability", "ProactiveComms"]
    },
    "Planning": {
        "Client": ["ScopeCreep", "StakeholderEngagement"],
        "Project Manager": ["CollaborativePlanning", "ConstructiveFeedback"],
        "Project Team": ["CollaborativePlanning", "Adaptability"]
    },
    "Execution": {
        "Project Manager": ["ConflictResolution", "ProactiveComms"],
        "Project Team": ["Adaptability", "Miscommunication"]
    },
    "Closure": {
        "Client": ["StakeholderEngagement", "RiskAversion"],
        "Project Manager": ["ConstructiveFeedback", "Adaptability"],
        "Project Team": ["ConstructiveFeedback", "Miscommunication"]
    }
}

ordinal_levels = ['Low', 'Medium', 'High']
ordinal_map = {'Low': 1, 'Medium': 2, 'High': 3}
behavior_weights = {
    "RiskAversion": {"cost": 2, "duration": 2, "quality": -1},
    "StakeholderEngagement": {"cost": -2, "duration": -1, "quality": 3},
    "ScopeCreep": {"cost": 3, "duration": 2, "quality": -2},
    "Adaptability": {"cost": -1, "duration": -1, "quality": 2},
    "ProactiveComms": {"cost": -1, "duration": -1, "quality": 2},
    "CollaborativePlanning": {"cost": -2, "duration": -2, "quality": 3},
    "ConstructiveFeedback": {"cost": -1, "duration": -1, "quality": 2},
    "ConflictResolution": {"cost": -1, "duration": -1, "quality": 2},
    "Miscommunication": {"cost": 1, "duration": 2, "quality": -2}
}

# --- Rationale Table ---
rationale_data = [
    ["Initiation", "Client", "RiskAversion, StakeholderEngagement", "Clients set direction and risk appetite; engagement critical for buy-in and scope clarity [3][4]"],
    ["Initiation", "Project Manager", "Adaptability, ProactiveComms", "PMs must adapt to ambiguity and communicate vision early [1][7]"],
    ["Planning", "Client", "ScopeCreep, StakeholderEngagement", "Clients drive scope; engagement prevents misalignment [3][4][8]"],
    ["Planning", "Project Manager", "CollaborativePlanning, ConstructiveFeedback", "PMs coordinate plans and foster team feedback [1][7]"],
    ["Planning", "Project Team", "CollaborativePlanning, Adaptability", "Teams must plan together and adapt to requirements [1][8]"],
    ["Execution", "Project Manager", "ConflictResolution, ProactiveComms", "PMs resolve issues and keep communication open [1][7][8]"],
    ["Execution", "Project Team", "Adaptability, Miscommunication", "Teams must adapt to changes; poor comms cause errors [1][8]"],
    ["Closure", "Client", "StakeholderEngagement, RiskAversion", "Engagement ensures acceptance; risk aversion affects sign-off [3][4]"],
    ["Closure", "Project Manager", "ConstructiveFeedback, Adaptability", "PMs must close out lessons and adapt for future [1][7]"],
    ["Closure", "Project Team", "ConstructiveFeedback, Miscommunication", "Teams provide feedback; comms issues can delay closure [1][8]"],
]
st.markdown("### Rationale for Selection of Behaviors (with References)")
st.table(pd.DataFrame(rationale_data, columns=["Phase", "Stakeholder", "Behaviors", "Rationale/Reference"]))

# --- Graphviz Tree ---
def make_tree():
    dot = graphviz.Digraph("StakeholderPhases", format="png")
    dot.attr(rankdir="LR", bgcolor="#f8f9fa", nodesep="0.6", ranksep="1.0")
    phase_colors = {
        "Initiation": "#AED6F1", "Planning": "#A9DFBF", "Execution": "#F9E79F", "Closure": "#F5B7B1"
    }
    role_colors = {
        "Client": "#2E86C1", "Project Manager": "#229954", "Project Team": "#B9770E"
    }
    beh_colors = {
        "RiskAversion": "#FFD700", "StakeholderEngagement": "#8E44AD", "ScopeCreep": "#2980B9",
        "Adaptability": "#58D68D", "ProactiveComms": "#5499C7", "CollaborativePlanning": "#45B39D",
        "ConstructiveFeedback": "#F1948A", "ConflictResolution": "#F5B041", "Miscommunication": "#85929E"
    }
    for phase in phase_structure:
        dot.node(f"phase_{phase}", phase, fillcolor=phase_colors[phase], fontcolor="#154360", shape="box", style="rounded,filled")
        for role in phase_structure[phase]:
            role_id = f"{role}_{phase}"
            dot.node(role_id, role, fillcolor=role_colors[role], fontcolor="white", shape="box", style="rounded,filled")
            dot.edge(f"phase_{phase}", role_id)
            for beh in phase_structure[phase][role]:
                beh_id = f"{beh}_{role}_{phase}"
                dot.node(beh_id, beh, fillcolor=beh_colors[beh], fontcolor="white", shape="ellipse", style="filled")
                dot.edge(role_id, beh_id)
    return dot

st.subheader("📊 Project Structure Tree")
st.graphviz_chart(make_tree())

st.header("Configure Stakeholder Behaviors (by Phase)")
profiles = []
for phase, stakeholders in phase_structure.items():
    with st.expander(f"{phase} Phase", expanded=True):
        for role, behaviors in stakeholders.items():
            st.subheader(f"{role}")
            for behavior in behaviors:
                val = st.selectbox(
                    f"{phase} - {role} - {behavior}",
                    ordinal_levels,
                    key=f"{phase}-{role}-{behavior}",
                    index=1
                )
                profiles.append({"Phase": phase, "Role": role, "Behavior": behavior, "Value": val})

profiles_df = pd.DataFrame(profiles)

def simulate_projects(num_projects, profiles_df):
    phases = list(phase_structure.keys())
    projects = []
    for _ in range(num_projects):
        phase = np.random.choice(phases)
        cost = 50
        duration = 50
        quality = 50
        relevant = profiles_df[profiles_df["Phase"] == phase]
        for _, row in relevant.iterrows():
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

st.sidebar.header("Simulation Settings")
num_projects = st.sidebar.select_slider(
    "Number of Simulation Runs", options=[100,200,300,400,500,600,700,800,900,1000], value=300)
st.sidebar.markdown("---")

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
    - **Realistic mapping:** Only the most impactful traits for each stakeholder in each phase are included.
    - **High cost/duration:** If many projects fall in the 'High' category, examine negative behaviors in the relevant phase.
    - **High quality:** Positive behaviors in the right phase and stakeholder improve quality.
    - **Action:** Use this to prioritize which stakeholder behaviors to address in each phase.
    """)
else:
    st.info("Configure behaviors above, then click 'Run Simulation 🚀' to see results.")
