# ============================================================
# Multi-Agent Accounting AI — Python CLI Orchestrator
# Google Colab: https://colab.research.google.com/drive/1Oy1fY63JIn3PPF7f6oBRn2YPjarQr5C7
# ============================================================

import os
import re
import json
import math
import random
import requests
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

import torch
import torch.nn as nn

from sentence_transformers import SentenceTransformer
import plotly.express as px
import plotly.graph_objects as go

SEED = 42
np.random.seed(SEED)
random.seed(SEED)
torch.manual_seed(SEED)

ERP_NEXT_REPO_URL = "https://github.com/frappe/erpnext"
ERP_NEXT_OWNER = "frappe"
ERP_NEXT_REPO = "erpnext"
ERP_NEXT_BRANCH = "develop"

os.makedirs("data", exist_ok=True)


# ============================================================
# Agent 1A: ERPNext GitHub Ingestion
# ============================================================
def collect_erpnext_artifacts(branch=ERP_NEXT_BRANCH, max_files=40):
    """
    Connects to the public ERPNext GitHub repository and identifies ERP/accounting-related artifacts.
    These artifacts are used as contextual ERP metadata for the accounting AI workflow.
    """
    print("[Agent 1A] Connecting to ERPNext GitHub repository...")

    accounting_keywords = [
        "account", "accounts", "accounting", "journal", "journal_entry",
        "general_ledger", "gl_entry", "ledger", "invoice", "sales_invoice",
        "purchase_invoice", "payment_entry", "payment", "bank", "banking",
        "tax", "company", "cost_center", "asset", "liability", "revenue", "expense"
    ]

    tree_url = f"https://api.github.com/repos/{ERP_NEXT_OWNER}/{ERP_NEXT_REPO}/git/trees/{branch}?recursive=1"

    headers = {}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(tree_url, headers=headers, timeout=25)
        response.raise_for_status()
        tree_items = response.json().get("tree", [])

        candidate_paths = []
        for item in tree_items:
            path = item.get("path", "")
            item_type = item.get("type", "")
            lower_path = path.lower()

            if item_type != "blob":
                continue
            if not lower_path.endswith((".json", ".csv", ".py", ".md", ".txt")):
                continue
            if any(keyword in lower_path for keyword in accounting_keywords):
                candidate_paths.append(path)

        candidate_paths = candidate_paths[:max_files]
        records = []

        for path in candidate_paths:
            raw_url = f"https://raw.githubusercontent.com/{ERP_NEXT_OWNER}/{ERP_NEXT_REPO}/{branch}/{path}"
            detected = sorted({kw for kw in accounting_keywords if kw in path.lower()})

            artifact_type = "ERPNext source artifact"
            if path.lower().endswith(".json"):
                artifact_type = "ERPNext JSON DocType/configuration artifact"
            elif path.lower().endswith(".csv"):
                artifact_type = "ERPNext CSV fixture/tabular artifact"
            elif path.lower().endswith(".py"):
                artifact_type = "ERPNext Python business logic/test artifact"
            elif path.lower().endswith(".md"):
                artifact_type = "ERPNext documentation artifact"

            records.append({
                "repository": f"{ERP_NEXT_OWNER}/{ERP_NEXT_REPO}",
                "branch": branch,
                "source_path": path,
                "raw_url": raw_url,
                "artifact_type": artifact_type,
                "detected_keywords": ", ".join(detected)
            })

        artifacts_df = pd.DataFrame(records)
        if artifacts_df.empty:
            print("[Agent 1A] No ERPNext artifacts found. Fallback metadata will be used.")
        else:
            artifacts_df.to_csv("data/erpnext_github_artifacts.csv", index=False)
            print(f"[Agent 1A] ERPNext artifacts collected: {len(artifacts_df)}")
            print("[Agent 1A] Saved: data/erpnext_github_artifacts.csv")

        return artifacts_df

    except Exception as e:
        print(f"[Agent 1A] ERPNext GitHub ingestion failed: {e}")
        return pd.DataFrame()


# ============================================================
# Agent 1B: ERP/General-ledger Simulator
# ============================================================
def generate_research_grade_ledger(artifacts_df=None, samples=15):
    """
    Generates a controlled ERP-style ledger dataset enriched with ERPNext source metadata.
    The ledger is synthetic for reproducible anomaly testing.
    """
    np.random.seed(SEED)

    companies = [f"Global_Enterprise_{100 + i}" for i in range(samples)]
    debit = np.random.uniform(50000, 2500000, samples)
    credit = debit.copy()

    # Inject accounting anomalies.
    credit[3] = credit[3] * 1.35
    credit[8] = credit[8] * 0.60

    procurement_waste_tons = np.random.uniform(5, 120, samples)
    procurement_waste_tons[12] = 450.0

    financial_narratives = [
        "Revenue recognized through normal channels matching invoice schedules flawlessly.",
        "Period-end financial close operations executed in accordance with IFRS frameworks.",
        "Standard amortization of intangible patent portfolios calculated across linear schedules.",
        "Special batch ledger adjustments committed via root administrative bypass authorization.",
        "Fixed asset reconciliation completed successfully against factory logistics tracking indices.",
        "Accounts receivable collections traced back securely to third-party merchant processor accounts.",
        "Routine accrual adjustments for utility overhead metrics performed under corporate supervision.",
        "Tax provision balancing entry executed following verified regional updates.",
        "Suspense account balancing clearing entry committed without secondary supervisory sign-off.",
        "Foreign exchange translation calculation matching real-time valuation windows.",
        "Deferred revenue segments released systematically following completion of client milestones.",
        "Intercompany balance netting process finalized across standard regional ledgers.",
        "Provisions for inventory obsolescence written down according to warehouse audits.",
        "Prepaid operating lease allocations systematically distributed to local business accounts.",
        "Minor adjustment to payroll expense variances matching labor output reports."
    ]

    esg_disclosures = [
        "Scope 1 emissions lowered by 14% through continuous solar infrastructure integration.",
        "Corporate inclusion goals hit target thresholds across operational manufacturing plants.",
        "Waste management protocols met all municipal environmental safety compliance rules.",
        "Supply chain validation audit verified zero exposure to child labor vectors.",
        "Corporate literature states our factory operation has achieved a net-zero impact framework instantly.",
        "Board restructuring enhanced transparency via addition of two independent monitoring leads.",
        "Strategic sourcing pipelines verified that 80% of primary components use recycled compounds.",
        "Employee training hours on compliance topics expanded by 25% year-over-year.",
        "Water remediation investments completed across processing facility footprints.",
        "Donation and lobbying records published completely online to ensure corporate accountability.",
        "Workplace protection metrics registered zero high-severity incidents for this cycle.",
        "Sustainable sourcing guidelines formalized across all tier-one logistics providers.",
        "Public report affirms absolute ecological care while heavy localized waste spikes continue.",
        "Community engagement initiatives deployed across new infrastructure building sites.",
        "Data privacy protection standards updated to enforce global regulatory compliance."
    ]

    cyber_disclosures = [
        "Perimeter logging metrics confirm zero security bypass actions or identity theft instances.",
        "Enterprise access points migrated securely to multi-factor zero-trust validation models.",
        "Phishing testing exercises achieved exceptional compliance values among ledger accountants.",
        "Database schemas for customer records encrypted via standard cryptographic layers.",
        "Critical ERP patch updates delayed due to legacy hardware optimization blocks.",
        "Regular perimeter scanning validated effective isolation of payment gateway components.",
        "Identity permission vectors verified strictly via role-based access control paradigms.",
        "Disaster recovery backups generated nightly and mirrored to cloud locations.",
        "Incident containment runbooks tested and approved by independent external panels.",
        "Network load monitors confirmed normal performance metrics throughout this cycle.",
        "Endpoint configuration auditing tools confirmed clean operation for core accounting infrastructure.",
        "Third-party system risk management protocols updated to include vendor tracking arrays.",
        "Minor firewall policy adjustments completed to isolate development testbeds.",
        "Access key rotation matrices executed across production database instances.",
        "Data governance rules updated to meet evolving multi-regional security rules."
    ]

    if artifacts_df is not None and not artifacts_df.empty:
        paths = artifacts_df["source_path"].tolist()
        types = artifacts_df["artifact_type"].tolist()
        keywords = artifacts_df["detected_keywords"].tolist()
    else:
        paths = ["ERPNext fallback simulator"]
        types = ["Synthetic ERP ledger simulator"]
        keywords = ["ledger, invoice, accounting"]

    df = pd.DataFrame({
        "Company_ID": companies,
        "Account_Segment": np.random.choice(["1000 Assets", "4000 Revenue", "2000 Liabilities", "5000 Expenses"], samples),
        "Debit_Value": debit,
        "Credit_Value": credit,
        "Procurement_Waste_Tons": procurement_waste_tons,
        "Financial_Narrative": financial_narratives,
        "ESG_Disclosure": esg_disclosures,
        "Cyber_Disclosure": cyber_disclosures,
        "ERPNext_Source_Path": [paths[i % len(paths)] for i in range(samples)],
        "ERPNext_Artifact_Type": [types[i % len(types)] for i in range(samples)],
        "ERPNext_Detected_Keywords": [keywords[i % len(keywords)] for i in range(samples)]
    })

    df.to_csv("data/raw_erp_accounting_data.csv", index=False)
    print("[Agent 1B] Synthetic ERP/GL matrix saved: data/raw_erp_accounting_data.csv")
    return df


# ============================================================
# Agent 2: Preprocessing
# ============================================================
def preprocessing_agent(df):
    """
    Cleans records, calculates debit-credit balance variance, and standardizes numeric features.
    """
    cleaned_df = df.drop_duplicates().ffill().bfill().copy()
    cleaned_df["Balance_Variance"] = (cleaned_df["Debit_Value"] - cleaned_df["Credit_Value"]).abs()

    numeric_cols = ["Debit_Value", "Credit_Value", "Procurement_Waste_Tons", "Balance_Variance"]
    scaler = StandardScaler()
    scaled_array = scaler.fit_transform(cleaned_df[numeric_cols])
    
    # Append scaled values to the original DataFrame to keep unscaled variables for plotting/export
    for i, col in enumerate(numeric_cols):
        cleaned_df[f"scaled_{col}"] = scaled_array[:, i]

    print("[Agent 2] Preprocessing complete.")
    return cleaned_df


# ============================================================
# Agent 3: Multi-BERT proxy analysis
# ============================================================
def keyword_score(text, terms):
    text = str(text).lower()
    matches = sum(1 for term in terms if term in text)
    return min(matches / max(len(terms), 1), 1.0)


def multi_bert_agent(df):
    """
    Simulated Multi-BERT analytical layer:
    - GeneralBERT proxy: semantic embedding profile
    - LedgerBERT proxy: accounting-risk keyword scoring
    - CyberBERT proxy: cybersecurity-risk keyword scoring
    - ESG-BERT proxy: ESG/greenwashing keyword scoring
    """
    df = df.copy()

    print("[Agent 3] Loading SentenceTransformer model...")
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    combined_text = (
        df["Financial_Narrative"].astype(str) + " " +
        df["ESG_Disclosure"].astype(str) + " " +
        df["Cyber_Disclosure"].astype(str) + " " +
        df["ERPNext_Source_Path"].astype(str)
    ).tolist()

    embeddings = embedder.encode(combined_text, show_progress_bar=False)

    ledger_terms = ["bypass", "suspense", "manual", "adjustment", "root", "without secondary", "period-end"]
    cyber_terms = ["patch", "legacy", "bypass", "identity", "access", "security", "firewall", "encryption"]
    esg_terms = ["waste", "net-zero", "emissions", "ecological", "sustainable", "recycled", "green", "privacy"]

    df["SubAgent_A_GeneralBERT_Risk"] = np.clip(np.var(embeddings, axis=1), 0, 1)
    df["SubAgent_B_LedgerBERT_Risk"] = df["Financial_Narrative"].apply(lambda x: keyword_score(x, ledger_terms))
    df["SubAgent_C_CyberBERT_Risk"] = df["Cyber_Disclosure"].apply(lambda x: keyword_score(x, cyber_terms))
    df["SubAgent_D_ESGBERT_Risk"] = df["ESG_Disclosure"].apply(lambda x: keyword_score(x, esg_terms))
    df["Text_Embedding_Proxy"] = np.mean(embeddings, axis=1)

    print("[Agent 3] Multi-BERT proxy scoring complete.")
    return df, embeddings


# ============================================================
# Agent 4A: PyTorch Autoencoder Anomaly Detection
# ============================================================
class PyTorchAutoencoder(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 6),
            nn.Tanh(),
            nn.Linear(6, 3)
        )
        self.decoder = nn.Sequential(
            nn.Linear(3, 6),
            nn.Tanh(),
            nn.Linear(6, input_dim)
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))


def autoencoder_anomaly_agent(df, threshold_percentile=85, epochs=160, lr=0.03):
    """
    Full research-mode anomaly detector.
    Uses reconstruction error from a lightweight PyTorch Autoencoder.
    """
    df = df.copy()
    torch.manual_seed(SEED)

    feature_cols = [
        "scaled_Debit_Value",
        "scaled_Credit_Value",
        "scaled_Procurement_Waste_Tons",
        "scaled_Balance_Variance",
        "SubAgent_A_GeneralBERT_Risk",
        "SubAgent_B_LedgerBERT_Risk",
        "SubAgent_C_CyberBERT_Risk",
        "SubAgent_D_ESGBERT_Risk",
        "Text_Embedding_Proxy"
    ]

    X = df[feature_cols].astype(float).values
    X_tensor = torch.tensor(X, dtype=torch.float32)

    model = PyTorchAutoencoder(input_dim=len(feature_cols))
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    model.train()
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(X_tensor)
        loss = criterion(outputs, X_tensor)
        loss.backward()
        optimizer.step()

    model.eval()
    with torch.no_grad():
        reconstructed = model(X_tensor)
        errors = torch.mean((X_tensor - reconstructed) ** 2, dim=1).numpy()

    threshold_value = np.percentile(errors, threshold_percentile)
    df["Reconstruction_Error"] = errors
    df["Autoencoder_Threshold"] = threshold_value
    df["Anomaly_Indicator"] = df["Reconstruction_Error"].apply(
        lambda e: "CRITICAL PROFILE ALERT" if e > threshold_value else "Normal Verified Ledger"
    )

    print("[Agent 4A] PyTorch Autoencoder anomaly detection complete.")
    return df


# ============================================================
# Agent 4B: Isolation Forest Fallback
# ============================================================
def isolation_forest_agent(df, text_embeddings, contamination=0.30):
    """
    Lightweight Google Agent / Antigravity-compatible anomaly detector.
    Combines sentence embeddings with structured risk features.
    """
    df = df.copy()

    structured_cols = [
        "scaled_Debit_Value",
        "scaled_Credit_Value",
        "scaled_Procurement_Waste_Tons",
        "scaled_Balance_Variance",
        "SubAgent_B_LedgerBERT_Risk",
        "SubAgent_C_CyberBERT_Risk",
        "SubAgent_D_ESGBERT_Risk"
    ]

    structured_features = df[structured_cols].astype(float).values
    combined_features = np.hstack([text_embeddings, structured_features])

    model = IsolationForest(contamination=contamination, random_state=SEED)
    pred = model.fit_predict(combined_features)

    df["IForest_Anomaly"] = [1 if p == -1 else 0 for p in pred]
    df["IForest_Indicator"] = df["IForest_Anomaly"].apply(
        lambda x: "CRITICAL PROFILE ALERT" if x == 1 else "Normal Verified Ledger"
    )

    print("[Agent 4B] Isolation Forest fallback complete.")
    return df


# ============================================================
# Agent 5: ESG Risk Assessment
# ============================================================
def esg_risk_agent(df):
    """
    Computes environmental, social, governance, and overall ESG scores.
    Uses min-max normalisation for waste to avoid unintuitive standardized-score mapping.
    """
    df = df.copy()

    waste = df["scaled_Procurement_Waste_Tons"].astype(float)
    waste_norm = (waste - waste.min()) / (waste.max() - waste.min() + 1e-6)

    df["Environmental_Score"] = (100 * (1 - waste_norm)).clip(15, 98)
    df["Social_Score"] = (100 * (1 - df["SubAgent_C_CyberBERT_Risk"].astype(float))).clip(20, 99)
    df["Governance_Score"] = (100 * (1 - df["SubAgent_B_LedgerBERT_Risk"].astype(float))).clip(10, 97)
    df["Overall_ESG_Score"] = (
        df["Environmental_Score"] + df["Social_Score"] + df["Governance_Score"]
    ) / 3

    def classify(row):
        if row["Anomaly_Indicator"] == "CRITICAL PROFILE ALERT" or row["Overall_ESG_Score"] < 50:
            return "High"
        elif row["Overall_ESG_Score"] < 75 or row["IForest_Indicator"] == "CRITICAL PROFILE ALERT":
            return "Medium"
        return "Low"

    df["ESG_Risk_Classification"] = df.apply(classify, axis=1)

    print("[Agent 5] ESG risk assessment complete.")
    return df


# ============================================================
# Agent 6: Trustworthy AI Compliance Audit
# ============================================================
def compliance_agent(df):
    """
    Prototype governance layer. This is not a legal determination.
    It converts technical risk outputs into transparent human-review logs.
    """
    df = df.copy()

    def score(row):
        compliance = 100
        if row["Anomaly_Indicator"] == "CRITICAL PROFILE ALERT":
            compliance -= 30
        if row["IForest_Indicator"] == "CRITICAL PROFILE ALERT":
            compliance -= 15
        if row["SubAgent_B_LedgerBERT_Risk"] > 0.20:
            compliance -= 20
        if row["SubAgent_C_CyberBERT_Risk"] > 0.20:
            compliance -= 15
        if row["Overall_ESG_Score"] < 60:
            compliance -= 10
        return max(compliance, 0)

    df["EU_AI_Act_Compliance_Score"] = df.apply(score, axis=1)

    def log(row):
        reasons = []
        if row["Anomaly_Indicator"] == "CRITICAL PROFILE ALERT":
            reasons.append(f"high autoencoder reconstruction loss ({row['Reconstruction_Error']:.4f})")
        if row["IForest_Indicator"] == "CRITICAL PROFILE ALERT":
            reasons.append("Isolation Forest fallback also flagged this profile")
        if row["SubAgent_B_LedgerBERT_Risk"] > 0.20:
            reasons.append("ledger-risk terminology was detected")
        if row["SubAgent_C_CyberBERT_Risk"] > 0.20:
            reasons.append("cybersecurity-risk terminology was detected")
        if row["Overall_ESG_Score"] < 60:
            reasons.append("ESG score is below the review threshold")

        if not reasons:
            return "Transparent automated classification. No immediate human escalation required under prototype thresholds."
        return "Human verification recommended because " + "; ".join(reasons) + "."

    df["AI_Explainability_Log"] = df.apply(log, axis=1)

    print("[Agent 6] Trustworthy AI compliance audit complete.")
    return df


# ============================================================
# Agent 7: Dashboard and Visual Analytics
# ============================================================
def dashboard_agent(df, save_html=True):
    """
    Plotly dashboard exporter for multi-agent accounting analytics.
    Generates summary df and writes interactive visualizations as HTML assets.
    """
    summary = pd.DataFrame({
        "Metric": [
            "Accounting Lines Evaluated",
            "Autoencoder Alerts",
            "Isolation Forest Alerts",
            "Average ESG Score",
            "Average AI Compliance Score"
        ],
        "Value": [
            len(df),
            int((df["Anomaly_Indicator"] == "CRITICAL PROFILE ALERT").sum()),
            int((df["IForest_Indicator"] == "CRITICAL PROFILE ALERT").sum()),
            round(df["Overall_ESG_Score"].mean(), 2),
            round(df["EU_AI_Act_Compliance_Score"].mean(), 2)
        ]
    })

    fig1 = px.scatter(
        df,
        x="Debit_Value" if "Debit_Value" in df.columns else "scaled_Debit_Value",
        y="Reconstruction_Error",
        color="Anomaly_Indicator",
        size="Procurement_Waste_Tons" if "Procurement_Waste_Tons" in df.columns else "scaled_Procurement_Waste_Tons",
        hover_name="Company_ID",
        hover_data=["ERPNext_Source_Path", "Overall_ESG_Score", "EU_AI_Act_Compliance_Score"],
        title="Autoencoder Reconstruction Error by Ledger Profile"
    )

    fig2 = px.bar(
        df,
        x="Company_ID",
        y="Overall_ESG_Score",
        color="ESG_Risk_Classification",
        hover_data=["ERPNext_Source_Path", "AI_Explainability_Log"],
        title="ESG Risk Classification by Entity"
    )

    fig3 = px.bar(
        df,
        x="Company_ID",
        y="EU_AI_Act_Compliance_Score",
        color="Anomaly_Indicator",
        hover_data=["AI_Explainability_Log"],
        title="Trustworthy AI Compliance Score by Entity"
    )

    if save_html:
        fig1.write_html("data/autoencoder_anomaly.html")
        fig2.write_html("data/esg_risk.html")
        fig3.write_html("data/trustworthy_ai.html")
        print("\nInteractive Plotly HTML visualizations successfully saved:")
        print("  - data/autoencoder_anomaly.html")
        print("  - data/esg_risk.html")
        print("  - data/trustworthy_ai.html")

    return summary


# ============================================================
# One-click Orchestrator
# ============================================================
def run_multi_agent_accounting_ai(
    branch=ERP_NEXT_BRANCH,
    max_files=40,
    show_dashboard=True,
    output_path="data/final_agent_output.csv"
):
    """
    Runs the complete Multi-Agent Accounting AI workflow.
    """
    print("\n" + "=" * 76)
    print("STARTING MULTI-AGENT ACCOUNTING AI — CLI PIPELINE")
    print("=" * 76 + "\n")

    artifacts = collect_erpnext_artifacts(branch=branch, max_files=max_files)
    raw = generate_research_grade_ledger(artifacts)
    preprocessed = preprocessing_agent(raw)
    bert_enriched, embeddings = multi_bert_agent(preprocessed)
    ae_scored = autoencoder_anomaly_agent(bert_enriched)
    if_scored = isolation_forest_agent(ae_scored, embeddings)
    esg_scored = esg_risk_agent(if_scored)
    final = compliance_agent(esg_scored)

    final = final.drop(columns=["Text_Embedding_Proxy"], errors="ignore")
    final.to_csv(output_path, index=False)
    print(f"\nFinal audit output saved to: {output_path}")

    if show_dashboard:
        summary = dashboard_agent(final, save_html=True)
        print("\nSummary Statistics Table:")
        print(summary.to_string(index=False))

    print("\n" + "=" * 76)
    print("WORKFLOW COMPLETE")
    print("=" * 76 + "\n")

    return final


if __name__ == "__main__":
    run_multi_agent_accounting_ai()
