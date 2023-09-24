# execute a command only if a condition is true

exec { 'kill-killmenow-process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
}
