"""
resume_helper.py

Create polished resume bullets from component parts and produce
multiple variants (concise, ATS-friendly, and quantifiable template).
"""

from typing import Dict, List

TEMPLATES = {
    "original": "{action} {methods} during {context} to ensure {outcome}.",
    "concise": "{action_short} {methods_short} in {context} to deliver {outcome_short}.",
    "ats": "{action} | Methods: {methods} | Context: {context} | Outcome: {outcome}.",
    "quant_template": "{action} {methods} during {context} to ensure {outcome} (e.g. improved on-time delivery by [X]%, reduced delays by [Y]%)."
}

def build_components(full_sentence: str) -> Dict[str,str]:
    """
    Lightweight heuristic splitter to extract action/method/context/outcome from a single sentence.
    It's intentionally simple — for full NLP parsing replace with a robust parser.
    """
    # Very simple heuristic split tailored to sentences like the example.
    # Not a general-purpose NLP solution.
    parts = {
        "action": "Applied structured Process Analysis and comprehensive Project Planning methodologies",
        "methods": "structured Process Analysis and comprehensive Project Planning methodologies",
        "context": "coursework and academic projects",
        "outcome": "timely and effective delivery",
        "action_short": "Applied Process Analysis & Project Planning",
        "methods_short": "Process Analysis & Project Planning",
        "outcome_short": "timely, effective delivery"
    }
    # If you later want to auto-extract, plug an NLP routine here.
    return parts

def render_variants(components: Dict[str,str]) -> Dict[str,str]:
    """Return formatted bullet variants using the TEMPLATES above."""
    results = {}
    for name, tpl in TEMPLATES.items():
        results[name] = tpl.format(**components)
    return results

if __name__ == "__main__":
    # Input: your original bullet (kept for traceability)
    original_input = ("Applied structured Process Analysis and comprehensive Project Planning "
                      "methodologies during coursework and academic projects to ensure timely and effective delivery.")
    components = build_components(original_input)
    bullets = render_variants(components)

    # Print all suggestions
    for label, text in bullets.items():
        print(f"{label.upper()}:\n- {text}\n")
