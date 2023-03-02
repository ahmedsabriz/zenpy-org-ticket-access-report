from argparse import ArgumentParser, Namespace
from dotenv import load_dotenv
from os import environ
from requests import Session
from zenpy import Zenpy
import csv


def main():
    # Parsing CLI arguments
    parser = ArgumentParser(
        description="Sample script for Zendesk Administrators utilising Zendesk API client for Python to create CSV report of number of incidents per problem ticket. Credentials can be configured in .env file or overriden through optional arguments."
    )
    parser.add_argument(
        "-s",
        action="store",
        type=str.lower,
        dest="subdomain",
        help="Zendesk Subdomain (e.g. d3v-test)",
    )
    parser.add_argument(
        "-o",
        action="store",
        type=str.lower,
        dest="oauthtoken",
        help='Pre-generated OAuth2 token with "tickets:read write" scope',
    )
    parser.add_argument(
        "-u",
        action="store",
        type=str.lower,
        dest="username",
        help="Agent Zendesk email address",
    )
    parser.add_argument(
        "-p",
        action="store",
        type=str.lower,
        dest="password",
        help="Agent Zendesk password",
    )
    parser.add_argument(
        "-t",
        action="store",
        dest="apitoken",
        type=str.lower,
        help="Zendesk API token",
    )

    parser.parse_args(namespace=Namespace)

    load_dotenv()
    creds = {
        "subdomain": Namespace.subdomain
        if Namespace.subdomain
        else environ["SUBDOMAIN"],
        "oauth_token": Namespace.oauthtoken
        if Namespace.oauthtoken
        else environ.get("OAUTHTOKEN"),
        "email": Namespace.username if Namespace.username else environ.get("USERNAME"),
        "password": Namespace.password
        if Namespace.password
        else environ.get("PASSWORD"),
        "token": Namespace.apitoken if Namespace.apitoken else environ.get("APITOKEN"),
    }

    session = Session()
    session.headers["Content-Type"] = "application/json"

    # Start Client
    zenpy_client = Zenpy(**creds, session=session)

    users = zenpy_client.users()
    rows = []
    for user in users:
        if user.active and user.organization_id and user.ticket_restriction == "organization":
            rows.append([user.name, zenpy_client.organizations(id=user.organization_id).name, user.url])
    
    with open("./org_ticket_access_report.csv", "w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name", "Organization", "URL"])
        writer.writerows(rows)


if __name__ == "__main__":
    main()