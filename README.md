# Federated Fraud Detection Research

## Core Question

Can multiple financial institutions collaboratively build a **fraud detection model without sharing customer data**, while still maintaining strong detection accuracy, privacy guarantees, and interpretability?

Traditional fraud detection systems rely on centralized transaction data. However banks cannot share data because of:

- privacy regulations (GDPR, financial compliance)
- security risks
- competitive restrictions

**Federated Learning (FL)** offers a solution by allowing institutions to train models locally and share only model updates.

This research investigates whether federated fraud detection can remain **accurate, private, robust, and explainable** under realistic conditions.

---

# Research Problem

Real financial systems introduce challenges rarely evaluated together:

- heterogeneous client data (non-IID)
- privacy constraints
- adversarial participants
- need for interpretability
- communication cost

Most existing research evaluates **only one of these constraints at a time**.

This project studies how these constraints interact in a realistic federated fraud detection pipeline.

---

# Research Question

**How does differential privacy affect fraud detection accuracy in non-IID federated environments, and can robust aggregation and explainability make the system production-viable?**

---

# Hypothesis

H0 (Null Hypothesis)  
Differential privacy and federated learning do not significantly affect fraud detection accuracy.

H1 (Alternative Hypothesis)

- DP-SGD reduces model accuracy due to gradient noise.
- Accuracy degradation becomes worse under **non-IID client distributions**.
- Robust aggregation improves stability in adversarial environments.
- Explainability (SHAP) can provide interpretable fraud reasoning without exposing raw data.
- Proper tuning of privacy budgets maintains usable production performance.

---

# Literature Baseline Taxonomy

Most federated fraud detection papers compare three categories.

| Category | Example |
|--------|--------|
| Centralized ML | Logistic Regression, Random Forest, LightGBM |
| Vanilla Federated Learning | FedAvg |
| Federated + Privacy | FedAvg + Differential Privacy |

Your experiments must include **all three baselines** plus the proposed method.

---

# Identified Research Gaps

### Gap 1 — Unrealistic Data Distribution

Most FL studies randomly split datasets across clients.  
Real financial institutions have **heterogeneous transaction patterns**.

---

### Gap 2 — Weak Privacy-Utility Analysis

Papers propose differential privacy but rarely measure how privacy budgets affect fraud detection accuracy.

---

### Gap 3 — Adversarial Client Behavior

Most research assumes all clients are honest.  
Real federated systems may contain **Byzantine clients sending poisoned updates**.

---

### Gap 4 — Lack of Explainability

Fraud detection systems require interpretability for regulators and analysts.

---

### Gap 5 — Communication Cost

Few studies evaluate training cost or communication overhead in federated systems.

---

### Gap 6 — Lack of Integrated Evaluation

Most studies examine only **one constraint at a time**.  
Real systems must handle privacy, heterogeneity, security, and interpretability simultaneously.

---

# Project Contribution

This project builds a **complete experimental framework** to evaluate federated fraud detection under realistic conditions.

Contributions include:

1. **Non-IID Federated Data Simulation**  
   Simulating heterogeneous financial institutions using regional transaction clusters.

2. **Privacy-Utility Tradeoff Evaluation**  
   Measuring how differential privacy affects fraud detection performance.

3. **Adversarial Robustness Testing**  
   Simulating Byzantine clients performing model poisoning.

4. **Robust Aggregation Strategies**  
   Evaluating aggregation methods resistant to malicious updates.

5. **Explainable Federated Fraud Detection**  
   Integrating SHAP explanations without exposing private data.

---

# Dataset

Dataset used:

**IEEE-CIS Fraud Detection Dataset**

Features include:

- transaction metadata
- device information
- identity attributes
- fraud labels

---

# Dataset Partition Strategy

Federated learning performance depends heavily on how data is distributed across clients.

Several partition strategies were evaluated.

| Partition Strategy | Description | Realism |
|---|---|---|
| Random split | Random division of dataset | Low |
| Time-based split | Clients represent different time periods | Medium |
| Merchant-based split | Clients represent merchant sectors | Medium |
| `addr1` regional clusters | Clients represent geographic populations | High |

### Selected Strategy: addr1 Cluster Partition

`addr1` represents anonymized billing regions.

Partitioning by `addr1` simulates institutions serving different geographic populations.

Example:

| Client | Data Source |
|---|---|
| Client 1 | addr1 cluster A |
| Client 2 | addr1 cluster B |
| Client 3 | addr1 cluster C |
| Client 4 | addr1 cluster D |

This produces **non-IID data distributions**, which better reflect real financial systems.

---

# Experimental Variables

## Controlled Variables

- Model architecture
- Dataset
- Feature preprocessing
- Training environment
- Random seed
- Evaluation split

---

## Independent Variables

### Learning Architecture

- Centralized
- Federated

---

### Privacy Level
ε = ∞ (no differential privacy)
ε = 10
ε = 5
ε = 3
ε = 1

---

### Data Distribution

- IID
- Non-IID

---

### Aggregation Strategy

- FedAvg
- Robust aggregation (Median / Trimmed Mean / Krum)

---

### Adversarial Clients

- Honest clients
- Byzantine clients

---

## Dependent Variables

- ROC-AUC
- PR-AUC
- F1 Score
- False Positive Rate
- Training convergence
- Communication cost

---

# Experimental Design Matrix

| Experiment | Partition | Privacy | Attack |
|---|---|---|---|
| Centralized | None | No | No |
| FL IID | Random | No | No |
| FL Non-IID | addr1 clusters | No | No |
| FL + DP ε=10 | addr1 clusters | Yes | No |
| FL + DP ε=5 | addr1 clusters | Yes | No |
| FL + DP ε=3 | addr1 clusters | Yes | No |
| FL + DP ε=1 | addr1 clusters | Yes | No |
| FL Byzantine | addr1 clusters | No | Yes |

---

# Evaluation Metrics

Fraud detection is an extreme class-imbalance problem.

Multiple metrics are used.

| Metric | Purpose |
|---|---|
| PR-AUC | performance on rare fraud cases |
| ROC-AUC | overall ranking ability |
| Recall@FPR=1% | practical fraud detection |
| Cost-weighted accuracy | financial impact |
| False positive rate | customer friction |
| Training convergence | federated stability |
| Communication cost | scalability |

---

# Expected Outcomes

This research will quantify:

- accuracy loss from differential privacy
- impact of heterogeneous client data
- vulnerability to adversarial clients
- robustness improvements from aggregation methods
- interpretability of federated fraud predictions

---

# Phase 1 — Research Design (Completed)


# Project Structure
project
│
├── data_partition
├── federated_training
├── privacy_dp
├── attacks
├── aggregation
├── explainability
├── experiments
├── results
└── paper



---

# Final Goal

The goal of this research is to determine whether **privacy-preserving collaborative fraud detection between financial institutions is feasible without sacrificing accuracy, robustness, or interpretability**.
