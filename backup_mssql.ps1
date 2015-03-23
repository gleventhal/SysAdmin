# Backup MSI DB #
#               #
# A Powershell  #
# script        #
#################
#load SQL snap-in
Add-PSSnapin *SQL*

$HOSTNAME=hostname
#pull the current date
$date = Get-Date -Format yyyyddMM

#set location of backup files and create it if not present
$directory = "D:\Temp\"
if (-Not (Test-Path $DIRECTORY) ) { md $directory }

#Grab the database names into an array
$dbname = dir "SQLSERVER:\SQL\$HOSTNAME\Default\Databases" | Select Name

#Backup each database found which matches the regex "stats". Change stats to a unique value matching your DB, or remove "where { $_ -match "stats" } |" to backup all.
$dbname | foreach { $_.Name.ToString() }|where { $_ -match "stats" } | foreach {$bakfile = "$directory" + $_ + "_" + $date + ".bak";
"Backing up Database: $_"; Invoke-Sqlcmd -QueryTimeout 10000 -SuppressProviderContextWarning -Query "BACKUP DATABASE $_ TO DISK=N'$bakfile' WITH INIT";}

# Move Backup from local disk to CIFS mount
Move-Item D:\Temp\*.bak Z:\backups
cd Z:\backups

#Get array of existing Backups
$backups=ls Z:\backups\*.bak|sort-object -property CreationTime -descending|foreach { $_.Name }

#Delete Anything Beyond 3 Newest Backups
if ($backups.Length -gt 3 ) {
    foreach ($_ in $backups[3..$backups.Length]) { Remove-Item $_ }
}
