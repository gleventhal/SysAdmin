# Test NginX Puppet Module
# This class installs NginX for Enterprise Linux 6
# Author: Gregg Leventhal 2014

class nginx {

  $dl_dir             = '/opt/downloads'
  $index_url          = 'https://github.com/puppetlabs/exercise-webpage.git'
  $pull_index_command = "git clone $index_url"
  $basic_path         = [
'/usr/local/bin', '/bin', '/usr/bin', '/usr/local/sbin', '/usr/sbin', '/sbin', '/usr/local/share'
  ]
  $document_root      = '/usr/share/nginx/html/'
  $epel               = 'epel-release-6-8.noarch'
  $epel_rpm           = "${epel}.rpm"
  $epel_url           = "http://dl.fedoraproject.org/pub/epel/6/x86_64/$epel_rpm"
  $wget_epel          = "wget $epel_url"
  $epel_install       = "rpm -Uvh $epel_rpm"


  file { "$dl_dir":
    ensure => 'directory',
    owner  => 'root',
    group  => 'root',
    mode   => '0755',
  }
  
  exec { "$wget_epel":
    path   => $basic_path,
    unless => "test $(rpm -q ${epel} &>/dev/null)$? -eq 0",
    cwd    => $dl_dir
  }
  
  exec { "$epel_install":
    path   => $basic_path,
    unless => "test $(rpm -q ${epel} &>/dev/null)$? -eq 0",
    cwd    => $dl_dir
  }

  package { 'nginx':
    ensure => installed
  }

  exec { "$pull_index_command":
    path    => $basic_path,
    creates => "${document_root}/exercise-webpage",
    cwd     => $document_root,
  }

  service { 'nginx':
    ensure => 'running'
  }
  
File["$dl_dir"] -> Exec["$wget_epel"] -> Exec["$epel_install"] -> Package['nginx'] -> Exec["$pull_index_command"] -> Service['nginx']
}

include nginx
