#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cat <<EOF > /etc/systemd/system/monitor-agent.service
[Unit]
Description=AI Monitor Agent
[Service]
ExecStart=$(pwd)/venv/bin/python $(pwd)/monitor.py
Restart=always
[Install]
WantedBy=multi-user.target
EOF
systemctl enable --now monitor-agent