# Detection Engineer Agent

Detection Engineer Agent is a Microsoft Foundry / Azure OpenAI-powered reasoning agent that helps SOC analysts and detection engineers convert suspicious activity into Microsoft Sentinel detection engineering drafts.

## Project Track

Reasoning Agent

## Tagline

From SOC investigation to detection logic in minutes.

## Problem

SOC analysts often investigate suspicious activity, but the lessons from those investigations are not always converted into reusable detections. This can create gaps where similar behavior may happen again without improved alerting.

## Solution

Detection Engineer Agent accepts a SOC scenario, alert summary, or suspicious behavior and generates a structured detection engineering draft.

The output includes:

- Executive summary
- Key observations
- Assumptions
- Likely attack behavior
- MITRE ATT&CK mapping
- Detection objective
- Microsoft Sentinel data sources
- Starter KQL query
- Suggested Sentinel analytics rule details
- False positive considerations
- Tuning recommendations
- Analyst investigation steps
- Response recommendations

## Built With

- Microsoft Foundry / Azure OpenAI
- GPT-4.1 mini deployment
- Python
- Streamlit
- Microsoft Sentinel concepts
- KQL
- MITRE ATT&CK

## How It Works

1. A SOC analyst enters an incident summary or suspicious behavior.
2. The app sends the scenario to the Azure OpenAI deployment using a structured system prompt.
3. The reasoning agent analyzes the scenario.
4. The agent generates a Sentinel-style detection engineering draft.
5. The analyst can review, tune, and download the draft.

## Demo Scenarios

- MFA fatigue followed by SharePoint file downloads
- Suspicious PowerShell launched by Microsoft Word
- New Global Administrator assignment and risky app registration
- Custom user-entered SOC scenarios

## Setup

Create a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
