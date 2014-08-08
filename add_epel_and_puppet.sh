#!/bin/bash

echo "Installing EPEL Repo and Puppet client"

if [[ $(lsb_release -d) =~ 'Red Hat Enterprise Linux Server release 5' ]]; then
        wget http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm
        rpm -Uvh epel-release-5*.rpm
elif [[  $(lsb_release -d) =~ 'Red Hat Enterprise Linux Server release 6' ]]; then
        wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
        rpm -Uvh epel-release-6*.rpm
else
        echo "This is not RHEL 5 or 6; Exiting.."
        exit1
fi

yum -y install puppet
