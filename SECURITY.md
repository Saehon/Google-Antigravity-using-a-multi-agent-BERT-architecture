# Security Policy

This repository is a public research prototype for accounting/audit AI, multi-agent systems, NLP, digital twins, and automation research.

## Reporting

Do not disclose credentials, tokens, private keys, confidential client data, restricted standards content, or exploitable vulnerability details in public issues. Use GitHub private security reporting where available or another appropriate private channel to the repository owner.

## Minimum safeguards

- never commit secrets or credentials;
- use synthetic, public, or appropriately licensed data in public examples;
- review model/API provider data-retention and privacy terms;
- treat prompts, logs, embeddings, vector stores, model outputs, generated reports, and workflow exports as potentially sensitive;
- isolate external integrations with least-privilege access;
- pin or document important dependency/model versions for reproducibility;
- require qualified human review before material accounting/audit conclusions are used outside research.

## Production boundary

The repository is not certified for production accounting, audit, regulatory, or client use. Real deployments require independent security, privacy, legal/regulatory, model-risk, and professional review.
