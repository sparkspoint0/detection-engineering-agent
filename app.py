import os

import streamlit as st
from dotenv import load_dotenv
from openai import AzureOpenAI

from agent_prompt import SYSTEM_PROMPT
from sample_scenarios import SAMPLE_SCENARIOS


load_dotenv()


def get_client() -> AzureOpenAI:
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

    if not endpoint or not api_key:
        st.error("Missing Azure OpenAI configuration. Check your .env file.")
        st.stop()

    return AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version=api_version,
    )


def generate_detection_draft(scenario: str) -> str:
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not deployment_name:
        st.error("Missing AZURE_OPENAI_DEPLOYMENT in your .env file.")
        st.stop()

    client = get_client()

    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": scenario},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content


st.set_page_config(
    page_title="Detection Engineer Agent",
    page_icon="🛡️",
    layout="wide",
)

st.title("Detection Engineer Agent")
st.caption("From SOC investigation to Microsoft Sentinel detection logic.")

with st.sidebar:
    st.header("Demo Scenarios")
    selected_scenario = st.selectbox(
        "Choose a sample scenario",
        ["Custom"] + list(SAMPLE_SCENARIOS.keys()),
    )

    st.markdown("---")
    st.markdown("### Project Output")
    st.markdown(
        """
        The agent generates:
        - MITRE ATT&CK mapping
        - Sentinel data sources
        - Starter KQL
        - Analytics rule details
        - False positives
        - Tuning guidance
        - Analyst steps
        """
    )

if selected_scenario == "Custom":
    default_text = ""
else:
    default_text = SAMPLE_SCENARIOS[selected_scenario]

scenario = st.text_area(
    "SOC scenario, incident summary, or suspicious behavior",
    value=default_text,
    height=240,
    placeholder="Example: A user had multiple failed sign-ins followed by a successful login from a new country...",
)

generate = st.button("Generate Detection Draft")

if generate:
    if not scenario.strip():
        st.warning("Please enter a SOC scenario first.")
        st.stop()

    with st.spinner("Generating detection engineering draft..."):
        try:
            result = generate_detection_draft(scenario)
        except Exception as error:
            st.error("The model call failed. Check your endpoint, key, deployment name, API version, and Azure access.")
            st.exception(error)
            st.stop()

    st.subheader("Detection Engineering Draft")
    st.markdown(result)

    st.download_button(
        label="Download Detection Draft",
        data=result,
        file_name="sentinel_detection_draft.md",
        mime="text/markdown",
    )
