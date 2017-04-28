Comcast.sdkman
==============

[![Build Status][travis-badge]][travis-link]
[![Apache 2.0 licensed][license-badge]][license-link]
[![Galaxy Role][role-badge]][galaxy-link]

An Ansible role that performs the following functions:
* Install [SDKMAN](http://sdkman.io/)
* Install/uninstall SDKMAN-managed software [candidates](http://sdkman.io/sdks.html)
* Set SDK version defaults
* Manage the SDKMAN configuration file: `/path/to/sdkman/etc/config`
* Flush the SDKMAN caches

Requirements
------------

None.

Role Variables
--------------

See the [defaults](defaults/main.yml) for a description of each overrideable
variable.

Dependencies
------------

None.

Example Playbook
----------------

Here's an example!

```yaml
- hosts: servers
  roles:
    - role: comcast.sdkman
      sdkman_dir: /usr/local/sdkman
      sdkman_auto_answer: true
      sdkman_update: true
      sdkman_uninstall_packages:
        - { candidate: groovy, version: 1.8.9 }
      sdkman_install_packages:
        - { candidate: java, version: 8u131 }
        - { candidate: gradle, version: '3.5' }
        - { candidate: gradle, version: 2.14.1 }
        - { candidate: maven, version: 3.5.0 }
        - { candidate: maven, version: 3.3.9 }
      sdkman_defaults:
        java: 8u131
        gradle: '3.5'
        maven: 3.3.9
```

License
-------

[Apache 2.0](License)

Author Information
------------------

* [Elliot Weiser](https://github.com/elliotweiser) @ [Comcast](https://github.com/Comcast)

[galaxy-link]: https://galaxy.ansible.com/Comcast/sdkman/
[license-badge]: https://img.shields.io/badge/license-Apache%202.0-blue.svg
[license-link]: https://raw.githubusercontent.com/Comcast/ansible-sdkman/master/LICENSE
[role-badge]: https://img.shields.io/ansible/role/17404.svg
[travis-badge]: https://api.travis-ci.org/Comcast/ansible-sdkman.svg?branch=master
[travis-link]: https://travis-ci.org/Comcast/ansible-sdkman
