# design.md – Cloud Cost Hero  
A single-file Streamlit mini-game to teach **Compute Savings Plans** through play.

---

## 1. Purpose
Create a **self-contained** Streamlit app (`cloud_cost_hero.py`) that lets students **minimize a 30-day AWS bill** by choosing the right hourly commitment for a Compute Savings Plan.  
The game must run with **zero external dependencies** beyond `streamlit`.

---

## 2. Core Game Loop (single screen)

| Phase | Description | Key UI Elements |
|-------|-------------|-----------------|
| **1. Setup** | Load a random “startup persona” (steady vs spiky) | `st.header`, `st.write` |
| **2. Live Usage** | Simulate EC2 usage every 2 s | `st.line_chart` |
| **3. Decision** | Player sets **hourly commitment** ($) and locks it | `st.slider`, `st.button("Lock-in Plan")` |
| **4. Fast-Forward** | Skip to end-of-month in 5 s | `st.progress`, `st.spinner` |
| **5. Score** | Show final bill, % saved, risk events | `st.metric`, `st.balloons` if ≥ 30 % saved |
| **6. Replay** | Button to restart with new persona | `st.button("Play Again")` |

---

## 3. Data Model (all in `st.session_state`)

| Key | Type | Meaning |
|-----|------|---------|
| `persona` | dict | keys: `name`, `base_rate`, `spike_prob`, `spike_factor` |
| `usage_log` | list[float] | per-hour usage (CPU hours) |
| `commit` | float | locked hourly commitment ($) |
| `locked` | bool | True once player locks plan |
| `tick` | int | current hour (0-719) |

---

## 4. Simulation Logic

### 4.1 Usage Generation
```python
def generate_usage(persona, hour):
    base = persona["base_rate"]
    if random.random() < persona["spike_prob"]:
        return base * persona["spike_factor"]
    return base
```

### 4.2 Cost Calculation
```python
on_demand_rate = 0.05  # $/CPU-hour
on_demand_cost = sum(usage_log) * on_demand_rate
savings_plan_cost = commit * 24 * 30
overage_cost = max(0, sum(usage_log) - commit * 24 * 30) * on_demand_rate
total_cost = savings_plan_cost + overage_cost
savings_pct = (on_demand_cost - total_cost) / on_demand_cost * 100
```

---

## 5. UI Specification

### 5.1 Layout (top-to-bottom)
1. **Title**: `st.title("🎮 Cloud Cost Hero")`
2. **Persona Card**: `st.info(f"Startup: {persona['name']}")`
3. **Live Chart**: `st.line_chart(usage_log[-50:])` (auto-scroll)
4. **Controls Panel** (disabled after lock):
   - `st.slider("Hourly commitment ($)", 0.0, 5.0, 1.0, 0.1, key="commit")`
   - `st.button("Lock-in Plan", disabled=st.session_state.locked)`
5. **Progress & Result**:
   - `st.progress(tick/719)`
   - After lock: `st.metric("Projected 30-day bill", f"${total_cost:,.2f}", delta=f"{savings_pct:.1f}%")`
6. **Replay**: `st.button("Play Again")` clears session state.

### 5.2 Feedback
- ≥ 30 % savings → `st.balloons()`
- < 0 % → `st.error("You paid more than On-Demand!")`

---

## 6. Constants & Personas
```python
PERSONAS = [
    {"name": "Steady SaaS", "base_rate": 2.0, "spike_prob": 0.05, "spike_factor": 1.5},
    {"name": "Spiky Batch", "base_rate": 1.0, "spike_prob": 0.2, "spike_factor": 3.0},
    {"name": "Weekend Peak", "base_rate": 1.5, "spike_prob": 0.1, "spike_factor": 2.5},
]
```

---

## 7. State Management Rules
- On first run → pick random persona, init empty `usage_log`, `tick=0`, `locked=False`.  
- On “Lock-in Plan” → set `locked=True`, freeze slider.  
- On “Play Again” → clear **all** session state keys.

---

## 8. Performance & UX
- **Tick interval**: 2 s real-time → 720 ticks in ~24 s.  
- After lock → accelerate to 50 ms/tick to finish month in ~5 s.  
- Chart shows **last 50 points** to stay responsive.

---

## 9. File Structure
```
cloud_cost_hero.py   # single file, <250 lines
requirements.txt     # only: streamlit
```

---

## 10. Run Instructions (for README)
```bash
pip install -r requirements.txt
streamlit run cloud_cost_hero.py
```

---

## 11. Acceptance Checklist
- [ ] App launches with `streamlit run`.  
- [ ] Persona changes every new game.  
- [ ] Slider disabled after lock.  
- [ ] Progress bar fills smoothly.  
- [ ] Savings % correct (cross-check with calculator).  
- [ ] Balloons appear on ≥ 30 % savings.  
- [ ] “Play Again” resets everything.

---

Happy coding!