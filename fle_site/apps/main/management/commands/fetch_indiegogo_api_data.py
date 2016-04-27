import os
import json
import requests

from django.conf import settings
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = """Downloads IndieGoGo API data and saves filtered JSON files."""

    def handle_noargs(self, **opts):

        contributor_keys = ["by", "created_at", "amount"]

        summary = json.loads(requests.get(settings.INDIEGOGO_SUMMARY_URL).content).get("response", {})

        summary_out = {
            "collected_funds": summary.get("collected_funds"),
            "goal": summary.get("goal"),
            "contributions_count": summary.get("contributions_count"),
            "latest_contributions": [{k: v for k,v in contributor.iteritems() if k in contributor_keys} for contributor in summary.get("latest_contributions", [])],
        }

        with open(os.path.join(settings.INDIEGOGO_API_DATA_LOCATION, "summary.json"), "w") as f:
            json.dump(summary_out, f)

        contributors = json.loads(requests.get(settings.INDIEGOGO_CONTRIBUTORS_URL).content).get("response", [])

        contributors_out = [{k: v for k,v in contributor.iteritems() if k in contributor_keys} for contributor in contributors or []]

        with open(os.path.join(settings.INDIEGOGO_API_DATA_LOCATION, "all_contributors.json"), "w") as f:
            json.dump(contributors_out, f)
