$id=[System.Security.Principal.WindowsIdentity]::GetCurrent()
$principal=New-Object System.Security.Principal.WindowsPrincipal($id)
if(!$principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)) {
 $powershell=[System.Diagnostics.Process]::GetCurrentProcess()
 $psi=New-Object System.Diagnostics.ProcessStartInfo $powershell.Path
 $script=$MyInvocation.MyCommand.Path
 $prm=$script
 foreach($a in $args) {
  $prm+=' '+$a
 }
 $psi.Arguments=$prm
 $psi.Verb="runas"
 [System.Diagnostics.Process]::Start($psi) | Out-Null
 return;
}

# Trigger
$Trigger_Start = New-JobTrigger -AtStartup

# Options
$option1 = New-ScheduledJobOption –StartIfIdle

$scriptPath1 = 'C:\PySync_Win\GitUpdater.ps1'

Register-ScheduledJob -Name PySync_Updater -FilePath $scriptPath1 -Trigger  $Trigger_Start -ScheduledJobOption $option1


echo "Synchronisierung wurde abgeschlossen!"


pause