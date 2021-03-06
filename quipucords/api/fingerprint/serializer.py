#
# Copyright (c) 2017 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 3 (GPLv3). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv3
# along with this software; if not, see
# https://www.gnu.org/licenses/gpl-3.0.txt.
#

"""Serializer for system fingerprint models."""

from rest_framework.serializers import (PrimaryKeyRelatedField,
                                        IntegerField,
                                        CharField,
                                        ChoiceField,
                                        DateField,
                                        NullBooleanField,
                                        ModelSerializer)
from api.models import (SystemFingerprint, FactCollection)
from api.common.serializer import CustomJSONField


class FingerprintSerializer(ModelSerializer):
    """Serializer for the Fingerprint model."""

    # Scan information
    fact_collection_id = PrimaryKeyRelatedField(
        queryset=FactCollection.objects.all())

    # Common facts
    name = CharField(required=False, max_length=256)

    os_name = CharField(required=False, max_length=64)
    os_release = CharField(required=False, max_length=128)
    os_version = CharField(required=False, max_length=64)

    infrastructure_type = ChoiceField(
        required=False, choices=SystemFingerprint.INFRASTRUCTURE_TYPE)
    virtualized_is_guest = NullBooleanField(default=None)

    mac_addresses = CustomJSONField(required=False)
    ip_addresses = CustomJSONField(required=False)

    cpu_count = IntegerField(required=False, min_value=0)

    # Network scan facts
    bios_uuid = CharField(required=False, max_length=36)
    subscription_manager_id = CharField(required=False, max_length=36)

    cpu_core_per_socket = IntegerField(required=False, min_value=0)
    cpu_siblings = IntegerField(required=False, min_value=0)
    cpu_hyperthreading = NullBooleanField(required=False)
    cpu_socket_count = IntegerField(required=False, min_value=0)
    cpu_core_count = IntegerField(required=False, min_value=0)

    system_creation_date = DateField(required=False)

    virtualized_type = CharField(required=False, max_length=64)
    virtualized_num_guests = IntegerField(required=False, min_value=0)
    virtualized_num_running_guests = IntegerField(required=False, min_value=0)

    # VCenter scan facts
    vm_state = CharField(required=False, max_length=24)
    vm_uuid = CharField(required=False, max_length=36)
    vm_memory_size = IntegerField(required=False, min_value=0)
    vm_dns_name = CharField(required=False, max_length=128)

    vm_host = CharField(required=False, max_length=128)
    vm_host_socket_count = IntegerField(required=False, min_value=0)
    vm_host_cpu_cores = IntegerField(required=False, min_value=0)

    vm_host_cpu_threads = IntegerField(required=False, min_value=0)

    vm_cluster = CharField(required=False, max_length=128)
    vm_datacenter = CharField(required=False, max_length=128)

    metadata = CustomJSONField(required=True)

    class Meta:
        """Meta class for FingerprintSerializer."""

        model = SystemFingerprint
        fields = '__all__'
