import argparse
import os
import subprocess
import yaml


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Run a tool from a YAML configuration file')
    parser.add_argument('-f','--config', help='the YAML configuration file')
    parser.add_argument('-d','--domain', help='the domain name')
    args = parser.parse_args()

    # Load the YAML configuration file
    with open(args.config) as f:
        data = yaml.safe_load(f)

    # Check if the output directory exists, create it if it doesn't
    output_dir = data[0]['subfinder']['output_dir']
    if not os.path.exists(output_dir):
        output_dir = data[0]['subfinder']['output_dir'].replace('{{domain}}', args.domain)
        os.makedirs(output_dir)

    # Build the subfinder command with the domain name and output directory
    subfinder_cmd = data[0]['subfinder']['cmd'].replace('{{domain}}', args.domain)
    subfinder_cmd = subfinder_cmd.replace('{{output_dir}}', output_dir)

    # Run the subfinder command and print the output to the console
    result = subprocess.run(subfinder_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode('utf-8'))


if __name__ == '__main__':
    main()
