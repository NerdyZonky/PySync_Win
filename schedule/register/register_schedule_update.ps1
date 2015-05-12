# Trigger
$Trigger_Start = New-JobTrigger -AtStartup

# Options
$option1 = New-ScheduledJobOption –StartIfIdle

$scriptPath1 = 'C:\PySync_Win\GitUpdater.ps1'

Register-ScheduledJob -Name PySync_Updater -FilePath $scriptPath1 -Trigger  $Trigger_Start -ScheduledJobOption $option1


echo "Synchronisierung wurde abgeschlossen!"


pause