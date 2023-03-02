# Zenpy Organization Ticket Access Report

Sample script for Zendesk administrators utilising Zendesk API client for Python [Zenpy](https://github.com/facetoe/zenpy) to create CSV report of users who have organization-level access to tickets. Credentials can be configured in .env file or
overriden through optional arguments.

## Getting started

- Clone repository
- Go to repository directory
- Install requirments `python3 -m pip install -r requirments.txt`
- [Optional] Create .env file using your favourite text editor to store your credentials

### .env file example

SUBDOMAIN=subdomain_only \
USERNAME=admin@example.com \
APITOKEN=foobarbaz

## Usage

`python3 script.py [-h] [-s SUBDOMAIN] [-o OAUTHTOKEN] [-u USERNAME] [-p PASSWORD] [-t APITOKEN] [--start STARTDATE] [--end ENDDATE]`

options: \
-h, --help show this help message and exit \
-s SUBDOMAIN Zendesk Subdomain (e.g. d3v-test) \
-o OAUTHTOKEN Pre-generated OAuth2 token with "users:read organizations:read" scope \
-u USERNAME Agent Zendesk email address \
-p PASSWORD Agent Zendesk password \
-t APITOKEN Zendesk API token \
