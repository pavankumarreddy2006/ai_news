Write-Host "Running backend tests..."
pytest backend/tests -q
Write-Host "Running frontend tests..."
Set-Location frontend
npm.cmd run test

