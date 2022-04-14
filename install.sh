clear

echo "Hello $(whoami)"
echo
sleep 1

echo "sudo apt update"
sudo apt update
echo
sleep 1

echo "apt list --upgradable"
apt list --upgradable
echo
sleep 1

echo "sudo apt install python3 -y"
sudo apt install python3 -y
echo
sleep 1

echo "sudo apt install python3-colorama -y"
sudo apt install python3-colorama -y
echo
sleep 1

echo "sudo apt install python3-isort -y"
sudo apt install python3-isort -y
echo
sleep 1

echo "sudo apt install python3-pyfiglet -y"
sudo apt install python3-pyfiglet -y
echo
sleep 1

echo "sudo apt install python3-requests -y"
sudo apt install python3-requests -y
echo
sleep 1

echo "sudo apt install python3-tk -y"
sudo apt install python3-tk -y
echo
sleep 1

echo "sudo apt install python3-pip -y"
sudo apt install python3-pip -y
echo
sleep 1

echo "sudo apt install libnotify-bin -y"
sudo apt install libnotify-bin -y  # Thanks to https://command-not-found.com
echo
sleep 1

echo "sudo apt autoremove -y"
sudo apt autoremove -y
echo
sleep 1

echo "python3 -m pip instal -r ./requirements.txt"
python3 -m pip install -r ./requirements.txt
echo
sleep 1

echo "Hello $(whoami)"
echo "Welcome to"
python3 -m pyfiglet "Remote Keylogger"
echo "Remote Keylogger (Reborn)"
echo "Created by JahidFariz. Made with Love in India."
echo
sleep 1

pyinstaller __main__.py -F --add-data "fonts/*:pyfiglet/fonts/" --add-data "assets/*:assets/" -n="rkl" -i="logo.ico" -y
echo
sleep 1

echo "sudo rm -fv ./rkl.spec"
sudo rm -fv ./rkl.spec
echo
sleep 1

echo "sudo rm -rv ./__pycache__"
sudo rm -rv ./__pycache__
echo
sleep 1

echo "sudo rm -rv ./build"
sudo rm -rv ./build
echo
sleep 1

echo "chmod +x ./dist/rkl"
chmod +x ./dist/rkl
echo
sleep 1

echo "sudo cp -fv ./dist/rkl /usr/bin/"
sudo cp -f -v ./dist/rkl /usr/bin/
echo
sleep 1

echo "rkl -h"
rkl -h
echo
sleep 1

exit
