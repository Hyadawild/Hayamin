echo >/dev/null # >nul & GOTO WINDOWS & rem ^

################################################################################
# Unix Main Codes                                                              #
################################################################################
repo="$(command -v $0)"
repo="${repo%%start.cmd}"
"${repo}/init/unix.sh" "$@"
################################################################################
# Unix Main Codes                                                              #
################################################################################
exit $?




:WINDOWS
::##############################################################################
:: Windows Main Codes                                                          #
::##############################################################################
@echo off
setlocal EnableDelayedExpansion
IF "%*"=="" ( goto :empty )
set location=%~dp0init\windows.ps1
set location="%location%"
set _parameters=%*
set _parameters=!_parameters:--=-!
set _parameters=!_parameters:input=path!
set _parameters=!_parameters:"=\"!
call Powershell.exe -NoProfile -executionpolicy bypass -Command "& '%location%' %_parameters%"
EXIT /B

:empty
set location=%~dp0init\windows.ps1
set location="%location%"
call Powershell.exe -NoProfile -executionpolicy bypass -Command "& '%location%'"
::##############################################################################
:: Windows Main Codes                                                          #
::##############################################################################
