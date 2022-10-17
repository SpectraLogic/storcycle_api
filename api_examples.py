# coding: utf-8

"""
    Spectra Logic Corporation Software

    StorCycle® REST API Copyright © 2020 Spectra Logic Corporation  # noqa: E501

    The version of the OpenAPI document: 0.1
    Contact: developer@spectralogic.com
"""

# Used for Python 2/3 compatibility
from __future__ import absolute_import

import os.path
import urllib3
import time

# Used to show a "pretty" print of the API response payloads
from pprint import pprint

# Necessary imports for using the API
import openapi_client
from openapi_client.models.api_storage_location_nas import ApiStorageLocationNas  # noqa: E501
from openapi_client.models.api_project_scan import ApiProjectScan  # noqa: E501
from openapi_client.models.api_project_archive import ApiProjectArchive  # noqa: E501
from openapi_client.models.api_project_restore import ApiProjectRestore  # noqa: E501
from openapi_client.rest import ApiException

# Suppress certificate warnings in output
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

########################################
# Setup general variables. Individual project names, filters, etc must be changed within each example.
# Note: Change these variables to appropriate local variables to run examples
example_host = "https://localhost/openapi"
example_password = "example_password"
example_username = "example_username"
email_on_complete = 'example@example.com'

# This time will vary based on the number of files in the directory tree. Adjust the time to be long enough such that a
# scan job finishes before the archive is attempted and the archive is finished before the restore is attempted.
sleep_time_seconds = 10

# Note: If the example directory tree is not created, these example variables will need to be changed.
example_directory_root = os.path.join(os.path.abspath(os.sep), "ApiPythonExampleData")

# These should be distinct file paths available on the host machine running StorCycle.
example_source_share_optional = os.path.join(example_directory_root, "example-source-storage-location-optional")
example_source_share = os.path.join(example_directory_root, "example-source-storage-location")
example_target_share_optional = os.path.join(example_directory_root, "example-target-storage-location-optional")
example_target_share = os.path.join(example_directory_root, "example-target-storage-location")
example_scan_working_directory = os.path.join(os.sep, "WorkingDirectory")

example_include_directory = "IncludeDirectory"
example_exclude_directory = "ExcludeDirectory"

# End of general variables that need to be changed for your environment.
########################################

# Example directory tree at the C:/ level.
# You need to create this directory structure populated with some files in the source subdirectories.

# C:/ApiPythonExampleData/example-source-storage-location/WorkingDirectory/ExcludeDirectory
# C:/ApiPythonExampleData/example-source-storage-location/WorkingDirectory/IncludeDirectory
# C:/ApiPythonExampleData/example-source-storage-location-optional/WorkingDirectory/ExcludeDirectory
# C:/ApiPythonExampleData/example-source-storage-location-optional/WorkingDirectory/IncludeDirectory
# C:/ApiPythonExampleData/example-target-storage-location/
# C:/ApiPythonExampleData/example-target-storage-location-optional

# Get Credentials/Login Example
def example_api_login():
    #  Set the configuration
    configuration = openapi_client.Configuration(
        host=example_host,
    )
    configuration.verify_ssl = False
    configuration.ssl_ca_cert = None
    configuration.assert_hostname = False
    configuration.cert_file = None

    print("# Get an access token")
    with openapi_client.ApiClient(configuration) as api_client:
        api_instance_auth = openapi_client.AuthenticationApi(api_client)
        body_login = openapi_client.ApiCredentials(password=example_password, username=example_username)
        api_response = api_instance_auth.login(body_login)
        pprint(api_response)

# Makes each example request body for creating/updating source storage locations
def make_instance_storage_location_source(include_optional):
    # model = openapi_client.models.api_storage_location_nas.ApiStorageLocationNas()  # noqa: E501

    # Example create/update source storage location request body with optional fields
    if include_optional:
        return ApiStorageLocationNas(
            cost_per_tb=1.337,
            description='A description of the storage location',
            is_target=False,
            off_peak_bytes_per_second_limit=1.337,
            off_peak_files_per_second_scan_limit=1.337,
            path=example_source_share_optional,
            peak_bytes_per_second_limit=1.337,
            peak_files_per_second_scan_limit=1.337,
            peak_times_schedule=[
                {"durationMinutes": 1063, "dayOfWeek": 4, "startTimeHourAndMinutes": "04:05"}
            ],
            type='NAS'
        )
    # Example create/update source storage location request body with required fields
    else:
        return ApiStorageLocationNas(
            is_target=False,
            path=example_source_share,
            type='NAS',
        )

# Makes each example request body for creating/updating target storage locations
def make_instance_storage_location_target(include_optional):
    # model = openapi_client.models.api_storage_location_nas.ApiStorageLocationNas()  # noqa: E501

    # Example create/update target storage location request body with optional fields
    if include_optional:
        return ApiStorageLocationNas(
            cost_per_tb=1.337,
            description='A description of the storage location',
            is_target=True,
            off_peak_bytes_per_second_limit=1.337,
            off_peak_files_per_second_scan_limit=1.337,
            path=example_target_share_optional,
            peak_bytes_per_second_limit=1.337,
            peak_files_per_second_scan_limit=1.337,
            peak_times_schedule=[
                {"durationMinutes": 1063, "dayOfWeek": 4, "startTimeHourAndMinutes": "04:05"}
            ],
            type='NAS'
        )
    # Example create/update target storage location request body with required fields
    else:
        return ApiStorageLocationNas(
            is_target=True,
            path=example_target_share,
            type='NAS',
        )

# Create/Update Storage Location Example
def example_api_create_update_storage_location():
    # Create instance of a source storage location (the request body)
    example_local_nas_source = make_instance_storage_location_source(include_optional=False)
    example_local_nas_source_optional = make_instance_storage_location_source(include_optional=True)

    # Create instance of a target storage location (the request body)
    example_local_nas_target = make_instance_storage_location_target(include_optional=False)
    example_local_nas_target_optional = make_instance_storage_location_target(include_optional=True)

    #  Set the configuration
    configuration = openapi_client.Configuration(
        host=example_host,
    )
    configuration.verify_ssl = False
    configuration.ssl_ca_cert = None
    configuration.assert_hostname = False
    configuration.cert_file = None

    #  Get an access token and add it to the configuration
    with openapi_client.ApiClient(configuration) as api_client:
        api_instance_auth = openapi_client.AuthenticationApi(api_client)
        body_login = openapi_client.ApiCredentials(password=example_password, username=example_username)
        api_response = api_instance_auth.login(body_login)
        configuration.access_token = api_response.token

        # Create a StorageApi instance to make API storage commands
        api_instance = openapi_client.StorageApi(api_client)

        print("# Create/Update source storage location using required fields")
        try:
            api_response = api_instance.update_storage_location(storage_location_name=
                                                                "Example-Source",
                                                                body=example_local_nas_source)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StorageApi->update_storage_location (example for local NAS source): %s\n"
                  % e)

        print("# Create/Update target storage location using required fields")
        try:
            api_response = api_instance.update_storage_location(storage_location_name=
                                                                "Example-Target",
                                                                body=example_local_nas_target)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StorageApi->update_storage_location (example for local NAS target): %s\n"
                  % e)

        print("# Create/Update source storage location optional fields")
        try:
            api_response = api_instance.update_storage_location(storage_location_name=
                                                                "Example-Source-Optional-Fields",
                                                                body=example_local_nas_source_optional)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StorageApi->update_storage_location (example for local NAS source w/ "
                  "optional fields): %s\n" % e)

        print("# Create/Update target storage location optional fields")
        try:
            api_response = api_instance.update_storage_location(storage_location_name=
                                                                "Example-Target-Optional-Fields",
                                                                body=example_local_nas_target_optional)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StorageApi->update_storage_location (example for local NAS target w/ "
                  "optional fields): %s\n" % e)

# Makes each example request body for creating/updating scan projects
def make_instance_scan_project(include_optional):
    # model = openapi_client.models.api_project_scan.ApiProjectScan()  # noqa: E501

    # Example create/update scan project request body with optional fields
    if include_optional:
        return ApiProjectScan(
            description='A description of the scan project',
            share='Example-Source-Optional-Fields',
            working_directory=example_scan_working_directory,
            tags=[
                'tag'
            ],
            schedule={"monthsOfYear": ["monthsOfYear", "monthsOfYear"], "period": "Now", "daysOfMonth": [0, 0],
                      "startMonth": 3, "startDay": 5, "startHour": 13, "startYear": 2021, "interval": 6,
                      "daysOfWeek": ["daysOfWeek", "daysOfWeek"], "startMinute": 33},
        )
    # Example create/update scan project request body with required fields
    else:
        return ApiProjectScan(
            share='Example-Source',
            schedule={"monthsOfYear": ["monthsOfYear", "monthsOfYear"], "period": "Now", "daysOfMonth": [0, 0],
                      "startMonth": 3, "startDay": 5, "startHour": 13, "startYear": 2021, "interval": 6,
                      "daysOfWeek": ["daysOfWeek", "daysOfWeek"], "startMinute": 33},
        )

# Create/Update Scan Project Example
def example_api_create_update_project_scan():
    # Create instance of a scan project (the request body)
    example_scan = make_instance_scan_project(include_optional=False)
    example_scan_optional = make_instance_scan_project(include_optional=True)

    #  Set the configuration
    configuration = openapi_client.Configuration(
        host=example_host,
    )
    configuration.verify_ssl = False
    configuration.ssl_ca_cert = None
    configuration.assert_hostname = False
    configuration.cert_file = None

    #  Get an access token and add it to the configuration
    with openapi_client.ApiClient(configuration) as api_client:
        api_instance_auth = openapi_client.AuthenticationApi(api_client)
        body_login = openapi_client.ApiCredentials(password=example_password, username=example_username)
        api_response = api_instance_auth.login(body_login)
        configuration.access_token = api_response.token

        # Create a ProjectApi instance to make API storage commands
        api_instance = openapi_client.ProjectApi(api_client)

        print("# Create scan project with required fields")
        try:
            api_response = api_instance.update_scan_project(project_name="Example-Scan-Project",
                                                            body=example_scan)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ProjectApi->update_scan_project (example for scan local nas): %s\n" % e)

        print("# Create scan project with optional fields")
        try:
            api_response = api_instance.update_scan_project(project_name="Example-Scan-Project-Optional-Fields",
                                                            body=example_scan_optional)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ProjectApi->update_scan_project (example for scan local nas w/ optional "
                  "fields): %s\n" % e)

# Makes each example request body for creating/updating archive projects
def make_instance_archive_project(include_optional):
    # model = openapi_client.models.api_project_archive.ApiProjectArchive()  # noqa: E501

    # Example create/update archive project request body with optional fields
    if include_optional:
        return ApiProjectArchive(
            description='A description of the archive project',
            share='Example-Source-Optional-Fields',
            tags=[
                'tag'
            ],
            active=True,
            project_type='Archive',
            bread_crumb_action='CreateHtmlLink',
            targets=[
                'Example-Target-Optional-Fields'
            ],
            filter={"excludeDirectories": [example_exclude_directory],
                    "minimumSize": "Any", "minimumAge": "AnyAge",
                    "includeDirectories": [example_include_directory]},
            schedule={"monthsOfYear": ["monthsOfYear", "monthsOfYear"], "period": "Now", "daysOfMonth": [0, 0],
                      "startMonth": 3, "startDay": 5, "startHour": 13, "startYear": 2021, "interval": 6,
                      "daysOfWeek": ["daysOfWeek", "daysOfWeek"], "startMinute": 33},
            status={"name": "Example-Archive-Name", "nextRunTime": "2021-01-23T04:56:07.000Z",
                    "createdBy": "Example User", "created": "2020-01-23T04:56:07.000Z",
                    "lastSuccessfulJob": "2020-01-23T04:56:07.000Z", "lastJobRunTime": "2020-01-23T04:56:07.000Z",
                    "updated": "2020-01-23T04:56:07.000Z", "conflictDetected": "2020-01-23T04:56:07.000Z"}
        )
    # Example create/update archive project request body with required fields
    else:
        return ApiProjectArchive(
            share='Example-Source',
            project_type='Archive',
            bread_crumb_action="RemoveOriginal",
            targets=[
                'Example-Target'
            ],
            schedule={"monthsOfYear": ["monthsOfYear", "monthsOfYear"], "period": "Now", "daysOfMonth": [0, 0],
                      "startMonth": 3, "startDay": 5, "startHour": 13, "startYear": 2021, "interval": 6,
                      "daysOfWeek": ["daysOfWeek", "daysOfWeek"], "startMinute": 33},
        )

# Create/Update Archive Project Example
def example_api_create_update_project_archive():
    # Create instance of an archive project (the request body)
    example_archive = make_instance_archive_project(include_optional=False)
    example_archive_optional = make_instance_archive_project(include_optional=True)

    #  Set the configuration
    configuration = openapi_client.Configuration(
        host=example_host,
    )
    configuration.verify_ssl = False
    configuration.ssl_ca_cert = None
    configuration.assert_hostname = False
    configuration.cert_file = None

    #  Get an access token and add it to the configuration
    with openapi_client.ApiClient(configuration) as api_client:
        api_instance_auth = openapi_client.AuthenticationApi(api_client)
        body_login = openapi_client.ApiCredentials(password=example_password, username=example_username)
        api_response = api_instance_auth.login(body_login)
        configuration.access_token = api_response.token

        # Create a ProjectApi instance to make API storage commands
        api_instance = openapi_client.ProjectApi(api_client)

        print("# Create archive project with required fields")
        try:
            api_response = api_instance.update_archive_project(project_name="Example-Archive-Project",
                                                               body=example_archive)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ProjectApi->update_archive_project (example for archive local nas to "
                  "local nas): %s\n" % e)

        print("# Create archive project with optional fields")
        try:
            api_response = api_instance.update_archive_project(project_name="Example-Archive-Project-Optional-Fields"
                                                               , body=example_archive_optional)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ProjectApi->update_archive_project (example for archive local nas to "
                  "local nas w/ optional fields): %s\n" % e)

# Makes each example request body for creating/updating restore projects
def make_instance_restore_project(include_optional):
    # model = openapi_client.models.api_project_restore.ApiProjectRestore()  # noqa: E501

    # Example create/update restore project request body with optional fields
    if include_optional:
        return ApiProjectRestore(
            description='A description of the restore project',
            share='Example-Source-Optional-Fields',
            tags=[
                'tag'
            ],
            active=True,
            project_type='Restore',
            email_on_complete=[
                email_on_complete
            ],
            restore_manifest='Example-Archive-Project-Optional-Fields-1',
            schedule={"monthsOfYear": ["December", "January"], "period": "Now", "daysOfMonth": [1, 15],
                      "startMonth": 12, "startDay": 1, "startHour": 13, "startYear": 2020, "interval": 6,
                      "daysOfWeek": ["daysOfWeek", "daysOfWeek"], "startMinute": 33},
            status={"name": "Example-Restore-Name", "nextRunTime": "2021-01-23T04:56:07.000Z",
                    "createdBy": "Example User", "created": "2020-01-23T04:56:07.000Z",
                    "lastSuccessfulJob": "2020-01-23T04:56:07.000Z", "lastJobRunTime": "2020-01-23T04:56:07.000Z",
                    "updated": "2020-01-23T04:56:07.000Z", "conflictDetected": "2020-01-23T04:56:07.000Z"}
        )
    # Example create/update restore project request body with required fields
    else:
        return ApiProjectRestore(
            share='Example-Source',
            project_type='Restore',
            restore_manifest='Example-Archive-Project-1',
            schedule={"monthsOfYear": ["monthsOfYear", "monthsOfYear"], "period": "Now", "daysOfMonth": [0, 0],
                      "startMonth": 3, "startDay": 5, "startHour": 13, "startYear": 2021, "interval": 6,
                      "daysOfWeek": ["daysOfWeek", "daysOfWeek"], "startMinute": 33},
        )

# Create/Update Restore Project Example
def example_api_create_update_project_restore():
    # Create instance of a restore project (the request body)
    example_restore = make_instance_restore_project(include_optional=False)
    example_restore_optional = make_instance_restore_project(include_optional=True)

    #  Set the configuration
    configuration = openapi_client.Configuration(
        host=example_host,
    )
    configuration.verify_ssl = False
    configuration.ssl_ca_cert = None
    configuration.assert_hostname = False
    configuration.cert_file = None

    #  Get an access token and add it to the configuration
    with openapi_client.ApiClient(configuration) as api_client:
        api_instance_auth = openapi_client.AuthenticationApi(api_client)
        body_login = openapi_client.ApiCredentials(password=example_password, username=example_username)
        api_response = api_instance_auth.login(body_login)
        configuration.access_token = api_response.token

        # Create a ProjectApi instance to make API storage commands
        api_instance = openapi_client.ProjectApi(api_client)

        print("# Create restore project with optional fields")
        try:
            api_response = api_instance.update_restore_project(project_name="Example-Restore-Project-Optional-Fields",
                                                               body=example_restore_optional)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ProjectApi->update_restore_project (example for restore from local nas "
                  "to local nas w/ optional fields): %s\n" % e)

        print("# Create restore project with required fields")
        try:
            api_response = api_instance.update_restore_project(project_name="Example-Restore-Project",
                                                               body=example_restore)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ProjectApi->update_restore_project (example for restore from local nas "
                  "to local nas): %s\n" % e)

# Get Storage Location Example
def example_api_get_storage_location():
    #  Set the configuration
    configuration = openapi_client.Configuration(
        host=example_host
    )
    configuration.verify_ssl = False
    configuration.ssl_ca_cert = None
    configuration.assert_hostname = False
    configuration.cert_file = None

    #  Get an access token and add it to the configuration
    with openapi_client.ApiClient(configuration) as api_client:
        api_instance_auth = openapi_client.AuthenticationApi(api_client)
        body_login = openapi_client.ApiCredentials(password=example_password, username=example_username)
        api_response = api_instance_auth.login(body_login)
        configuration.access_token = api_response.token

        # Create a ProjectApi instance to make API storage commands
        api_instance = openapi_client.StorageApi(api_client)

        print("# Get a single storage location")
        try:
            api_response = api_instance.get_storage_location("Example-Source")
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StorageApi->get_storage_location (example GET single storage location): "
                  "%s\n" % e)

        print("# Get ALL storage locations")
        try:
            api_response = api_instance.list_storage_locations()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling StorageApi->list_storage_locations (example GET list of storage "
                  "locations): %s\n" % e)

# Get Project Example
def example_api_get_project():
    #  Set the configuration
    configuration = openapi_client.Configuration(
        host=example_host,
    )
    configuration.verify_ssl = False
    configuration.ssl_ca_cert = None
    configuration.assert_hostname = False
    configuration.cert_file = None

    #  Get an access token and add it to the configuration
    with openapi_client.ApiClient(configuration) as api_client:
        api_instance_auth = openapi_client.AuthenticationApi(api_client)
        body_login = openapi_client.ApiCredentials(password=example_password, username=example_username)
        api_response = api_instance_auth.login(body_login)
        configuration.access_token = api_response.token

        # Create a ProjectApi instance to make API storage commands
        api_instance = openapi_client.ProjectApi(api_client)

        print("# Get a single project")
        try:
            api_response = api_instance.get_project(project_name="Example-Archive-Project")
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ProjectApi->get_project (example GET single project): %s\n" % e)

        print("# Get ALL projects")
        try:
            api_response = api_instance.list_projects()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ProjectApi->list_projects (example GET list of projects): %s\n" % e)

def example_api_get_jobs():
    #  Set the configuration
    configuration = openapi_client.Configuration(
        host=example_host,
    )
    configuration.verify_ssl = False
    configuration.ssl_ca_cert = None
    configuration.assert_hostname = False
    configuration.cert_file = None

    #  Get an access token and add it to the configuration
    with openapi_client.ApiClient(configuration) as api_client:
        api_instance_auth = openapi_client.AuthenticationApi(api_client)
        body_login = openapi_client.ApiCredentials(password=example_password, username=example_username)
        api_response = api_instance_auth.login(body_login)
        configuration.access_token = api_response.token

        # Create a JobStatusAPI instance to make API commands
        api_instance = openapi_client.JobStatusApi(api_client)

        print("# Get five Job statuses")
        try:
            params = {"include_all": True, "limit": 5}
            api_response = api_instance.list_all_jobs_status(**params)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling JobStatusApi->list_all_jobs_status: %s\n" % e)

# Runs each API call sequentially as to show workflow.
def main():
    example_api_login()
    example_api_create_update_storage_location()
    example_api_create_update_project_scan()
    time.sleep(sleep_time_seconds)  # sleep long enough for the scan to finish before attempting archive
    example_api_create_update_project_archive()
    time.sleep(sleep_time_seconds)  # sleep long enough for the archive to finish before attempting restore
    example_api_create_update_project_restore()
    example_api_get_storage_location()
    example_api_get_project()
    example_api_get_jobs()

if __name__ == '__main__':
    main()
