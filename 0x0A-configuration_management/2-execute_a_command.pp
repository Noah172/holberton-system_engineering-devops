#!/usr/bin/env bash
#kill procces with puppet
exec { 'kill':
    command => 'pkill -f killmenow',
    path    => '/usr/bin',
}
