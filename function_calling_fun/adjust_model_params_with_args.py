from sys import argv

def prompt_params():
    global instructions
    global reasoningEffort
    global developerCommand

    if len(argv)<2:
        instructions = ""
    else:
        instructions = argv[1]

    if len(argv)<3:
        reasoningEffort = "medium"
    else:
        reasoningEffort = argv[3]

    if len(argv)<4:
        developerCommand = ""
    else:
        developerCommand = argv[3]
    
    model_params = {
        "instructions": instructions,
        "reasoningEffort": reasoningEffort,
        "developerCommand": developerCommand
    }

    return model_params