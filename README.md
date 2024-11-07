# Semantic textual matching IfcProduct to external databases

## Description
This code example and class was defined within the dissertation 
"BIM-based semantic enrichment for environmental analyses using Large Language Models" 
by Kasimir Forth at the Technical University of Munich.

This matching method and its class can be used to semantically enrich for several environmental analyses, 
such as *Life Cycle Assessments (LCA)*, *Material Passports (MP)* or *Building Energy Performance Simulations (BEPS)*.

Depending on the use case, the *IfcProduct* varies from *IfcSpace*, *IfcElement*, and its associated *IfcMaterial*.
In the attached short example, we use the *IfcMaterial* and simple material list as database.

## Installation and Setup

### Forking the repo

Start with creating a fork of this repository by clicking the fork symbol in the upper right corner. 
You will be asked to specify the target hub (normally, only your personal space can be chosen).
Once forking is done, run `git clone` to download the repo on your machine. 

### Versions and packages
The code is written with Python 3.12.

Used libraries:
- sentence-transformers 
- re

## Use cases and used LLM

### Use Case 1: IfcElement matching to LCA Knowledge database:
- DOI of Publication: 10.1016/j.enbuild.2023.112837
- LLM (pretrained): https://huggingface.co/google-bert/bert-base-german-cased

### Use Case 2: IfcMaterial matching for Material Passports (IfcMaterial2MP):
- DOI of Publication: tba
- LLM (best-performing, fine-tuned): https://huggingface.co/kforth/IfcMaterial2MP
- DOI of LLM: 10.57967/hf/3414

### Use Case 3.a: IfcSpace matching to Space Types:
- DOI of Publication: 10.1016/j.jobe.2024.110312
- LLM (best-performing, fine-tuned): https://huggingface.co/kforth/IfcSpace2SpaceTypes
- DOI of LLM: 10.57967/hf/3439

### Use Case 3.b: IfcElement matching to construction sets:
- DOI of Publication: 10.1016/j.jobe.2024.110312
- LLM (best-performing, fine-tuned): https://huggingface.co/kforth/IfcElement2ConstructionSets
- DOI of LLM: 10.57967/hf/3438