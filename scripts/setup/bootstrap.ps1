Write-Host "Installing backend dependencies..."
python -m pip install -r backend\requirements.txt
Write-Host "Installing frontend dependencies..."
Set-Location frontend
npm.cmd install

