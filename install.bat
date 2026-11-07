@ cls 
@ color 3 
@ color 
echo Uninstall apysc... 
python -m pip uninstall apysc -y
echo Install apysc... 
python -m pip install -e .
@ color 3 
echo apycs sucefull installed!
@ color 