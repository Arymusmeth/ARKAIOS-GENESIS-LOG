
@echo off
icacls "C:\ARKAIOS" /deny "Authenticated Users":(W,M)
echo Permisos actualizados. Protegido contra escritura/modificación.
pause
