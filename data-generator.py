import json

# Générer 200 posts Twitter (positifs et négatifs)
twitter_posts = []
for i in range(200):
    if i < 120:  # 120 positifs
        texts = [
            'J adore ce produit ! Excellent 👍',
            'Super qualité, content de mon achat 😊',
            'Livraison rapide, produit parfait 👌',
            'Service client excellent, merci 👍',
            'Ravi de mon achat, qualité impeccable 😍',
            'Super fast, merci pour la livraison 🚀',
            'Je suis ravi, produit génial 😄',
            'Top qualité, je recommande 👍',
            'Le meilleur achat ever 🏆',
            'Parfait, exactement ce que je voulais ✅',
            'Content et satisfait à 100% 💯',
            'Excellent, je suis impressionné 👏',
            'Rapid et efficace, parfait 👍',
            'Produit incroyable, je adore ❤️',
            'Service impeccable, bravo 👏',
            'Qualité premium, worth every penny 💎',
            'Délai respecté, emballage parfait 📦',
            'Je recommande vivement ce vendeur ⭐',
            'Produit correspond à la description 👍',
            'RAS, tout est parfait ✅'
        ]
    else:  # 80 négatifs
        texts = [
            'Service client horrible, je déteste 😠',
            'Je déteste cette marque, jamais plus 👎',
            'Déçu, ne correspond pas à la description 👎',
            'Je déteste, jamais je n achète encore 😤',
            'Produit nul, ne fonctionne pas 👎',
            'Livraison en retard, produit abîmé 😡',
            'Qualité médiocre, déçu 👎',
            'Service client inexistant 💔',
            'Pire achat de l année 😤',
            'Fuyez ce vendeur 🚫',
            'Arnaque totale 💸',
            'Produit cassé à la réception 💔',
            'Description trompeuse 👎',
            'Je regrette mon achat 😞',
            'Mauvaise qualité, pas durable 📉',
            'SAV injoignable 📵',
            'Défaut de fabrication 🛠️',
            'Ne marchait pas dès le début ❌',
            'Trop cher pour la qualité 💸',
            'Déception complète 👎'
        ]
    twitter_posts.append({
        'platform': 'twitter',
        'text': texts[i % len(texts)]
    })

# Générer 200 posts Facebook (positifs et négatifs)
facebook_posts = []
for i in range(200):
    if i < 110:  # 110 positifs
        texts = [
            'Je suis très satisfait du service 😊',
            'Content du résultat final 👍',
            'Excellent rapport qualité-prix 💯',
            'Super content, merci 😊',
            'Produit exceptionnel, bravo 🌟',
            'Je adore, merci pour tout ❤️',
            'Super expérience, merci 😊',
            'Très bon produit, je recommande ✅',
            'Service rapide et professionnel ⚡',
            'Produit de grande qualité 🏅',
            'Emballage soigné, livraison rapide 🎁',
            'Correspond parfaitement à mes attentes 🎯',
            'Rien à redire, parfait 👍',
            'Achat sans problème ✅',
            'Je suis conquis 😍',
            'Rapport qualité-prix excellent 💰',
            'Service client réactif 📞',
            'Produit robuste et fiable 🔧',
            'Facile à utiliser 👌',
            'Belle finition ✨'
        ]
    else:  # 90 négatifs
        texts = [
            'Le pire achat de ma vie 😡',
            'Très déçu, pas du tout comme sur la photo 💔',
            'Très mauvais produit, je regrette 😞',
            'Le pire service que j ai jamais vu 😡',
            'Produit défectueux, je retourne ↩️',
            'Service client lent et inefficace 😠',
            'Qualité vraiment décevante 👎',
            'Ne fonctionne pas comme prévu ❌',
            'Pieces manquantes dans le colis 📦',
            'Trop de défauts 🚫',
            'Je demande un remboursement 💸',
            'Produit déjà utilisé 😠',
            'Mauvaise expérience globale 📉',
            'Temps d attente trop long ⏳',
            'Communication difficile 📵',
            'Garantie non respectée 🚫',
            'Problème non résolu 🔧',
            'Déçu par la marque 💔',
            'Je ne recommande pas 👎',
            'A éviter 🚫'
        ]
    facebook_posts.append({
        'platform': 'facebook',
        'text': texts[i % len(texts)]
    })

# Générer 200 posts Instagram (positifs et négatifs)
instagram_posts = []
for i in range(200):
    if i < 140:  # 140 positifs
        texts = [
            'Incroyable ce restaurant ❤️',
            'Superbe expérience, je reviendrai 🌟',
            'Magnifique produit, je adore ✨',
            'Service impeccable, merci beaucoup 👏',
            'Incroyable, je suis fan 😍',
            'Super qualité, livraison rapide 🚀',
            'Très belle découverte, je recommande 🌟',
            'Magnifique, je suis conquis ✨',
            'Coup de cœur ❤️',
            'Parfait pour mes besoins ✅',
            'Design magnifique 🎨',
            'Fonctionnalités géniales 🔥',
            'Je suis sous le charme 💫',
            'Qualité exceptionnelle 💎',
            'Service au top ⭐',
            'Rien à dire, parfait 👍',
            'Je l adore 😻',
            'Super achat 🛍️',
            'Vraiment satisfait 😊',
            'Je recommande à 100% 💯'
        ]
    else:  # 60 négatifs
        texts = [
            'Déçu de la qualité, je ne recommande pas 💔',
            'Horrible service client 😠',
            'Le pire restaurant de ma vie 🤮',
            'Déception totale, à éviter ❌',
            'Horrible expérience client 😤',
            'Mauvaise surprise, produit cassé 💔',
            'La pire chose que j ai achetée 💩',
            'Déçu par la qualité, pas top 👎',
            'Service catastrophique 😡',
            'Produit de mauvaise qualité 📉',
            'Je suis dégoûté 🤢',
            'A ne pas acheter 🚫',
            'Très mauvaise expérience 😞',
            'Qualité inférieure aux attentes 👎',
            'Je suis déçu 💔',
            'Ne correspond pas aux photos 📸',
            'Problème de taille/size 📏',
            'Couleur différente de la photo 🎨',
            'Mauvais goût/saveur 👅',
            'Je retourne le produit ↩️'
        ]
    instagram_posts.append({
        'platform': 'instagram',
        'text': texts[i % len(texts)]
    })

# Combiner tous les posts
all_posts = twitter_posts + facebook_posts + instagram_posts

# Sauvegarder en JSON
with open('social_media_posts.json', 'w', encoding='utf-8') as f:
    json.dump(all_posts, f, ensure_ascii=False, indent=2)

print("✅ Dataset créé avec 600 posts!")
print("📊 Statistiques:")
print(f"   Twitter: 200 posts (120 positifs, 80 négatifs)")
print(f"   Facebook: 200 posts (110 positifs, 90 négatifs)")
print(f"   Instagram: 200 posts (140 positifs, 60 négatifs)")
print(f"📁 Fichier: social_media_posts.json")

# Aperçu des premiers posts
print("\n🎪 APERÇU DES PREMIERS POSTS:")
for i, post in enumerate(all_posts[:10]):
    print(f"{i+1}. {post}")