# A-Multi-Agent-Reinforcement-Learning-Framework-for-Autonomous-Cyber-Defense
Agentic AI for e-Governance: A Multi-Agent Reinforcement Learning Framework for Autonomous Cyber Defense
# Data Generation Methodology

It includes code and datasets for simulating, validating, and analyzing cyber defense methods using realistic benchmarks.

A-Multi-Agent-Reinforcement-Learning-Framework-for-Autonomous-Cyber-Defense
Agentic AI for e-Governance: A Multi-Agent Reinforcement Learning Framework for Autonomous Cyber Defense
Data Generation Methodology

It includes code and datasets for simulating, validating, and analyzing cyber defense methods using realistic benchmarks.

---

  Overview
All results are based on simulation-driven data generation.  
The datasets reflect realistic attack scenarios, scalability constraints, and adversarial robustness, while remaining reproducible (seed=42) and statistically validated.

---

 Datasets

1. Performance Comparison (`performance_comparison.csv`)  
   - 600 records (6 methods × 100 trials)  
   - Metrics: TDR (%), FPR (%), MTTD (s), MTTR (s), CSR (%)  
   - Example: H-MAPPO achieved 94.7% detection with 4.1% false positives.

2. Scenario Performance (`scenario_performance.csv`)  
   - 1,500 records (5 scenarios × 6 methods × 50 trials)  
   - Scenarios: APT, Insider Threat, DDoS, Zero-Day, Multi-Vector  
   - Example: Against DDoS, H-MAPPO scored 97.8% vs. 85.6% (Rule-Based).

3. Coordination Metrics (`coordination_metrics.csv`)  
   - 120 records (4 methods × 30 trials)  
   - Metrics: Coordination Efficiency, Resource Utilization, Scalability Index, Communication Overhead.

4. Scalability Data (`scalability_data.csv`)  
   - 360 records (3 methods × 6 network sizes × 20 trials)  
   - Network sizes: 100 → 5000 nodes  
   - Example: H-MAPPO scales nearly linearly; PPO grows near-quadratic.

5. Adversarial Robustness (`adversarial_robustness.csv`)  
   - 300 records (3 methods × 4 adaptation levels × 25 trials)  
   - Levels: Static, Reactive, Predictive, Co-evolutionary  
   - Metrics: Detection Rate, Robustness Score, Adaptation Time.

6. Compliance Data (`compliance_data.csv`)  
   - 240 records (3 methods × 4 categories × 20 trials)  
   - Categories: Policy Compliance, Audit Completeness, Human Escalation, Response-Time Compliance.

---

 Tools

- `simple_data_generator.py`  
  Generates all CSV datasets with realistic noise.  
  ```bash
  python simple_data_generator.py
