# Third-Party Notices

The Multi-Agent Accounting AI Framework is an independent NAAIL OpenLab research project. Third-party software, models, agent frameworks, APIs, datasets, standards, publications, and trademarks remain governed by their own licences and terms.

## Declared root software dependencies

The current `requirements.txt` declares:

- `requests`
- `numpy`
- `pandas`
- `scikit-learn`
- `torch`
- `sentence-transformers`
- `openpyxl`
- `python-docx`
- `matplotlib`

These dependencies retain their upstream licences and notices. The current manifest is not version-pinned; a release-time dependency/SBOM and licence scan is recommended.

## Models and model ecosystems

References to BERT, sentence-transformer models, financial language models, LLMs, or other foundation models do not transfer rights in model weights, training data, model names, APIs, or hosted services. Model licence/terms should be checked separately from the licence of any Python library used to call the model.

## Agent and interoperability frameworks

References to Google, Microsoft, OpenAI, MCP, A2A, GraphRAG, n8n, or other frameworks/providers identify public technologies, architectural inspiration, interoperability targets, or external services where applicable.

They do **not** imply affiliation, sponsorship, endorsement, certification, partnership, or access to proprietary internal systems.

Any external SDK, workflow engine, API, or cloud service must be used under its applicable terms.

## Accounting, auditing and regulatory content

References to accounting/auditing standards, regulators, Big Four platforms, or professional frameworks are descriptive, comparative, or research-oriented only. Do not copy proprietary audit methodologies, restricted standards text, confidential templates, or other protected content into the repository without permission.

## Data and publications

Public filings, market/financial data, academic papers, commercial databases, and synthetic-data tools each carry separate provenance and rights conditions. See `DATA_SOURCES.md`.

## Trademarks and naming

Third-party organization/product/model names and trademarks belong to their respective owners. The repository name's historical use of “Google-Antigravity” does not imply that Google owns, endorses, sponsors, or maintains this project. A future neutral repository rename is recommended for clearer NAAIL product identity.

## Release-time requirement

Before an external release or deployment:

1. freeze dependencies and generate an SBOM/dependency inventory;
2. verify software/model/API/data licences and required notices;
3. preserve upstream attribution;
4. remove credentials and restricted/confidential content;
5. verify no proprietary audit-firm or standards-body content has been copied without authorization;
6. keep NAAIL-original implementation clearly separated from third-party components.

This file is a research-governance notice, not legal advice.
