# Create a file to execute a command

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => 'usr/bin',
  onlyif  => 'pgrep killmenow',
}
