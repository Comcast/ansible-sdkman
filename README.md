comcast.sdkman
==============

A brief description of the role goes here.
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

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
    - role: comcast.sdkman
      sdkman_auto_answer: true
      sdkman_update: true
      sdkman_uninstall_packages:
        - { candidate: groovy, version: 1.8.9 }
      sdkman_install_packages:
        - { candidate: java, version: 8u131 }
        - { candidate: java, version: 7u80 }
        - { candidate: java, version: 6u45 }
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

TBD

Author Information
------------------

* [Elliot Weiser](https://github.com/elliotweiser) @ [Comcast](https://github.com/Comcast)
