import os
import argparse
import subprocess
import yaml

def run_tool(tool, domain, output_dir):
    cmd = tool["cmd"].replace("{{domain}}", domain)
    if "{{output_dir}}" in cmd:
        cmd = cmd.replace("{{output_dir}}", output_dir)

    print(f"Running tool: {tool['name']}")
    subprocess.run(cmd, shell=True, check=True)


def run_scan(config_dir, domain, output_dir=None):
    for filename in os.listdir(config_dir):
        if filename.endswith(".yaml"):
            with open(os.path.join(config_dir, filename), 'r') as f:
                data = yaml.safe_load(f)
            for tool in data[0]:
                if "cmd" in data[0][tool]:
                    run_tool(data[0][tool], domain, output_dir)
                else:
                    print(f"{tool} Command not found in Yaml file")


def main():
    parser = argparse.ArgumentParser(description="Run a set of security tools for a given domain.")
    parser.add_argument("domain", help="The domain to scan.")
    parser.add_argument("config_dir", help="The directory containing the tool configuration YAML files.")
    parser.add_argument("--output-dir", "-o", default="./output", help="The directory where tool output will be stored.")
    args = parser.parse_args()

    output_dir = os.path.join(args.output_dir, args.domain)
    os.makedirs(output_dir, exist_ok=True)

    run_scan(args.config_dir, args.domain, output_dir)

if __name__ == '__main__':
    main()
