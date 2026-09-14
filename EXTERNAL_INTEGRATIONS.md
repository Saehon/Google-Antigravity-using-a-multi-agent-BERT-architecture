# Multi-Agent Accounting AI — External Research Integrations

Owner: Saeid Homayoun  
ORCID: https://orcid.org/0000-0002-2536-0446

## Recommended agent / digital-twin stack

### Google / Linux Foundation

- **Google Antigravity SDK** → optional `AntigravityAdapter` for agent harness, tools, hooks, MCP, persistence, triggers and stateful research sessions. Apache-2.0 source; hosted model/service terms remain separate.
- **Google Agent Development Kit (ADK)** → `GoogleADKAdapter` for modular multi-agent orchestration, sequential/parallel/loop workflows, tools, evaluation and deployment. Apache-2.0.
- **Agent2Agent (A2A)** → `A2AGateway` for cross-framework and cross-vendor agent interoperability. Apache-2.0 Linux Foundation project originally contributed by Google.
- **Gemini CLI** → developer/research automation and MCP integration. Apache-2.0 software; Google service terms/quotas apply to hosted model use.
- **Google Agents CLI** → optional project/evaluation/deployment skills for Gemini Enterprise Agent Platform. Apache-2.0 code; cloud use may be billable.
- **TimesFM** → `TimesFMAdapter` for ICFR, risk, cash-flow, temporal digital-twin and forecasting research. Verify source and checkpoint/model-weight licenses separately for the exact version selected.
- **Google Co-Scientist / ERA / AlphaEvolve / AlphaFold / Science One** → methodological inspiration for hypothesis generation, executable empirical research, evaluator-guided discovery, latent-structure reasoning and Chain-of-Evidence. Do not imply that proprietary or experimental systems are bundled with NAAIL.

### Microsoft / Azure

- **Microsoft Agent Framework** → `MicrosoftAgentFrameworkAdapter` for multi-agent orchestration, workflows, RAG, A2A, MCP, checkpoints and human-in-the-loop. MIT. Preferred Microsoft foundation for new work.
- **Microsoft GraphRAG** → `GraphRAGAdapter` for standards, evidence, controls, CAM/KAM, ESG and literature knowledge graphs. MIT.
- **Magentic-UI / MagenticLite** → optional human-agent collaboration and task-orchestration interface research. MIT.
- **AutoGen / Magentic-One** → legacy/research reference for specialized multi-agent teams. AutoGen is in maintenance mode; new work should prefer Microsoft Agent Framework.
- **Semantic Kernel** → migration/reference integration. MIT; Microsoft directs new agent development toward Agent Framework.
- **Prompt flow** → optional evaluation, testing, tracing and reproducible LLM-flow layer. MIT; dependency licenses should be reviewed before production use.
- **Open Digital Twins / DTDL** → `DTDLAdapter` / schema inspiration for accounting and audit digital-twin entities and relationships. Preserve upstream license and notices.
- **Azure Digital Twins / Microsoft Foundry Agent Service / Copilot Studio** → optional managed enterprise adapters only; these are not free/open-source dependencies and may incur licensing or cloud charges.

## Existing NAAIL supporting integrations

- Financial Sentiment / BERT / FinBERT → `FinancialNLPAdapter` for financial-text classification, sentiment and benchmark comparisons.
- fg-data-synthetic → `SyntheticDataAdapter` for synthetic ERP/ledger data, anomaly scenarios, class balancing and privacy-safe demonstrations.
- AuditData-API → `AuditDataAdapter` for structured accounting/audit-data interchange and ledger ingestion.
- yfinance → `MarketDataAdapter` for finance-market validation where agent outputs are evaluated against market evidence.
- TimesFM → optional `TimesFMAdapter` for temporal risk and forecasting agents.

## Canonical multi-agent use

```text
Connector / Twin Ingestion
 -> Validation Agent
 -> Domain Specialist Agents
 -> Co-Scientist / ERA Research Agents
 -> Critic / Defender / Replicator / Falsifier
 -> Evidence Passport + GraphRAG
 -> Chain-of-Evidence / DAG Governance
 -> Human Gate
```

See [`BIG4_MULTI_AGENT_DIGITAL_TWIN_STACK.md`](./BIG4_MULTI_AGENT_DIGITAL_TWIN_STACK.md) for the full vendor-neutral architecture, Big Four-style benchmark design, reuse classifications, and IP/licensing rules.

All upstream projects retain their original authorship, trademarks and licenses. These integrations are dependencies, adapters, methodological references or comparison targets; they are not claims of upstream authorship, sponsorship, endorsement or ownership.
