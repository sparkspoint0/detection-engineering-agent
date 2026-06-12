SAMPLE_SCENARIOS = {
    "MFA Fatigue + SharePoint Download": """
A user received 12 MFA push notifications in 5 minutes. One request was approved.
The successful login came from a country the user does not normally access from.
After login, the account accessed SharePoint and downloaded multiple files.
""",

    "Suspicious PowerShell from Word": """
An endpoint executed PowerShell with an encoded command. The process attempted to
download a file from a remote URL and save it to the user's AppData directory.
The command was launched by Microsoft Word.
""",

    "New Global Admin Assignment": """
A standard user account was assigned Global Administrator privileges. Shortly after,
the account created a new application registration and granted it high-risk API permissions.
"""
}
