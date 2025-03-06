
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

#Upload data frame of dimensions
df_country = pd.read_excel("culture_map.xlsx", sheet_name = "countries")
df_dimensions = pd.read_excel("culture_map.xlsx", sheet_name = "dimensions")

# --- 1) LOAD THE SCORE-DESCRIPTION MAPPINGS ---
# Create a dictionary like {1: 'Extremely Direct / Explicit', 2: 'Very Direct', ...}
score_to_text = dict(zip(df_dimensions["Score"], df_dimensions["Communication"]))

# Assuming the Excel file has columns named "Country" and "Communication"
# Group countries by their Communication score
scores = sorted(df_country['Communication'].unique())

fig = go.Figure()

# For clarity, we add jitter on the y-axis so markers in the same cluster don’t overlap.
# Here we generate a small range of y-values for each country in a group.
for score in scores:
    cluster = df_country[df_country['Communication'] == score]
    # Create jitter values; the more points, the more spread out they will be.
    jitter = np.linspace(-0.4, 0.4, len(cluster))
    
    fig.add_trace(go.Scatter(
        x=[score] * len(cluster),
        y=jitter,
        mode='markers+text',
        marker=dict(size=12),
        text=cluster['Country'],      # Display country names on hover (or as labels)
        textposition='top center',
        name=f"Score {score}"
    ))

# --- 4) CONFIGURE THE X-AXIS TO SHOW TEXT INSTEAD OF NUMBERS ---
fig.update_layout(
    title="Countries Grouped by Communication Score",
    xaxis=dict(
        title="Communication Style",
        tickmode='array',
        # 'tickvals' are the numeric positions
        tickvals=list(score_to_text.keys()),  
        # 'ticktext' are the labels we want to display
        ticktext=list(score_to_text.values()),
        # If you want to ensure we see all ticks from 1 to 10, you can do:
        range=[0.5, 10.5]  # This centers ticks from 1..10
    ),
    yaxis=dict(
        title="Countries",
        showticklabels=False  # Hides y-axis labels, since we only use it for jitter
    ),
    margin=dict(l=80, r=80, t=80, b=80)
)
fig.update_layout(
    width=1500,    # Increase width
    height=1000,    # Increase height
    margin=dict(l=80, r=80, t=80, b=80),
    title="Countries Grouped by Communication Score",
    xaxis=dict(
        title="Communication Style",
        tickmode='array',
        tickvals=list(score_to_text.keys()),
        ticktext=list(score_to_text.values()),
        range=[0.5, 10.5]
    ),
    yaxis=dict(
        title="Countries",
        showticklabels=False
    )
)
fig.show()



