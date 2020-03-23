#!/usr/bin/env bash
#Installing puppet-lint version 2.1.1 using puppet
package { 'puppet-lint':
    ensure   => '2.1.1',
    provider => 'gem',
}
