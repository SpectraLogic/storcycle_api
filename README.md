# storcycle_api
###StorCycle API Examples

This repository contains examples for interacting with the StorCycle API. These general examples require either creation of the example directory tree, or adjusting variables to suit the local system.

To use the examples, client code must first be generated in the desired language.

####Python:

Download a client generator plugin for your local IDE and install. Note that while the OpenAPI Generator plugin by Jim Schubert was used to generate the example Python client, any client generator should be adequate.

Download and navigate to the openapi.yaml file from which the client will be generated.

Use the now installed openapi generator plugin to generate client code from the openapi.yaml file.


*Code -> OpenAPI -> Generate from Document*

Navigate to the desired language (Python) and fill in the appropriate values for package name etc. Then generate.

Download and place the example Python code within the directory to which the generated code has been saved.

Create the example directory tree used in the example code or change example variable fields to appropriate local system values.

*Example directory tree at the C:/ level.
You need to either create this directory structure populated with some files in the source subdirectories, or populate with an appropriate local directory tree.*

- *C:/ApiPythonExampleData/example-source-storage-location/WorkingDirectory/ExcludeDirectory*
- *C:/ApiPythonExampleData/example-source-storage-location/WorkingDirectory/IncludeDirectory*
- *C:/ApiPythonExampleData/example-source-storage-location-optional/WorkingDirectory/ExcludeDirectory*
- *C:/ApiPythonExampleData/example-source-storage-location-optional/WorkingDirectory/IncludeDirectory*
- *C:/ApiPythonExampleData/example-target-storage-location/*
- *C:/ApiPythonExampleData/example-target-storage-location-optional*

