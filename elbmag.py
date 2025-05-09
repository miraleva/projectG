import random

# Semboller
symbols = ["🍒", "💎", "7️⃣", "🍋", "🔔"]

# Başlangıç puanı
score = 5000

print("🎰 Slot Machine'e Hoş Geldin!")
print("Kurallar:")
print("- Başlangıç puanın: 5000")
print("- Her spin -400 puan")
print("- 3 aynı sembol gelirse +2000 puan")
print("- Çıkmak için 'q' yaz, devam etmek için Enter'a bas")

while score >= 5:
    user_input = input("\n▶️ Spin atmak için Enter'a bas ('q' ile çık): ")
    
    if user_input.lower() == 'q':
        print(f"👋 Oyundan çıktın. Son puanın: {score}")
        break

    score -= 400

    # 3 sembol seç
    result = [random.choice(symbols) for _ in range(3)]
    
    # Sonuçları göster
    print("------------------")
    print(f"| {result[0]} | {result[1]} | {result[2]} |")
    print("------------------")

    # Kazanma durumu kontrolü
    if result[0] == result[1] == result[2]:
        print("🎉 Tebrikler! 3 sembol aynı! +20 puan")
        score += 2000
    else:
        print("😢 Kaybettin! -400 puan")

    print(f"🔢 Güncel puanın: {score}")

if score < 5:
    print("\n💀 Puanın bitti. Oyun sona erdi.")
