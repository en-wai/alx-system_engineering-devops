# Create a manifest to install specific packages.

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
