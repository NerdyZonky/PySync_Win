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

Unregister-ScheduledJob PySync_Synchronize

pause