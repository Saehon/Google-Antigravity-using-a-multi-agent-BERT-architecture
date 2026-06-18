$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

$venvPath = Join-Path $root ".venv"
if (-not (Test-Path $venvPath)) {
    Write-Host "Creating virtual environment..."
    python -m venv $venvPath
}

$python = Join-Path $venvPath "Scripts\python.exe"
if (-not (Test-Path $python)) {
    throw "Python executable not found in .venv. Ensure Python is installed and accessible from PATH."
}

Write-Host "Installing dependencies..."
& $python -m pip install --upgrade pip
& $python -m pip install -r "$(Join-Path $root 'requirements.txt')"

Write-Host "Running the multi-agent accounting runner..."
& $python "$(Join-Path $root 'multi_agent_accounting_ai_runner.py')"

Write-Host "`nDeployment complete. Output files are available in the data folder."
