import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import graphviz

st.set_page_config(page_title="Scenario Analysis - Stakeholder Simulation", layout="wide")

# phase_structure, ordinal_levels, ordinal_map, behavior_weights, rationale_data, make_tree as in stakeholder_simulation.py above

# (Copy the same phase_structure, rationale_data, and make_tree function from above)

# --- Rationale Table ---
st.markdown("### Rationale for Selection of Behaviors (with References)")
st.table(pd.DataFrame(rationale_data, columns=["Phase", "Stakeholder", "Behaviors", "Rationale/Reference"]))

# --- Graphviz Tree ---
st.subheader("📊 Project Structure Tree")
st.graphviz_chart(make_tree())

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
    for phase, stakeholders in phase_structure.items():
        with st.expander(f"{phase} Phase ({scenario})", expanded=(scenario=="Base")):
            for role, behaviors in stakeholders.items():
                st.subheader(f"{role}")
                for behavior in behaviors:
                    val = st.selectbox(
                        f"{phase} - {role} - {behavior} ({scenario})",
                        ordinal_levels,
                        key=f"{scenario}-{phase}-{role}-{behavior}",
                        index=1 if scenario=="Base" else 0
                    )
                    profiles.append({"Phase": phase, "Role": role, "Behavior": behavior, "Value": val})
    scenarios[scenario] = pd.DataFrame(profiles)

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

    st.header("🔎 Insights from Scenario Analysis")
    st.markdown("""
    - **Realistic mapping:** Each scenario only involves the top impactful traits per stakeholder/phase.
    - **Pessimistic scenarios** (more negative traits) will show higher cost/duration and lower quality.
    - **Optimistic scenarios** (more positive traits) will show lower cost/duration and higher quality.
    """)
else:
    st.info("Configure each scenario above, then click 'Run Scenario Analysis 🚀' to compare results.")
