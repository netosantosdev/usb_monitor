@echo off
setlocal

set PYTHON_EXE="C:\Python312\python.exe"

echo Instalando dependências...
%PYTHON_EXE% -m pip install --upgrade pip
%PYTHON_EXE% -m pip install psutil watchdog

where nssm >nul 2>&1
if errorlevel 1 (
    echo ERRO: nssm.exe não encontrado no PATH. Copie para C:\Windows\System32
    exit /b 1
)

if not exist "C:\ProgramData\USBMonitorService\" (
    mkdir "C:\ProgramData\USBMonitorService\"
    icacls "C:\ProgramData\USBMonitorService\" /grant "NT AUTHORITY\SYSTEM:(OI)(CI)(F)" /T
)

set SERVICE_NAME=USBMonitorService

nssm status %SERVICE_NAME% >nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando o servico %SERVICE_NAME%...
    nssm install %SERVICE_NAME% %PYTHON_EXE% "C:\usb_monitor_service\monitor.py"
    nssm set %SERVICE_NAME% AppDirectory "C:\usb_monitor_service"
    nssm set %SERVICE_NAME% AppStdout "C:\usb_monitor_service\service_output.log"
    nssm set %SERVICE_NAME% AppStderr "C:\usb_monitor_service\service_error.log"
) else (
    echo Servico %SERVICE_NAME% ja instalado.
)

echo Reiniciando o servico...
nssm restart %SERVICE_NAME%

echo Servico atualizado e reiniciado com sucesso.
endlocal