# medicine_data.py

medicine_db = {
    "Fever": {
        "medicines": ["Paracetamol"],
        "alternatives": ["Crocin", "Calpol", "Dolo 650"],
        "precaution": "Drink fluids and take rest. Avoid alcohol.",
        "not_for_children": [],
        "allergy_risk": ["Paracetamol"],
        "timing": "After food, Morning/Afternoon/Evening"
    },
    "Headache": {
        "medicines": ["Aspirin"],
        "alternatives": ["Brufen", "Combiflam"],
        "precaution": "Avoid stress, loud noise, and prolonged screen time.",
        "not_for_children": ["Aspirin"],
        "allergy_risk": ["Aspirin", "Ibuprofen"],
        "timing": "After food, Morning/Evening"
    },
    "Cold": {
        "medicines": ["Cetirizine"],
        "alternatives": ["Levocetirizine", "Loratadine"],
        "precaution": "Avoid dust, keep warm, drink warm fluids.",
        "not_for_children": [],
        "allergy_risk": [],
        "timing": "Before food, Night"
    },
    "Cough": {
        "medicines": ["Benadryl"],
        "alternatives": ["Ascoril", "Corex"],
        "precaution": "Avoid cold drinks and smoking.",
        "not_for_children": ["Corex"],
        "allergy_risk": ["Benadryl"],
        "timing": "After food, Night"
    },
    "Stomach Pain": {
        "medicines": ["Ranitidine"],
        "alternatives": ["Pantoprazole", "Omeprazole"],
        "precaution": "Avoid spicy food, stay hydrated.",
        "not_for_children": [],
        "allergy_risk": ["Ranitidine"],
        "timing": "Before food, Morning"
    },
    "Back Pain": {
        "medicines": ["Ibuprofen"],
        "alternatives": ["Diclofenac", "Naproxen"],
        "precaution": "Avoid heavy lifting, apply heat/cold packs.",
        "not_for_children": [],
        "allergy_risk": ["Ibuprofen", "Diclofenac"],
        "timing": "After food, Morning/Evening"
    },
    "Sore Throat": {
        "medicines": ["Lozenges", "Paracetamol"],
        "alternatives": ["Strepsils", "Dolo 650"],
        "precaution": "Drink warm fluids, avoid cold drinks.",
        "not_for_children": [],
        "allergy_risk": ["Paracetamol"],
        "timing": "After food, Morning/Night"
    },
    "Diarrhea": {
        "medicines": ["ORS", "Loperamide"],
        "alternatives": ["Dioralyte"],
        "precaution": "Stay hydrated, avoid oily food.",
        "not_for_children": [],
        "allergy_risk": ["Loperamide"],
        "timing": "After food, As needed"
    },
    "Constipation": {
        "medicines": ["Lactulose"],
        "alternatives": ["Docusate", "Senna"],
        "precaution": "Drink water, eat fiber-rich foods.",
        "not_for_children": [],
        "allergy_risk": ["Senna"],
        "timing": "Before food, Morning/Night"
    },
    "Acidity": {
        "medicines": ["Ranitidine"],
        "alternatives": ["Omeprazole", "Pantoprazole"],
        "precaution": "Avoid spicy/fatty foods, avoid lying immediately after meals.",
        "not_for_children": [],
        "allergy_risk": ["Ranitidine"],
        "timing": "Before food, Morning"
    },
    "Vomiting": {
        "medicines": ["Ondansetron"],
        "alternatives": ["Domperidone", "Metoclopramide"],
        "precaution": "Stay hydrated, eat bland food.",
        "not_for_children": [],
        "allergy_risk": ["Ondansetron"],
        "timing": "After food, As needed"
    },
    "Skin Rash": {
        "medicines": ["Hydrocortisone Cream"],
        "alternatives": ["Betamethasone Cream", "Clobetasol Cream"],
        "precaution": "Avoid scratching, keep area clean.",
        "not_for_children": [],
        "allergy_risk": ["Hydrocortisone"],
        "timing": "Topical, 2-3 times/day"
    },
    "Muscle Pain": {
        "medicines": ["Paracetamol", "Ibuprofen"],
        "alternatives": ["Diclofenac Gel", "Naprosyn"],
        "precaution": "Rest and mild stretching.",
        "not_for_children": [],
        "allergy_risk": ["Ibuprofen"],
        "timing": "After food, Morning/Evening"
    },
    "Allergy": {
        "medicines": ["Cetirizine"],
        "alternatives": ["Levocetirizine", "Loratadine"],
        "precaution": "Avoid allergen exposure.",
        "not_for_children": [],
        "allergy_risk": [],
        "timing": "After food, Morning/Night"
    },
    "Asthma Attack": {
        "medicines": ["Salbutamol Inhaler"],
        "alternatives": ["Levosalbutamol", "Formoterol"],
        "precaution": "Avoid triggers, use inhaler as prescribed.",
        "not_for_children": [],
        "allergy_risk": [],
        "timing": "As needed"
    },
    "High BP": {
        "medicines": ["Amlodipine"],
        "alternatives": ["Losartan", "Metoprolol"],
        "precaution": "Monitor salt intake, exercise regularly.",
        "not_for_children": [],
        "allergy_risk": ["Amlodipine"],
        "timing": "Morning"
    },
    "Low BP": {
        "medicines": ["Fludrocortisone"],
        "alternatives": ["Midodrine"],
        "precaution": "Drink water, increase salt intake if advised.",
        "not_for_children": [],
        "allergy_risk": [],
        "timing": "Morning"
    },
    "Diabetes": {
        "medicines": ["Metformin"],
        "alternatives": ["Glipizide", "Glibenclamide"],
        "precaution": "Monitor blood sugar, avoid sugary foods.",
        "not_for_children": [],
        "allergy_risk": ["Metformin"],
        "timing": "After food, Morning/Night"
    },
    "Anemia": {
        "medicines": ["Iron Supplements"],
        "alternatives": ["Ferrous Sulfate", "Ferrograd"],
        "precaution": "Eat iron-rich foods, avoid tea with supplements.",
        "not_for_children": [],
        "allergy_risk": [],
        "timing": "After food, Morning"
    },
    "Joint Pain": {
        "medicines": ["Ibuprofen"],
        "alternatives": ["Diclofenac", "Naprosyn"],
        "precaution": "Avoid heavy lifting, apply hot/cold packs.",
        "not_for_children": [],
        "allergy_risk": ["Ibuprofen"],
        "timing": "After food, Morning/Evening"
    },
    "Insomnia": {
        "medicines": ["Melatonin"],
        "alternatives": ["Zolpidem", "Temazepam"],
        "precaution": "Avoid caffeine and screen before bed.",
        "not_for_children": [],
        "allergy_risk": [],
        "timing": "Night"
    },
    "Anxiety": {
        "medicines": ["Escitalopram"],
        "alternatives": ["Sertraline", "Fluoxetine"],
        "precaution": "Practice relaxation techniques.",
        "not_for_children": [],
        "allergy_risk": ["Escitalopram"],
        "timing": "Morning"
    },
    "Depression": {
        "medicines": ["Fluoxetine"],
        "alternatives": ["Sertraline", "Escitalopram"],
        "precaution": "Consult therapist and exercise.",
        "not_for_children": [],
        "allergy_risk": ["Fluoxetine"],
        "timing": "Morning"
    },
    "Migraine": {
        "medicines": ["Sumatriptan"],
        "alternatives": ["Rizatriptan", "Zolmitriptan"],
        "precaution": "Avoid bright lights and triggers.",
        "not_for_children": [],
        "allergy_risk": ["Sumatriptan"],
        "timing": "As needed"
    },
    "Ear Pain": {
        "medicines": ["Amoxicillin"],
        "alternatives": ["Cefuroxime", "Azithromycin"],
        "precaution": "Keep ear dry, avoid inserting objects.",
        "not_for_children": [],
        "allergy_risk": ["Amoxicillin"],
        "timing": "After food, Morning/Evening"
    },
    "Eye Infection": {
        "medicines": ["Ofloxacin Eye Drops"],
        "alternatives": ["Ciprofloxacin Eye Drops"],
        "precaution": "Avoid touching eyes, wash hands frequently.",
        "not_for_children": [],
        "allergy_risk": ["Ofloxacin"],
        "timing": "As prescribed"
    },
    "Toothache": {
        "medicines": ["Paracetamol"],
        "alternatives": ["Ibuprofen", "Aspirin"],
        "precaution": "Avoid very hot/cold food.",
        "not_for_children": ["Aspirin"],
        "allergy_risk": ["Paracetamol", "Ibuprofen"],
        "timing": "After food, Morning/Evening"
    },
    "Cold Sores": {
        "medicines": ["Acyclovir Cream"],
        "alternatives": ["Valacyclovir", "Famciclovir"],
        "precaution": "Avoid touching sores, maintain hygiene.",
        "not_for_children": [],
        "allergy_risk": ["Acyclovir"],
        "timing": "Topical, 3-4 times/day"
    },
    "Urinary Tract Infection": {
        "medicines": ["Nitrofurantoin"],
        "alternatives": ["Cefixime", "Ciprofloxacin"],
        "precaution": "Drink plenty of water, avoid irritants.",
        "not_for_children": [],
        "allergy_risk": ["Nitrofurantoin"],
        "timing": "After food, Morning/Evening"
    },
    "Cold Feet/Hands": {
        "medicines": ["Nifedipine"],
        "alternatives": ["Amlodipine"],
        "precaution": "Keep warm, improve circulation.",
        "not_for_children": [],
        "allergy_risk": ["Nifedipine"],
        "timing": "Morning"
    },
    "Heartburn": {
        "medicines": ["Omeprazole"],
        "alternatives": ["Ranitidine", "Pantoprazole"],
        "precaution": "Avoid spicy food, eat small meals.",
        "not_for_children": [],
        "allergy_risk": ["Omeprazole"],
        "timing": "Before food, Morning"
    },
    "Nausea": {
        "medicines": ["Ondansetron"],
        "alternatives": ["Domperidone"],
        "precaution": "Stay hydrated, eat bland food.",
        "not_for_children": [],
        "allergy_risk": ["Ondansetron"],
        "timing": "After food, As needed"
    },
    "Skin Infection": {
        "medicines": ["Clindamycin Cream"],
        "alternatives": ["Mupirocin Cream"],
        "precaution": "Keep area clean and dry.",
        "not_for_children": [],
        "allergy_risk": ["Clindamycin"],
        "timing": "Topical, 2-3 times/day"
    },
    "Cold Sweats": {
        "medicines": ["Atropine"],
        "alternatives": ["Glycopyrrolate"],
        "precaution": "Consult doctor if persistent.",
        "not_for_children": [],
        "allergy_risk": ["Atropine"],
        "timing": "As prescribed"
    },
    "Fatigue": {
        "medicines": ["Vitamin B12"],
        "alternatives": ["Iron Supplements", "Multivitamins"],
        "precaution": "Rest and balanced diet.",
        "not_for_children": [],
        "allergy_risk": [],
        "timing": "Morning"
    },
    "Cold Hands/Feet": {
        "medicines": ["Nifedipine"],
        "alternatives": ["Amlodipine"],
        "precaution": "Keep warm and exercise.",
        "not_for_children": [],
        "allergy_risk": ["Nifedipine"],
        "timing": "Morning"
    }
    # Continue adding remaining symptoms as needed...
}
