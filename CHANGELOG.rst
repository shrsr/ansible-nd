======================================================
Cisco Nexus Dashboard Ansible Collection Release Notes
======================================================

.. contents:: Topics


v0.4.0
======

Release Summary
---------------

Release v0.4.0 of the ``ansible-nd`` collection on 2023-08-04.
This changelog describes all changes made to the modules and plugins included in this collection since v0.3.0.


Minor Changes
-------------

- Add new module nd_site (#47)

v0.3.0
======

Release Summary
---------------

Release v0.3.0 of the ``ansible-nd`` collection on 2023-04-05.
This changelog describes all changes made to the modules and plugins included in this collection since v0.2.0.


Minor Changes
-------------

- Add module nd_compliance_analysis and nd_compliance_requirement_communication and nd_compliance_requirement_config_import and nd_compliance_requirement_config_manual and nd_compliance_requirement_config_snapshot and nd_compliance_requirement_config_template and nd_epoch

Bugfixes
--------

- Ensure python2 compatible methods are used for the bytes io object in ND HTTPAPI Connection Plugin (#41)

New Modules
-----------

- cisco.nd.nd_compliance_analysis - Query compliance analysis data from Cisco Nexus Dashboard Insights (NDI)
- cisco.nd.nd_compliance_requirement_communication - Manage communication type compliance requirements
- cisco.nd.nd_compliance_requirement_config_import - Manage import configuration type compliance requirements
- cisco.nd.nd_compliance_requirement_config_manual - Manage manual configuration type compliance requirements
- cisco.nd.nd_compliance_requirement_config_snapshot - Manage snapshot configuration type compliance requirements
- cisco.nd.nd_compliance_requirement_config_template - Manage template configuration type compliance requirements
- cisco.nd.nd_epoch - Query epoch data from Cisco Nexus Dashboard Insights (NDI)

v0.2.0
======

Release Summary
---------------

Release v0.2.0 of the ``ansible-nd`` collection on 2023-02-04.
This changelog describes all changes made to the modules and plugins included in this collection since v0.1.2.


Minor Changes
-------------

- Add ansible_httpapi_login_domain global inventory variable

Bugfixes
--------

- Allow local to be set as login_domain && set DefaultAuth as default for login_domain
- Fix HTTPAPI Connection plugin when wrong login_domain is provided
- Fix HTTPAPI ND connection plugin missing login_domain definition

New Modules
-----------

- cisco.nd.nd_delta_analysis - Manage delta analysis jobs
- cisco.nd.nd_instant_assurance_analysis - Manage instant online assurance analysis jobs
- cisco.nd.nd_pcv - Manage pre-change validation job
- cisco.nd.nd_pcv_compliance - Query pre-change validation compliance
- cisco.nd.nd_pcv_delta_analysis - Query delta analysis of pre-change validation

v0.1.2
======

Release Summary
---------------

New release v0.1.2

Bugfixes
--------

- Fix ND HTTAPI plugin login_domain issue when used with cisco.mso collection
- Fix default user when not defining the user. Default username "admin" has been removed. Always specify username via module attribute or define the ansible_user variable in inventory.
- Remove empty sanity ignore files

v0.1.1
======

Release Summary
---------------

New release v0.1.1

Bugfixes
--------

- Fix ND HTTAPI plugin to support remote users
- Remove required params for attributes that are handled by the HTTPAPI plugin

v0.1.0
======

Release Summary
---------------

Initial release of Nexus Dashboard collection
