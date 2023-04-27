# Create a file to execute a command

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
