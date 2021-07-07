import webbrowser

chrome ="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

webbrowser.get(chrome).open_new("google.com")
webbrowser.get(chrome).open_new("bing.com")

