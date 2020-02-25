#!/usr/bin/env ruby
f = ARGV[0].scan(/from:([^\]]+)/).join
t = ARGV[0].scan(/to:([^\]]+)/).join
f =  ARGV[0].scan(/flags:([^\]]+)/).join

puts f + "," + t + "," + f
