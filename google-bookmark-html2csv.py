import pandas as pd
import subprocess
import pychrome
import json

#Html path that read GoogleBookMark
_url = "file:///C:/Users/USER/Documents/bookmarks_2020_01_15.html"

subprocess.run('start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --headless --disable-gpu --remote-debugging-port=9222', shell=True)
browser = pychrome.Browser(url="http://127.0.0.1:9222")
tab = browser.new_tab()
tab.start()
tab.Network.enable()
tab.Page.navigate(url=_url, _timeout=60)
tab.wait(60)
result = tab.Runtime.evaluate(expression="""JSON.stringify([...document.links].map(e => e.href))""")
a = json.loads(result["result"]["value"])
w = pd.DataFrame(a)
w.to_csv("test.csv", index=False, encoding="utf-8")
browser.close_tab(tab)
