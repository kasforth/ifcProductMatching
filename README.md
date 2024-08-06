# Semantically matching IfcProduct to external databases

## Description
This code example and class was defined within the dissertation 
"BIM-based semantic enrichment for environmental analyses using Large Language Models" 
by Kasimir Forth at the Technical University of Munich.

This matching method and its class can be used to semantically enrich for several environmental analyses, 
such as *Life Cycle Assessments (LCA)*, *Material Passports (MP)* or *Building Energy Performance Simulations (BEPS)*.
Depending on the use case, the *IfcProduct* varies from *IfcSpace*, *IfcElement*, and its associated *IfcMaterial*.
In the attached short example, we use the *IfcMaterial* and simple material list as database.


## Versions and packages
The code is written with Python 3.9.

Used libraries:
- sentence-transformers 
- re
