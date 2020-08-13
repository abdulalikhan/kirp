from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
print('#    # # #####  #####')  
print('#   #  # #    # #    #') 
print('####   # #    # #    #') 
print('#  #   # #####  #####')  
print('#   #  # #   #  #')      
print('#    # # #    # #')
print("                 v1.2")
print('The Smart Whatsapp Marketing Bot')
print('Coded by Abdul Ali Khan')

# Launch the web driver and a Chrome window
# To hide all errors from the user, set log level to 3.
chrome_options = Options()
chrome_options.add_argument("log-level=3")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://web.whatsapp.com/')

# The name of the user or group to send messages to
name = input('Name of user/group: ')
# The message to be sent
msg = input('Message: ')
# The number of messages to send to the user/group
count = int(input('Number of messages: '))
# Error check 1
while (count<=0):
	print('Error: The number of messages to send cannot be a negative number or zero.')
	count = int(input('Number of messages: '))
# The number of minutes betweeen each message
interval_mins = int(input('Interval between messages (in minutes): '))
# Error check 2
while (interval_mins<0 or interval_mins>9999):
	print('Error: The interval must be an integer between 0 and 9999.')
	interval_mins = int(input('Interval between messages (in minutes): '))
# Scan the QR code before pressing any key.
input('Please scan the QR code and then hit enter.')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3uMse')
start_time = time.time()
done = False
i = 1
while done == False:
	current_time = time.time()
	elapsed = current_time - start_time
	while (i<=count) and (elapsed>=(interval_mins*60)):
		msg_box.send_keys(msg)
		button = driver.find_element_by_xpath("(//div[@class='_1JNuk'])[2]").click()
		try:
			button.click()
		except AttributeError as e:
			print('')
		print('{0} message(s) sent'.format(i))
		i = i + 1
		start_time = time.time()
		elapsed = 0
	if i>count:
		done = True
print('')
print('{0} message(s) were successfully sent to {1}.'.format(count, name))
