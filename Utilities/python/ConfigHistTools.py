import os
import json
import imp
import glob
import copy
import logging

def readPythonOrJson(file_path):
    if ".pyc" in file_path[-4:] or ".jsonc" in file_path[-6:]:
        return ""
    if ".py" not in file_path[-3:] and ".json" not in file_path[-5:]:
        if os.path.isfile(file_path+".py"):
            file_path = file_path +".py"
        elif os.path.isfile(file_path+".json"): 
            file_path = file_path +".json"
        else:
            raise ValueError("Configuration file %s(.py/json) not found!" % file_path)
    return file_path

def readAllInfo(file_path):
    info = {}
    for info_file in glob.glob(file_path):
        logging.debug("Trying to read info from %s" % info_file)
        file_info = readInfo(info_file)
        if file_info:
            info.update(file_info)
    return info

def readInfo(file_path):
    try:
        file_path = readPythonOrJson(file_path)
    # Fall back to single analysis-wide definition (not different by selection)
    except ValueError:
        if "/" in file_path:
            file_path = file_path.rsplit("/", 1)[0]
        pass
        file_path = readPythonOrJson(file_path)
    info = {}
    if not os.path.isfile(file_path):
        return info
    if ".py" in file_path[-3:]:
        file_info = imp.load_source(file_path.split("/")[-1], file_path)
        info = file_info.info
    else:
        info = readJson(file_path)
    return info

def readJson(json_file_name):
    json_info = {}
    with open(json_file_name) as json_file:
        try:
            json_info = json.load(json_file)
        except ValueError as err:
            print "Error reading JSON file %s. The error message was:" % json_file_name 
            print(err)
    return json_info

def getHistType(manager_path, selection, hist_name):
    hist_file = "/".join([manager_path, 
        "ZZ4lRun2DatasetManager", "PlotObjects", selection]) 
    all_hist_info = readInfo(hist_file)
    if hist_name not in all_hist_info.keys():
        raise ValueError("Invalid hist name '%s'. Must be defined in %s"
                % (hist_name, hist_file))
    hist_info = all_hist_info[hist_name]["Initialize"]
    return hist_info["type"]

def getHistBinInfo(manager_path, selection, hist_name):
    bin_info = {}
    hist_file = "/".join([manager_path, 
        "ZZ4lRun2DatasetManager", "PlotObjects", selection]) 
    all_hist_info = readInfo(hist_file)
    if hist_name not in all_hist_info.keys():
        raise ValueError("Invalid hist name '%s'. Must be defined in %s"
                % (hist_name, hist_file))
    hist_info = all_hist_info[hist_name]["Initialize"]
    if "TH1" in hist_info["type"]:
        if len(hist_info)==2:
            args=['nbins']
        else:
            args = ['nbins', 'xmin', 'xmax']
    elif "TH2" in hist_info["type"]:
        args = ['nbinsx', 'xmin', 'xmax', 'nbinsy', 'ymin', 'ymax']
    else:
        raise ValueError("Invalid histogram type %s" % hist_info['type'])
        
    for key in args:
        bin_info.update({key : hist_info[key]})
    return bin_info

def getAllHistNames(manager_path, selection):
    bin_info = {}
    hist_file = "/".join([manager_path, 
        "ZZ4lRun2DatasetManager", "PlotObjects", selection]) 
    all_hist_names = readInfo(hist_file).keys()

    return all_hist_names
