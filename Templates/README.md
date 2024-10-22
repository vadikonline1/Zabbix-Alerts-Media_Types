# Zabbix-Template-Settings

## Windows_Inventory_Settings
[Windows_Inventory_Settings](Windows_Inventory.yaml)

Administration_Macros:
- `{$SYSTEM.RUN.INSTALLEDAPPS}` : `$installedApps = foreach ($path in $paths) { Get-ItemProperty $path -ErrorAction SilentlyContinue | Where-Object { $_.DisplayName } | Select-Object DisplayName, InstallDate, DisplayVersion, Publisher, InstallLocation }`
- `{$SYSTEM.RUN.PATH}` : `"powershell.exe -Command \"if (Test-Path 'C:\\Program Files\\Zabbix Agent 2') { if (-Not (Test-Path 'C:\\Program Files\\Zabbix Agent 2\\system')) { New-Item -ItemType Directory -Path 'C:\\Program Files\\Zabbix Agent 2\\system'; 'C:\\Program Files\\Zabbix Agent 2\\system' } else { 'C:\\Program Files\\Zabbix Agent 2\\system' } } else { if (-Not (Test-Path 'C:\\Program Files\\Zabbix Agent\\system') ) { New-Item -ItemType Directory -Path 'C:\\Program Files\\Zabbix Agent\\system'; 'C:\\Program Files\\Zabbix Agent\\system' } else { 'C:\\Program Files\\Zabbix Agent\\system' } }\""`
- `{$SYSTEM.RUN.REGEDIT}` : `$paths = @('HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*','HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*')`
