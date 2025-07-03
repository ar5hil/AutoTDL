# main.py
import os

os.system("curl -sSL https://docs.iyear.me/tdl/install.sh | sudo bash")
os.system("tdl login -T qr")
os.system("tdl extension install iyear/tdl-whoami")
os.system("tdl whoami")
os.system("tdl chat export -c 2138555103 --all")
os.system("tdl forward --from tdl-export.json --to 2592163268 --silent --desc --mode clone")
os.system("curl -d 'Transfer Success to BAMSA successful 😀' ntfy.sh/marrow6991")
os.system("date")
