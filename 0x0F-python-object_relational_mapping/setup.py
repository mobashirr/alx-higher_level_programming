import subprocess
import sys

# run this script using:
# sudo python3 setup.py

def run_command(command, use_bash=False):
    """Run a shell command and wait for it to complete."""
    try:
        if use_bash:
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True, executable='/bin/bash')
        else:
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with exit status {e.returncode}")
        print(f"Error output: {e.stderr}")
        sys.exit(e.returncode)

def main():
    # Install and activate venv
    print("Installing and setting up virtual environment...")
    run_command("sudo apt-get update")
    run_command("sudo apt-get install -y python3.8-venv")
    run_command("python3 -m venv venv")

    print("Activating virtual environment and upgrading pip...")
    run_command("source venv/bin/activate && pip install --upgrade pip", use_bash=True)

    # Install MySQLdb module version 2.0.x
    print("Installing MySQLdb module version 2.0.x...")
    run_command("sudo apt-get install -y python3-dev")
    run_command("sudo apt-get install -y libmysqlclient-dev")
    run_command("sudo apt-get install -y zlib1g-dev")
    run_command("source venv/bin/activate && pip install mysqlclient", use_bash=True)

    # Verify MySQLdb installation
    print("Verifying MySQLdb installation...")
    run_command("source venv/bin/activate && python3 -c 'import MySQLdb; print(MySQLdb.version_info)'", use_bash=True)

    # Install SQLAlchemy module version 1.4.x
    print("Installing SQLAlchemy module version 1.4.x...")
    run_command("source venv/bin/activate && pip install SQLAlchemy==1.4.22", use_bash=True)

    # Verify SQLAlchemy installation
    print("Verifying SQLAlchemy installation...")
    run_command("source venv/bin/activate && python3 -c 'import sqlalchemy; print(sqlalchemy.__version__)'", use_bash=True)

    print("all set")
if __name__ == "__main__":
    main()
