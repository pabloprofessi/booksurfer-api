#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import json

from mock import patch, Mock
from app import create_app
from app.extensions import db



@pytest.fixture
def basic_api():
    app = create_app("test")
    return app.test_client()


class TestPingResource:

    def test_api_is_up_and_responds_ping_pong(self, basic_api):
        ping = basic_api.get('/ping')

        assert ping.status_code == 200


