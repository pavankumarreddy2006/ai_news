$paths = @("frontend\\dist", "backend\\__pycache__", "backend\\app\\__pycache__")
foreach ($path in $paths) {
  if (Test-Path $path) {
    Remove-Item -LiteralPath $path -Recurse -Force
  }
}
Write-Host "Artifacts cleaned."

