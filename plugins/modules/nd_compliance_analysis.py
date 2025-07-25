#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Akini Ross (@akinross) <akinross@cisco.com>

# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {"metadata_version": "1.1", "status": ["preview"], "supported_by": "community"}

DOCUMENTATION = r"""
---
module: nd_compliance_analysis
version_added: "0.3.0"
short_description: Query compliance analysis data from Cisco Nexus Dashboard Insights (NDI)
description:
- Query compliance analysis data from Cisco Nexus Dashboard Insights (NDI).
author:
- Akini Ross (@akinross)
options:
  insights_group:
    description:
    - The name of the insights group.
    - This attribute should only be set for NDI versions prior to 6.3. Later versions require this attribute to be set to default.
    type: str
    default: default
    aliases: [ fab_name, ig_name ]
  fabric:
    description:
    - The name of the fabric.
    type: str
    required: true
    aliases: [site, site_name, fabric_name ]
  snapshot_id:
    description:
    - The snapshot/epoch ID.
    - When the O(snapshot_id) is not provided it will retrieve the latest known snapshot/epoch ID.
    type: str
    aliases: [ epoch_id ]
extends_documentation_fragment:
- cisco.nd.modules
- cisco.nd.check_mode
"""

EXAMPLES = r"""
- name: Run compliance analysis for latest snapshot ID
  cisco.nd.nd_compliance_analysis:
    insights_group: igName
    fabric: fabricName
  register: query_results

- name: Run compliance analysis with specified snapshot ID
  cisco.nd.nd_compliance_analysis:
    insights_group: igName
    fabric: fabricName
    snapshot_id: 0e5604f9-373a123c-b535-33fc-8d11-672d08f65fd1
  register: query_results
"""

RETURN = r"""
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.nd.plugins.module_utils.nd import NDModule, nd_argument_spec
from ansible_collections.cisco.nd.plugins.module_utils.ndi import NDI


def main():
    argument_spec = nd_argument_spec()
    argument_spec.update(
        insights_group=dict(type="str", default="default", aliases=["fab_name", "ig_name"]),
        fabric=dict(type="str", required=True, aliases=["site", "site_name", "fabric_name"]),
        snapshot_id=dict(type="str", aliases=["epoch_id"]),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    nd = NDModule(module)
    ndi = NDI(nd)

    insights_group = nd.params.get("insights_group")
    fabric = nd.params.get("fabric")
    snapshot_id = nd.params.get("snapshot_id")

    if not snapshot_id:
        snapshot_id = ndi.get_last_epoch(insights_group, fabric).get("epochId")

    nd.existing["smart_events"] = ndi.query_compliance_smart_event(insights_group, fabric, snapshot_id)
    nd.existing["events_by_severity"] = ndi.query_msg_with_data(insights_group, fabric, "eventsBySeverity?%24epochId={0}".format(snapshot_id))
    nd.existing["unhealthy_resources"] = ndi.query_unhealthy_resources(insights_group, fabric, snapshot_id)
    nd.existing["compliance_score"] = ndi.query_compliance_score(insights_group, fabric, snapshot_id)
    nd.existing["count"] = ndi.query_compliance_count(insights_group, fabric, snapshot_id)
    nd.existing["result_by_requirement"] = ndi.query_msg_with_data(
        insights_group, fabric, "complianceResultsByRequirement?%24epochId={0}&%24sort=-requirementName&%24page=0&%24size=10".format(snapshot_id)
    )

    nd.exit_json()


if __name__ == "__main__":
    main()
