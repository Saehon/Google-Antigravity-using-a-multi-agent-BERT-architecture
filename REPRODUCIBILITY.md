# Multi-Agent Accounting AI Reproducibility Contract

This repository treats reproducibility as a scientific and engineering requirement. A multi-agent conversation, model output, or successful local execution is not sufficient by itself to establish a reproducible result.

## Current maturity

The repository is a **Research Prototype** containing executable scripts, notebooks, workflow examples, and architecture experiments. Some legacy material may not yet satisfy the current NAAIL standard for frozen environments, run manifests, tests, or independent validation.

## Declared root environment

The current `requirements.txt` declares:

```text
requests
numpy
pandas
scikit-learn
torch
sentence-transformers
openpyxl
python-docx
matplotlib
```

These requirements are not version-pinned. Therefore exact environment reproduction can vary over time. A validated release should add pinned/locked dependencies and record Python/system versions.

## Minimum run record

For every material experiment, preserve where applicable:

- Git commit SHA;
- Python/environment version;
- exact package/model versions;
- experiment/case identifier;
- agent graph, role definitions, and routing configuration;
- model/provider/model-version identifier per agent;
- prompt/policy/tool configuration or content hashes;
- dataset provenance, version, and rights;
- transformations/feature construction;
- train/validation/test or temporal holdout design;
- random seeds;
- baseline architecture;
- evaluation metrics;
- cost/latency where relevant;
- raw/governed outputs and traces;
- failures, disagreements, and null results;
- human-review status.

## Architecture-comparison rule

When comparing deterministic, single-agent, sequential-agent, or multi-agent systems, all treatments should receive the same frozen task/evidence bundle and be evaluated with the same predeclared metrics. Agents may not rewrite gold labels or evaluation criteria after observing results.

## Data and model separation

Keep original evidence separate from:

- embeddings/features;
- weak labels;
- model-generated summaries;
- agent critiques;
- synthetic transactions;
- final model decisions.

Every reported conclusion should be traceable back to the underlying evidence and transformation path.

## Restricted material

Do not commit credentials, confidential company/client data, licensed standards text, proprietary benchmark answers, or restricted model/data assets. Use manifests, hashes, schemas, synthetic substitutes, or secure external storage references.

## Reproduction target

A future validated research package should make it possible for an independent researcher to reconstruct:

**environment → lawful data/evidence → preprocessing → model/agent configuration → execution → evaluation → reported tables/figures → human review**

from a frozen commit and documented manifests.
