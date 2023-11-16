# web debug 4

exec { 'debug4':
  command  => 'sudo apt-get purge nginx nginx-common nginx-full -y; sudo apt-get install nginx -y; sudo service nginx restart',
  provider => shell,
  path     => '/usr/bin',
}
