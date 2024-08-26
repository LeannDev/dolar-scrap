def match_models_with_data(json_data, names_db):
    model_mappings = {}
    
    for model, casa in names_db.items():
        for data in json_data:
            if data['casa'] == casa:
                model_mappings[model] = data
                break
    
    return model_mappings