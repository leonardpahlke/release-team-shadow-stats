# Copyright 2022 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# This file contains logic to create dummy data which is used to present the application
# and its also used for testing.
#

from faker import Faker
from faker.providers import company, python, lorem
from vars import timezone_aliases, pronouns, RELEASE_TEAM_TEAMS
import secrets

# first, import a similar Provider or use the default one
from faker.providers import BaseProvider


# Timezone provider class
class TimezoneProvider(BaseProvider):
    def timezone(self) -> str:
        return secrets.choice(list(timezone_aliases.keys()))


# Yes/No provider class
class YesNoProvider(BaseProvider):
    def yesno(self) -> str:
        return secrets.choice(["Yes", "No"])


# Pronouns provider class
class PronounsProvider(BaseProvider):
    def pronoun(self) -> str:
        return secrets.choice(pronouns)


# How many times applied before provider class
class AppliedBeforeProvider(BaseProvider):
    def applied_before(self) -> str:
        return secrets.choice(["This is my first time", "Once before", "Twice before", "Three or more times before"])


# Company provider class
class CompanyProvider(BaseProvider):
    def company2(self) -> str:
        return secrets.choice(["Walmart", "Amazon", "Apple", "CVS Health", "UnitedHealth Group", "Berkshire Hathaway", "McKesson", "AmerisourceBergen", "Alphabet", "Exxon Mobil",
        "At&T", "Costco Wholesale", "Cigna", "Cardinal Health", "Microsoft", "Walgreens Boots Appliance", "Kroger", "Home Depot", "JPMorgan Chase", "Verizon Communications"])


# Release Team provider class
class ReleaseTeamProvider(BaseProvider):
    def release_team(self) -> str:
        return secrets.choice(RELEASE_TEAM_TEAMS)


fake = Faker()
fake.add_provider(company)
fake.add_provider(python)
fake.add_provider(lorem)
fake.add_provider(TimezoneProvider)
fake.add_provider(PronounsProvider)
fake.add_provider(ReleaseTeamProvider)
fake.add_provider(CompanyProvider)
fake.add_provider(YesNoProvider)
fake.add_provider(AppliedBeforeProvider)



# The methods below are getting used in dataclasses to generate defaults for testing


def fake_get_name() -> str:
    return fake.name()


def fake_get_email() -> str:
    return f'{fake.ssn()}@example.com'


def fake_get_pargraph() -> str:
    return fake.paragraph(nb_sentences=1)


def fake_get_bool() -> str:
    return fake.yesno()

def fake_applied_before() -> str:
    return fake.applied_before()


def fake_get_company() -> str:
    return fake.company2()


def fake_get_text() -> str:
    return fake.paragraph(nb_sentences=4)


def fake_get_pronoun() -> str:
    return fake.pronoun()


def fake_get_timezone() -> str:
    return fake.timezone()


def fake_get_number_code() -> str:
    return fake.ssn()


def fake_get_release_team_team() -> str:
    return fake.release_team()
