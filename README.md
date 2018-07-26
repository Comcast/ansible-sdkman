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

> **Warning**: Oracle has made it increasingly difficult to install their JDKs,
> which has impeded the ability to install them via SDKMAN. Consider using the
> OpenJDK instead or installing/managing the Oracle JDK by other means.

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
    - role: Comcast.sdkman
      sdkman_dir: /usr/local/sdkman
      sdkman_auto_answer: true
      sdkman_update: true
      sdkman_uninstall_packages:
        - { candidate: groovy, version: 1.8.9 }
      sdkman_install_packages:
        - { candidate: gradle, version: '3.5' }
        - { candidate: gradle, version: 2.14.1 }
        - { candidate: maven, version: 3.5.0 }
        - { candidate: maven, version: 3.3.9 }
      sdkman_defaults:
        gradle: '3.5'
        maven: 3.3.9
      sdkman_flush_caches_before:
        - temp
      sdkman_flush_caches_after:
        - archives
        - broadcast
        - candidates
        - temp
```

License
-------

[Apache 2.0](LICENSE)

Author Information
------------------

* [Elliot Weiser](https://github.com/elliotweiser) @ [Comcast](https://github.com/Comcast)

[galaxy-link]: https://galaxy.ansible.com/Comcast/sdkman/
[license-badge]: https://img.shields.io/badge/license-Apache%202.0-blue.svg
[license-link]: https://raw.githubusercontent.com/Comcast/ansible-sdkman/master/LICENSE
[role-badge]: https://img.shields.io/ansible/role/20938.svg
[travis-badge]: https://api.travis-ci.org/Comcast/ansible-sdkman.svg?branch=master
[travis-link]: https://travis-ci.org/Comcast/ansible-sdkman
