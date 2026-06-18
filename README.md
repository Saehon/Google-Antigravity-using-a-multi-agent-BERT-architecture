# 🛡️ Multi-Agent Accounting AI Framework

* Multi-agent AI system for accounting and audit analytics
* ERPNext-based structural integration for financial context simulation
* ESG risk scoring (Environmental, Social, Governance)
* Cybersecurity disclosure and risk detection
* Anomaly detection using deep learning and statistical models
* AI governance and compliance scoring (explainability + transparency layer)
* Lightweight and full research execution modes
* Google Colab and agent-based execution support

## ⚙️ Core Architecture

The framework operates through coordinated AI agents:

* Data Agent: Extracts and simulates ERP-based accounting data
* Preprocessing Agent: Cleans and prepares financial datasets
* NLP Agent: Applies transformer-based embeddings for financial text analysis
* Anomaly Detection Agent: Identifies irregular transactions and patterns
* ESG Agent: Computes sustainability and ESG risk scores
* Compliance Agent: Evaluates AI transparency and governance alignment
* Visualization Agent: Produces dashboards and analytical reports

## 🔬 Methodological Approach

The system combines:

* Transformer-based semantic representation (BERT-like embeddings)
* Autoencoder-based anomaly detection
* Isolation Forest for lightweight detection mode
* Multi-agent orchestration for modular decision-making
* Synthetic ERP-based dataset generation for controlled experimentation

## 🌱 ESG & Compliance Layer

The framework calculates ESG scores and classifies organizational risk into:

* Low Risk (Green)
* Medium Risk (Yellow)
* High Risk (Red)

It also includes an AI governance module aligned with transparency, accountability, and auditability principles.

---

## ☁️ Execution Modes

* Full Mode: Deep learning + full multi-agent pipeline
* Mini Mode: Lightweight ML version for fast execution
* Google Mode: Colab-based agent execution for cloud deployment

## 📊 Output

The system generates:

* Anomaly detection reports
* ESG risk dashboards
* AI compliance scores
* Visual analytics (Streamlit / Plotly)
* API-based audit results

## 🎯 Purpose

This framework is designed for:

* Accounting and auditing research
* ESG and sustainability analytics
* AI governance and compliance studies
* Agent-based financial intelligence systems
* Educational and research demonstrations

## Note

The system uses synthetic datasets and proxy models for research purposes. It is not intended for direct production use in real financial environments without further validation and regulatory adaptation.

Homayoun, S., 2026. Multi-Agent Accounting AI Framework: ERP-Integrated ESG and Anomaly Detection System. GitHub repository.
Available at: <https://github.com/Saehon/Google-Antigravity-using-a-multi-agent-BERT-architecture> [Accessed 17 June 2026].

# Multi-Agent Accounting AI Runner

This repository contains a standalone Python runner for a multi-agent accounting workflow that ingests ERPNext artifacts, generates a synthetic accounting ledger, scores risk, and exports results to CSV, Excel, and Word.

## Deployment

1. Open PowerShell in this folder.
2. Create or reuse a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
4. Run the workflow:
   ```powershell
   python .\multi_agent_accounting_ai_runner.py
   ```

## Outputs

The runner writes the following files under `data/`:

- `final_agent_output.csv`
- `multi_agent_accounting_ai_results.xlsx`
- `multi_agent_accounting_ai_figures.docx`

## GitHub Actions

This repository includes a workflow at `.github/workflows/python-app.yml`.
It runs on push and pull request events to `main`, installs dependencies, executes `multi_agent_accounting_ai_runner.py`, and uploads the generated `data/` files as workflow artifacts.

## Auditor support

This repo includes an audit-focused issue template at `.github/ISSUE_TEMPLATE/bug_report.md`.
Use the tag `bug4Audit` in issue titles and labels when reporting audit findings or compliance bugs.

## Optional

Set `GITHUB_TOKEN` as an environment variable to increase GitHub API rate limits for ERPNext artifact collection.

