# fix it and then automate it using Puppet

exec { 'fix wordpress':
  command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  path      => '/usr/local/bin/:/bin/',
  provider => shell,
}
