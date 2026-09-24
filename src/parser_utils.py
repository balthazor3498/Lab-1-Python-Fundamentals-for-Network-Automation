import logging
import json
import yaml
import csv
import xml.etree.ElementTree as ET

#success log
def file_success(file_type):
    logging.info(f"PARSE_{file_type.upper()}_SUCCESS")

#error log
def file_error(file_type):
    logging.error(f"PARSE_{file_type.upper()}_ERROR")


#json file parsing
def parse_json(file_json):
    try:
        with open(file_json, 'r') as file:
            data = json.load(file)
        file_success("json")
        return data
    except FileNotFoundError:
        print(f"{file_json} not found - file doesn't exist")
        file_error("json")
        return []
    except json.JSONDecodeError:
        print(f"{file_json} is not a valid JSON file")
        file_error("json")
        return []
    except Exception as e:
        print(f"An error occurred while parsing {file_json}: {e}")
        file_error("json")
        return []

#yaml file parsing
def parse_yaml(file_yaml):
    try:
        with open(file_yaml, 'r') as file:
            data = yaml.safe_load(file)
        file_success("yaml")
        return data
    except FileNotFoundError:
        print(f"{file_yaml} not found - file doesn't exist")
        file_error("yaml")
        return []
    except yaml.YAMLError:
        print(f"{file_yaml} is not a valid YAML file")
        file_error("yaml")
        return []

#csv file parsing
def parse_csv(file_csv):
    try:
        with open(file_csv, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            contents = [row for row in csv_reader]
            file_success('csv')
            return contents
    except FileNotFoundError:
        print(f"{file_csv} not found - file doesn't exist")
        file_error("csv")
        return []
    except csv.Error:
        print(f"{file_csv} is not a valid CSV file")
        file_error("csv")
        return []   

#xml file parsing
def parse_xml(file_xml):
    try:
        tree = ET.parse(file_xml)
        root = tree.getroot()
        file_success('xml')
        return root
    except FileNotFoundError:
        print(f"{file_xml} not found - file doesn't exist")
        file_error("xml")
        return []
    except ET.ParseError as e:
        print(f"{file_xml} is not a valid XML file")
        file_error("xml")
        return []

#testing output for each parser

#json test
#print(parse_json("data/devices.json"))

#yaml test
#print(parse_yaml("data/interfaces.yaml"))

#csv test
#print(parse_csv("data/inventory.csv"))

#xml test
#print(parse_xml("data/vlans.xml"))
