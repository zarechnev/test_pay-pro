###### Cloning ans install
```
git clone git@github.com:zarechnev/test_pay-pro.git
cd ./test_pay-pro
python3 -m venv ./venv
./venv/bin/pip install -r ./requires.txt
```

###### Make config file for connect to DB
```
echo "connect_string = \"mysql+pymysql://<db_user>:<db_pass>@<db_server>/<db_name>\"" > ./app/db_connect_conf.py
vim ./app/db_connect_conf.py
```

###### Use
```
./venv/bin/python3 ./main.py [-s, --start <start date in "dd.mm.yyyy"-format>]  [-e, --end <end date in "dd.mm.yyyy"-format>]
```
