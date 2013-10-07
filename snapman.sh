#!/bin/bash
###############################
#       Snapshot Manager v1.0 #
#       By Gregg Leventhal    #
###############################
#
# Creates a simple management interface for the Linux Logical Volume Manager (LVM)
# For the purpose of managing and creating Logical Volume Snapshots of KVM Virtual Disk formats living on a LVM2 logical Volume
# This assumes 3 KVM domains named vm1, vm2, and vm3, each living on an LVM logical volume under /opt/virt/img/<vmname>, all within the volume group vg1
# If you are restoring a snapshot, shutdown the VM/domain first or you will have problems!
# Example Usage: snapman.sh list


DATE=$(date +%H-%M-%m-%d-%y)
PATH_VM1=vm1
PATH_VM2=vm2
PATH_VM3=vm3
FREE_SPACE=$(vgs vg1|awk '$7 ~ /[0-9].*/ {print $7}')

usage()
{
cat << EOF

`basename $0` <create|restore|list>


EOF
exit 1

}

if [[ $1 =~ ^-[a-z]$ ]]; then
  shift
fi


create_snap()
{
echo "Which VM do you want to SnapShot?"
echo "(1) VM1"
echo "(2) VM2"
echo "(3) VM3"
echo ""
echo "Choose a number 1-3 or q to quit:"
read CREATE_CHOICE
case $CREATE_CHOICE in
        1)
          NAME=lv_vm1 ;;
        2)
          NAME=lv_vm2 ;;
        3)
          NAME=lv_vm3 ;;
        q)
          exit 1 ;;
        *)
          usage ;;
esac
[ ${FREE_SPACE/\.*} -lt 55 ] && echo "There is not enough free space to create a snapshot
Please Run \"./snapman.sh delete\" to delete an uneeded snapshot" && exit 1

lvcreate -L 50G -n ${NAME}_snap_${DATE} -s /dev/vg1/${NAME}
}

list_snap()
{
if [ "$1" = "restore" ];
then
CURR_SNAPS=(
`/sbin/lvdisplay|grep -B4 'active destination for'|sed -n '1~6p'|awk '{print $3}'`
)
LEN=${#CURR_SNAPS[*]}
echo "Current Snapshots:  Choose one to restore[0-$((LEN -1))] (q to quit)"
i=0
while [ $i -lt $LEN ]; do
  echo $i: ${CURR_SNAPS[$i]}
  let i++
done
read NUM
if [ "$NUM" = "q" ]; then exit 1; fi
  echo restoring ${CURR_SNAPS[$NUM]}
  echo ${CURR_SNAPS[$NUM]} |grep vm1 && VM=vm1 && IMGPATH=$PATH_VM1 2>/dev/null
  echo ${CURR_SNAPS[$NUM]} |grep vm2 && VM=vm2 && IMGPATH=$PATH_VM2 2>/dev/null
  echo ${CURR_SNAPS[$NUM]} |grep vm3 && VM=vm3 && IMGPATH=$PATH_VM3 2>/dev/null
  virsh list |grep $VM 2>/dev/null && virsh shutdown $VM
  echo $VM should be shut down now...
  #If Shutdown command fails, forcefully halt machine..
  virsh list |grep $VM 2>/dev/null && virsh destroy $VM
  umount /opt/virt/img/${IMGPATH}
  lvconvert --merge ${CURR_SNAPS[$NUM]}
  mount /opt/virt/img/${IMGPATH}
  ls /opt/virt/img/${IMGPATH} && virsh start $VM
else
  /sbin/lvdisplay|grep -B4 'active destination for'|sed -n '1~6p'|awk '{print $3}'
fi
}

delete_snap()
{
CURR_SNAPS=(
`/sbin/lvdisplay|grep -B4 'active destination for'|sed -n '1~6p'|awk '{print $3}'`
)
LEN=${#CURR_SNAPS[*]}
echo "Current Snapshots:  Choose one to delete[0-$((LEN -1))] (q to quit)"
i=0
while [ $i -lt $LEN ]; do
  echo $i: ${CURR_SNAPS[$i]}
  let i++
done
read NUM
if [ "$NUM" = "q" ]; then exit 1; fi
lvremove ${CURR_SNAPS[$NUM]}
}


if [ $# -lt 1 ]; then
        usage

elif [ "$1" = "create" ];then
        create_snap

elif [ "$1" = "restore" ]; then
        list_snap restore

elif [ "$1" = "list" ]; then
        list_snap

elif [ "$1" = "delete" ]; then
        delete_snap
else
        usage
fi


