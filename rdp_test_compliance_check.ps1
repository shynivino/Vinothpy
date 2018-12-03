<#
<synopsis>

To check if the RDP status by fetching its value from windows registery and based on the values we will tell if the system is compliant or not.

#>

#Variables
$TSRegPath = "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server"
$TSRegProperty = "fDenyTSConnections"
$RDPTcpRegPath = "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp"
$RDPTcpRegProperty = "UserAuthentication"
 
#Set initial values
$TSSet = $True
$RDPTCPSet = $True

#Test fDenyTSConnections state
$TSReturn = (Get-ItemProperty -Path $TSRegPath -Name $TSRegProperty -ErrorAction SilentlyContinue).fDenyTSConnections
If ($TSReturn -eq 1) {
    $TSSet = $false
}
 
#Test RDP-TCP State
$RDPTCPReturn = (Get-ItemProperty -Path $RDPTcpRegPath -Name $RDPTcpRegProperty -ErrorAction SilentlyContinue).UserAuthentication
If ($RDPTCPReturn -eq 0) {
    $RDPTCPSet = $false
}

If (!($TSSet) -and ($RDPTCPSet)) {
    Write-Host "Compliant!"

} 

else {

       Write-Host "Not Compliant!"
 }

