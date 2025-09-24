import csv
import random
import json
from datetime import datetime, timedelta

# Set seed for reproducibility
random.seed(42)

def generate_performance_comparison_data():
    """Generate the main performance comparison data from Table I"""
    methods = ['Rule_Based', 'Single_Agent_PPO', 'Independent_Learning', 'Standard_MAPPO', 'TFP_Baseline', 'H_MAPPO_Ours']
    
    # Base performance data from the paper
    performance_data = {
        'Rule_Based': {'TDR': 78.3, 'FPR': 12.7, 'MTTD': 45.2, 'MTTR': 127.8, 'CSR': 72.1},
        'Single_Agent_PPO': {'TDR': 85.2, 'FPR': 8.4, 'MTTD': 23.7, 'MTTR': 89.3, 'CSR': 79.6},
        'Independent_Learning': {'TDR': 82.7, 'FPR': 9.8, 'MTTD': 28.1, 'MTTR': 95.7, 'CSR': 76.8},
        'Standard_MAPPO': {'TDR': 89.4, 'FPR': 6.2, 'MTTD': 18.9, 'MTTR': 67.4, 'CSR': 84.3},
        'TFP_Baseline': {'TDR': 87.1, 'FPR': 7.3, 'MTTD': 21.4, 'MTTR': 73.2, 'CSR': 81.7},
        'H_MAPPO_Ours': {'TDR': 94.7, 'FPR': 4.1, 'MTTD': 12.3, 'MTTR': 45.8, 'CSR': 91.2}
    }
    
    # Generate multiple trials with noise
    detailed_data = []
    for method in methods:
        base = performance_data[method]
        for trial in range(100):  # 100 trials per method
            row = {
                'Method': method,
                'Trial': trial + 1,
                'TDR_Percent': base['TDR'] + random.gauss(0, 2.0),  # Add noise
                'FPR_Percent': max(0, base['FPR'] + random.gauss(0, 0.5)),
                'MTTD_Seconds': max(1, base['MTTD'] + random.gauss(0, 3.0)),
                'MTTR_Seconds': max(5, base['MTTR'] + random.gauss(0, 8.0)),
                'CSR_Percent': min(100, max(0, base['CSR'] + random.gauss(0, 2.5)))
            }
            detailed_data.append(row)
    
    return detailed_data

def generate_scenario_performance_data():
    """Generate scenario-specific performance data from Figure 1"""
    scenarios = ['APT', 'Insider_Threat', 'DDoS', 'Zero_Day', 'Multi_Vector']
    methods = ['Rule_Based', 'Single_Agent_PPO', 'Independent_Learning', 'Standard_MAPPO', 'TFP_Baseline', 'H_MAPPO_Ours']
    
    # Performance matrix from the paper
    scenario_performance = {
        'Rule_Based': [81.4, 74.2, 85.6, 69.8, 76.3],
        'Single_Agent_PPO': [84.7, 79.1, 88.2, 73.5, 81.2],
        'Independent_Learning': [82.3, 77.8, 86.9, 71.4, 78.9],
        'Standard_MAPPO': [88.7, 83.6, 92.4, 79.2, 86.1],
        'TFP_Baseline': [87.1, 81.9, 90.8, 77.6, 84.3],
        'H_MAPPO_Ours': [96.2, 89.3, 97.8, 85.7, 93.4]
    }
    
    scenario_data = []
    for i, scenario in enumerate(scenarios):
        for method in methods:
            base_performance = scenario_performance[method][i]
            # Generate multiple samples with noise
            for trial in range(50):
                row = {
                    'Scenario': scenario,
                    'Method': method,
                    'Trial': trial + 1,
                    'Detection_Rate': base_performance + random.gauss(0, 1.5),
                    'Response_Time': random.uniform(10, 120),  # Response time in seconds
                    'Success_Rate': min(100, max(0, base_performance + random.gauss(0, 2.0)))
                }
                scenario_data.append(row)
    
    return scenario_data

def generate_coordination_metrics():
    """Generate coordination and scalability data from Table II"""
    methods = ['Independent_Learning', 'Standard_MAPPO', 'TFP_Baseline', 'H_MAPPO_Ours']
    
    coordination_data = {
        'Independent_Learning': {'CE': 0.23, 'RU': 67.8, 'SI': 0.89, 'Comm_Overhead': 'Low'},
        'Standard_MAPPO': {'CE': 0.71, 'RU': 74.2, 'SI': 0.76, 'Comm_Overhead': 'High'},
        'TFP_Baseline': {'CE': 0.45, 'RU': 71.3, 'SI': 0.82, 'Comm_Overhead': 'Medium'},
        'H_MAPPO_Ours': {'CE': 0.87, 'RU': 69.4, 'SI': 0.94, 'Comm_Overhead': 'Medium'}
    }
    
    coord_data = []
    for method in methods:
        base = coordination_data[method]
        for trial in range(30):
            row = {
                'Method': method,
                'Trial': trial + 1,
                'Coordination_Efficiency': base['CE'] + random.gauss(0, 0.03),
                'Resource_Utilization': base['RU'] + random.gauss(0, 2.0),
                'Scalability_Index': base['SI'] + random.gauss(0, 0.02),
                'Communication_Overhead': base['Comm_Overhead'],
                'Network_Size': random.choice([100, 200, 500, 1000, 2000])
            }
            coord_data.append(row)
    
    return coord_data

def generate_scalability_data():
    """Generate computational efficiency data from Figure 3"""
    network_sizes = [100, 200, 500, 1000, 2000, 5000]
    methods = ['Single_Agent_PPO', 'Standard_MAPPO', 'H_MAPPO_Ours']
    
    # Base computational times (in seconds)
    base_times = {
        'Single_Agent_PPO': [2.3, 9.2, 58.4, 234.7, 941.2, 5847.3],
        'Standard_MAPPO': [3.1, 8.7, 42.1, 189.3, 756.8, 4523.2],
        'H_MAPPO_Ours': [2.8, 6.4, 24.7, 78.2, 198.7, 743.1]
    }
    
    scalability_data = []
    for method in methods:
        times = base_times[method]
        for i, size in enumerate(network_sizes):
            base_time = times[i]
            for trial in range(20):
                row = {
                    'Method': method,
                    'Network_Size': size,
                    'Trial': trial + 1,
                    'Computational_Time_Seconds': base_time + random.gauss(0, base_time * 0.1),
                    'Memory_Usage_GB': size * 0.005 + random.gauss(0, size * 0.001),
                    'CPU_Usage_Percent': random.uniform(20, 90),
                    'Throughput_Events_Per_Second': random.uniform(1000, 10000)
                }
                scalability_data.append(row)
    
    return scalability_data

def generate_adversarial_robustness_data():
    """Generate adversarial robustness data from Table IV"""
    adaptation_levels = ['Static', 'Reactive', 'Predictive', 'Co_evolutionary']
    methods = ['Rule_Based', 'Standard_MAPPO', 'H_MAPPO_Ours']
    
    robustness_performance = {
        'Rule_Based': [78.3, 71.2, 65.8, 59.4],
        'Standard_MAPPO': [89.4, 84.7, 79.2, 73.6],
        'H_MAPPO_Ours': [94.7, 91.3, 87.8, 84.2]
    }
    
    adversarial_data = []
    for method in methods:
        performances = robustness_performance[method]
        for i, adaptation in enumerate(adaptation_levels):
            base_perf = performances[i]
            for trial in range(25):
                row = {
                    'Method': method,
                    'Adaptation_Level': adaptation,
                    'Trial': trial + 1,
                    'Detection_Rate_Percent': base_perf + random.gauss(0, 1.0),
                    'Robustness_Score': random.uniform(0.6, 1.0),
                    'Adaptation_Time_Minutes': random.uniform(1, 30),
                    'Attack_Success_Rate': random.uniform(0.1, 0.8)
                }
                adversarial_data.append(row)
    
    return adversarial_data

def generate_compliance_data():
    """Generate governance compliance data"""
    methods = ['Standard_MAPPO', 'TFP_Baseline', 'H_MAPPO_Ours']
    compliance_categories = ['Policy_Compliance', 'Audit_Completeness', 'Human_Escalation_Rate', 'Response_Time_Compliance']
    
    compliance_scores = {
        'Standard_MAPPO': [94.2, 96.8, 18.7, 89.3],
        'TFP_Baseline': [95.8, 97.2, 15.4, 91.7],
        'H_MAPPO_Ours': [98.7, 99.2, 12.3, 96.8]
    }
    
    compliance_data = []
    for method in methods:
        scores = compliance_scores[method]
        for i, category in enumerate(compliance_categories):
            base_score = scores[i]
            for trial in range(20):
                row = {
                    'Method': method,
                    'Compliance_Category': category,
                    'Trial': trial + 1,
                    'Score_Percent': base_score + random.gauss(0, 1.0),
                    'Timestamp': (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
                }
                compliance_data.append(row)
    
    return compliance_data

def save_to_csv(data, filename):
    """Save data to CSV file"""
    if not data:
        print(f"No data to save for {filename}")
        return
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} records to {filename}")

def create_data_summary():
    """Create a summary of all generated datasets"""
    summary = {
        "data_generation_info": {
            "generation_date": datetime.now().isoformat(),
            "total_datasets": 6,
            "random_seed": 42,
            "paper_reference": "Agentic AI for e-Governance: A Multi-Agent Reinforcement Learning Framework for Autonomous Cyber Defense"
        },
        "datasets": {
            "performance_comparison": {
                "description": "Main performance metrics across all methods (Table I)",
                "records": 600,  # 6 methods × 100 trials
                "metrics": ["TDR", "FPR", "MTTD", "MTTR", "CSR"]
            },
            "scenario_performance": {
                "description": "Performance across different attack scenarios (Figure 1)",
                "records": 1500,  # 5 scenarios × 6 methods × 50 trials
                "scenarios": ["APT", "Insider_Threat", "DDoS", "Zero_Day", "Multi_Vector"]
            },
            "coordination_metrics": {
                "description": "Coordination efficiency and resource utilization (Table II)",
                "records": 120,  # 4 methods × 30 trials
                "metrics": ["Coordination_Efficiency", "Resource_Utilization", "Scalability_Index"]
            },
            "scalability_data": {
                "description": "Computational efficiency across network sizes (Figure 3)",
                "records": 360,  # 3 methods × 6 sizes × 20 trials
                "network_sizes": [100, 200, 500, 1000, 2000, 5000]
            },
            "adversarial_robustness": {
                "description": "Performance under adversarial adaptation (Table IV)",
                "records": 300,  # 3 methods × 4 adaptation levels × 25 trials
                "adaptation_levels": ["Static", "Reactive", "Predictive", "Co_evolutionary"]
            },
            "compliance_data": {
                "description": "Governance compliance metrics (Figure 2)",
                "records": 240,  # 3 methods × 4 categories × 20 trials
                "categories": ["Policy_Compliance", "Audit_Completeness", "Human_Escalation_Rate", "Response_Time_Compliance"]
            }
        }
    }
    
    with open('/home/sandbox/data_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print("Data summary saved to data_summary.json")

def main():
    """Main function to generate all datasets"""
    print("Generating Cyber Defense Sample Data...")
    print("=" * 50)
    
    # Generate all datasets
    datasets = {
        'performance_comparison': generate_performance_comparison_data(),
        'scenario_performance': generate_scenario_performance_data(),
        'coordination_metrics': generate_coordination_metrics(),
        'scalability_data': generate_scalability_data(),
        'adversarial_robustness': generate_adversarial_robustness_data(),
        'compliance_data': generate_compliance_data()
    }
    
    # Save datasets to CSV files
    for name, data in datasets.items():
        filename = f'/home/sandbox/{name}.csv'
        save_to_csv(data, filename)
    
    # Create summary
    create_data_summary()
    
    print("\n" + "=" * 50)
    print("Data generation completed successfully!")
    print(f"Generated {sum(len(data) for data in datasets.values())} total records")
    print("Files created:")
    for name in datasets.keys():
        print(f"  - {name}.csv")
    print("  - data_summary.json")

if __name__ == "__main__":
    main()