$OutPath = "C:\Users\thiba\Desktop\Memoire\Memoire\assets"

Copy-Item -Path ".\generated\figures\*" -Destination $OutPath -Recurse -Force
Set-Location -Path $OutPath
git add .
