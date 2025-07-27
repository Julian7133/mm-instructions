#!/usr/bin/env python3
import json
import os

# Files that need translation
files_to_translate = [
    "development-unit-testing.json",
    "management-performance-reviews.json", 
    "management-strategic-planning.json",
    "management-team-feedback-coaching.json",
    "productivity-customer-service-templates.json",
    "productivity-document-formatting.json", 
    "productivity-email-automation.json",
    "productivity-meeting-summarization.json",
    "productivity-presentation-creation.json",
    "productivity-research-gathering.json",
    "productivity-task-prioritization.json"
]

# German translations for each file
translations = {
    "development-unit-testing.json": {
        "steps": [
            {
                "title": "Teststrategie und Implementierung",
                "description": "Code analysieren und umfassende Test-Suite generieren",
                "tool": "Claude-4-Sonnet",
                "toolReason": "Überlegene Code-Analyse und systematischer Test-Ansatz",
                "timeEstimate": "20 Minuten",
                "prompt": "Du bist ein leitender Software-Ingenieur, der auf Testen spezialisiert ist. Denke schrittweise, um umfassende Tests zu erstellen.\n\nAnalysiere diesen Code und erstelle Tests:\n1. Alle Code-Pfade und Grenzfälle identifizieren\n2. Testdaten für normale und Grenzbedingungen entwerfen\n3. Mocking-Strategie für Abhängigkeiten planen\n4. Vollständige Testimplementierung schreiben\n\nZu testender Code: [füge deine Funktion/Klasse/Modul hier ein]\n\nWenn du Details über Test-Framework, Sprache oder spezifische Anforderungen benötigst, stelle klärende Fragen.\n\nStelle bereit:\n**Teststrategie**: [was getestet werden muss und warum]\n**Testfälle**: [spezifische Szenarien zur Abdeckung]\n**Mock-Strategie**: [was und wie gemockt wird]\n**Vollständiger Testcode**: [funktionierende Testimplementierung]\n**Coverage-Analyse**: [erwartete Abdeckung und kritische Pfade]\n\nStelle sicher, dass Tests:\n- Unabhängig und wiederholbar sind\n- Schnelle Ausführung haben\n- Klare Fehlermeldungen liefern",
                "tips": [
                    "Verhalten testen, nicht Implementierungsdetails",
                    "Sowohl positive als auch negative Testfälle einschließen"
                ]
            }
        ]
    },
    "management-performance-reviews.json": {
        "steps": [
            {
                "title": "Leistungsbeurteilungsstrategie und -durchführung",
                "description": "Mitarbeiterleistung bewerten und konstruktives Feedback erstellen",
                "tool": "Claude-4-Opus",
                "toolReason": "Überlegen bei nuancierter Bewertung und professioneller Kommunikation",
                "timeEstimate": "30 Minuten",
                "prompt": "Du bist ein erfahrener HR-Manager und Führungsexperte. Denke schrittweise, um faire und konstruktive Leistungsbeurteilungen zu erstellen.\n\nErstelle eine umfassende Leistungsbeurteilung:\n1. Zielerreichung und Leistungsmetriken bewerten\n2. Stärken und Verbesserungsbereiche identifizieren\n3. Konstruktives Feedback und Entwicklungsempfehlungen\n4. Ziele und Entwicklungsplan für das nächste Jahr\n\nMitarbeiterinformationen: [Name, Position, wichtige Projekte/Ziele des Jahres]\n\nWenn du mehr Kontext über Unternehmenskultur, spezifische Ziele oder Bewertungskriterien benötigst, stelle klärende Fragen.\n\nStelle bereit:\n**Leistungsübersicht**: [allgemeine Bewertung und wichtige Errungenschaften]\n**Zielerreichung**: [spezifische Ziele und Ergebnisse]\n**Stärken**: [wichtige Stärken mit Beispielen]\n**Entwicklungsbereiche**: [Bereiche zur Verbesserung mit konkreten Empfehlungen]\n**Ziele für nächstes Jahr**: [SMART-Ziele mit Zeitrahmen]\n**Entwicklungsplan**: [Training, Mentoring, neue Herausforderungen]\n\nFokus auf:\n- Konstruktives, umsetzbares Feedback\n- Spezifische Beispiele und Verhalten\n- Unterstützung für Wachstum und Entwicklung",
                "tips": [
                    "Spezifische Beispiele und Verhalten verwenden, nicht vage Aussagen",
                    "Ausgewogene Bewertung von Leistungen und Entwicklungsbereichen"
                ]
            }
        ]
    },
    "management-strategic-planning.json": {
        "steps": [
            {
                "title": "Strategische Planung und Ausrichtung",
                "description": "Langfristige Geschäftsstrategie entwickeln und umsetzen",
                "tool": "Claude-4-Opus",
                "toolReason": "Essenziell für komplexe strategische Analyse und Planung",
                "timeEstimate": "40 Minuten",
                "prompt": "Du bist ein leitender Strategieberater und Geschäftsführer. Denke schrittweise, um umfassende strategische Pläne zu entwickeln.\n\nEntwickle einen strategischen Plan:\n1. Markt- und Wettbewerbsanalyse\n2. SWOT-Analyse und strategische Positionierung\n3. Langfristige Ziele und Prioritäten\n4. Umsetzungsplan und Ressourcenzuteilung\n\nUnternehmensinformationen: [Branche, Größe, aktuelle Herausforderungen]\nPlanungshorizont: [1-3 Jahre/3-5 Jahre/5+ Jahre]\n\nWenn du mehr Details über Marktbedingungen, interne Fähigkeiten oder spezifische Herausforderungen benötigst, stelle klärende Fragen.\n\nStelle bereit:\n**Situationsanalyse**: [aktuelle Position und Marktkontext]\n**SWOT-Bewertung**: [Stärken, Schwächen, Chancen, Bedrohungen]\n**Strategische Vision**: [langfristige Ausrichtung und Ziele]\n**Prioritäten**: [wichtigste strategische Initiativen]\n**Umsetzungsplan**: [Zeitrahmen, Meilensteine, Ressourcen]\n**Erfolgsmessung**: [KPIs und Bewertungsmetriken]\n**Risikomanagement**: [wichtige Risiken und Minderungsstrategien]\n\nFokus auf:\n- Umsetzbare und messbare Strategien\n- Marktgetriebene Entscheidungen\n- Nachhaltige Wettbewerbsvorteile",
                "tips": [
                    "Strategien auf Marktdaten und Wettbewerbsanalyse basieren",
                    "Klare Prioritäten und Meilensteine für die Umsetzung setzen"
                ]
            }
        ]
    }
}

def add_german_translation(file_path, german_steps):
    """Add German translation to a JSON instruction file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Add German language section
        if 'languages' in data and 'en' in data['languages']:
            data['languages']['de'] = {
                'steps': german_steps
            }
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"✓ Added German translation to {os.path.basename(file_path)}")
            return True
    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False

def main():
    instructions_dir = "/root/repo/instructions"
    
    print("Adding German translations to instruction files...")
    
    for filename in files_to_translate:
        file_path = os.path.join(instructions_dir, filename)
        
        if filename in translations:
            success = add_german_translation(file_path, translations[filename]['steps'])
            if not success:
                print(f"Failed to translate {filename}")
        else:
            print(f"No translation available for {filename}")

if __name__ == "__main__":
    main()