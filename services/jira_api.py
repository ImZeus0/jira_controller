import requests
from jira import JIRA
from core.config import get_settings

jira_options = {'server': 'https://lvl99-betapps.atlassian.net/'}
jira_connection = JIRA(options=jira_options, basic_auth=(get_settings().jira_email, get_settings().jira_token))

def add_file_to_issue(issue_key,file_name):
    current_issue = jira_connection.issue(issue_key)
    with open(f'{file_name}.zip', 'rb') as f:
        jira_connection.add_attachment(issue=current_issue, attachment=f,)

def move_to_qaqc(issue_key):
    jira_connection.transition_issue(issue_key, 'to qa')

