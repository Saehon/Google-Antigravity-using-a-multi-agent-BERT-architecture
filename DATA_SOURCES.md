# Multi-Agent Accounting AI Data Sources and Provenance

This repository uses or contemplates synthetic accounting data, financial text, public filing/regulatory information, and researcher-provided datasets for multi-agent, BERT/NLP, anomaly-detection, explainability, and digital-twin experiments.

## Provenance record

Each material dataset or evidence bundle should record where applicable:

- source/provider;
- dataset/file/filing identifier;
- acquisition date and version/vintage;
- rights/licence/permission status;
- unit of observation and time period;
- identifiers and join keys;
- transformations/features/embeddings;
- exclusions and missing-data rules;
- train/validation/test or temporal split;
- integrity/hash information;
- whether the material is observed, synthetic, weak-labelled, or model-generated.

## Source classes

Keep these classes separate:

1. public filings/regulatory data;
2. public financial or market data;
3. licensed/restricted research data;
4. researcher-provided data;
5. synthetic ERP/ledger/digital-twin data;
6. model-generated text, labels, scores, or embeddings.

Model-generated outputs and synthetic records should not be silently represented as observed company evidence.

## Synthetic ERP / ledger experiments

Synthetic data are preferred for public demonstrations of anomaly detection, controls, audit procedures, and agent coordination. A synthetic case should document:

- case objective;
- generator/version;
- planted anomalies or control failures;
- seed/configuration where relevant;
- expected labels/outcomes;
- whether any confidential real data influenced generation.

Performance on a frozen synthetic case does not establish real-world audit effectiveness.

## Public filing and financial-text research

Where SEC EDGAR/XBRL, issuer reports, regulatory publications, earnings materials, or similar public sources are used, freeze the relevant filing/document identifiers, dates, retrieval path, transformations, and exclusions.

Public availability does not automatically grant unrestricted redistribution, and public text does not automatically constitute authoritative professional guidance.

## Restricted material

Do not commit confidential client/company data, credentials, restricted standards content, private benchmark answers, or commercial datasets that cannot lawfully be redistributed. Use manifests, schemas, hashes, or acquisition instructions instead.

## Derived AI artifacts

Embeddings, anomaly scores, classifications, summaries, agent critiques, or decision traces are derived artifacts. Preserve lineage to the original source and record the model/configuration used to generate them.

## Publication gate

Before publishing results or example data, verify source rights, provenance, transformations, leakage controls, sample counts, evaluation splits, and the distinction between real, synthetic, and model-generated evidence.
