# Using Puppet, install flask from pip3

exec { 'puppet-lint':
	command => 'pip3 install flask flask_restful apiai',
	path => ['/usr/bin/'],
}
