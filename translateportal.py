import discord, deepl, requests, json

with open('./config.cfg') as f:
    config = json.load(f)

client = discord.Client()
dlauth = config["deepl_auth_key"]
tl = deepl.Translator(dlauth)

channel_en_id = config["channel_en_id"]
channel_cn_id = config["channel_cn_id"]


@client.event
async def on_ready():
   
    
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    channel_cn = client.get_channel(channel_cn_id)
    channel_en = client.get_channel(channel_en_id)
    msgfiles = [await atch.to_file() for atch in message.attachments]
    md = ''
    msgcontent = message.clean_content

    if msgcontent.startswith('~~') and msgcontent.endswith('~~'):
        md = '~~'
        msgcontent = msgcontent[2:-2]
    elif msgcontent.startswith('**') and msgcontent.endswith('**'):
        md = '**'
        msgcontent = msgcontent[2:-2]
    elif msgcontent.startswith('*') and msgcontent.endswith('*'):
        md = '*'
        msgcontent = msgcontent[1:-1]
    elif msgcontent.startswith('||') and msgcontent.endswith('||'):
        md = '||'
        msgcontent = msgcontent[2:-2]
    

    if (message.author == client.user) or message.author.bot:
        return

    if message.content.startswith('$bing'):
        print(message.channel)
        await message.channel.send('bong')
        
        #chinese channel input
    if message.channel.id == channel_cn_id:
        tlmessage = md + await gettl(msgcontent, "EN-GB") + md
        await pretend(channel_en, message.author, tlmessage, files=msgfiles)
        
        #english input
    if message.channel.id == channel_en_id:
        tlmessage = md + await gettl(msgcontent, "ZH") + md
        await pretend(channel_cn, message.author, tlmessage, files=msgfiles)
        
    # maybe set up some key:value pair with inputchannel and outputsettings? i do later
        
async def gettl(message=None, target_lang="EN-GB", httpmode = True):
    if httpmode:
        url = 'https://api-free.deepl.com/v2/translate'
        data = {
            'auth_key' : dlauth,
            'text' : message,
            'target_lang' : target_lang
        }
        r = requests.post(url, data=data)
        return r.json()["translations"][0]["text"]

async def pretend(tchannel, member: discord.Member, message=None, files=None):

        if message == None:
                print('attempted to send message with None ' + 'in ' + tchannel.name)
                return
        
        webhooks = await tchannel.webhooks()
        for webhook in webhooks:
            print(webhook.name + ' ' + tchannel.name)
            if webhook.name == 'NThook':
                await webhook.send(
                    str(message), username=member.display_name, avatar_url=member.avatar_url, files=files)
                return
        
        print('webhook not found in ' + tchannel.name)
        webhook = await tchannel.create_webhook(name='NThook')
        await webhook.send(
                    str(message), username=member.display_name, avatar_url=member.avatar_url, files=files)
        

client.run(config["bot_token"])