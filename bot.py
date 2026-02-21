import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

# 🔐 Tokeningizni shu yerga qo‘ying
API_TOKEN = "8535106559:AAGoR_Od2xnMYyMaSMVU0HekCUPXZG9IDqE"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
async def on_start(message: types.Message):
    await message.reply("Hello, welcome to the bot!")

dp.register_message_handler(on_start, Command("start"))

async def handler(request):
    # aiogram botning ishga tushurilishi
    await bot.start_polling()

    return Response(status_code=200)
# --- START tugmasi ---
start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📋 Chegirmalar")],
        [KeyboardButton(text="START")]
    ],
    resize_keyboard=True
)

# --- Kategoriya tugmalari ---
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💧 Suv"), KeyboardButton(text="👕 Kiyimlar")],
        [KeyboardButton(text="👟 Oyoq kiyim"), KeyboardButton(text="🍞 Oziq-ovqat")],
        [KeyboardButton(text="🍎 Mevalar"), KeyboardButton(text="🍫 Shirinliklar")],
        [KeyboardButton(text="🥕 Sabzavotlar"), KeyboardButton(text="🏠 Maishiy texnika")],
        [KeyboardButton(text="📱 Telefonlar")]
    ],
    resize_keyboard=True
)

# --- Mahsulotlar bazasi ---
products = {
    "💧 Suv": [
        {"name": "Nestle 1L", "price": 5000, "discount": 10},
        {"name": "Bonaqua 1.5L", "price": 6000, "discount": 15},
        {"name": "Hydrolife 1L", "price": 4500, "discount": 5},
        {"name": "Arktika 1L", "price": 4000, "discount": 8},
        {"name": "Montella 1.5L", "price": 6500, "discount": 12},
        {"name": "Asu 1L", "price": 3500, "discount": 5},
        {"name": "Chortoq 1L", "price": 4800, "discount": 10},
        {"name": "Everest 1.5L", "price": 6200, "discount": 9},
        {"name": "Musaffo 1L", "price": 4300, "discount": 6},
        {"name": "Pure Life 1L", "price": 5500, "discount": 11},
    ],
    "👕 Kiyimlar": [
        {"name": "Futbolka S", "price": 120000, "discount": 10},
        {"name": "Futbolka M", "price": 130000, "discount": 15},
        {"name": "Kofta L", "price": 180000, "discount": 5},
        {"name": "Shim 32", "price": 250000, "discount": 10},
        {"name": "Shim 34", "price": 260000, "discount": 12},
        {"name": "Kurtka M", "price": 450000, "discount": 20},
        {"name": "Kurtka L", "price": 470000, "discount": 15},
        {"name": "Bluzka S", "price": 150000, "discount": 5},
        {"name": "Bluzka M", "price": 160000, "discount": 8},
        {"name": "Sport kiyim", "price": 200000, "discount": 10},
    ],
    "👟 Oyoq kiyim": [
        {"name": "Sport krossovka 40", "price": 300000, "discount": 10},
        {"name": "Sport krossovka 41", "price": 310000, "discount": 12},
        {"name": "Sport krossovka 42", "price": 320000, "discount": 15},
        {"name": "Klassik oyoq kiyim 40", "price": 280000, "discount": 5},
        {"name": "Klassik oyoq kiyim 41", "price": 290000, "discount": 8},
        {"name": "Krossovka bolalar 35", "price": 150000, "discount": 10},
        {"name": "Krossovka bolalar 36", "price": 155000, "discount": 12},
        {"name": "Krossovka bolalar 37", "price": 160000, "discount": 10},
        {"name": "Shimoliy oyoq kiyim", "price": 270000, "discount": 7},
        {"name": "Yozgi sport oyoq", "price": 250000, "discount": 5},
    ],
    "🍞 Oziq-ovqat": [
        {"name": "Non loch", "price": 12000, "discount": 5},
        {"name": "Bug'doy uni 1kg", "price": 15000, "discount": 10},
        {"name": "Shakar 1kg", "price": 18000, "discount": 8},
        {"name": "Tuz 1kg", "price": 5000, "discount": 5},
        {"name": "Yog' 1L", "price": 25000, "discount": 12},
        {"name": "Guruch 1kg", "price": 22000, "discount": 10},
        {"name": "Makaron 1kg", "price": 20000, "discount": 8},
        {"name": "Sut 1L", "price": 12000, "discount": 5},
        {"name": "Pishloq 1kg", "price": 80000, "discount": 15},
        {"name": "Yogurt 1L", "price": 18000, "discount": 5},
    ],
    "🍎 Mevalar": [
        {"name": "Olma 1kg", "price": 25000, "discount": 10},
        {"name": "Banan 1kg", "price": 30000, "discount": 8},
        {"name": "Apelsin 1kg", "price": 28000, "discount": 5},
        {"name": "Nok 1kg", "price": 26000, "discount": 10},
        {"name": "Anor 1kg", "price": 35000, "discount": 12},
        {"name": "Uzum 1kg", "price": 32000, "discount": 15},
        {"name": "Kivi 1kg", "price": 40000, "discount": 10},
        {"name": "Qulupnay 1kg", "price": 45000, "discount": 20},
        {"name": "Olxo'ri 1kg", "price": 28000, "discount": 5},
        {"name": "Mandarin 1kg", "price": 30000, "discount": 10},
    ],
    "🍫 Shirinliklar": [
        {"name": "Shokolad 100g", "price": 15000, "discount": 5},
        {"name": "Konfet 1kg", "price": 80000, "discount": 10},
        {"name": "Pechenye 500g", "price": 20000, "discount": 8},
        {"name": "Karamel 1kg", "price": 60000, "discount": 12},
        {"name": "Chizkek", "price": 70000, "discount": 15},
        {"name": "Muzqaymoq 1L", "price": 50000, "discount": 10},
        {"name": "Puding 500g", "price": 30000, "discount": 5},
        {"name": "Biskvit 1kg", "price": 40000, "discount": 10},
        {"name": "Shirin kulcha", "price": 25000, "discount": 5},
        {"name": "Jele 500g", "price": 20000, "discount": 8},
    ],
    "🥕 Sabzavotlar": [
        {"name": "Kartoshka 1kg", "price": 12000, "discount": 5},
        {"name": "Sabzi 1kg", "price": 10000, "discount": 5},
        {"name": "Piyoz 1kg", "price": 9000, "discount": 5},
        {"name": "Bodring 1kg", "price": 15000, "discount": 10},
        {"name": "Pomidor 1kg", "price": 18000, "discount": 8},
        {"name": "Baqara 1kg", "price": 20000, "discount": 12},
        {"name": "Ko‘k piyoz 1kg", "price": 8000, "discount": 5},
        {"name": "Karam 1kg", "price": 22000, "discount": 10},
        {"name": "Sabzavot aralash 1kg", "price": 25000, "discount": 8},
        {"name": "Batareyali sabzavotlar", "price": 30000, "discount": 10},
    ],
    "🏠 Maishiy texnika": [
        {"name": "Choynak elektr 1L", "price": 250000, "discount": 10},
        {"name": "Mikroto‘lqin 20L", "price": 600000, "discount": 12},
        {"name": "Blender 1.5L", "price": 350000, "discount": 8},
        {"name": "Kofe mashinasi", "price": 800000, "discount": 15},
        {"name": "Toaster", "price": 150000, "discount": 5},
        {"name": "Changyutgich 1800W", "price": 300000, "discount": 10},
        {"name": "Konditsioner", "price": 1200000, "discount": 20},
        {"name": "Sovutgich 200L", "price": 900000, "discount": 10},
        {"name": "Kir yuvish mashinasi", "price": 1000000, "discount": 15},
        {"name": "Qahva qaynatgich", "price": 200000, "discount": 5},
    ],
    "📱 Telefonlar": [
        {"name": "iPhone 14", "price": 1500000, "discount": 10},
        {"name": "iPhone 14 Pro", "price": 2000000, "discount": 12},
        {"name": "Samsung S23", "price": 1400000, "discount": 10},
        {"name": "Samsung S23 Ultra", "price": 2200000, "discount": 15},
        {"name": "Xiaomi 13", "price": 1200000, "discount": 8},
        {"name": "Xiaomi 13 Pro", "price": 1600000, "discount": 12},
        {"name": "Realme GT 3", "price": 900000, "discount": 5},
        {"name": "Nokia G22", "price": 400000, "discount": 10},
        {"name": "Oppo Reno 9", "price": 1100000, "discount": 8},
        {"name": "Huawei P60", "price": 1800000, "discount": 12},
    ],
}

# --- foydalanuvchi holatini saqlash uchun dictionary ---
user_started = {}  # {user_id: True/False}

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    if user_started.get(user_id):  # agar foydalanuvchi oldin bosgan bo‘lsa
        await message.answer(
            "START tugmasini bosing 👇",
            reply_markup=start_btn
        )
    else:  # birinchi marta bosgan foydalanuvchi
        await message.answer(
            "🛍 ZUMA MARKET ga xush kelibsiz!\nPastdagi START tugmasini bosing 👇",
            reply_markup=start_btn
        )
        user_started[user_id] = True  # foydalanuvchini belgilaymiz
 


# --- START tugmasi bosilganda ---
@dp.message(lambda message: message.text == "START")
async def open_menu(message: types.Message):
    await message.answer("Kategoriyani tanlang 👇", reply_markup=menu)

# --- Chegirmalar tugmasi ---
@dp.message(lambda message: message.text == "📋 Chegirmalar")
async def open_menu2(message: types.Message):
    await message.answer("Kategoriyani tanlang 👇", reply_markup=menu)

# --- Mahsulotlarni chiqarish ---
@dp.message()
async def show_products(message: types.Message):
    category = message.text
    if category in products:
        text = f"📋 {category} bo‘yicha chegirmalar:\n\n"
        for item in products[category]:
            new_price = item["price"] * (100 - item["discount"]) / 100
            text += (
                f"🛍 {item['name']}\n"
                f"Eski narx: {item['price']} so'm\n"
                f"Chegirma: {item['discount']}%\n"
                f"Yangi narx: {int(new_price)} so'm\n\n"
            )
        await message.answer(text)

# --- Botni ishga tushirish ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
