# SuperWebClient
A Python WebClient.  
It can request POST or GET method and <b>keep cookie exist</b>.  
If you want to request some url and need to login auth,you will use it.

## Support
python 2.7

## Installation
pip install requests

## USEAGE
<pre>
from SuperWebClient import SuperWebClient 
#init
client = SuperWebClient()

#Set Header

client.setHeader('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
client.setHeader('Referer','http://<b>{YOUR_URL}</b>/')

#POST

data = {'user_login': '123', 'user_pass': '123'}
rs = client.UploadValues('http://<b>{YOUR_URL}</b>',data)
print rs

#GET
rs = client.DownloadString('http://<b>{YOUR_URL}</b>/')
print rs

client.clean()
</pre>

## License

SuperWebClient is licensed under The MIT License (MIT).
