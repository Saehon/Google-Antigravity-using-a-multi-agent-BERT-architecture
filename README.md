# Multi-Agent Accounting AI Framework

**NAAIL OpenLab research prototype for auditor-focused financial intelligence, BERT/NLP analytics, anomaly detection, explainable AI, governed multi-agent systems, and accounting/audit digital twins.**

**Researcher:** Dr. Saeid Homayoun  
**ORCID:** https://orcid.org/0000-0002-2536-0446  
**NAAIL OpenLab:** https://github.com/Saehon/Saeid-Homayoun/tree/main/NAAIL-OpenLab

> Independent research project. References to Google, Microsoft, OpenAI, Big Four firms, regulators, standard setters, or other organizations identify methodological inspiration, technologies, public materials, or comparison targets only. They do not imply affiliation, sponsorship, endorsement, certification, or validation.

## Research purpose

This repository investigates how multi-agent AI, digital twins, language models, machine learning, explainability, scientific-discovery workflows, and agent orchestration can support accounting and audit research while preserving evidence provenance, reproducibility, professional skepticism, uncertainty disclosure, and human judgment.

## Current capabilities

- synthetic ERP/ledger experimentation;
- BERT-style semantic and risk analytics;
- PyTorch autoencoder and Isolation Forest anomaly detection;
- fuzzy-logic explainability experiments;
- ESG and governance scoring prototypes;
- n8n multi-agent workflow examples;
- CSV/XLSX/DOCX research outputs;
- GitHub Actions for reproducible execution;
- audit/control mapping research;
- vendor-neutral accounting/audit digital-twin architecture;
- Google + Microsoft multi-agent interoperability roadmap.

Important research assets include `multi_agent_accounting_ai_runner.py`, `AUDIT_STANDARDS.md`, `FUZZY_LOGIC_EXPLAINABILITY.md`, and the workflows under `n8n/`.

## Google + Microsoft multi-agent digital twin stack

The current recommended research foundation combines:

```text
Google Antigravity SDK / Google ADK
        +
Microsoft Agent Framework
        +
A2A / MCP interoperability
        +
Microsoft GraphRAG
        +
NAAIL accounting/audit Digital Twin
        +
Co-Scientist -> ERA -> AlphaEvolve -> latent-structure reasoning
        +
Science One-style Chain-of-Evidence
        +
AI-to-AI Critic / Defender / Replicator / Falsifier
        +
Human Gate
```

See **[`BIG4_MULTI_AGENT_DIGITAL_TWIN_STACK.md`](./BIG4_MULTI_AGENT_DIGITAL_TWIN_STACK.md)** for the full architecture, current Google/Microsoft technology map, open-source/reuse status, Big Four-style audit-twin design, scientific-discovery protocol, and IP/licensing rules.

See **[`EXTERNAL_INTEGRATIONS.md`](./EXTERNAL_INTEGRATIONS.md)** for adapter-level integration targets.

## NAAIL scientific protocol

Original research extensions follow:

**Literature Validation → Co-Scientist Hypothesis Arena → ERA Empirical Design → AlphaEvolve / Computational Discovery → latent-structure reasoning → AI-to-AI Critic/Defender/Replicator/Falsifier → robustness → falsification → temporal/OOS validation → Chain-of-Evidence → DAG Governance → Human Gate.**

See [`NAAIL_RESEARCH_PROTOCOL.md`](./NAAIL_RESEARCH_PROTOCOL.md).

Scientific invariants:

```text
agent_consensus_is_truth = false
model_confidence_is_evidence = false
optimize_for_p_value = false
failed_runs_are_deleted = false
human_gate_required = true
discovery_claim_allowed = false
```

## Reproducibility

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python .\multi_agent_accounting_ai_runner.py
```

Generated research artifacts are written to the repository's data/output paths. Results from synthetic or proxy models must not be represented as validated professional conclusions.

## Relationship to NAAIL

This repository is a supporting experimental system for the broader NAAIL portfolio, including POMELO/VERA, KIWI CAM/KAM research, IFRS-AI-Inspector, ICFR/time-series research, and AAA Audit & Accounting AI Laboratory.

## Citation

Use [`CITATION.cff`](./CITATION.cff). Suggested citation:

> Homayoun, S. (2026). *Multi-Agent Accounting AI Framework: BERT, Audit Analytics, Explainability, Digital Twins and Governed Agentic Research* [Research software]. GitHub. https://github.com/Saehon/Google-Antigravity-using-a-multi-agent-BERT-architecture. ORCID: 0000-0002-2536-0446.

## IP / patent-readiness notice

This repository may describe original research concepts, architectures, methods, or prototypes for which intellectual-property protection may be considered. **Publication on GitHub is not a patent filing and does not guarantee patentability.** Patent-sensitive implementation details may be withheld pending IP review. No trademark, patent, endorsement, or affiliation rights are granted by this notice.

## License and third-party rights

This repository currently contains MIT and Apache licensing materials. Those existing grants cannot be retroactively converted into a non-commercial restriction for copies already distributed under those terms. Third-party software, models, standards, datasets, workflows, and trademarks remain subject to their original terms.

Open-source SDK licenses and hosted-model/service terms are separate. A library may be Apache-2.0 or MIT while the model API, cloud deployment, model weights, or commercial service remains subject to additional provider terms or charges.

Future proprietary or research-only NAAIL modules should be kept clearly separate and licensed before public release if commercial use is intended to be restricted.

## Responsible use

This project is for research, demonstration, and prototype evaluation. It is not an audit opinion, accounting advice, legal/regulatory advice, or a production accounting system. Real professional use requires appropriate validation, security, authorization, regulatory assessment, and qualified human judgment.
