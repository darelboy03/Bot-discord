import discord

TOKEN = "TOKEN DAREL"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Bot {client.user} sudah online!")

@client.event
async def on_message(message):

    # Jangan membalas pesan dari bot sendiri
    if message.author == client.user:
        return

    # Membaca pesan
    pesan = message.content.strip().lower()

    print(f"Pesan masuk: {pesan}")

    # =========================
    # SAMPAH B3
    # =========================

    b3 = [
        "baterai",
        "oli",
        "lampu neon",
        "lampu tl",
        "thinner",
        "solvent",
        "cat",
        "bahan kimia",
        "toner",
        "cartridge",
        "obat kadaluarsa",
        "obat kedaluwarsa"
    ]

    # =========================
    # SAMPAH ORGANIK
    # =========================

    organik = [
        "apel",
        "pisang",
        "kulit pisang",
        "nasi",
        "sisa makanan",
        "makanan",
        "sayuran",
        "buah",
        "daun",
        "ranting"
    ]

    # =========================
    # SAMPAH ANORGANIK
    # =========================

    anorganik = [
        "botol",
        "botol plastik",
        "botol minum",
        "plastik",
        "kantong plastik",
        "kardus",
        "kaleng",
        "kertas",
        "koran",
        "gelas plastik"
    ]

    # =========================
    # SAMPAH RESIDU
    # =========================

    residu = [
        "pensil",
        "tisu",
        "popok",
        "pembalut",
        "puntung rokok",
        "styrofoam",
        "karet",
        "sapu",
        "spons"
    ]

    # =========================
    # CEK B3
    # =========================

    ditemukan = next((item for item in b3 if item in pesan), None)

    if ditemukan:
        await message.channel.send(
            f"⚠️ **{ditemukan.title()}** termasuk sampah **B3**.\n"
            "Jangan dicampur dengan sampah biasa. "
            "Buang ke tempat sampah B3 ya!"
        )
        return

    # =========================
    # CEK ORGANIK
    # =========================

    ditemukan = next((item for item in organik if item in pesan), None)

    if ditemukan:
        await message.channel.send(
            f"🍎 **{ditemukan.title()}** termasuk sampah **ORGANIK**.\n"
            "Buang ke tempat sampah organik ya!"
        )
        return

    # =========================
    # CEK ANORGANIK
    # =========================

    ditemukan = next((item for item in anorganik if item in pesan), None)

    if ditemukan:
        await message.channel.send(
            f"♻️ **{ditemukan.title()}** termasuk sampah **ANORGANIK**.\n"
            "Kalau bersih dan dapat didaur ulang, "
            "masukkan ke tempat sampah anorganik/recyclable ya!"
        )
        return

    # =========================
    # CEK RESIDU
    # =========================

    ditemukan = next((item for item in residu if item in pesan), None)

    if ditemukan:
        await message.channel.send(
            f"🗑️ **{ditemukan.title()}** termasuk sampah **RESIDU**.\n"
            "Buang ke tempat sampah residu ya!"
        )
        return

    # =========================
    # TIDAK DIKENALI
    # =========================

    await message.channel.send(
        "❓ Saya belum mengenali jenis sampah tersebut.\n"
        "Coba sebutkan nama barang atau sampahnya."
    )

client.run(TOKEN)