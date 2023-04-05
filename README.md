![image](https://user-images.githubusercontent.com/101802030/229880570-edc35d5f-addc-438d-9a0a-a825150f24d4.png)


# securemessh
This is a python application that can be used to send a multilined message that looks like an e-mail via ssh.

## How to:
- run : `nc -l -p 443 -k` in your terminal to start a listener. This method is recommended for receiving e-mail style messages.
- run : `securemessh.py` and follow the prompts. You will be required to provide the hostname where the ssh service is running on, as well as the username and password
- input : At initial start-up, the application will prompt you to select a text-editor. You have a choice between nano and vim. Once selected, can you then enter your multiline message to be sent.

## Windows Installer
- The Windows installer provides the ability to run the application on a Windows device. If you would like a chat-style experience, it recommended to use the listener along with the Windows application.

## Multi-threaded server output(as it is received. Tons of messages can now be sent securely). See screenshot :

![image](https://user-images.githubusercontent.com/101802030/229977759-e0223fe0-15de-4aaa-9916-a45eb626fe14.png)
