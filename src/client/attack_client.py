import os
import json
import requests

from typing import List, Optional
from business_object.attack.attack_factory import AttackFactory
from business_object.attack.abstract_attack import AbstractAttack
from utils.singleton import Singleton

END_POINT = "/attack"


class AttackClient(metaclass=Singleton):
    def __init__(self) -> None:
        # Using an environment variable defined in the .env file
        self.__HOST = os.environ["HOST_WEBSERVICE"]

    def get_attack(self, id: int) -> Optional[AbstractAttack]:
        """
        Get a specific attack from the webservice by calling the GET endpoint
        with a specific resource identifier.Do not raise any
        exception if any attack is found, just return None.

        :param id: attack id wanted
        :type id: int
        :return: The attack object with all value if the attack is found.
                 else None
        :rtype: AbstractAttack
        """
        url = f"{self.__HOST}{END_POINT}/{id}"
        print("GET  " + url + "\n")
        req = requests.get(url)

        attack = None

        # Check if the request is ok
        if req.status_code == 200:
            raw_attack = req.json()

            print("Réponse JSON obtenue :\n" + json.dumps(raw_attack, indent=2) + "\n")
            instantiate_attack(type=raw_attack[attack_type],id=raw_attack[id],power=raw_attack[power],name=raw_attack[name],description=raw_attack[description],accuracy=raw_attack[accuracy],element=raw_attack[element])
            # TODO
            #   create an attack using the data contained in the json
            #   see class AttackFactory to do this
            print(attack)
        return attack


# Execute Code When the File Runs as a Script
if __name__ == "__main__":
    # To load environment variables contained in the .env file
    import dotenv

    dotenv.load_dotenv(override=True)

    attack_client = AttackClient()

    attack_id = 1
    attack_client.get_attack(attack_id)

def get_all_attacks(self, limit, offset)->List[AbstractAttack]:
    params={}
    if limit>0:
        params["limit"]=limit
    if offset >0:
        params["offset"]=offset
    req.request.get(f"{self._HOST}{END_POINT}", params=params)
    all_attacks = []
    if req.status_code==200:
        raw_attacks=req.json()["results"]
        attack_factory=AttackFactory()
        for raw_attack in raw_attacks:
            attack=attack_factory.instatntiate_attack(
                type=raw_attack["attack_type"],
                id=raw_attack["id"],
                name=raw_attack["name"],
        )
        if attack:
            attacks.append(attack)
    print(attacks)
    return attacks

def create_attack(self, attack:AbstractAttack)->bool:
    """ Creates a new attack calling the web service"""
    playlod={
        "name": attack.name,
        "id": attack.id,
        "power": attack.power,
        "description":attack.description,
        "accuracy":attack.accuracy,
        "element":attack.element
    }
    # Prepare Arguments
    url = f"{self.__HOST}{END_POINT}"
    headers = {'accept': 'application/json'}
    data = {AbstractAttack}

    # Launch Request
    post = requests.post(url, headers=headers, json = data)
    if req.status_code == 201:
            raw_attack = req.json()

            print("Attaque Créée")
    return attack

def update_attack(AbstractAttack):
    """modifies it in the web service"""
    # Prepare Arguments
    url = f"{self.__HOST}{END_POINT}/"
    headers = {'accept': 'application/json'}
    data = {AbstractAttack}

    # Launch Request
    put = requests.put(url, headers=headers, json = data)

def delete_attack(AbstractAttack):
    """deletes it in the web service"""
    # Prepare Arguments
    url = f"{self.__HOST}{END_POINT}/"
    headers = {'accept': 'application/json'}
    data = {AbstractAttack}

    # Launch Request
    delete = requests.delete(url, headers=headers, json = data)
    
