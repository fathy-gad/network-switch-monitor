📡 Network Switch Monitor

A simple Python-based tool to monitor network switch availability using ICMP (ping).

✨ Features
Reads switches from a configuration file
Performs automatic ping checks
Displays real-time status (UP / DOWN)
Lightweight and easy to run
Helps in quick network troubleshooting
📁 Configuration

Create a switches.txt file in the following format:

Switch-1,192.168.1.1
Switch-2,192.168.1.2
DataCenter-Switch,192.168.1.10

Each line should contain:

Switch Name,IP Address
▶️ Usage

Run the script:

python check_switches.py
📊 Example Output
Switch-1 (192.168.1.1) is UP
Switch-2 (192.168.1.2) is DOWN
⚙️ Requirements
Python 3.x

🚀 Future Improvements
Add logging
Export results to CSV
Send alerts (Email / Telegram)
Build GUI dashboard

*comm*
python check_switches.py

👨‍💻 Author
Fathy Gad — IT Engineer
