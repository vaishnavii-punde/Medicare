def suggest_medicine(symptoms):
    if 'fever' in symptoms.lower():
        return 'Paracetamol'
    elif 'cough' in symptoms.lower():
        return 'Cough Syrup'
    else:
        return 'Please consult a doctor'
