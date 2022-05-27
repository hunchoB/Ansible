#!/usr/bin/python

import re
from ansible.errors import (
    AnsibleFilterTypeError, AnsibleOptionsError
)


def change_to_mac_address(input_row):
    pattern = re.compile("[A-F0-9]+")
    
    if not isinstance(input_row, str):
        raise AnsibleFilterTypeError("It is not a string, check your input")
    elif len(input_row) % 2 ==0 and pattern.fullmatch(input_row):
        mac = ''
        index = 2
        for i in range(8):
            temp = input_row[index - 2:index]
            mac += temp + ":"
            index += 2
        return mac[:len(mac)-1]
    else:
        raise AnsibleOptionsError("It is not a even string, check your input")


class FilterModule(object):
    def filters(self):
        return {
            'change_to_mac_address': change_to_mac_address
        }