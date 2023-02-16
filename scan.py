import os
import argparse
import subprocess
import yaml

#function to reduce code
def update_command(cmd, output_dir, domain, subdomain_tool_output):
    var_map = {
        "{{output_dir}}": output_dir,
        # "{{domain}}": domain,
        "{{subfinder_output}}": os.path.join(output_dir, f"{domain}_subfinder.txt"),
        "{{httpx_output}}": os.path.join(output_dir, f"{domain}_httpx.txt"),
        "{{getJS_output}}": os.path.join(output_dir, f"{domain}_getJS.txt"),
    }
    for var, val in var_map.items():
        if var in cmd:
            cmd = cmd.replace(var, val)
    if subdomain_tool_output:
        cmd = cmd.replace("{{subdomain_tool_output}}", os.path.join(output_dir, f"{domain}_{subdomain_tool_output}.txt"))
    return cmd


def run_tool(tool_name, domain, output_dir,config_dir):
    #get the tool name and open that tool name .yaml file in config_dir
    try:
        with open(os.path.join(config_dir, tool_name+'.yaml'), 'r') as f:
            data = yaml.safe_load(f)
            #check if cmd key exist in yaml file to run
            if "cmd" in data[0][tool_name]:
                tool = data[0][tool_name]
                cmd = tool["cmd"].replace("{{domain}}", domain)
                #check if output_dir variable on yaml file inside cmd key
                if "{{output_dir}}" in cmd:
                    cmd = update_command(cmd, output_dir, domain, None)
                if "{{subfinder_output}}" in cmd:
                    cmd = update_command(cmd, output_dir, domain, "subfinder")
                if "{{httpx_output}}" in cmd:
                    cmd = update_command(cmd, output_dir, domain, "httpx")
                if "{{getJS_output}}" in cmd:
                    cmd = update_command(cmd, output_dir, domain, "getJS")

                print(f"Running tool: {tool['name']}")
                print(cmd)
                subprocess.run(cmd, shell=True, check=True)
            else:
                print(f"{tool_name} Command not found in Yaml file")
    except FileNotFoundError as e:
        print(f"Configuration file not found for tool '{tool_name}'")
        exit()

def run_workflow(config_dir, workflow_file, domain, output_dir):
    with open(workflow_file, 'r') as f:
        data = yaml.safe_load(f)
        for tool in data:
            run_tool(tool,domain,output_dir,config_dir)

def run_scan(config_dir, domain, output_dir=None):
    #find all .yaml tools file in config dir
    for filename in os.listdir(config_dir):
        if filename.endswith(".yaml"):
            #remove .yaml extension from the file
            tool_name_only = filename.rsplit('.', maxsplit=1)[0] 
            run_tool(tool_name_only, domain, output_dir,config_dir)


def main(workflow=False):
    parser = argparse.ArgumentParser(description="Run a set of security tools for a given domain.")
    parser.add_argument("domain", help="The domain to scan.")
    parser.add_argument("config_dir", help="The directory containing the tool configuration YAML files.")
    parser.add_argument("--output-dir", "-o", default="./output", help="The directory where tool output will be stored.")
    parser.add_argument("--workflow-file", "-w", help="The YAML file containing the tool workflow.")
    args = parser.parse_args()

    output_dir = os.path.join(args.output_dir, args.domain)
    os.makedirs(output_dir, exist_ok=True)

    if args.workflow_file:
        run_workflow(args.config_dir, args.workflow_file, args.domain, output_dir)
    else:
        run_scan(args.config_dir, args.domain, output_dir)


if __name__ == '__main__':
    main()
