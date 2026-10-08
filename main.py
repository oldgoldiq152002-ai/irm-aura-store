import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

TOKEN = '8884755347:AAHRdI8D9-YM_BSsv5qeGzED2t5NKLl3EY0'
bot = telebot.TeleBot(TOKEN)

user_balances = {}

def get_main_menu_inline():
    inline_markup = InlineKeyboardMarkup()
    inline_markup.row(InlineKeyboardButton("🛒 Shop Now", callback_data="shop_now"))
    inline_markup.row(InlineKeyboardButton("👤 Profile", callback_data="profile"), InlineKeyboardButton("💸 Add Balance", callback_data="add_balance"))
    inline_markup.row(InlineKeyboardButton("➡️ How to use", callback_data="how_to_use"))
    inline_markup.row(InlineKeyboardButton("⬇️ Download Panel", callback_data="download_panel"), InlineKeyboardButton("🎁 Daily Gift", callback_data="daily_gift"))
    inline_markup.row(InlineKeyboardButton("💸 Refer & Earn", callback_data="refer_earn"), InlineKeyboardButton("✔️ Support", callback_data="support"))
    inline_markup.row(InlineKeyboardButton("🛑 VIP Reseller Access", callback_data="vip_access"))
    return inline_markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    
    if user_id not in user_balances:
        user_balances[user_id] = 0.00
        
    current_balance = user_balances[user_id]
    
    welcome_text = f"""
🛒 - 🌐 𝑰r𝑴 𝑨𝑼𝑑𝑨 𝑺𝑻𝑶𝑑𝑬 🛍️ - 🛒

  Welcome, - ⚡ {first_name}!

🔹 Premium Game Keys
⚡ Instant Delivery 24/7
🛍️ 100% Secure Payment
📊 Best Prices Guaranteed
🔐 Safe And Trusted
✉️ Professional Support
───────────────────────
💬 Wallet Balance: ₹{current_balance:.2f}
───────────────────────

  Tap Shop Now to Start!
"""
    bot.send_message(message.chat.id, "Loading IRM AURA STORE...", reply_markup=ReplyKeyboardRemove())
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_menu_inline())

@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    balance = user_balances.get(user_id, 0.00)
    
    if call.data == "shop_now":
        device_msg = f"""
🛒 SELECT YOUR DEVICE TYPE ✨

🍏 Yoo {user_name}!
First select your device type. The available products will then be shown.
───────────────────────
"""
        inline_markup = InlineKeyboardMarkup()
        inline_markup.row(InlineKeyboardButton("🤖 ANDROID NON ROOT", callback_data="dev_non_root"))
        inline_markup.row(InlineKeyboardButton("🔐 ANDROID ROOT", callback_data="dev_root"))
        inline_markup.row(InlineKeyboardButton("🍎 iPHONE", callback_data="dev_iphone"))
        inline_markup.row(InlineKeyboardButton("✖️ Back to Menu", callback_data="back_to_main"))
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=device_msg, reply_markup=inline_markup)
        
    elif call.data == "back_to_main":
        welcome_text = f"""
🛒 - 🌐 𝑰r𝑴 𝑨𝑼𝑑𝑨 𝑺𝑻𝑶𝑑𝑬 🛍️ - 🛒

  Welcome, - ⚡ {user_name}!

🔹 Premium Game Keys
⚡ Instant Delivery 24/7
🛍️ 100% Secure Payment
📊 Best Prices Guaranteed
🔐 Safe And Trusted
✉️ Professional Support
───────────────────────
💬 Wallet Balance: ₹{balance:.2f}
───────────────────────

  Tap Shop Now to Start!
"""
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=welcome_text, reply_markup=get_main_menu_inline())

    elif call.data == "add_balance":
        add_bal_msg = """
💰 ADD BALANCE 

───────────────────────

📁 Select your preferred payment method. 

📁 FAMGATEWAY / UPI — Scan QR or Transfer (₹)
🪙 BINANCE PAY — Crypto payments ($)

───────────────────────
🚨 Payments are verified securely.
"""
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton("💳 FAMGATEWAY / UPI", callback_data="pay_famgateway"), InlineKeyboardButton("🪙 BINANCE PAY", callback_data="pay_binance"))
        markup.row(InlineKeyboardButton("↩️ Back", callback_data="back_to_main"))
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=add_bal_msg, reply_markup=markup)

    elif call.data == "pay_famgateway":
        bot.answer_callback_query(call.id, "Sending QR Code...")
        try:
            with open("UPI_QR.png", "rb") as qr_photo:
                bot.send_photo(
                    call.message.chat.id, 
                    photo=qr_photo, 
                    caption="🇮🇳 India Post Payments Bank\nUPI ID: 9677606117@postbank\nName: IEJAZ\n\nScan this QR code and make payment!"
                )
        except FileNotFoundError:
            bot.send_message(call.message.chat.id, "⚠️ QR Image file 'UPI_QR.png' not found in project folder!")

    elif call.data == "pay_binance":
        bot.answer_callback_query(call.id, "BINANCE PAY Selected")
        bot.send_message(call.message.chat.id, "🪙 **BINANCE PAY**\n\nSend payment to Binance ID / Pay Link:\n📩 Contact Admin: "9677606117@postbank", parse_mode="Markdown")

    elif call.data == "dev_non_root":
        msg = f"ANDROID NON ROOT – SELECT A PRODUCT\n───────────────────────\n\n🍏 Yoo {user_name}!\nChoose any product below to view its price and available duration plans.\n───────────────────────"
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton("🌆 DRIP CLIENT (APK)", callback_data="prod_drip_apk"))
        markup.row(InlineKeyboardButton("🌌 ABCD PANEL", callback_data="prod_abcd"))
        markup.row(InlineKeyboardButton("👾 DRIP WIRE", callback_data="prod_drip_wire"))
        markup.row(InlineKeyboardButton("🥷 SILENT CHEATS (PROXY)", callback_data="prod_silent_proxy"))
        markup.row(InlineKeyboardButton("🎆 BALA MODZ V6", callback_data="prod_bala"))
        markup.row(InlineKeyboardButton("🗿 TROLL MODZ", callback_data="prod_troll"))
        markup.row(InlineKeyboardButton("💥 NINE X MODZ", callback_data="prod_ninex"))
        markup.row(InlineKeyboardButton("🎯 AIM HACK", callback_data="prod_aim"))
        markup.row(InlineKeyboardButton("🌌 XYZ CHEATS(APK MOD)", callback_data="prod_xyz"))
        markup.row(InlineKeyboardButton("🌈 PATO TEAM(MIXED COLOUR)", callback_data="prod_pato"))
        markup.row(InlineKeyboardButton("✖️ Back", callback_data="shop_now"))
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=msg, reply_markup=markup)

    elif call.data == "dev_root":
        msg = f"ANDROID ROOT – SELECT A PRODUCT\n───────────────────────\n\n🍏 Yoo {user_name}!\nChoose any product below to view its price and available duration plans.\n───────────────────────"
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton("🎛️ RAPID CORE(ROOT)", callback_data="prod_rapid"))
        markup.row(InlineKeyboardButton("🌌 SILENT CHEATS (ROOT)", callback_data="prod_silent_root"))
        markup.row(InlineKeyboardButton("⚔️ X BLADE(ROOT)", callback_data="prod_xblade"))
        markup.row(InlineKeyboardButton("🌆 DRIP CLIENT FF(ROOT)", callback_data="prod_drip_ff"))
        markup.row(InlineKeyboardButton("✖️ Back", callback_data="shop_now"))
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=msg, reply_markup=markup)

    elif call.data == "dev_iphone":
        msg = f"iPHONE – SELECT A PRODUCT\n───────────────────────\n\n🍏 Yoo {user_name}!\nChoose any product below to view its price and available duration plans.\n───────────────────────"
        markup = InlineKeyboardMarkup()
        markup.row(InlineKeyboardButton("📱 MIGUL IOS(BASIC IND SERVER)", callback_data="prod_migul_basic"))
        markup.row(InlineKeyboardButton("📲 MIGUL IOS(PRO IND SERVER)", callback_data="prod_migul_pro"))
        markup.row(InlineKeyboardButton("🔮 FLUORITE IOS MLBB", callback_data="prod_fluorite"))
        markup.row(InlineKeyboardButton("✖️ Back", callback_data="shop_now"))
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=msg, reply_markup=markup)

    elif call.data == "profile":
        profile_txt = f"👤 **YOUR PROFILE DETAILS**\n\n👤 **Name:** {user_name}\n🆔 **User ID:** `{user_id}`\n💰 **Wallet Balance:** ₹{balance:.2f}\n📦 **Total Orders:** 0"
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, profile_txt, parse_mode="Markdown")

    elif call.data == "download_panel":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📥 **DOWNLOAD PANEL APKS**\n\nOfficial Download Links will be provided here.", parse_mode="Markdown")

    elif call.data == "how_to_use":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📖 **HOW TO USE GUIDE**\n\nWatch full tutorial here: @YourChannel", parse_mode="Markdown")

    elif call.data == "daily_gift":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🎉 **DAILY BONUS**\n\nNo active daily reward right now.", parse_mode="Markdown")

    elif call.data == "refer_earn":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"🔗 **REFERRAL PROGRAM**\n\nYour Referral Link:\n`https://t.me/IRM_AURA_STORE_bot?start={user_id}`", parse_mode="Markdown")

    elif call.data == "support":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "👨‍💻 **24/7 SUPPORT**\n\nContact: @YourAdminUsername", parse_mode="Markdown")

    elif call.data == "vip_access":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "👑 **VIP RESELLER PANEL**\n\nContact: @YourAdminUsername", parse_mode="Markdown")

    elif call.data.startswith("prod_"):
        bot.answer_callback_query(call.id, "Product Selected!")
        bot.send_message(call.message.chat.id, "💳 **Plan Selection & Pricing Details** will appear here upon set up.")

print("IRM AURA STORE Bot Started...")
bot.infinity_polling()

