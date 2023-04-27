# Use puppet to create a file in /tmp

file {'/tmp/school':
  ensure     => file,
  permission => '0744',
  owner      => 'www-data',
  group      => 'www-data',
  content    => 'I love Puppet',
}
