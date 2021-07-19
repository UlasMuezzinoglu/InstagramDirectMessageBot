# InstagramDirectMessageBot
İnstagram Direct Message Sender Bot Using Selenium &amp; WebDriver Pack

# Usage

First You install selenium
```bash
pip install selenium
```
and webDriver Pack

## Step 2:

Edit the Main.py file, type your Username, password and target username ,message and how many times to send the message.

```python
from instadm import InstaDM

if __name__ == '__main__':
	# Auto login
	insta = InstaDM(username='he.justulas (your id)', password='your_password', headless=False)
	
	# Send message


insta.sendMessage(user='target_user_id', message='Hey !',repeat=2)
#repeat is default 1 if you want change as param
```
HAVE FUN ! Configured by Ulaş Müezzinoğlu
