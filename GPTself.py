import selfai_tool_kit as satk
import getllminput as llmi
import re

#@#@#@#@#@#@#@##@#@#@#@#@#@#@#@#@##@#@
# GPTMODEL="gpt-3.5-turbo-0125"
# GPTMODEL="gpt-4-turbo"
GPTMODEL="gpt-4o-2024-05-13"
#@#@#@#@#@#@#@##@#@#@#@#@#@#@#@#@##@#@

bestF1=0
f1_score=0
bestcode=""

satk.print_big("FIRST RUN")
satk.print_big(GPTMODEL)
#######################################################################################################################


first_requirement,outcome,first_instructions=llmi.get_input_text()

#Complile input text
input_content= f"{first_requirement}\n\n{outcome}\n\n{first_instructions}"
print(f"\033[34m{input_content}\033[0m") #BLUE

#Run input text
code_output = satk.runinput(input_content,GPTMODEL)
print(f"\033[32m{code_output}\033[0m") #GREEN

#Save output to file
filtered_code=satk.save_output_to_script_file(code_output)

#Run the script
script_output = satk.run_script()
print(f"\033[91m{script_output}\033[0m") #RED

#Check if F1 Score is given
has_f1_score,f1_score=satk.check_for_outcome(script_output)
print(f"\033[38;5;208mHas F1 score:{has_f1_score}\033[0m")  # Orange
if has_f1_score=="YES":
    satk.print_big(f1_score)
    if float(f1_score) > float(bestF1):
        print("Past Best F1 Score:",bestF1)
        print_output=f"{f1_score}>{bestF1}"
        satk.print_big(print_output)
        bestF1=f1_score
        bestcode=filtered_code
    

satk.print_big("END OF FIRST RUN")

# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP
########################################################################################################################

while float(f1_score) < 1:
    satk.do_pause()
    satk.print_big("LOOP START")
    print("Current F1 SCORE:", f1_score)
    print("Highest F1 SCORE:", bestF1)
    print("HAS F1 SCORE:", has_f1_score)
    
    if has_f1_score == "YES":
        print("-->HAS F1 SCORE!<---")
        llm_input_pass_or_fail = f"""
        This code gave an F1 score of {f1_score}. 

        For Reference:
        The BEST F1 overall score you could manage was {bestF1}
        This was produced by this code:
        {bestcode}

        Please come up with a new way to try to improve the F1 score, be it via additional data processing or a new ML model approach.
        """
    else:
        print("-->NO F1 SCORE DETECTED!<---")
        llm_input_pass_or_fail = f"""
        THIS HAS GIVEN THE FOLLOWING OUTPUT:
        {script_output}

        Look at the code you have given me and the output or error, then update the code you have given me to resolve the issue.
        This has not met the output I asked for.
        """
    #-----UPDATE DEPENDING OF HAD F1 OR NOT

    complied_instructions = f"""
    HERE IS THE CODE YOU HAVE GIVEN ME:
    {filtered_code}

    {llm_input_pass_or_fail}

    Here is the background of the task:
    {first_requirement}

    {outcome}

    {first_instructions}
    """

    #Complile input text
    print(f"\033[34m{complied_instructions}\033[0m") #BLUE

    #Run input text
    code_output = satk.runinput(complied_instructions,GPTMODEL)
    print(f"\033[32m{code_output}\033[0m") #GREEN

    #Save output to file
    filtered_code=satk.save_output_to_script_file(code_output)

    #Run the script
    script_output = satk.run_script()
    print(f"\033[91m{script_output}\033[0m") #RED

    #Check if F1 Score is given
    has_f1_score,f1_score=satk.check_for_outcome(script_output)
    print(f"\033[38;5;208mHas F1 score:{has_f1_score}\033[0m")  # Orange
    if has_f1_score=="YES":
        satk.print_big(f1_score)
        if float(f1_score) > float(bestF1):
            print("Past Best F1 Score:",bestF1)
            print_output=f"{f1_score}>{bestF1}"
            satk.print_big(print_output)
            bestF1=f1_score
            bestcode=filtered_code
        


    satk.print_big("END OF LOOP")

# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP# LOOP
########################################################################################################################
