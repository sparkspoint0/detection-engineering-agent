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


def generate_detection_draft(user_prompt: str) -> str:
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not deployment_name:
        st.error("Missing AZURE_OPENAI_DEPLOYMENT in your .env file.")
        st.stop()

    client = get_client()

    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
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

# Initialize session state for the user prompt.
if "user_prompt" not in st.session_state:
    st.session_state.user_prompt = ""

with st.sidebar:
    st.header("Demo Scenarios")

    selected_scenario = st.selectbox(
        "Choose a sample scenario to load",
        list(SAMPLE_SCENARIOS.keys()),
    )

    if st.button("Load Sample Scenario"):
        st.session_state.user_prompt = SAMPLE_SCENARIOS[selected_scenario]

    if st.button("Clear Prompt"):
        st.session_state.user_prompt = ""

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

st.markdown("### Enter any SOC scenario or detection engineering request")

user_prompt = st.text_area(
    "Type or paste your own prompt below:",
    key="user_prompt",
    height=260,
    placeholder=(
        "Example: A user had multiple failed sign-ins followed by a successful login "
        "from a new country. MFA was approved, and the account downloaded several "
        "SharePoint files."
    ),
)

st.markdown("You can enter a full incident summary, suspicious behavior, alert details, or a detection engineering request.")

generate = st.button("Generate Detection Draft")

if generate:
    if not user_prompt.strip():
        st.warning("Please enter a SOC scenario or detection engineering request first.")
        st.stop()

    with st.spinner("Generating detection engineering draft..."):
        try:
            result = generate_detection_draft(user_prompt)
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
