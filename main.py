import amino

comId = "xxxxxxxx"
email="xxxxxxxxxxxxx@gmail.com"
password="xxxxxxxxxxx"
client = amino.client.Client(certificatePath=None, socket_trace=True, socketDebugging=True)
client.login(email=email,password=password)
print('\n Login...')
subclient = amino.SubClient(comId=comId,profile=client.profile)
print('\n Joined in community...')

@client.event("on_text_message")
def on_text_message(data):
    #print(f"{data.message.author.nickname}: {data.message.content}")
