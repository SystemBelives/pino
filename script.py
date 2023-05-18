import requests
from bs4 import BeautifulSoup
import random
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, Application
from telegram import Update


async def send_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
     # Codifica la query per l'URL

    # Effettua una richiesta a Google Immagini
    randompage = random.randint(1,200)
    url = f"https://www.google.com/search?q=palle&start={randompage}&tbm=isch"
    headers = {
        "Authority": "www.google.com",
        "Method": "GET",
        "Scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "no-cache",
        "Cookie": "CONSENT=PENDING+821; SOCS=CAISHAgCEhJnd3NfMjAyMzAyMjItMF9SQzEaAml0IAEaBgiAn-WfBg; OTZ=7006662_48_52_123900_48_436380; OGPC=1151720448-7:19027681-1:19022552-1:19035226-2:; SID=WggtEbG2Dg7qVpeDIYGZRHm8EQJgk4Cdd_LMD403gEzFhLdIhzD1lxSdrRw545pdpsLI9g.; __Secure-1PSID=WggtEbG2Dg7qVpeDIYGZRHm8EQJgk4Cdd_LMD403gEzFhLdIJvKi4YWU1TCciwJ5vJ8rDg.; __Secure-3PSID=WggtEbG2Dg7qVpeDIYGZRHm8EQJgk4Cdd_LMD403gEzFhLdIQxtUKdzEt6q-n3g4sVzlVg.; HSID=AlZ1Nh0aKMOFtMWan; SSID=Aq_45IvbV-mUpCaMa; APISID=-Z2bgjEr8tLrma-F/AEYY2JTamtD26yxBB; SAPISID=jb0gExK71JUdDm8s/AurC2Ac0kXgSxhFMl; __Secure-1PAPISID=jb0gExK71JUdDm8s/AurC2Ac0kXgSxhFMl; __Secure-3PAPISID=jb0gExK71JUdDm8s/AurC2Ac0kXgSxhFMl; SEARCH_SAMESITE=CgQIp5gB; AEC=AUEFqZfnXNCMRm3lmrMW7JDDWaaZB-ieSlsTxdpcr09Gyyq2oVSNLsACoPw; NID=511=mixECmPTS_WOw5UvbnfrYHYcQdQlXpqpO4TXcfbeeGRRTQ92xymJJ-hmfxfb2WyLhmckpXpMsdI8RNQvAowE0tPsUrtecA3UKWlh-nNrEJr-gHyUyUc8cb6zdiakMZoK2s2aOkHGUIld",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Estrai i link alle immagini dai risultati della ricerca
    soup = BeautifulSoup(response.text, "html.parser")
    
    image_urls = []
    image_elements = soup.find_all("img")
    for img in image_elements:
        src = img.get('src')
        if src.startswith('https://encrypted-tbn0.gstatic.com/images'):
            image_urls.append(src)
        

    

    # Scarica un'immagine casuale
    random_image_url = random.choice(image_urls)
    print(image_urls)
    response = requests.get(random_image_url)
    response.raise_for_status()

    # Salva l'immagine su disco
    with open("random_image.jpg", "wb") as file:
        file.write(response.content)

    print("Immagine scaricata con successo.")

    await update.message.reply_photo("C:/Users/nhkce/Desktop/bot/random_image.jpg")
    



   
def main():
        application = Application.builder().token(
            "5696757918:AAG3gA7k_mO79vM3zilxs4aJy6A6l405Njc"
        ).build()
        application.add_handler(CommandHandler("palle", send_photo))
        application.run_polling()
        print("ciao")

def test() -> None:
        print("ciao")

main()
