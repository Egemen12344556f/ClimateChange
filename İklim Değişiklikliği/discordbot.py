import discord
from discord.ext import commands
from imageclass import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="İklim Değişikliği"))


@bot.event
async def on_ready():
       await bot.change_presence(status=discord.Status.online, activity=discord.Game('İklim Değişikliği'))
       print(f'{bot.user} Ok Ok I am here! :) ')
    

@bot.command()
async def selam(ctx):
      await ctx.send(f'Selam benim adım {bot.user} ve benim amacım size iklim değişiklikliğini anlatmak')
      await ctx.send(f'/yardım yazın ve siz anlatayım')



@bot.command()
@commands.has_permissions(ban_members=True)
async def iklimban(ctx, member:discord.Member, reason=None):
         if reason == None:
           reason = "sebep yok cıraylasın"
           await ctx.guild.ban(member)
           await ctx.send(f"Kullanıcı {member.mention} banlandı {reason}")

           

async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Sonunda geldin) {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)
 



# mamun
@bot.command()
async def mamun(ctx):
    with open('images/mamun.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


# sikko dans
@bot.command()
async def sikkodans(ctx):
    #BURAYA LİNKİ YAZ
    with open('', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    await ctx.send("")
    #BURAYA MESAJI YAZ





@bot.command()
async def yardım(ctx):
      await ctx.send(f'/yardım size bu komut sekmesini açar')
      await ctx.send(f'/chat benle konuşmanızı')
      await ctx.send(f'/iklim size ikli değişikliğinin ne olduğunu anlatır')
      await ctx.send(f'/check yazıp bir fotoğraf atarsanız size o fotoğrafın yüzde kaç iklim değişiklikliğine uyn olduğunu söyler')
      await ctx.send(f'/')



@bot.command()
async def check(ctx):

    if ctx.message.attachments:

        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            img_path = f"img/{file_name}"    
            await attachment.save(img_path)

        class_name, score = get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=img_path)
        await ctx.send(f"Bu bir {class_name.strip()}. Bundan {str(score)[2:4]}% eminim.")

    else: 
        await ctx.send("resim göndermediniz")

    




bot.run("MTIwNTE5MTgyMTI2MTgwMzU2MQ.GybbCQ.nzmAxCH4w9UGrbr2E7DhtFle9E-D2WnmQxna7Y")
