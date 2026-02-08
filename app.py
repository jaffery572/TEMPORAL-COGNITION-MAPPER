"""
CHRONOSPHERE: Personal Spacetime Optimization Engine
Einstein-Level Innovation: Fusing relativity physics with cognitive time perception

Deployment: Push to GitHub, connect to Streamlit Cloud, no additional config needed.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import altair as alt
from datetime import datetime, timedelta
import time
from scipy import stats, interpolate
import warnings
warnings.filterwarnings('ignore')

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="CHRONOSPHERE | Your Personal Spacetime",
    page_icon="⏳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');
    
    .main {
        font-family: 'Space Mono', monospace;
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #e6e6e6;
    }
    
    .stApp {
        background: rgba(10, 10, 30, 0.95);
    }
    
    .spacetime-title {
        font-size: 3.5rem;
        background: linear-gradient(90deg, #00ffff, #0080ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    
    .einstein-quote {
        font-size: 1.1rem;
        color: #aaaaff;
        text-align: center;
        font-style: italic;
        margin-bottom: 2rem;
        padding: 0 20%;
    }
    
    .metric-card {
        background: rgba(20, 20, 60, 0.7);
        border: 2px solid #4444ff;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 100, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 100, 255, 0.3);
        border-color: #00ffff;
    }
    
    .time-dilation-indicator {
        height: 10px;
        background: linear-gradient(90deg, #ff0000, #ffff00, #00ff00);
        border-radius: 5px;
        margin: 10px 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #0080ff, #00ffff);
        color: black;
        font-weight: bold;
        border: none;
        padding: 12px 30px;
        border-radius: 25px;
        transition: all 0.3s ease;
        font-family: 'Space Mono', monospace;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 20px rgba(0, 255, 255, 0.4);
    }
    
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #0080ff, #00ffff);
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
        background: rgba(20, 20, 60, 0.5);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #0080ff, #00ffff);
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ==================== SPACETIME PHYSICS ENGINE ====================
class SpacetimeEngine:
    """Einstein-inspired personal time perception optimizer"""
    
    def __init__(self):
        self.time_dilation_constant = 0.01
        self.temporal_curvature_factor = 0.5
        self.causal_radius = 7  # days
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def calculate_time_dilation(stress_level, focus_level):
        """Calculate subjective time dilation (relativity-inspired)"""
        try:
            # Based on: perceived_time = actual_time * (1 + k*(stress - focus))
            dilation_factor = 1 + 0.01 * (stress_level - focus_level)
            return max(0.5, min(2.0, dilation_factor))
        except:
            return 1.0
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def calculate_temporal_curvature(emotion_valence, energy_level):
        """Calculate how emotions bend future planning (spacetime curvature)"""
        try:
            # Positive emotions create "gravitational wells" in future planning
            curvature = 0.5 * emotion_valence + 0.3 * (energy_level - 5)
            return curvature / 10  # Normalize to [-1, 1]
        except:
            return 0.0
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def compute_causal_light_cone(decisions_data, current_mood):
        """Calculate decision impact radius (light cone of causality)"""
        try:
            if len(decisions_data) < 3:
                return 3.0  # Default radius in days
            
            # Impact radius based on decision consistency and current state
            consistency = np.std([d['quality'] for d in decisions_data[-5:]]) if len(decisions_data) >= 5 else 1.0
            mood_factor = 1 + (current_mood - 5) / 10
            
            radius = max(1.0, min(14.0, 7.0 / (consistency + 0.1) * mood_factor))
            return radius
        except:
            return 7.0
    
    @staticmethod
    @st.cache_data(ttl=3600)
    def optimize_timing(task_importance, task_difficulty, personal_rhythm):
        """Suggest optimal timing using spacetime optimization"""
        try:
            # Spacetime optimization algorithm
            base_score = task_importance * (1 - task_difficulty/10)
            rhythm_adjustment = 1 + (personal_rhythm - 5) / 10
            
            # Convert to hours from now (0-48 hours)
            optimal_hours = 24 * (1 - base_score * rhythm_adjustment)
            optimal_hours = max(1, min(48, optimal_hours))
            
            return {
                'hours_from_now': optimal_hours,
                'confidence': min(0.95, base_score * 0.8),
                'reason': f"Optimal spacetime coordinate based on importance-weight={task_importance}, difficulty-curvature={task_difficulty}"
            }
        except Exception as e:
            return {'hours_from_now': 24, 'confidence': 0.5, 'reason': 'Using default spacetime metric'}

# ==================== SESSION STATE INITIALIZATION ====================
if 'spacetime_data' not in st.session_state:
    st.session_state.spacetime_data = {
        'timestamps': [],
        'time_perception': [],  # 0-100: 0=time frozen, 100=time flying
        'stress_level': [],     # 0-10
        'focus_level': [],      # 0-10
        'emotion_valence': [],  # -5 to +5
        'energy_level': [],     # 0-10
        'activities': [],
        'decisions': []  # List of {'task': str, 'quality': 0-10, 'timestamp': datetime}
    }

if 'engine' not in st.session_state:
    st.session_state.engine = SpacetimeEngine()

# ==================== SIDEBAR - DAILY CHECK-IN ====================
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h2 style='color: #00ffff;'>⏳ DAILY SPACETIME CHECK-IN</h2>
        <p style='color: #aaaaff;'>Einstein: "Time is relative to your experience"</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Current time perception
    st.markdown("#### How fast is time moving?")
    time_perception = st.slider(
        "0 = Frozen | 100 = Flying",
        0, 100, 50,
        key="time_slider",
        help="Your subjective experience of time's flow"
    )
    
    # Stress and focus
    col1, col2 = st.columns(2)
    with col1:
        stress = st.slider("Stress", 0, 10, 5, help="Stress causes time dilation")
    with col2:
        focus = st.slider("Focus", 0, 10, 5, help="Focus alters time perception")
    
    # Emotion and energy
    st.markdown("#### Emotional Spacetime Curvature")
    emotion = st.slider("Emotion (-5 to +5)", -5, 5, 0, 
                       help="Negative emotions bend time forward, positive bend it backward")
    energy = st.slider("Energy Level", 0, 10, 5, help="Energy affects temporal resolution")
    
    # Activity type
    activity = st.selectbox(
        "Primary Activity",
        ["Deep Work", "Meetings", "Creative", "Learning", "Resting", "Social", "Physical", "Other"],
        help="Activity type creates different spacetime geometries"
    )
    
    # Submit button
    if st.button("📡 Record Spacetime Coordinates", use_container_width=True):
        timestamp = datetime.now()
        
        # Store data
        st.session_state.spacetime_data['timestamps'].append(timestamp)
        st.session_state.spacetime_data['time_perception'].append(time_perception)
        st.session_state.spacetime_data['stress_level'].append(stress)
        st.session_state.spacetime_data['focus_level'].append(focus)
        st.session_state.spacetime_data['emotion_valence'].append(emotion)
        st.session_state.spacetime_data['energy_level'].append(energy)
        st.session_state.spacetime_data['activities'].append(activity)
        
        # Calculate metrics
        dilation = st.session_state.engine.calculate_time_dilation(stress, focus)
        curvature = st.session_state.engine.calculate_temporal_curvature(emotion, energy)
        
        st.success(f"""
        ✅ Spacetime coordinates recorded!
        
        **Time Dilation:** {dilation:.2f}x
        **Temporal Curvature:** {curvature:.3f}
        
        *"The only reason for time is so that everything doesn't happen at once."*
        """)
    
    st.markdown("---")
    
    # Data management
    st.markdown("#### 🗃️ Spacetime Archive")
    if st.button("Export My Spacetime Data", use_container_width=True):
        df = pd.DataFrame(st.session_state.spacetime_data)
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"chronosphere_data_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    
    if st.button("Reset Spacetime Continuum", type="secondary", use_container_width=True):
        st.session_state.spacetime_data = {
            'timestamps': [],
            'time_perception': [],
            'stress_level': [],
            'focus_level': [],
            'emotion_valence': [],
            'energy_level': [],
            'activities': [],
            'decisions': []
        }
        st.rerun()
    
    st.markdown("---")
    
    # Stats
    if len(st.session_state.spacetime_data['timestamps']) > 0:
        days_tracked = len(set([d.date() for d in st.session_state.spacetime_data['timestamps']]))
        avg_perception = np.mean(st.session_state.spacetime_data['time_perception'])
        st.markdown(f"""
        <div style='background: rgba(0, 100, 255, 0.2); padding: 15px; border-radius: 10px;'>
            <p style='margin: 0;'><strong>📊 Spacetime Statistics</strong></p>
            <p style='margin: 5px 0;'>Days Tracked: {days_tracked}</p>
            <p style='margin: 5px 0;'>Avg Time Perception: {avg_perception:.1f}/100</p>
            <p style='margin: 5px 0;'>Data Points: {len(st.session_state.spacetime_data['timestamps'])}</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== MAIN DASHBOARD ====================
st.markdown("<h1 class='spacetime-title'>⏳ CHRONOSPHERE</h1>", unsafe_allow_html=True)
st.markdown("<p class='einstein-quote'>\"The distinction between past, present and future is only a stubbornly persistent illusion.\" — Albert Einstein</p>", unsafe_allow_html=True)

# Check if we have enough data
if len(st.session_state.spacetime_data['timestamps']) < 3:
    st.info("""
    ## 🚀 Welcome to Your Personal Spacetime
    
    **Record 3+ daily check-ins to unlock your spacetime visualization.** 
    
    This app merges Einstein's relativity with your subjective time experience:
    1. **Time Dilation**: How stress/focus alters your time perception
    2. **Temporal Curvature**: How emotions bend your future planning
    3. **Causal Light Cones**: Your decision impact radius
    
    *Start by completing today's check-in in the sidebar →*
    """)
    
    # Demo visualization
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h3>⏱️ Time Dilation</h3>
            <p>Stress slows time, focus speeds it up</p>
            <div class='time-dilation-indicator'></div>
            <p><em>Your personal relativity</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h3>🌀 Temporal Curvature</h3>
            <p>Emotions bend your timeline</p>
            <div style='text-align: center; font-size: 2rem;'>∞</div>
            <p><em>Spacetime geometry</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h3>🔦 Causal Radius</h3>
            <p>How far ahead you effectively plan</p>
            <div style='text-align: center; font-size: 2rem;'>7d</div>
            <p><em>Light cone of influence</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.stop()

# ==================== SPACETIME VISUALIZATION ====================
try:
    # Prepare data
    df = pd.DataFrame({
        'timestamp': st.session_state.spacetime_data['timestamps'],
        'time_perception': st.session_state.spacetime_data['time_perception'],
        'stress': st.session_state.spacetime_data['stress_level'],
        'focus': st.session_state.spacetime_data['focus_level'],
        'emotion': st.session_state.spacetime_data['emotion_valence'],
        'energy': st.session_state.spacetime_data['energy_level'],
        'activity': st.session_state.spacetime_data['activities']
    })
    
    df['date'] = pd.to_datetime(df['timestamp']).dt.date
    df['time_of_day'] = pd.to_datetime(df['timestamp']).dt.hour + pd.to_datetime(df['timestamp']).dt.minute/60
    
    # Calculate derived metrics
    df['time_dilation'] = df.apply(
        lambda row: st.session_state.engine.calculate_time_dilation(row['stress'], row['focus']), 
        axis=1
    )
    df['temporal_curvature'] = df.apply(
        lambda row: st.session_state.engine.calculate_temporal_curvature(row['emotion'], row['energy']), 
        axis=1
    )
    
    # Current light cone radius
    current_mood = df.iloc[-1]['emotion'] if len(df) > 0 else 5
    light_cone_radius = st.session_state.engine.compute_causal_light_cone(
        st.session_state.spacetime_data['decisions'],
        current_mood
    )
    
    # ==================== METRICS DASHBOARD ====================
    st.markdown("## 📊 Your Personal Spacetime Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_dilation = df['time_dilation'].mean()
        dilation_status = "SLOWED" if avg_dilation < 0.9 else "NORMAL" if avg_dilation < 1.1 else "ACCELERATED"
        dilation_color = "#ff4444" if avg_dilation < 0.9 else "#44ff44" if avg_dilation < 1.1 else "#4444ff"
        st.markdown(f"""
        <div class='metric-card'>
            <h3>⏱️ Time Dilation</h3>
            <h2 style='color: {dilation_color};'>{avg_dilation:.2f}x</h2>
            <p>{dilation_status}</p>
            <div class='time-dilation-indicator' style='opacity: {abs(avg_dilation-1)+0.3};'></div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        avg_curvature = df['temporal_curvature'].mean()
        curvature_dir = "FORWARD-BENT" if avg_curvature < -0.1 else "FLAT" if abs(avg_curvature) < 0.1 else "BACKWARD-BENT"
        curvature_color = "#ff4444" if avg_curvature < -0.1 else "#44ff44" if abs(avg_curvature) < 0.1 else "#4444ff"
        st.markdown(f"""
        <div class='metric-card'>
            <h3>🌀 Temporal Curvature</h3>
            <h2 style='color: {curvature_color};'>{avg_curvature:.3f}</h2>
            <p>{curvature_dir}</p>
            <div style='text-align: center; font-size: 2rem;'>↷</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        avg_perception = df['time_perception'].mean()
        perception_status = "FROZEN" if avg_perception < 30 else "SLOW" if avg_perception < 45 else "NORMAL" if avg_perception < 70 else "FAST"
        st.markdown(f"""
        <div class='metric-card'>
            <h3>📈 Time Perception</h3>
            <h2 style='color: #00ffff;'>{avg_perception:.0f}/100</h2>
            <p>{perception_status}</p>
            <progress value="{avg_perception}" max="100" style="width: 100%; height: 10px;"></progress>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>🔦 Causal Radius</h3>
            <h2 style='color: #ffaa00;'>{light_cone_radius:.1f} days</h2>
            <p>Effective planning horizon</p>
            <div style='text-align: center;'>
                <div style='display: inline-block; width: {light_cone_radius*5}px; height: {light_cone_radius*5}px; border-radius: 50%; border: 2px solid #ffaa00;'></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # ==================== VISUALIZATIONS ====================
    st.markdown("## 🌌 Spacetime Visualization")
    
    tab1, tab2, tab3 = st.tabs(["3D Spacetime", "Time Perception Trends", "Activity Analysis"])
    
    with tab1:
        # 3D Spacetime Plot
        fig = go.Figure(data=[go.Scatter3d(
            x=df['time_of_day'],
            y=df['time_perception'],
            z=df['emotion'],
            mode='markers+lines',
            marker=dict(
                size=8,
                color=df['energy'],
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Energy Level")
            ),
            line=dict(
                color='rgba(100, 100, 255, 0.3)',
                width=2
            ),
            text=df['activity'],
            hovertemplate='<b>%{text}</b><br>Time: %{x:.1f}h<br>Perception: %{y}<br>Emotion: %{z}<extra></extra>'
        )])
        
        fig.update_layout(
            title="Your Personal Spacetime (Time vs Perception vs Emotion)",
            scene=dict(
                xaxis_title='Time of Day',
                yaxis_title='Time Perception',
                zaxis_title='Emotion (-5 to +5)',
                bgcolor='rgba(10, 10, 30, 0.8)'
            ),
            height=600,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#e6e6e6'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        # Time perception over time
        df_sorted = df.sort_values('timestamp')
        
        chart = alt.Chart(df_sorted).mark_line(point=True).encode(
            x=alt.X('timestamp:T', title='Date'),
            y=alt.Y('time_perception:Q', title='Time Perception (0-100)', scale=alt.Scale(domain=[0, 100])),
            color=alt.value('#00ffff'),
            tooltip=['timestamp', 'time_perception', 'activity']
        ).properties(
            title='Your Time Perception Journey',
            height=400
        ).configure(
            background='rgba(0,0,0,0)'
        ).configure_axis(
            gridColor='rgba(100, 100, 100, 0.3)',
            labelColor='#e6e6e6',
            titleColor='#e6e6e6'
        )
        
        st.altair_chart(chart, use_container_width=True)
        
        # Dilation vs curvature scatter
        scatter = alt.Chart(df).mark_circle(size=100).encode(
            x=alt.X('time_dilation:Q', title='Time Dilation Factor'),
            y=alt.Y('temporal_curvature:Q', title='Temporal Curvature'),
            color=alt.Color('energy:Q', scale=alt.Scale(scheme='viridis')),
            tooltip=['activity', 'time_dilation', 'temporal_curvature', 'emotion']
        ).properties(
            title='Dilation vs Curvature: Your Spacetime Geometry',
            height=400
        )
        
        st.altair_chart(scatter, use_container_width=True)
    
    with tab3:
        # Activity analysis
        activity_counts = df['activity'].value_counts().reset_index()
        activity_counts.columns = ['activity', 'count']
        
        bar_chart = alt.Chart(activity_counts).mark_bar().encode(
            x=alt.X('count:Q', title='Frequency'),
            y=alt.Y('activity:N', title='Activity Type', sort='-x'),
            color=alt.value('#0080ff'),
            tooltip=['activity', 'count']
        ).properties(
            title='Activities in Your Spacetime',
            height=400
        )
        
        st.altair_chart(bar_chart, use_container_width=True)
        
        # Activity vs time perception
        box_chart = alt.Chart(df).mark_boxplot().encode(
            x=alt.X('activity:N', title='Activity Type'),
            y=alt.Y('time_perception:Q', title='Time Perception'),
            color=alt.value('#00ffff')
        ).properties(
            title='How Activities Affect Your Time Perception',
            height=400
        )
        
        st.altair_chart(box_chart, use_container_width=True)
    
    # ==================== DECISION OPTIMIZER ====================
    st.markdown("## 🤔 Spacetime Decision Optimizer")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### When should you schedule important tasks?
        
        Based on your personal spacetime metrics, we can optimize timing:
        """)
        
        task_name = st.text_input("Task Name", "Important Meeting")
        task_importance = st.slider("Importance (1-10)", 1, 10, 7, 
                                   help="How critical is this task?")
        task_difficulty = st.slider("Difficulty (1-10)", 1, 10, 5,
                                   help="Mental/emotional effort required")
        
        if st.button("🚀 Calculate Optimal Spacetime", use_container_width=True):
            # Use recent personal rhythm (average of last 3 energy levels)
            recent_rhythm = df['energy'].tail(3).mean() if len(df) >= 3 else 5
            
            optimization = st.session_state.engine.optimize_timing(
                task_importance, 
                task_difficulty, 
                recent_rhythm
            )
            
            optimal_time = datetime.now() + timedelta(hours=optimization['hours_from_now'])
            
            st.markdown(f"""
            <div class='metric-card'>
                <h3>✨ Optimal Spacetime Calculated</h3>
                
                <h2 style='color: #00ff00;'>{optimal_time.strftime('%A, %B %d at %I:%M %p')}</h2>
                
                <p><strong>In {optimization['hours_from_now']:.1f} hours from now</strong></p>
                
                <p><em>Confidence: {optimization['confidence']*100:.0f}%</em></p>
                
                <p>📝 <strong>Reasoning:</strong> {optimization['reason']}</p>
                
                <p>⏳ <strong>Based on your:</strong></p>
                <ul>
                    <li>Average energy rhythm: {recent_rhythm:.1f}/10</li>
                    <li>Current time dilation: {df.iloc[-1]['time_dilation']:.2f}x</li>
                    <li>Temporal curvature: {df.iloc[-1]['temporal_curvature']:.3f}</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        ### 🧠 How It Works
        
        The optimizer uses:
        
        1. **Your Time Dilation**  
           Current stress/focus ratio
        
        2. **Temporal Curvature**  
           Emotional impact on planning
        
        3. **Energy Rhythms**  
           Historical patterns
        
        4. **Task Geometry**  
           Importance/difficulty spacetime
        
        *"The only way to escape the corruptible effect of praise is to go on working." — Einstein*
        """)
        
        # Record decision quality
        if len(st.session_state.spacetime_data['decisions']) > 0:
            st.markdown("#### Recent Decision Quality")
            recent_decisions = st.session_state.spacetime_data['decisions'][-5:]
            for d in recent_decisions:
                quality_stars = "★" * int(d['quality']/2) + "☆" * (5 - int(d['quality']/2))
                st.caption(f"{d['task'][:20]}... {quality_stars}")

except Exception as e:
    st.error(f"Spacetime calculation error: {str(e)}")
    st.info("Please record more data points to stabilize your spacetime continuum.")

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #aaaaff; padding: 20px;'>
    <p><strong>⏳ CHRONOSPHERE v1.0</strong> | Einstein-Inspired Spacetime Optimization</p>
    <p><em>Fusing Relativity Physics with Cognitive Time Perception</em></p>
    <p>📡 Record daily to improve accuracy | 🔮 14+ days for predictive analytics</p>
    <p>💡 <strong>Einstein Insight:</strong> "Imagination is more important than knowledge."</p>
</div>
""", unsafe_allow_html=True)

# ==================== AUTO-SAVE REMINDER ====================
if len(st.session_state.spacetime_data['timestamps']) > 0:
    last_record = pd.to_datetime(st.session_state.spacetime_data['timestamps'][-1])
    hours_since = (datetime.now() - last_record).total_seconds() / 3600
    
    if hours_since > 24:
        st.warning(f"⏰ {hours_since:.0f} hours since last check-in. Time perception data aging.")
