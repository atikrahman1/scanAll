import re

def find_variables(command):
    # Find all the variables enclosed within {{ }}
    variables = re.findall(r"\{\{(\w+)\}\}", command)
    return variables



print(find_variables("cat {{getJS_output}} | xargs -I% python386 E:\\PENTEST-POCS\\tools\\secretfinder\\SecretFinder.py -i % -g 'jquery;bootstrap;api.google.com' -o cli >> {{output_dir}}/{{domain}}_SecretFinder.txt"))