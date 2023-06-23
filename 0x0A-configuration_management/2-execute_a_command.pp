#A script to  create a manifest that kills a process named killmenow using Pippet.
exec {'kill': command => 'pkill -f killmenow', path => ['/usr/bin', '/usr/sbin']}
