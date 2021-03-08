#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
from sys import path
from ansible.module_utils.basic import AnsibleModule
from os import path
__metaclass__ = type

DOCUMENTATION = r'''
---
module: file_create

short_description: This is a simple module which creates a file

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    new:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - dallen.utils.my_doc_fragment_name

author:
    - Daniel Allen (@a118n)
'''

EXAMPLES = r'''
# Create file
- name: Create file
  dallen.utils.file_create:
    path: "/tmp/test.txt"
    content: "Hello there\n"
    new: true
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
path:
    description: File path param that was passed in.
    type: str
    returned: always
    sample: '/tmp/test.txt'
content:
    description: File content that this module generates.
    type: str
    returned: always
    sample: 'Hello there'
'''


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        path='',
        content=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)

    if path.exists(module.params['path']):
        with open(module.params['path'], 'r') as f:
            file_content = f.read()

    if file_content == module.params['content']:
        result['changed'] = False
    else:
        with open(module.params['path'], 'w') as f:
            f.write(module.params['content'])
            f.close()
            result['path'] = module.params['path']
            result['content'] = module.params['content']
            result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    # if module.params['name'] == 'fail me':
    #     module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
