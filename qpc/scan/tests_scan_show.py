#
# Copyright (c) 2017-2018 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 3 (GPLv3). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv3
# along with this software; if not, see
# https://www.gnu.org/licenses/gpl-3.0.txt.
#
"""Test the CLI module."""

import unittest
import sys
from io import StringIO
from argparse import ArgumentParser, Namespace
import requests
import requests_mock
from qpc.tests_utilities import HushUpStderr, redirect_stdout, DEFAULT_CONFIG
from qpc.request import CONNECTION_ERROR_MSG, SSL_ERROR_MSG
from qpc.scan import SCAN_URI
from qpc.scan.show import ScanShowCommand
from qpc.utils import get_server_location, write_server_config

PARSER = ArgumentParser()
SUBPARSER = PARSER.add_subparsers(dest='subcommand')


class ScanShowCliTests(unittest.TestCase):
    """Class for testing the scan show commands for qpc."""

    def setUp(self):
        """Create test setup."""
        write_server_config(DEFAULT_CONFIG)
        # Temporarily disable stderr for these tests, CLI errors clutter up
        # nosetests command.
        self.orig_stderr = sys.stderr
        sys.stderr = HushUpStderr()

    def tearDown(self):
        """Remove test setup."""
        # Restore stderr
        sys.stderr = self.orig_stderr

    def test_show_scan_ssl_err(self):
        """Testing the show scan command with a connection error."""
        scan_out = StringIO()
        url = get_server_location() + SCAN_URI + '1/'
        with requests_mock.Mocker() as mocker:
            mocker.get(url, exc=requests.exceptions.SSLError)
            nsc = ScanShowCommand(SUBPARSER)
            args = Namespace(id='1', results=False)
            with self.assertRaises(SystemExit):
                with redirect_stdout(scan_out):
                    nsc.main(args)
                    self.assertEqual(scan_out.getvalue(), SSL_ERROR_MSG)

    def test_show_scan_conn_err(self):
        """Testing the show scan command with a connection error."""
        scan_out = StringIO()
        url = get_server_location() + SCAN_URI + '1/'
        with requests_mock.Mocker() as mocker:
            mocker.get(url, exc=requests.exceptions.ConnectTimeout)
            nsc = ScanShowCommand(SUBPARSER)
            args = Namespace(id='1', results=False)
            with self.assertRaises(SystemExit):
                with redirect_stdout(scan_out):
                    nsc.main(args)
                    self.assertEqual(scan_out.getvalue(),
                                     CONNECTION_ERROR_MSG)

    def test_show_scan_internal_err(self):
        """Testing the show scan command with an internal error."""
        scan_out = StringIO()
        url = get_server_location() + SCAN_URI + '1/'
        with requests_mock.Mocker() as mocker:
            mocker.get(url, status_code=500, json={'error': ['Server Error']})
            nsc = ScanShowCommand(SUBPARSER)
            args = Namespace(id='1', results=False)
            with self.assertRaises(SystemExit):
                with redirect_stdout(scan_out):
                    nsc.main(args)
                    self.assertEqual(scan_out.getvalue(), 'Server Error')

    def test_show_scan_data(self):
        """Testing the show scan command successfully with stubbed data."""
        scan_out = StringIO()
        url = get_server_location() + SCAN_URI + '1/'
        scan_entry = {'id': 1,
                      'source': {
                          'id': 1,
                          'name': 'scan1'},
                      'scan_type': 'host',
                      'status': 'completed'}
        with requests_mock.Mocker() as mocker:
            mocker.get(url, status_code=200, json=scan_entry)
            nsc = ScanShowCommand(SUBPARSER)
            args = Namespace(id='1', results=False)
            with redirect_stdout(scan_out):
                nsc.main(args)
                expected = '{"id":1,"scan_type":"host",' \
                           '"source":{"id":1,"name":"scan1"},'\
                           '"status":"completed"}'
                self.assertEqual(scan_out.getvalue().replace('\n', '')
                                 .replace(' ', '').strip(), expected)

    def test_show_scan_results(self):
        """Testing the show scan results command with stubbed data."""
        scan_out = StringIO()
        url = get_server_location() + SCAN_URI + '1/results/'

        scan_entry = {
            'connection_results': {
                'results': [
                    {
                        'source': {
                            'id': 1,
                            'name': 'vc1',
                            'source_type': 'vcenter'
                        },
                        'systems': [
                            {
                                'credential': {
                                    'id': 1,
                                    'name': 'vc1'
                                },
                                'name': 'sonar-jbossfuse-rhel-7-vc',
                                'status': 'success'
                            }
                        ]
                    }
                ]
            }
        }
        with requests_mock.Mocker() as mocker:
            mocker.get(url, status_code=200, json=scan_entry)
            nsc = ScanShowCommand(SUBPARSER)
            args = Namespace(id='1', results=True)
            with redirect_stdout(scan_out):
                nsc.main(args)
                expected = '{"connection_results":{"results":' \
                    '[{"source":{"id":1,"name":"vc1","source_type":' \
                    '"vcenter"},"systems":[{"credential":{"id":1,' \
                    '"name":"vc1"},"name":"sonar-jbossfuse-rhel-7-vc"' \
                    ',"status":"success"}]}]}}'
                self.assertEqual(scan_out.getvalue().replace('\n', '')
                                 .replace(' ', '').strip(), expected)
