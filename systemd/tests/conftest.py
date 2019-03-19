# (C) Datadog, Inc. 2019
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest


@pytest.fixture
def instance():
    return {
        'units': [
            "ssh.service",
            "cron.service",
            "networking.service"
        ],
        'report_status': False,
        'report_processes': True
    }


@pytest.fixture
def instance_collect_all():
    return {
        'units': [
            "ssh.service",
            "cron.service",
            "networking.service"
        ],
        'report_status': True,
        'report_processes': True
    }