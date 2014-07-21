# Class: duo-win
#
# Gregg Leventhal 
#

class duo-win (
  $ikey         = 'Your ikey Here',
  $skey         = 'Your skey Here',
  $host         = 'Your host API here',
  $install_path = ['C:/Puppet', 'C:/Puppet/Duo' ],
  $install_dir  = 'C:/Puppet/Duo',
){

  if $::kernel != 'windows' {
    fail('This module is designed to run on Windows')
  }

    if $::architecture == 'x86' {
      case $::kernelmajversion {
        /(?i-mx:^5)/ : {
          $duo_package = 'duo-gina-latest-win32.msi'
        }
        /(?i-mx:^6)/ : {
          $duo_package = 'duo-credprov-latest-win32.msi'
        }
        default:       {
          fail("Unknown Kernel Version ${::kernelmajversion}")
        }
      }
    } elsif $::architecture == 'x86_64' or $::architecture == 'x64' {
      case $::kernelmajversion {
        /(?i-mx:^5)/ : {
          $duo_package = 'duo-gina-latest-x64.msi'
        }
        /(?i-mx:^6)/ : {
          $duo_package = 'duo-credprov-latest-x64.msi'
        }
        default:       {
          fail("Unknown Kernel Version ${::kernelmajversion}")
        }
      }

    file { $install_path:
      ensure => 'directory',
      mode   => '0777',
      group  => 'Administrators',
      before => [
        File["${install_dir}/${duo_package}"]
      ]
    }

    file { "${install_dir}/${duo_package}":
      ensure => present,
      source => "puppet:///modules/duo-win/${duo_package}",
      mode   => '0777',
    }

    file { "${install_dir}/install.bat":
      ensure  => present,
      content => template('duo-win/install.bat.erb'),
      mode    => '0777',
      require => [
        File["${install_dir}/${duo_package}"]
      ]
    }

    exec { "${install_dir}/install.bat":
      command => "${install_dir}/install.bat",
      require => [
        File["${install_dir}/install.bat"]
      ]
    }
  } else { fail('Unknown architecture or OS version') }
}