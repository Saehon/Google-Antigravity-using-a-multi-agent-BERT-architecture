# 🛡️ Multi-Agent Accounting AI Framework

A GitHub-ready project for auditor-focused financial intelligence, BERT-based NLP analytics, cybersecurity risk control, and governance compliance.

## Overview

This repository combines:

- `multi_agent_accounting_ai_runner.py` — a standalone Python workflow for ERPNext-based synthetic accounting, anomaly detection, ESG scoring, and compliance evaluation.
- `n8n` workflows for automation and orchestration.
- audit documentation and standards for IFRS-as-code and EU AI Act control layers.
- GitHub Actions CI for reproducible execution and artifact generation.
- audit issue templates for structured bug reporting.

## Key capabilities

- Synthetic ERP/ledger data generation with accounting and compliance context.
- Multi-agent scoring using BERT-style semantic embeddings and proxy risk models.
- Anomaly detection via PyTorch autoencoder and Isolation Forest.
- ESG score computation and EU AI Act-style compliance scoring.
- Export to CSV, Excel (`.xlsx`), and Word (`.docx`) reports.
- n8n automation examples for audit workflow orchestration.
- Audit standard alignment with IFRS, EU AI Act, and international control layers.

## Project structure

- `multi_agent_accounting_ai_runner.py` — main runnable workflow.
- `requirements.txt` — Python package dependencies.
- `deploy.ps1` — Windows deployment helper.
- `.github/workflows/python-app.yml` — GitHub Actions workflow.
- `.github/ISSUE_TEMPLATE/bug_report.md` — auditor-friendly issue template.
- `AUDIT_STANDARDS.md` — IFRS-as-code, EU AI Act compliance, and audit layering.
- `n8n/bert_cyber_audit_workflow.json` — BERT + cyber audit automation.
- `n8n/big4_llm_rag_tool.json` — Big4-style LLM + RAG audit tool.
- `LICENSE-APACHE-2.0.txt` and `LICENSE-MIT.txt` — license options.

## Deployment

### Local setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Run the main workflow

```powershell
python .\multi_agent_accounting_ai_runner.py
```

### Outputs

The workflow generates files in the `data/` folder:

- `final_agent_output.csv`
- `multi_agent_accounting_ai_results.xlsx`
- `multi_agent_accounting_ai_figures.docx`
- `data/n8n_bert_cyber_audit_log.json` (if n8n workflow is used)
- `data/big4_llm_rag_audit_response.json` (if n8n workflow is used)

## GitHub Actions

Continuous integration is provided by `.github/workflows/python-app.yml`.
It runs on pushes and pull requests to `main`, installs dependencies, executes the runner, and uploads generated artifacts.

## Auditor support

Use the GitHub issue template at `.github/ISSUE_TEMPLATE/bug_report.md` for audit findings.
Tag issues with `bug4Audit` to highlight compliance or control gaps.

## n8n automation

This repo includes n8n workflow examples for audit and automation:

- `n8n/bert_cyber_audit_workflow.json` — ERPNext artifact collection, BERT risk proxy, and audit log generation.
- `n8n/big4_llm_rag_tool.json` — a Big4-style retrieval augmented generation tool for LLM-guided audit guidance.

## Audit standards and controls

See `AUDIT_STANDARDS.md` for:

- IFRS-as-code controls.
- EU AI Act compliance layer.
- Audit Data Standards (ADS) and data governance controls.
- PCAOB and internal audit control alignment.
- ISSB sustainability and ESG reporting.
- international audit standard mapping.
- GitHub-based transparency and traceability.

### Recommended GitHub tags

Use these tags to organize audit and compliance issues:

- `bug4Audit`
- `PCAOB`
- `internal-control`
- `risk-control`
- `audit-traceability`
- `ADS`
- `EU-AI-Act`
- `IFRS`
- `ISSB`

## License

See `LICENSE-APACHE-2.0.txt` and `LICENSE-MIT.txt` for licensing options.

## Notes

This project is designed for research, demonstration, and audit automation support.
It uses synthetic and proxy modeling approaches; it should not be used as a direct production accounting system without further validation and regulatory review.

