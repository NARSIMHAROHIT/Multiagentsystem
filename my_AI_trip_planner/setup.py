from setuptools import setup,find_packages
from typing import List
def get_requirements()->List[str]:
    """
    Docstring for get_requirements
    
    This function will return the list of requirements
    """
    requirements_list : List[str] = []
    try:
        #Open and read the requirements.txt file
        with open ('requirements.txt','r') as file:
            #read the lines in the file  and store them in lin lines
            lines = file.readlines()
            #interate and process through each ine in lines
            for line in lines:
                #strip the white space and new line character
                requirement = line.strip()
                #ingnore the empty lines and -e
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("your requirements.txt file is not found. Please make sure it is in the same directory as setup.py")

    return requirements_list
print(get_requirements())
setup(
    name = 'my_AI_trip_planner',
    version = '0.1',
    packages = find_packages(),
    install_requires = get_requirements(),
    author='Rohit Avadhanula',
    description='A multi-agent system for AI trip planning',
    author_email='20n31a4321@gmail.com'
    )