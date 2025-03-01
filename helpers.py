def generate_models_to_test(models, func, system_prompt):
    return [
        {'name': model, 'func': func, 'system_prompt': system_prompt}
        for model in models
    ]
