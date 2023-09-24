#using puppet to set up my client config file
include stdlib

file_line { 'Turn off passwd auth':
  ensure => present,
  replace => true,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'Delare identity file':
  ensure => present,
  line   => '     IdentityFile ~/.ssh/school',
  replace => true,
  path   => '/etc/ssh/ssh_config',
}
