#      _                   _     _      _
#     | |_   _ _ __   __ _(_) __| |    / \   _ __  _ __  ___ 
#  _  | | | | | '_ \ / _` | |/ _` |   / _ \ | '_ \| '_ \/ __|
# | |_| | |_| | | | | (_| | | (_| |  / ___ \| |_) | |_) \__ \
#  \___/ \__,_|_| |_|\__,_|_|\__,_| /_/   \_\ .__/| .__/|___/
#                                           |_|   |_|
# By Junaid

clear

python logo.py

echo
echo "Installing Dependencies of this game ..."
echo

# Dependencies
pip install pyfiglet
pip install simple_chalk
pip install inquirer
pip install tqdm


echo
echo "Dependencies are installed."
echo "You are ready to GO!"
echo

# deleting installation files 
rm -rf logo.py
rm -rf install.sh

yellow='\033[33m'
NC='\033[0m' # No Color
echo -e "${yellow}Default : This Game will works best in VS code terminal.${NC}"
echo "To start game type : (In VS code terminal only)"
echo "___________________________________"
echo
echo "==> python atm.py"
echo "___________________________________"