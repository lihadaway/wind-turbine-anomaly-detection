# Activate the virtual environment
source venv/bin/activate

# Create a directory named 'plots' if it doesn't already exist
mkdir -p plots

# Loop through each Python script in the 'scripts' directory
for script in scripts/*.py; do
  # Print the name of the script being run
  echo "Running $script"
  
  # Execute the script using Python 3
  python3 "$script"
  
  # Print a newline after each script execution
  echo "\n"
done

# Deactivate the virtual environment
deactivate
