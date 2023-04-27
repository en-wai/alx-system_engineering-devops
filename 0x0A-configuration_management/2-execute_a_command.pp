# Create a file to execute a command

exec { 'pkill':
  command  => 'pkill killmenow',
  path     => 'usr/bin',
  onlyif   => 'pgrep killmenow',
}
