# this puppet script will fix the issue with of high number of opened files

exec {'replace-1':
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  provider => shell,
  before   => Exec['replace-2'],
}

exec {'replace-2':
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  provider => shell,
}
