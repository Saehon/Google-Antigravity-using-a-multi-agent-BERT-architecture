# Multi-Agent Accounting AI — External Research Integrations

Owner: Saeid Homayoun  
ORCID: https://orcid.org/0000-0002-2536-0446

## Relevant integrations
- Financial Sentiment / BERT / FinBERT → `FinancialNLPAdapter` for financial-text classification, sentiment and benchmark comparisons.
- fg-data-synthetic → `SyntheticDataAdapter` for synthetic ERP/ledger data, anomaly scenarios, class balancing and privacy-safe demonstrations.
- AuditData-API → `AuditDataAdapter` for structured accounting/audit-data interchange and ledger ingestion.
- yfinance → `MarketDataAdapter` for finance-market validation where agent outputs are evaluated against market evidence.
- TimesFM → optional `TimesFMAdapter` for temporal risk and forecasting agents.

## Multi-agent use
Connector Agent → Validation Agent → Domain Agent → Critic/Defender → Evidence/Provenance Check → Human Gate

All upstream projects retain their original authorship and licenses. These integrations are dependencies/reference components, not claims of upstream authorship or ownership.
