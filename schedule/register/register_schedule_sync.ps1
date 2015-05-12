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
$Trigger1 = New-JobTrigger -Daily -At "00:00 AM"
$Trigger2 = New-JobTrigger -Daily -At "04:00 AM"
$Trigger3 = New-JobTrigger -Daily -At "08:00 AM"
$Trigger4 = New-JobTrigger -Daily -At "12:00 PM"
$Trigger5 = New-JobTrigger -Daily -At "04:00 PM"
$Trigger6 = New-JobTrigger -Daily -At "08:00 PM"
  
#$atStartupeveryFiveMinutesTrigger = New-JobTrigger -once -At $(get-date) -RepetitionInterval $([timespan]::FromMinutes("1")) -RepeatIndefinitely

# Options
$option1 = New-ScheduledJobOption –StartIfIdle

$scriptPath1 = 'C:\PySync_Win\PySync_Launcher.ps1'

Register-ScheduledJob -Name PySync_Launch -FilePath $scriptPath1 -Trigger  $Trigger_Start,$Trigger1,$Trigger2,$Trigger3,$Trigger4,$Trigger5,$Trigger6 -ScheduledJobOption $option1
#Register-ScheduledJob -Name Hallo_Welt2 -FilePath $scriptPath2 -Trigger $atStartupeveryFiveMinutesTrigger


pause