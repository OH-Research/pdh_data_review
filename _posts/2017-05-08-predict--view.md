---
categories: new-zealand public-health-and-research
date: '2017-05-08 13:16:22'
description: "PREDICT is a web-based clinical decision support system for supporting
  the assessment and management of cardiovascular (CVD) risk that is integrated with
  major GP practice management systems (PMS) in New Zealand. It calculates a standardised
  cardiovascular risk profile on each visit that the GP uses the tool and estimates
  a 5-year percentage CVD risk based on age, gender, ethnicity, blood pressure, lipid
  profile, family history of CVD, smoking and diabetes status [1,2]. PREDICT simultaneously
  generates a research cohort comprising CVD risk profiles that are able to be anonymously
  linked to routine national and regional health databases using encrypted National
  Health Identifier (NHI) numbers.\nRecently the Vascular Informatics using Epidemiology
  & the Web (VIEW) programme, funded by the New Zealand Health Research Council (HRC),
  has been initiated which builds on PREDICT with the aim to improve risk prediction
  methods and tools. VIEW also aims to develop a comprehensive \u2018national vascular
  atlas\u2019 to identify high-risk CVD patients, quantify and map gaps and disparities
  in appropriate treatment and model the impact of treatment disparities on CVD burden."
id: predict__view
layout: post
link: http://www.enigma.co.nz/2015/12/23/predict-enigma-view-university-of-auckland-looking-forward-to-2016/
provider: Enigma
tags:
- cardiology
- nzte-report
title: PREDICT / VIEW
---


 <h4> <u>Description:</u> </h4>
PREDICT is a web-based clinical decision support system for supporting the assessment and management of cardiovascular (CVD) risk that is integrated with major GP practice management systems (PMS) in New Zealand. It calculates a standardised cardiovascular risk profile on each visit that the GP uses the tool and estimates a 5-year percentage CVD risk based on age, gender, ethnicity, blood pressure, lipid profile, family history of CVD, smoking and diabetes status [1,2]. PREDICT simultaneously generates a research cohort comprising CVD risk profiles that are able to be anonymously linked to routine national and regional health databases using encrypted National Health Identifier (NHI) numbers.
Recently the Vascular Informatics using Epidemiology & the Web (VIEW) programme, funded by the New Zealand Health Research Council (HRC), has been initiated which builds on PREDICT with the aim to improve risk prediction methods and tools. VIEW also aims to develop a comprehensive ‘national vascular atlas’ to identify high-risk CVD patients, quantify and map gaps and disparities in appropriate treatment and model the impact of treatment disparities on CVD burden.
 <h4> <u>Additional information:</u> </h4>
 <table style="border: 1px solid">
 <tr> <td width="40%">Have_(encrypted)_NHI</td> <td>Yes</td> </tr>
 <tr> <td width="40%">Personally identifiable (e.g. linked to NHI numbers) and longitudinal or aggregated (e.g. for planning, clinical research etc.)?</td> <td>NHI based - but these are encrypted in the final deidentified dataset (eNHI)</td> </tr>
 <tr> <td width="40%">Volume of data (e.g. how many records)
Since when?</td> <td>around 300,000 and growing rapidly</td> </tr>
 <tr> <td width="40%">Purpose and governance including ethics committee/patient consent mechanisms. Q: How do you get around ethics/privacy issues with your data sources? Esp. DHBs?</td> <td>VIEW Programme has a multi-regional (national) ethic approval and individual patient consent is not required. However pamphlets and posters need to be present at point of care and healthcare professionals are obliged to inform patients. It is possible to opt-out of the study.</td> </tr>
 <tr> <td width="40%">Scope</td> <td>Cohort</td> </tr>
 <tr> <td width="40%">Does the data contain diagnoses and clinical outcomes?
Does the data contain procedures, device information and medication for therapy?
Does this data set have cost / price data?</td> <td>Yes - data has rich clinical information, augmented further by data linkages to national collections, Labs and Pharms. No device information. No price information but potentially can be obtained through further linkages.</td> </tr>
 <tr> <td width="40%">Presence of Data dictionary? Column headings in Excel or any kind of data model if residing in a relational database (e.g. Access, SQL Server, Oracle etc.) </td> <td>Data dictionary present, data collected by a secure Web based application developed by ENIGMA which uses SQL Server and then NHI numbers encrypted and sent to University of Auckland  VIEW research team. Data are then cleaned and stored in Oracle. External data sources also are stored in Oracle. Furthermore VIEW datasets have been modelled using openEHR.</td> </tr>
 <tr> <td width="40%">Linked (or linkable) to other datasets within your organisation or across the Sector</td> <td>yes - using eNHI with the National Mortality Register, the National Minimum Dataset (public and private hospital discharges), the National Pharmaceutical Collection (drugs dispensed from community pharmacies with government subsidy), the National PHO Enrolment Collection and Auckland regional CVD-relevant laboratory data from Diagnostic Medlab Ltd (DML) and TestSafe</td> </tr>
 <tr> <td width="40%">How often does this data set get updated? Daily? Weekly? Monthly? Quarterly? Yearly?</td> <td>real-time</td> </tr>
 <tr> <td width="40%">Indication of data quality (e.g. missing values, duplications, inconsistencies etc.). Q: Audits? How do you ensure the data is valid and correct?</td> <td>very good - rigorous data cleaning and improvement by the use of linkages.</td> </tr>
 <tr> <td width="40%">Brief info about the systems and processes used to collect/manage data. Q: Where the data is collected, in what form, and accessibility?</td> <td>PREDICT is a web-based clinical decision support system used in primary care that is integrated with major GP practice management systems (PMS) in New Zealand. Using usual practice management system (PMS) the GP can fire up the integrated PREDICT forms and prepopulate existing data from PMS. Then additional information can be entered throught the user interface and saved. Data are validated and saved in SQL Server database in a secure hosting organisation. No one other than authorised ENIGMA personnel can access raw data - only after removal of identifiers and encryption of NHI data are sent to the University of Auckland research team.</td> </tr>
 <tr> <td width="40%">Data format, e.g., data structure, data types, and storage form (relational database, Excel, csv, etc.).</td> <td>SQL Server and Oracle.
Also in SAS format.
Data are highly structured with appropriate data types.</td> </tr>
 <tr> <td width="40%">How well the data is structured, e.g. free text VS coded text VS pick-list (drop-down list)</td> <td>very high level of structured data</td> </tr>
 </table>