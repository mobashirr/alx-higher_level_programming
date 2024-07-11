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

    # Check if MySQL is already installed
    print("Checking if MySQL is already installed...")
    try:
        run_command("mysql --version")
        print("MySQL is already installed. Exiting...")
        sys.exit(0)
    except subprocess.CalledProcessError:
        print("MySQL is not installed. Proceeding with installation...")

    # Update the package list
    print("Updating package list...")
    run_command("sudo apt-get update")

    # Install necessary dependencies
    print("Installing dependencies...")
    run_command("sudo apt-get install -y wget lsb-release gnupg")

    # Add the MySQL APT repository if not already added
    config_package = "mysql-apt-config_0.8.23-1_all.deb"
    if not os.path.exists(config_package):
        print("Adding MySQL APT repository...")
        run_command(f"wget https://dev.mysql.com/get/{config_package}")
        run_command(f"sudo dpkg -i {config_package}")
    else:
        print("MySQL APT repository configuration package already exists. Skipping download...")

    # Update the package list again
    print("Updating package list again...")
    run_command("sudo apt-get update")

    # Install MySQL server
    print("Installing MySQL server...")
    run_command("sudo apt-get install -y mysql-server")

    # Start MySQL service
    print("Starting MySQL service...")
    run_command("sudo systemctl start mysql")

    # Enable MySQL to start on boot
    print("Enabling MySQL to start on boot...")
    run_command("sudo systemctl enable mysql")

    # Secure MySQL installation
    print("Securing MySQL installation...")
    run_command("sudo mysql_secure_installation", use_bash=True)

    # Verify MySQL installation
    print("Verifying MySQL installation...")
    run_command("mysql --version")

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
