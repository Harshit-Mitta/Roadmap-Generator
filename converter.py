

# def generate_mermaid_code(input_data):
#     # Initialize the mermaid code variable
#     mermaid_code = ''

#     # Check if the input data contains 'result'
#     if 'result' in input_data:
#         result = input_data['result']

#         # Handle generation of Mermaid code from step-by-step guide
#         if result.startswith("I can provide a text-based step-by-step guide"):
#             steps = result.split('\n\n')
#             mermaid_code = "flowchart TB\n"
#             previous_step = None
#             for step in steps:
#                 if step.startswith("**"):
#                     step_number = step.split(":")[0].replace("**", "").replace(" ", "_").strip()
#                     step_description = step.split(":")[1].strip().replace("\n", " - ").replace("**", "")
#                     step_description = step_description.replace(" - ", "<br>- ")
#                     step_description = step_description.replace('"', '\\"')  # Escape quotes for Mermaid
#                     step_node = f'{step_number}["{step_description}"]'
#                     if previous_step:
#                         mermaid_code += f"    {previous_step} --> {step_node}\n"
#                     else:
#                         mermaid_code += f"    {step_node}\n"
#                     previous_step = step_number
#             return mermaid_code

#         # Check if backticks (`) are present in the result for Mermaid code block extraction
#         if '```' in result:
#             # Split the result by backticks to get the content within backticks
#             mermaid_section = result.split('```')[1].strip()
#             # Check if 'graph TD', 'graph LR', 'graph TB', 'flowchart TD', 'flowchart LR', or 'flowchart TB' is present in the mermaid section
#             if any(keyphrase in mermaid_section for keyphrase in ['graph TD', 'graph LR', 'graph TB', 'flowchart TD', 'flowchart LR', 'flowchart TB']):
#                 # Extract the relevant Mermaid code
#                 start_phrases = ['graph TD', 'graph LR', 'graph TB', 'flowchart TD', 'flowchart LR', 'flowchart TB']
#                 for phrase in start_phrases:
#                     if phrase in mermaid_section:
#                         mermaid_code = mermaid_section.split(phrase, 1)[1].strip()
#                         mermaid_code = f'{phrase}\n{mermaid_code}'
#                         break

#     # Replace '->' with '-->' only if '-->' is not already present
#     mermaid_code = mermaid_code.replace(' -> ', ' --> ')

#     # Find the index of 'classDef' to remove extra content after it
#     index_class_def = mermaid_code.find('classDef')
#     if index_class_def != -1:
#         # Remove any content after 'classDef'
#         mermaid_code = mermaid_code[:index_class_def].strip()

#     return mermaid_code


def generate_mermaid_code(input_data):
    # Initialize the mermaid code variable
    mermaid_code = ''

    # Check if the input data contains 'result'
    if 'result' in input_data:
        result = input_data['result']

        # Handle generation of Mermaid code from step-by-step guide
        if result.startswith("I can provide a text-based step-by-step guide"):
            steps = result.split('\n\n')
            mermaid_code = "flowchart TB\n"
            previous_step = None
            for step in steps:
                if step.startswith("**"):
                    step_number = step.split(":")[0].replace("**", "").replace(" ", "_").strip()
                    step_description = step.split(":")[1].strip().replace("\n", " - ").replace("**", "")
                    step_description = step_description.replace(" - ", "<br>- ")
                    step_description = step_description.replace('"', '\\"')  # Escape quotes for Mermaid
                    step_node = f'{step_number}["{step_description}"]'
                    if previous_step:
                        mermaid_code += f"    {previous_step} --> {step_node}\n"
                    else:
                        mermaid_code += f"    {step_node}\n"
                    previous_step = step_number
            return mermaid_code

        # Check if backticks (```) are present in the result for Mermaid code block extraction
        if '```' in result:
            # Split the result by backticks to get the content within backticks
            mermaid_sections = result.split('```')
            for section in mermaid_sections:
                section = section.strip()
                if any(keyphrase in section for keyphrase in ['graph TD', 'graph LR', 'graph TB', 'flowchart TD', 'flowchart LR', 'flowchart TB']):
                    # Extract the relevant Mermaid code
                    start_phrases = ['graph TD', 'graph LR', 'graph TB', 'flowchart TD', 'flowchart LR', 'flowchart TB']
                    for phrase in start_phrases:
                        if phrase in section:
                            mermaid_code = section.split(phrase, 1)[1].strip()
                            mermaid_code = f'{phrase}\n{mermaid_code}'
                            break

    # Replace '->' with '-->' only if '-->' is not already present
    mermaid_code = mermaid_code.replace(' -> ', ' --> ')

    # Find the index of 'classDef' to remove extra content after it
    index_class_def = mermaid_code.find('classDef')
    if index_class_def != -1:
        # Remove any content after 'classDef'
        mermaid_code = mermaid_code[:index_class_def].strip()

    return mermaid_code

