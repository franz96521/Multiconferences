Param(
    [bool]$zoom=$false,
    [bool]$telmex=$false
)
if ($zoom) {    
    $zoomURL = "https://zoom.us/client/latest/ZoomInstaller.exe?archType=x64"
    Invoke-WebRequest $zoomURL -OutFile "zoom.exe"
    Start-Process -Wait -FilePath "zoom.exe" -Argument "/silent" -PassThru
}

if ($telmex) {
    $telmexURL = "https://videoconferencia.telmex.com/client/latest/VideoconferenciaTelmex.exe"
    Invoke-WebRequest $telmexURL -OutFile "telmex.exe"
    Start-Process -Wait -FilePath "telmex.exe" -Argument "/silent" -PassThru    
}