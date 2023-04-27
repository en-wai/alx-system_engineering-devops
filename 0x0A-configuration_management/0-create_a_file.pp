# Use puppet to create a file in /tmp

file {'/tmp/school':
  ensure => present,
  permission => '0744',
  owner => 'www-data',
  group => 'www-data',
  content => 'I love Puppet'
}
