"""
Sphere result integration with ATF
"""
import os
import requests

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


path = "https://tdmsapi.zebra.lan/api/"

session = requests.Session()


def new_execution(station_name, user_name):
    """
    Create a new execution id.
    :param station_name:
    :param user_name:
    :return:
    """
    new_execution_url = path + "CommonExecution/NewExecution"
    new_execution_json = {
        "stationName": station_name,
        "operatorName": user_name,
        "loopCount": 1,
        "duttype": "",
        "testDataSource": "ZSB Mobile Automation",
        "resultsSchema": ""
    }

    api_response = session.post(new_execution_url, json=new_execution_json, timeout=60)
    exec_id = api_response.json()

    return exec_id

def insert_device(exec_id, version, hardware_name, firmware_name, serial_number, communication_details):
    """
    Insert the information of printer, station etc.
    :param hardware_name:
    :param firmware_name:
    :param serial_number:
    :param communication_details:
    :return:
    """
    insert_device_url = path + "ExecEngineDevice/Insert_Device"
    insert_device_json = {
        "executionId": exec_id,
        "version": version,
        "hardwareID": 0,
        "firmwareID": 0,
        "hardwareName": hardware_name,
        "firmwareName": firmware_name,
        "serialNumber": serial_number,
        "communicationDetails": communication_details,
        "project": "ZSB Automation",
        "timings": "",
        "dependencies": "",
        "learnMode": "",
        "basePath": ""
    }
    session.put(insert_device_url, json=insert_device_json, timeout=60)

# where is this one
def insert_tool_version(execid,version):
    """
    Insert the tool and version.
    :return:
    """
    insert_tool_version_url = path + "CommonExecution/InsertToolVersion"
    insert_tool_version_json = {
        "executionId": execid,
        "appName": "Airtest",
        "version": version
    }
    session.put(insert_tool_version_url, json=insert_tool_version_json, timeout=60)

def start_execution_loop(exec_id):
    """
    Start the execution in loop.
    :return:
    """
    start_execution_loop_url = path + "ExecutionLoop/StartExecutionLoop"
    start_execution_loop_json = {
        "executionId": exec_id,
        "loopIndex": 1
    }
    session.put(start_execution_loop_url, json=start_execution_loop_json, timeout=60)

def start_main(exec_id):
    start_main_loop_url = path + "ExecEngineMain/StartMain"
    start_main_json={
        "executionId": exec_id,
        "loopIndex": 1,
        "leftId": 0
    }
    session.put(start_main_loop_url, json=start_main_json, timeout=60)

def end_main(exec_id,exec_time):
    start_main_loop_url = path + "ExecEngineMain/EndMain"
    start_main_json={
        "executionId": exec_id,
        "loopIndex": 0,
        "leftId": 0,
        "executionTime": exec_time
    }
    session.put(start_main_loop_url, json=start_main_json, timeout=60)

def insert_case_results(execid,loopindex,leftId,reportext,errormsg,result,exec_time):
    """
    Update the execution result for each case.
    :param total_suite_result_list:
    :return:
    """
    insert_case_results_url = path + "ExecEngineCase/Insert_CaseResult"

    insert_case_results_loop_json={
        "executionId": execid,
        "loopIndex": loopindex,
        "leftID": leftId,
        "result": result,
        "executionTime": exec_time,
        "reportText": reportext,
        "errorMessage": errormsg

    }

    session.post(insert_case_results_url, json=insert_case_results_loop_json, timeout=60)


def upload_case_files(self, execid, output_directory):
    """
    Upload the files in local, like selenium report, ATF report etc.
    :param output_directory:
    :return:
    """
    count=0
    for file in os.listdir(output_directory):
        ext = os.path.splitext(file)
        if ext[1] in ('.log', '.html', '.xml'):
            with open(os.path.join(output_directory, file), "rb") as logs:
                files = {"file": logs}
                upload_case_files_url = f"{self.path}FileSave/UploadCaseFile"
                params = {
                    "executionId":execid ,
                    "caseId": 1,
                    "leftID": count,
                    "fileName": ext[0]
                }
                session.post(upload_case_files_url, files=files, timeout=60, params=params)
            count += 2

def end_execution_loop(execid):
    """
    End execution in loop.
    :return:
    """
    end_execution_loop_url = path + "ExecutionLoop/EndExecutionLoop"
    end_execution_loop_json = {
        "executionId": execid,
        "loopIndex": 1
    }
    session.post(end_execution_loop_url, json=end_execution_loop_json, timeout=60)

def end_execution(self,exec_id):
    """
    Stop the execution with execution id.
    :return:
    """
    end_execution_url = self.path + "CommonExecution/EndExecution/" + str(exec_id)
    session.post(end_execution_url, timeout=60)


def get_test_case(exec_id):
    url = path+"ExecEngineHierarchy/Get_CasesHierarchy/"+str(exec_id)
    # print(u)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    # response = requests.get(url,verify=False)
    # print(response)
    # print(response.content)

    resp = session.get(url,verify=False)
    print(resp)
    print(resp.content)



get_test_case(912240)