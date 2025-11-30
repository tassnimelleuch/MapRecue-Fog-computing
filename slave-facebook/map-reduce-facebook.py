from flask import Flask, request, jsonify
from collections import Counter, defaultdict
import json

app = Flask(__name__)

# Listes de mots pour l'analyse de sentiment
POSITIVE_WORDS = {
    'bon', 'excellent', 'génial', 'super', 'aimer', 'adorer', 'parfait', 'fantastique',
    'heureux', 'content', 'satisfait', 'recommande', 'exceptionnel', 'professionnel',
    'rapide', 'conforme', 'intuitif', 'innovant', 'bravo', 'competent', 'ravis',
    'excellent', 'superbe', 'magnifique', 'impressionnant', 'formidable', 'merveilleux',
    'idéal', 'agréable', 'sympa', 'cool', 'top', 'extra', 'sublime', 'fabuleux'
}

NEGATIVE_WORDS = {
    'mauvais', 'horrible', 'nul', 'détester', 'pas', 'probleme', 'colère', 'triste',
    'deçu', 'énervé', 'déçu', 'endommagé', 'médiocre', 'tard', 'inacceptable',
    'incompréhensible', 'difficile', 'manquant', 'injoignable', 'frustrant', 'scandaleux',
    'affreux', 'exécrable', 'minable', 'pitoyable', 'désolant', 'navrant', 'catastrophe',
    'décevant', 'lent', 'cher', 'compliqué', 'insupportable', 'inutile', 'désastre'
}

def map_function(comment):
    """Fonction Map: Analyse le sentiment d'un commentaire individuel"""
    text = comment['text'].lower()
    
    # Compter les mots positifs et négatifs
    positive_words_found = []
    negative_words_found = []
    
    for word in text.split():
        if word in POSITIVE_WORDS:
            positive_words_found.append(word)
        elif word in NEGATIVE_WORDS:
            negative_words_found.append(word)
    
    # Analyser les émojis
    positive_emojis = ['😊', '👍', '❤️', '😍', '😂', '🔥', '👏', '💯', '🎉', '⭐']
    negative_emojis = ['😠', '👎', '💔', '😢', '😡', '🤮', '💩', '☹️', '😞']
    
    for emoji in positive_emojis:
        if emoji in text:
            positive_words_found.append(emoji)
    
    for emoji in negative_emojis:
        if emoji in text:
            negative_words_found.append(emoji)
    
    # Déterminer le sentiment
    positive_score = len(positive_words_found)
    negative_score = len(negative_words_found)
    
    if positive_score > negative_score:
        sentiment = 'positive'
    elif negative_score > positive_score:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return {
        'sentiment': sentiment,
        'positive_words': positive_words_found,
        'negative_words': negative_words_found,
        'positive_score': positive_score,
        'negative_score': negative_score,
        'platform': comment['platform'],
        'text_preview': comment['text'][:50] + '...' if len(comment['text']) > 50 else comment['text']
    }

def reduce_function(mapped_results):
    """Fonction Reduce: Agrège les résultats du mapping"""
    sentiment_count = Counter()
    word_frequency = Counter()
    platform_stats = Counter()
    
    total_positive_score = 0
    total_negative_score = 0
    total_comments = len(mapped_results)
    
    for result in mapped_results:
        # Compter les sentiments
        sentiment_count[result['sentiment']] += 1
        
        # Compter les plateformes
        platform_stats[result['platform']] += 1
        
        # Compter les mots
        for word in result['positive_words']:
            word_frequency[f"positive_{word}"] += 1
        for word in result['negative_words']:
            word_frequency[f"negative_{word}"] += 1
        
        # Scores totaux
        total_positive_score += result['positive_score']
        total_negative_score += result['negative_score']
    
    # Calculer les pourcentages
    if total_comments > 0:
        positive_percentage = (sentiment_count['positive'] / total_comments) * 100
        negative_percentage = (sentiment_count['negative'] / total_comments) * 100
        neutral_percentage = (sentiment_count['neutral'] / total_comments) * 100
    else:
        positive_percentage = negative_percentage = neutral_percentage = 0
    
    # Score de sentiment global
    sentiment_score = total_positive_score - total_negative_score
    
    return {
        'sentiment_distribution': {
            'positive': sentiment_count['positive'],
            'negative': sentiment_count['negative'],
            'neutral': sentiment_count['neutral'],
            'positive_percentage': round(positive_percentage, 2),
            'negative_percentage': round(negative_percentage, 2),
            'neutral_percentage': round(neutral_percentage, 2)
        },
        'platform_distribution': dict(platform_stats),
        'word_frequency': dict(word_frequency.most_common(20)),  # Top 20 mots
        'scores': {
            'total_positive_score': total_positive_score,
            'total_negative_score': total_negative_score,
            'sentiment_score': sentiment_score,
            'average_sentiment_intensity': round((total_positive_score + total_negative_score) / total_comments, 2) if total_comments > 0 else 0
        },
        'summary': {
            'total_comments_processed': total_comments,
            'dominant_sentiment': max(sentiment_count, key=sentiment_count.get) if sentiment_count else 'neutral',
            'sentiment_ratio': round(positive_percentage / negative_percentage, 2) if negative_percentage > 0 else positive_percentage
        }
    }

def map_reduce_facebook_comments(comments):
    """Exécute le processus MapReduce complet sur les commentaires Facebook"""
    print(f"🔧 Nœud Facebook: Début du MapReduce sur {len(comments)} commentaires...")
    
    # PHASE MAP: Traiter chaque commentaire individuellement
    print("📊 Phase MAP: Analyse de chaque commentaire...")
    mapped_results = []
    for i, comment in enumerate(comments):
        if i % 50 == 0:  # Log toutes les 50 opérations
            print(f"   ↳ Traitement du commentaire {i+1}/{len(comments)}")
        mapped_result = map_function(comment)
        mapped_results.append(mapped_result)
    
    print("✅ Phase MAP terminée")
    
    # PHASE REDUCE: Agrégation des résultats
    print("📈 Phase REDUCE: Agrégation des résultats...")
    reduced_result = reduce_function(mapped_results)
    
    print("✅ Phase REDUCE terminée")
    print(f"🎯 Analyse terminée: {reduced_result['summary']['total_comments_processed']} commentaires traités")
    
    return reduced_result

@app.route('/analyze', methods=['POST'])
def analyze_facebook_comments():
    """Endpoint pour analyser les commentaires Facebook avec MapReduce"""
    try:
        data = request.get_json()
        
        if not data or 'comments' not in data:
            return jsonify({'error': 'Données manquantes. Format attendu: {"comments": [...]}'}), 400
        
        comments = data['comments']
        
        print(f"📘 Nœud Facebook: Réception de {len(comments)} commentaires...")
        
        # Filtrer seulement les commentaires Facebook
        facebook_comments = [c for c in comments if c.get('platform') == 'facebook']
        
        if not facebook_comments:
            return jsonify({'error': 'Aucun commentaire Facebook trouvé'}), 400
        
        print(f"📘 Nœud Facebook: Traitement de {len(facebook_comments)} commentaires Facebook...")
        
        # Exécuter MapReduce
        result = map_reduce_facebook_comments(facebook_comments)
        
        # Ajouter des métadonnées du nœud
        result['node_info'] = {
            'node_type': 'slave',
            'platform': 'facebook',
            'status': 'completed',
            'comments_processed': len(facebook_comments)
        }
        
        print(f"✅ Nœud Facebook: Analyse MapReduce terminée")
        print(f"   📊 Résultats: {result['sentiment_distribution']['positive']} 👍, "
              f"{result['sentiment_distribution']['negative']} 👎, "
              f"{result['sentiment_distribution']['neutral']} ⚪")
        
        return jsonify(result)
        
    except Exception as e:
        print(f"❌ Erreur lors de l'analyse: {str(e)}")
        return jsonify({'error': f'Erreur interne: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de santé du nœud esclave"""
    return jsonify({
        'status': 'healthy', 
        'node': 'facebook_slave',
        'role': 'map_reduce_processor',
        'platform': 'facebook'
    })

@app.route('/stats', methods=['GET'])
def get_stats():
    """Endpoint pour obtenir les statistiques du nœud"""
    return jsonify({
        'node_info': {
            'name': 'Facebook Slave Node',
            'role': 'MapReduce Processor',
            'platform': 'facebook',
            'status': 'running'
        },
        'capabilities': {
            'map_function': 'Analyse sentiment par commentaire',
            'reduce_function': 'Agrégation des résultats',
            'processing_type': 'facebook_comments'
        },
        'dictionaries': {
            'positive_words_count': len(POSITIVE_WORDS),
            'negative_words_count': len(NEGATIVE_WORDS)
        }
    })

if __name__ == '__main__':
    print("=" * 60)
    print("📘 NŒUD ESCLAVE FACEBOOK - MAPREDUCE PROCESSOR")
    print("=" * 60)
    print("📍 Port: 5002")
    print("🎯 Rôle: Traitement MapReduce des commentaires Facebook")
    print("🔧 Capacités:")
    print("   • Fonction MAP: Analyse sentiment par commentaire")
    print("   • Fonction REDUCE: Agrégation des résultats")
    print("   • Dictionnaires: {} mots positifs, {} mots négatifs".format(
        len(POSITIVE_WORDS), len(NEGATIVE_WORDS)))
    print("🌐 Accessible depuis: ip:5002")
    print("📋 Endpoints:")
    print("   • POST /analyze - Analyser les commentaires Facebook")
    print("   • GET /health - Vérifier la santé du nœud")
    print("   • GET /stats - Obtenir les statistiques du nœud")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=5002, debug=False)