"""
MIND-GRAVITY FIELD MAPPER: Cognitive Gravity Simulator
Einstein-Level Innovation: Applying gravitational physics to attention management

Deployment: Push to GitHub, connect to Streamlit Cloud, no additional config needed.
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx
import pandas as pd
import altair as alt
from datetime import datetime, timedelta
from scipy import integrate, interpolate
import warnings
warnings.filterwarnings('ignore')

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="MIND-GRAVITY | Your Cognitive Field",
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .main {
        font-family: 'Orbitron', monospace;
        background: radial-gradient(circle at center, #000428, #004e92);
        color: #e6f7ff;
    }
    
    .stApp {
        background: rgba(0, 10, 40, 0.95);
    }
    
    .gravity-title {
        font-size: 3.8rem;
        background: linear-gradient(90deg, #00ffff, #ff00ff, #ffff00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: 700;
        text-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
    }
    
    .einstein-quote {
        font-size: 1.1rem;
        color: #88ccff;
        text-align: center;
        font-style: italic;
        margin-bottom: 2rem;
        padding: 0 15%;
    }
    
    .gravity-card {
        background: rgba(10, 30, 70, 0.8);
        border: 2px solid;
        border-image: linear-gradient(45deg, #00ffff, #ff00ff) 1;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 150, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .gravity-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 200, 255, 0.4);
    }
    
    .field-line {
        height: 3px;
        background: linear-gradient(90deg, transparent, #00ffff, transparent);
        margin: 10px 0;
        border-radius: 2px;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #004e92, #000428);
        color: white;
        font-weight: bold;
        border: 1px solid #00ffff;
        padding: 12px 30px;
        border-radius: 25px;
        transition: all 0.3s ease;
        font-family: 'Orbitron', monospace;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #000428, #004e92);
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
        transform: scale(1.05);
    }
    
    .slider-container {
        background: rgba(0, 30, 60, 0.5);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(0, 50, 100, 0.3);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #00ffff, #ff00ff);
        border-radius: 4px;
    }
    
    /* Animation for gravity wells */
    @keyframes pulse {
        0% { opacity: 0.7; }
        50% { opacity: 1; }
        100% { opacity: 0.7; }
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
</style>
""", unsafe_allow_html=True)

# ==================== GRAVITY PHYSICS ENGINE ====================
class CognitiveGravityEngine:
    """Einstein-inspired attention gravity simulator"""
    
    def __init__(self):
        self.G = 6.67430e-11  # Gravitational constant (for scaling)
        self.c = 299792458    # Speed of light (for relativity effects)
        self.time_step = 0.1   # Simulation time step
        
    @staticmethod
    @st.cache_data(ttl=3600)
    def calculate_mental_mass(emotional_intensity, importance, dwell_time):
        """Calculate cognitive mass: M = EI × I × ln(DT+1)"""
        try:
            # Emotional intensity (0-10), importance (0-10), dwell_time in minutes
            mass = emotional_intensity * importance * np.log(dwell_time + 1)
            return max(0.1, min(100.0, mass))
        except:
            return 5.0
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def compute_gravity_force(mass1, mass2, distance):
        """Newton's law of universal gravitation: F = G * (m1*m2)/r²"""
        try:
            G = 1.0  # Normalized gravitational constant
            force = G * (mass1 * mass2) / (distance**2 + 0.01)  # Avoid division by zero
            return force
        except:
            return 0.0
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def calculate_escape_velocity(mass, radius):
        """Calculate velocity needed to escape mental orbit: v = √(2GM/r)"""
        try:
            G = 1.0
            if radius <= 0:
                radius = 0.1
            velocity = np.sqrt(2 * G * mass / radius)
            return velocity
        except:
            return 1.0
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def predict_orbit_period(mass, semi_major_axis):
        """Kepler's third law: T² ∝ a³/M (simplified)"""
        try:
            # Simplified version: T = k * sqrt(a³/M)
            period = 2 * np.pi * np.sqrt(semi_major_axis**3 / (mass + 0.1))
            return period  # In arbitrary time units
        except:
            return 10.0
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def generate_gravitational_field(mental_objects, grid_size=20):
        """Generate 2D gravitational potential field"""
        try:
            # Create coordinate grid
            x = np.linspace(-10, 10, grid_size)
            y = np.linspace(-10, 10, grid_size)
            X, Y = np.meshgrid(x, y)
            
            # Initialize potential
            potential = np.zeros_like(X)
            
            # Add contribution from each mental object
            for obj in mental_objects:
                if len(obj) >= 4:  # Ensure we have x, y, mass
                    x0, y0, mass = obj[1], obj[2], obj[3]
                    distance = np.sqrt((X - x0)**2 + (Y - y0)**2 + 0.01)
                    potential -= mass / distance
            
            return X, Y, potential
        except Exception as e:
            # Return default field
            x = np.linspace(-10, 10, 20)
            y = np.linspace(-10, 10, 20)
            X, Y = np.meshgrid(x, y)
            potential = -1 / (np.sqrt(X**2 + Y**2) + 0.1)
            return X, Y, potential
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def simulate_attention_trajectory(start_pos, mental_objects, steps=100):
        """Simulate attention drift in cognitive gravity field"""
        try:
            trajectory = [start_pos]
            current_pos = np.array(start_pos, dtype=float)
            
            for _ in range(steps):
                total_force = np.zeros(2)
                
                # Calculate force from each mental object
                for obj in mental_objects:
                    if len(obj) >= 4:
                        obj_pos = np.array([obj[1], obj[2]])
                        obj_mass = obj[3]
                        
                        # Vector from object to current position
                        r_vec = current_pos - obj_pos
                        distance = np.linalg.norm(r_vec) + 0.01
                        
                        # Force direction (toward object)
                        force_dir = -r_vec / distance
                        
                        # Force magnitude
                        force_mag = CognitiveGravityEngine.compute_gravity_force(
                            1.0,  # Unit attention mass
                            obj_mass,
                            distance
                        )
                        
                        total_force += force_dir * force_mag
                
                # Update position (Euler integration)
                current_pos += total_force * 0.1
                trajectory.append(current_pos.copy())
                
                # Boundary check
                current_pos = np.clip(current_pos, -12, 12)
            
            return np.array(trajectory)
        except:
            # Return simple circular trajectory
            t = np.linspace(0, 2*np.pi, 100)
            return np.column_stack([np.cos(t)*5, np.sin(t)*5])

# ==================== SESSION STATE INITIALIZATION ====================
if 'mind_gravity_data' not in st.session_state:
    st.session_state.mind_gravity_data = {
        'timestamps': [],
        'mental_objects': [],  # List of [name, x, y, mass, color, category]
        'attention_trajectories': [],
        'gravity_scores': [],
        'escape_velocities': []
    }

if 'gravity_engine' not in st.session_state:
    st.session_state.gravity_engine = CognitiveGravityEngine()

# ==================== SIDEBAR - MIND OBJECT INPUT ====================
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h2 style='color: #00ffff;'>🌀 ADD MENTAL OBJECTS</h2>
        <p style='color: #aaaaff;'>Each thought has gravity. Map yours.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Object 1
    st.markdown("#### 🧠 Mental Object 1")
    obj1_name = st.text_input("Name", "Work Deadline", key="obj1_name")
    col1, col2 = st.columns(2)
    with col1:
        obj1_emotion = st.slider("Emotional Charge", 0, 10, 7, key="obj1_emo")
    with col2:
        obj1_importance = st.slider("Importance", 0, 10, 8, key="obj1_imp")
    obj1_dwell = st.slider("Dwell Time (min)", 0, 120, 45, key="obj1_dwell")
    
    st.markdown("---")
    
    # Object 2
    st.markdown("#### 🧠 Mental Object 2")
    obj2_name = st.text_input("Name", "Personal Worry", key="obj2_name")
    col1, col2 = st.columns(2)
    with col1:
        obj2_emotion = st.slider("Emotional Charge", 0, 10, 6, key="obj2_emo")
    with col2:
        obj2_importance = st.slider("Importance", 0, 10, 4, key="obj2_imp")
    obj2_dwell = st.slider("Dwell Time (min)", 0, 120, 30, key="obj2_dwell")
    
    st.markdown("---")
    
    # Object 3
    st.markdown("#### 🧠 Mental Object 3")
    obj3_name = st.text_input("Name", "Creative Project", key="obj3_name")
    col1, col2 = st.columns(2)
    with col1:
        obj3_emotion = st.slider("Emotional Charge", 0, 10, 8, key="obj3_emo")
    with col2:
        obj3_importance = st.slider("Importance", 0, 10, 7, key="obj3_imp")
    obj3_dwell = st.slider("Dwell Time (min)", 0, 120, 20, key="obj3_dwell")
    
    st.markdown("---")
    
    # Calculate and add objects
    if st.button("⚡ CALCULATE GRAVITY FIELD", use_container_width=True):
        timestamp = datetime.now()
        
        # Calculate mental masses
        mass1 = st.session_state.gravity_engine.calculate_mental_mass(
            obj1_emotion, obj1_importance, obj1_dwell
        )
        mass2 = st.session_state.gravity_engine.calculate_mental_mass(
            obj2_emotion, obj2_importance, obj2_dwell
        )
        mass3 = st.session_state.gravity_engine.calculate_mental_mass(
            obj3_emotion, obj3_importance, obj3_dwell
        )
        
        # Assign positions (x, y coordinates in mental space)
        # Positive emotion = right, negative = left
        # Importance = vertical position
        positions = [
            [obj1_name, 2, 3, mass1, '#ff4444', 'Stress'],
            [obj2_name, -3, 1, mass2, '#44ff44', 'Worry'],
            [obj3_name, 0, 5, mass3, '#4444ff', 'Passion']
        ]
        
        # Store data
        st.session_state.mind_gravity_data['timestamps'].append(timestamp)
        st.session_state.mind_gravity_data['mental_objects'].append(positions)
        
        # Calculate gravity metrics
        gravity_force = st.session_state.gravity_engine.compute_gravity_force(mass1, mass2, 5.0)
        escape_vel = st.session_state.gravity_engine.calculate_escape_velocity(mass1, 2.0)
        
        st.session_state.mind_gravity_data['gravity_scores'].append(gravity_force)
        st.session_state.mind_gravity_data['escape_velocities'].append(escape_vel)
        
        st.success(f"""
        ✅ Gravity Field Updated!
        
        **Mental Masses Calculated:**
        • {obj1_name}: {mass1:.1f} units
        • {obj2_name}: {mass2:.1f} units  
        • {obj3_name}: {mass3:.1f} units
        
        **Strongest Attractor:** {positions[np.argmax([mass1, mass2, mass3])][0]}
        
        *"Gravity explains the motions of the planets, but it cannot explain who sets the planets in motion."*
        """)
    
    st.markdown("---")
    
    # Data management
    st.markdown("#### 🗃️ Gravity Archives")
    if st.button("Export Cognitive Field Data", use_container_width=True):
        # Create export dataframe
        export_data = []
        for i, positions in enumerate(st.session_state.mind_gravity_data['mental_objects']):
            for obj in positions:
                export_data.append({
                    'timestamp': st.session_state.mind_gravity_data['timestamps'][i],
                    'object_name': obj[0],
                    'x_position': obj[1],
                    'y_position': obj[2],
                    'mass': obj[3],
                    'category': obj[5]
                })
        
        df = pd.DataFrame(export_data)
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"mind_gravity_data_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    
    if st.button("Reset Gravity Field", type="secondary", use_container_width=True):
        st.session_state.mind_gravity_data = {
            'timestamps': [],
            'mental_objects': [],
            'attention_trajectories': [],
            'gravity_scores': [],
            'escape_velocities': []
        }
        st.rerun()
    
    st.markdown("---")
    
    # Stats
    if len(st.session_state.mind_gravity_data['timestamps']) > 0:
        total_objects = sum(len(objs) for objs in st.session_state.mind_gravity_data['mental_objects'])
        avg_mass = np.mean([mass for objs in st.session_state.mind_gravity_data['mental_objects'] 
                           for obj in objs for mass in [obj[3]]])
        
        st.markdown(f"""
        <div style='background: rgba(0, 100, 200, 0.2); padding: 15px; border-radius: 10px;'>
            <p style='margin: 0;'><strong>📊 Field Statistics</strong></p>
            <p style='margin: 5px 0;'>Total Observations: {len(st.session_state.mind_gravity_data['timestamps'])}</p>
            <p style='margin: 5px 0;'>Mental Objects: {total_objects}</p>
            <p style='margin: 5px 0;'>Avg Mental Mass: {avg_mass:.1f}</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== MAIN DASHBOARD ====================
st.markdown("<h1 class='gravity-title'>🌀 MIND-GRAVITY FIELD MAPPER</h1>", unsafe_allow_html=True)
st.markdown("<p class='einstein-quote'>\"Gravity is not responsible for people falling in love.\" — Albert Einstein</p>", unsafe_allow_html=True)

# Check if we have data
if len(st.session_state.mind_gravity_data['mental_objects']) == 0:
    st.info("""
    ## 🚀 Welcome to Your Cognitive Gravity Field
    
    **Add mental objects to visualize your attention gravity.** 
    
    This app applies Einstein's gravity physics to your mind:
    1. **Mental Mass**: Emotional charge × importance × dwell time
    2. **Gravity Wells**: Thoughts that pull your attention
    3. **Escape Velocity**: Energy needed to break thought loops
    4. **Attention Orbits**: Predictable thought recurrence patterns
    
    *Start by adding 3 mental objects in the sidebar →*
    """)
    
    # Demo visualization
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='gravity-card'>
            <h3>⚫ Mental Black Holes</h3>
            <p>Thoughts with escape velocity > focus energy</p>
            <div class='field-line'></div>
            <div class='pulse' style='text-align: center; font-size: 3rem;'>⚫</div>
            <p><em>High-gravity thoughts</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='gravity-card'>
            <h3>🔄 Attention Orbits</h3>
            <p>Predictable thought recurrence patterns</p>
            <div class='field-line'></div>
            <div style='text-align: center; font-size: 3rem;'>🔄</div>
            <p><em>Kepler's laws of cognition</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='gravity-card'>
            <h3>🚀 Escape Training</h3>
            <p>Build focus to break gravity wells</p>
            <div class='field-line'></div>
            <div style='text-align: center; font-size: 3rem;'>🚀</div>
            <p><em>v = √(2GM/r)</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.stop()

# ==================== GRAVITY VISUALIZATION ====================
try:
    # Get latest mental objects
    latest_objects = st.session_state.mind_gravity_data['mental_objects'][-1]
    
    # Extract data for visualization
    object_names = [obj[0] for obj in latest_objects]
    x_positions = [obj[1] for obj in latest_objects]
    y_positions = [obj[2] for obj in latest_objects]
    masses = [obj[3] for obj in latest_objects]
    colors = [obj[4] for obj in latest_objects]
    categories = [obj[5] for obj in latest_objects]
    
    # Calculate metrics
    strongest_idx = np.argmax(masses)
    weakest_idx = np.argmin(masses)
    
    # Calculate distances between objects
    distances = []
    for i in range(len(latest_objects)):
        for j in range(i+1, len(latest_objects)):
            dist = np.sqrt((x_positions[i]-x_positions[j])**2 + (y_positions[i]-y_positions[j])**2)
            gravity = st.session_state.gravity_engine.compute_gravity_force(masses[i], masses[j], dist)
            distances.append((object_names[i], object_names[j], dist, gravity))
    
    # ==================== METRICS DASHBOARD ====================
    st.markdown("## 📊 Your Cognitive Gravity Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_mass = sum(masses)
        st.markdown(f"""
        <div class='gravity-card'>
            <h3>⚖️ Total Mental Mass</h3>
            <h2 style='color: #ff4444;'>{total_mass:.1f}</h2>
            <p>Sum of all cognitive objects</p>
            <div class='field-line'></div>
            <p><em>Higher = more attention demand</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        strongest_escape = st.session_state.gravity_engine.calculate_escape_velocity(
            masses[strongest_idx], 2.0
        )
        st.markdown(f"""
        <div class='gravity-card'>
            <h3>🚀 Escape Velocity</h3>
            <h2 style='color: #44ff44;'>{strongest_escape:.1f}</h2>
            <p>To break from: {object_names[strongest_idx][:15]}...</p>
            <div class='field-line'></div>
            <p><em>v = √(2GM/r)</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if len(distances) > 0:
            max_gravity = max(distances, key=lambda x: x[3])[3]
        else:
            max_gravity = 0
        
        st.markdown(f"""
        <div class='gravity-card'>
            <h3>💫 Max Gravity Force</h3>
            <h2 style='color: #4444ff;'>{max_gravity:.2f}</h2>
            <p>Between two thoughts</p>
            <div class='field-line'></div>
            <p><em>F = G(m₁m₂)/r²</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        orbit_period = st.session_state.gravity_engine.predict_orbit_period(
            masses[strongest_idx], 5.0
        )
        st.markdown(f"""
        <div class='gravity-card'>
            <h3>🔄 Orbit Period</h3>
            <h2 style='color: #ff44ff;'>{orbit_period:.1f} units</h2>
            <p>Thought recurrence time</p>
            <div class='field-line'></div>
            <p><em>T² ∝ a³/M</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    # ==================== VISUALIZATIONS ====================
    st.markdown("## 🌌 Your Cognitive Gravity Field")
    
    tab1, tab2, tab3 = st.tabs(["3D Gravity Wells", "Attention Network", "Field Simulation"])
    
    with tab1:
        # 3D surface plot of gravitational potential
        X, Y, Z = st.session_state.gravity_engine.generate_gravitational_field([
            [obj[0], obj[1], obj[2], obj[3]] for obj in latest_objects
        ])
        
        fig = go.Figure(data=[
            go.Surface(
                x=X, y=Y, z=Z,
                colorscale='Viridis',
                contours={
                    "z": {"show": True, "usecolormap": True, "highlightcolor": "limegreen", "project": {"z": True}}
                },
                opacity=0.8
            ),
            go.Scatter3d(
                x=x_positions,
                y=y_positions,
                z=[-5]*len(x_positions),  # Place objects at bottom
                mode='markers+text',
                marker=dict(
                    size=[m*2 for m in masses],  # Size proportional to mass
                    color=colors,
                    opacity=0.9,
                    line=dict(color='white', width=2)
                ),
                text=object_names,
                textposition="top center",
                hoverinfo='text'
            )
        ])
        
        fig.update_layout(
            title="Your Mental Gravity Wells (Negative Potential = Attraction)",
            scene=dict(
                xaxis_title='Emotional Valence (-left to +right)',
                yaxis_title='Importance (low to high)',
                zaxis_title='Gravitational Potential',
                bgcolor='rgba(0, 20, 40, 0.8)'
            ),
            height=700,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#e6e6e6'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        # Network graph of mental objects
        G = nx.Graph()
        
        # Add nodes
        for i, (name, mass) in enumerate(zip(object_names, masses)):
            G.add_node(i, label=name, mass=mass, color=colors[i])
        
        # Add edges with gravity as weight
        for i in range(len(latest_objects)):
            for j in range(i+1, len(latest_objects)):
                dist = np.sqrt((x_positions[i]-x_positions[j])**2 + (y_positions[i]-y_positions[j])**2)
                gravity = st.session_state.gravity_engine.compute_gravity_force(masses[i], masses[j], dist)
                if gravity > 0.1:  # Only show significant connections
                    G.add_edge(i, j, weight=gravity*10, label=f"{gravity:.2f}")
        
        # Create network visualization
        pos = nx.spring_layout(G, weight='weight', seed=42)
        
        edge_trace = []
        for edge in G.edges(data=True):
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_trace.append(go.Scatter(
                x=[x0, x1, None], y=[y0, y1, None],
                line=dict(width=edge[2]['weight'], color='rgba(100, 100, 255, 0.6)'),
                hoverinfo='none',
                mode='lines'
            ))
        
        node_trace = go.Scatter(
            x=[pos[node][0] for node in G.nodes()],
            y=[pos[node][1] for node in G.nodes()],
            mode='markers+text',
            marker=dict(
                size=[G.nodes[node]['mass']*5 for node in G.nodes()],
                color=[G.nodes[node]['color'] for node in G.nodes()],
                line=dict(color='white', width=2)
            ),
            text=[G.nodes[node]['label'] for node in G.nodes()],
            textposition="top center",
            hoverinfo='text'
        )
        
        fig = go.Figure(data=edge_trace + [node_trace])
        
        fig.update_layout(
            title="Attention Network (Edge thickness = Gravity strength)",
            showlegend=False,
            hovermode='closest',
            height=600,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#e6e6e6',
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        # Attention trajectory simulation
        st.markdown("#### 🎯 Simulate Attention Drift")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            start_x = st.slider("Start X", -10.0, 10.0, 0.0, key="start_x")
            start_y = st.slider("Start Y", -10.0, 10.0, 0.0, key="start_y")
            
            if st.button("🌀 Simulate Attention Path", use_container_width=True):
                # Convert latest objects to format expected by simulator
                mental_objects_formatted = []
                for obj in latest_objects:
                    mental_objects_formatted.append([obj[0], obj[1], obj[2], obj[3]])
                
                # Simulate trajectory
                trajectory = st.session_state.gravity_engine.simulate_attention_trajectory(
                    [start_x, start_y],
                    mental_objects_formatted
                )
                
                # Store trajectory
                st.session_state.mind_gravity_data['attention_trajectories'].append(trajectory)
            
            # Display latest trajectory info
            if len(st.session_state.mind_gravity_data['attention_trajectories']) > 0:
                latest_traj = st.session_state.mind_gravity_data['attention_trajectories'][-1]
                st.metric("Trajectory Length", f"{len(latest_traj)} steps")
                
                # Find which object it ends closest to
                if len(latest_traj) > 0:
                    end_pos = latest_traj[-1]
                    distances = []
                    for obj in latest_objects:
                        dist = np.sqrt((end_pos[0]-obj[1])**2 + (end_pos[1]-obj[2])**2)
                        distances.append(dist)
                    
                    closest_idx = np.argmin(distances)
                    st.metric("Ends Near", object_names[closest_idx])
        
        with col2:
            # Plot trajectory
            if len(st.session_state.mind_gravity_data['attention_trajectories']) > 0:
                trajectory = st.session_state.mind_gravity_data['attention_trajectories'][-1]
                
                fig = go.Figure()
                
                # Add mental objects
                fig.add_trace(go.Scatter(
                    x=x_positions,
                    y=y_positions,
                    mode='markers+text',
                    marker=dict(
                        size=[m*10 for m in masses],
                        color=colors,
                        opacity=0.8,
                        line=dict(color='white', width=2)
                    ),
                    text=object_names,
                    textposition="top center",
                    name="Mental Objects"
                ))
                
                # Add trajectory
                fig.add_trace(go.Scatter(
                    x=trajectory[:, 0],
                    y=trajectory[:, 1],
                    mode='lines+markers',
                    line=dict(color='cyan', width=2),
                    marker=dict(size=4, color='white'),
                    name="Attention Path"
                ))
                
                # Add starting point
                fig.add_trace(go.Scatter(
                    x=[trajectory[0, 0]],
                    y=[trajectory[0, 1]],
                    mode='markers',
                    marker=dict(size=12, color='lime', symbol='star'),
                    name="Start"
                ))
                
                fig.update_layout(
                    title="Attention Drift Simulation",
                    height=500,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font_color='#e6e6e6',
                    xaxis=dict(range=[-12, 12]),
                    yaxis=dict(range=[-12, 12])
                )
                
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Run a simulation to see attention drift patterns")
    
    # ==================== ESCAPE VELOCITY TRAINING ====================
    st.markdown("## 🚀 Escape Velocity Training")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Build Focus to Escape Mental Gravity Wells
        
        **Training Principle:**  
        Escape velocity = √(2GM/r)  
        Where:
        - **G** = Gravitational constant (fixed)
        - **M** = Mental mass of the thought
        - **r** = Your current distance from it
        
        **To escape a thought loop:**
        1. **Reduce M**: Lower emotional charge (through reframing)
        2. **Increase r**: Create mental distance (through mindfulness)
        3. **Increase v**: Build focus energy (through practice)
        """)
        
        # Interactive training
        selected_object = st.selectbox(
            "Select thought to escape:",
            object_names,
            index=strongest_idx
        )
        
        selected_idx = object_names.index(selected_object)
        selected_mass = masses[selected_idx]
        
        current_distance = st.slider(
            "Your mental distance from this thought (r):",
            0.1, 10.0, 2.0, 0.1,
            help="How much psychological distance you have"
        )
        
        required_velocity = st.session_state.gravity_engine.calculate_escape_velocity(
            selected_mass, current_distance
        )
        
        your_focus = st.slider(
            "Your current focus energy (v):",
            0.0, 10.0, 5.0, 0.1,
            help="Your available attention/focus energy"
        )
        
        if your_focus >= required_velocity:
            st.success(f"""
            ✅ **ESCAPE VELOCITY ACHIEVED!**
            
            Required: {required_velocity:.1f}  
            Your focus: {your_focus:.1f}  
            
            You can break free from "{selected_object}"!
            """)
        else:
            st.warning(f"""
            ⚠️ **ESCAPE VELOCITY NOT REACHED**
            
            Required: {required_velocity:.1f}  
            Your focus: {your_focus:.1f}  
            
            **To escape:**
            1. Increase focus by {required_velocity - your_focus:.1f} units
            2. Increase distance to {selected_mass * 2 / your_focus**2:.1f}
            3. Reduce thought's emotional charge
            """)
    
    with col2:
        st.markdown("""
        ### 🧠 Training Exercises
        
        **1. Distance Building:**
        - Objectify the thought ("I notice I'm thinking about...")
        - Write it down physically
        - Schedule worry time later
        
        **2. Focus Building:**
        - 5-minute mindfulness meditation
        - Pomodoro technique (25 min focus)
        - Single-tasking practice
        
        **3. Mass Reduction:**
        - Cognitive reframing
        - Emotional labeling
        - Perspective shifting
        
        *"The measure of intelligence is the ability to change." — Einstein*
        """)
        
        # Progress chart
        if len(st.session_state.mind_gravity_data['escape_velocities']) > 1:
            progress_df = pd.DataFrame({
                'Session': range(len(st.session_state.mind_gravity_data['escape_velocities'])),
                'Escape Velocity': st.session_state.mind_gravity_data['escape_velocities']
            })
            
            chart = alt.Chart(progress_df).mark_line(point=True).encode(
                x='Session',
                y='Escape Velocity',
                color=alt.value('#00ffff'),
                tooltip=['Session', 'Escape Velocity']
            ).properties(
                title='Escape Velocity Progress',
                height=200
            )
            
            st.altair_chart(chart, use_container_width=True)

except Exception as e:
    st.error(f"Gravity calculation error: {str(e)}")
    st.info("Please check your mental object data and try again.")

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #88ccff; padding: 20px;'>
    <p><strong>🌀 MIND-GRAVITY FIELD MAPPER v1.0</strong> | Einstein-Inspired Cognitive Physics</p>
    <p><em>Applying Gravitational Physics to Attention Management</em></p>
    <p>⚫ Map mental black holes | 🚀 Calculate escape velocities | 🔄 Predict attention orbits</p>
    <p>💡 <strong>Einstein Insight:</strong> "We cannot solve our problems with the same thinking we used when we created them."</p>
</div>
""", unsafe_allow_html=True)

# ==================== AUTO-ANALYSIS ====================
if len(st.session_state.mind_gravity_data['timestamps']) > 0:
    latest_objects = st.session_state.mind_gravity_data['mental_objects'][-1]
    
    if len(latest_objects) >= 2:
        # Find the strongest gravitational relationship
        max_gravity = 0
        strongest_pair = None
        
        for i in range(len(latest_objects)):
            for j in range(i+1, len(latest_objects)):
                dist = np.sqrt((latest_objects[i][1]-latest_objects[j][1])**2 + 
                              (latest_objects[i][2]-latest_objects[j][2])**2)
                gravity = st.session_state.gravity_engine.compute_gravity_force(
                    latest_objects[i][3], latest_objects[j][3], dist
                )
                
                if gravity > max_gravity:
                    max_gravity = gravity
                    strongest_pair = (latest_objects[i][0], latest_objects[j][0])
        
        if strongest_pair:
            st.info(f"""
            🔍 **GRAVITY INSIGHT:** Your strongest mental connection is between  
            **"{strongest_pair[0]}"** and **"{strongest_pair[1]}"**  
            Gravity force: {max_gravity:.2f}  
            
            *This relationship may be draining your attention energy.*
            """)
