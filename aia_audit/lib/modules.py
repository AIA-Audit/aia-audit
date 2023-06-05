import json
import os

from aia_audit.lib.database import Database

def get_modules_from_folder():
    modules = []
    for module in os.listdir(os.path.dirname(__file__) + "/../modules"):
        if os.path.isdir(os.path.dirname(__file__) + "/../modules/" + module):
            with open(os.path.dirname(__file__) + "/../modules/" + module + "/data.json") as json_file:
                modules.append(json.load(json_file))
    db_modules = get_modules_from_database()
    for module in modules:
        if module["name"] in [x["name"] for x in db_modules]:
            module["installed"] = "yes"
            for db_module in db_modules:
                if db_module["name"] == module["name"]:
                    print (db_module)
                    module["module_settings"] = db_module["settings"]
        else:
            module["installed"] = "no"
    return modules

def get_modules_from_database():
    modules = []
    database = Database()
    for module in database.query_select("SELECT name, import, settings FROM modules"):
        modules.append({"name": module[0], "import": module[1], "settings": json.loads(module[2])})
    return modules

def install_module_from_folder(module):
    if module in get_modules_from_database():
        return "Module is already installed"
    if not os.path.isdir(os.path.dirname(__file__) + "/../modules/" + module):
        return "Module does not exist"
    with open(os.path.dirname(__file__) + "/../modules/" + module + "/data.json") as json_file:
        module_data = json.load(json_file)
    database = Database()
    database.insert("modules", "name, version, settings, import", "'" + module_data["name"] + "', '" + module_data["version"] + "', '" + json.dumps(module_data["module_settings"]) + "', '" + module_data["module_import"] + "'")
    return "Module installed"

def uninstall_module_from_database(module):
    modules_from_db = get_modules_from_database()
    if module not in [x["name"] for x in modules_from_db]:
        return "Module is not installed"
    database = Database()
    database.query("DELETE FROM modules WHERE name = '" + module + "'")
    return "Module uninstalled"