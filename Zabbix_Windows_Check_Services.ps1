# Check the status of the Zabbix Agent service
try {
    $zabbixAgentService = Get-Service -Name "Zabbix Agent" -ErrorAction Stop
    Write-Host "Status of 'Zabbix Agent' service: $($zabbixAgentService.Status)"
} catch {
    Write-Host "'Zabbix Agent' service not found."
}

# Check the status of the Zabbix Agent 2 service
try {
    $zabbixAgent2Service = Get-Service -Name "Zabbix Agent 2" -ErrorAction Stop
    Write-Host "Status of 'Zabbix Agent 2' service: $($zabbixAgent2Service.Status)"
} catch {
    Write-Host "'Zabbix Agent 2' service not found."
    $zabbixAgent2Service = $null  # Set to null for later checks
}

# Check the status of both services
if ($zabbixAgentService -and $zabbixAgent2Service) {
    if ($zabbixAgentService.Status -eq 'Running' -or $zabbixAgent2Service.Status -eq 'Running') {
        Write-Host "At least one service is running. Exiting."
        exit
    } elseif ($zabbixAgentService.Status -eq 'Stopped' -and $zabbixAgent2Service.Status -eq 'Stopped') {
        Write-Host "Both services are stopped. Checking log files."
        $logFile1 = "C:\Program Files\Zabbix Agent\zabbix_agentd.log"
        $logFile2 = "C:\Program Files\Zabbix Agent 2\zabbix_agent2.log"

        $logFiles = @()
        if (Test-Path $logFile1) {
            $logFiles += Get-Item $logFile1
        }
        if (Test-Path $logFile2) {
            $logFiles += Get-Item $logFile2
        }

        if ($logFiles.Count -gt 0) {
            $mostRecentLog = $logFiles | Sort-Object LastWriteTime -Descending | Select-Object -First 1
            Write-Host "Most recent log file: $($mostRecentLog.FullName)"

            # Start the corresponding service based on the most recent log
            if ($mostRecentLog.FullName -eq $logFile1) {
                Start-Service -Name "Zabbix Agent"
                Write-Host "'Zabbix Agent' service has been started."
            } elseif ($mostRecentLog.FullName -eq $logFile2) {
                Start-Service -Name "Zabbix Agent 2"
                Write-Host "'Zabbix Agent 2' service has been started."
            }
        } else {
            Write-Host "No log files found to check for recent changes."
        }
    }
} elseif ($zabbixAgentService -and $zabbixAgent2Service -eq $null) {
    # If Zabbix Agent 2 does not exist, but Zabbix Agent is stopped, start it
    if ($zabbixAgentService.Status -eq 'Stopped') {
        Write-Host "'Zabbix Agent' service is stopped. Starting it now."
        Start-Service -Name "Zabbix Agent"
        Write-Host "'Zabbix Agent' service has been started."
    }
}
