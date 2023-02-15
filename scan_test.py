import yaml
import subprocess
import os

def run_workflow(workflow_file, domain, output_dir):
    with open(workflow_file, 'r') as f:
        workflow = yaml.safe_load(f)

    outputs = {}
    for step in workflow:
        tool = step['tool']
        inputs = {}
        for inp in step.get('inputs', []):
            key = inp['name']
            if 'from' in inp:
                source_tool, source_key = inp['from'].split('.')
                inputs[key] = outputs[source_tool][source_key]
            else:
                inputs[key] = inp['value']
        outputs[tool] = {}

        for outp in step.get('outputs', []):
            key = outp['name']
            output_value = outp.get('value', None)
            if output_value is not None:
                outputs[tool][key] = output_value
            else:
                outputs[tool][key] = os.path.join(output_dir, outp['filename'].format(domain=domain))

        cmd = tool['cmd'].format(**inputs).split()
        print(f"Running tool: {tool['name']} with inputs: {inputs} and outputs: {outputs[tool]}")
        subprocess.run(cmd, cwd=output_dir, check=True)

        if 'cleanup' in step:
            for file in step['cleanup']:
                file_path = os.path.join(output_dir, file.format(domain=domain))
                if os.path.isfile(file_path):
                    os.remove(file_path)

# Sample workflow.yaml file
workflow_yaml = '''
- tool: subfinder
  inputs:
    - name: domain
      value: example.com
  outputs:
    - name: subdomains_file
      filename: "{domain}_subdomains.txt"
- tool: amass
  inputs:
    - name: domain
      value: example.com
    - name: subdomains_file
      from: subfinder.subdomains_file
  outputs:
    - name: subdomains_file
      filename: "{domain}_subdomains.txt"
- tool: nmap
  inputs:
    - name: domain
      value: example.com
    - name: ports
      value: 80,443
    - name: subdomains_file
      from: amass.subdomains_file
  outputs:
    - name: nmap_output_file
      filename: "{domain}_nmap.txt"
  cleanup:
    - "{domain}_subdomains.txt"
'''

# Usage example
if __name__ == '__main__':
    domain = 'example.com'
    config_dir = 'config'
    workflow_file = 'workflow.yaml'
    output_dir = 'output'

    os.makedirs(output_dir, exist_ok=True)

    run_workflow(workflow_file, domain, output_dir)
