Param(
    [string[]]$URLS
)
$zoomOriginalPath="$env:APPDATA\Zoom\bin\Zoom.exe"
$zoomInstall =[System.IO.File]::Exists($zoomOriginalPath)
$zoomInstall
$telmexOriginalPath="$env:APPDATA\Videoconferencia Telmex\bin\VideoconferenciaTelmex.exe" 
$telmexInstall =[System.IO.File]::Exists($telmexOriginalPath)
$index = 0;
$URLS | ForEach-Object -Process {
    if ($_ -match 'zoom' ) {
        if( "False" -eq $zoomInstall){
            ./CheckExisting.ps1 -zoom $true
            $zoomInstall="True"
        }
        $Zoompath = "$env:APPDATA\Zoom\bin\zoom$($index).exe"
        Copy-Item -Path $zoomOriginalPath -Destination $Zoompath
        Start-Process  $Zoompath --url=$_        
    }  elseif ($_ -match 'telmex' ) {
        if("False" -eq $telmexInstall){
            ./CheckExisting.ps1 -telmex $true
            $telmexInstall="True"
        }
        $TelmexPath = "$env:APPDATA\Videoconferencia Telmex\bin\VideoconferenciaTelmex$($index).exe"
        Copy-Item -Path $telmexOriginalPath -Destination $TelmexPath
        Start-Process  $TelmexPath --url=$_ 
    }
    else {
        Write-Output "no conocido $($_)"
    }
    $index++
}
