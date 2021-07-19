from instadm import InstaDM

if __name__ == '__main__':
	# Auto login
	insta = InstaDM(username='he.justulas (your id)', password='your_password', headless=False)
	
	# Send message


insta.sendMessage(user='target_user_id', message='Hey !',repeat=2)
#repeat is default 1 if you want change as param
    
