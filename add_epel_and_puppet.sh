#!/bin/bash

[[ -z "$1" ]] && puppetmaster='default_puppetmaster' || puppetmaster="$1"
epel=$(yum repolist|egrep -q '^epel')$?
mailto=puppet_admin@foo.bar
function install_epel()
{
echo "Installing EPEL Repo and Puppet client"

if [[ $(lsb_release -d) =~ 'Red Hat Enterprise Linux Server release 5' ]]; then
        wget http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm
        rpm -Uvh epel-release-5*.rpm
elif [[  $(lsb_release -d) =~ 'Red Hat Enterprise Linux Server release 6' ]]; then
        wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
        rpm -Uvh epel-release-6*.rpm
else
        echo "This is not RHEL 5 or 6; Exiting.."
        exit 1
fi
}

function config_puppet()
{
  yum -y install puppet
  chkconfig puppet on
  sed -i "12 a\    server = $puppetmaster" /etc/puppet/puppet.conf
  echo signme|mail -s "$(hostname) is waiting to be signed on puppet master" $mailto
  puppet agent --test --waitforcert 5
  service puppet start
}

if ! [[ epel -eq 0 ]]; then
  install_epel
fi

config_puppet
