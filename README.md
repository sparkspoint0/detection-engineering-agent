# Sentinel Detection Copilot

Sentinel Detection Copilot is a Microsoft Foundry / Azure AI-powered reasoning agent that helps SOC analysts convert suspicious activity into Microsoft Sentinel detection engineering drafts.

## Problem

SOC analysts often investigate suspicious activity, but the lessons from those investigations are not always converted into reusable detections.

## Solution

This agent takes a SOC scenario or incident summary and generates:

- Executive summary
- Key observations
- MITRE ATT&CK mapping
- Detection objective
- Recommended Microsoft Sentinel data sources
- Starter KQL query
- Suggested analytics rule details
- False positive considerations
- Tuning recommendations
- Analyst investigation steps

## Built With

- Microsoft Foundry / Azure OpenAI
- Python
- Streamlit
- Microsoft Sentinel concepts
- KQL
- MITRE ATT&CK

## Demo Scenarios

1. MFA fatigue followed by SharePoint file downloads
2. Suspicious PowerShell launched by Microsoft Word
3. New Global Administrator assignment and risky app registration

## Run in Ubuntu

```bash
cd ~/projects/sentinel-detection-copilot
source .venv/bin/activate
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
