---
categories: new-zealand integrated-care
date: '2017-05-08 13:16:22'
description: To support clinical and care management planning and delivery for patients
  with long term conditions by providing shared care services and workflow and information
  integration with patient management systems across the sector.
id: aucklandcanterbury_shared_care_systems
layout: post
link: http://www.whanautahi.com/
provider: (ex) HSA Global
tags:
- global-health
- nzte-report
title: Auckland/Canterbury Shared Care systems
---


 <h4> <u>Description:</u> </h4>
To support clinical and care management planning and delivery for patients with long term conditions by providing shared care services and workflow and information integration with patient management systems across the sector.
 <h4> <u>Additional information:</u> </h4>
 <table style="border: 1px solid">
 <tr> <td width="40%">Have_(encrypted)_NHI</td> <td>Yes</td> </tr>
 <tr> <td width="40%">Personally identifiable (e.g. linked to NHI numbers) and longitudinal or aggregated (e.g. for planning, clinical research etc.)?</td> <td>Personally identifiable.  Linked to NHI numbers supplemented by name, gender, date of birth and residential address.</td> </tr>
 <tr> <td width="40%">Volume of data (e.g. how many records)
Since when?</td> <td>Currently about 3000-4000 patients have been registered in CCMS by existing NZ tenants and this is growing rapidly.  We expect that within 18 to 24 months it will include 150,000 to 250,000 patients that are classified as eligible for long term care funding under the Community Pharmacy Services Agreement.</td> </tr>
 <tr> <td width="40%">Purpose and governance including ethics committee/patient consent mechanisms. Q: How do you get around ethics/privacy issues with your data sources? Esp. DHBs?</td> <td>The system formally recognises and implements a patient consent process to ensure that patient records are maintained only with the informed consent of the patient.  Governance groups in each customer project team ensure compliance with privacy and security requirements.  Data is stored in a secured technical environment.  Audit mechanisms are included to record all patient record activity to ensure its appropriate use.</td> </tr>
 <tr> <td width="40%">Scope</td> <td>Regional</td> </tr>
 <tr> <td width="40%">Does the data contain diagnoses and clinical outcomes?
Does the data contain procedures, device information and medication for therapy?
Does this data set have cost / price data?</td> <td>The data contains patient-specific diagnosis and clinical outcomes information, as well as procedures, medical devices and medications.  Although cost and price data is not explicitly included, information about services delivered can be mapped to catalogues that may contain unit costs and prices.</td> </tr>
 <tr> <td width="40%">Presence of Data dictionary? Column headings in Excel or any kind of data model if residing in a relational database (e.g. Access, SQL Server, Oracle etc.) </td> <td>Data is extracted regularly (hourly or daily) into a transactional (OLTP) relational reporting database.  The data dictionary and entity relationship diagram for this reporting database are attached.</td> </tr>
 <tr> <td width="40%">Linked (or linkable) to other datasets within your organisation or across the Sector</td> <td>Currently linked to external clinical systems and practice management systems through an integration module.  Designed to enable data extracts to be imported into client data warehouses to support business intelligence data mining and analysis.  Patient record cross-references utilise the NHI number as well as other identifying attributes including gender and date of birth.</td> </tr>
 <tr> <td width="40%">How often does this data set get updated? Daily? Weekly? Monthly? Quarterly? Yearly?</td> <td>Continuously in real time through web application user interfaces and message-based integration mechanisms.</td> </tr>
 <tr> <td width="40%">Indication of data quality (e.g. missing values, duplications, inconsistencies etc.). Q: Audits? How do you ensure the data is valid and correct?</td> <td>The system includes a range of input data validation mechanisms as well as data capture quality management using controlled lists of valid values.  Quality control reports that highlight possible data integrity issues are produced regularly for client review.</td> </tr>
 <tr> <td width="40%">Brief info about the systems and processes used to collect/manage data. Q: Where the data is collected, in what form, and accessibility?</td> <td>Staff in general practice, community pharmacies, secondary care services, hospital emergency departments, community care organisations, acute demand services (incl St John's), patients, their families, allied health, district nursing and other health providers interact with the system in real time either directly or through interfaces with other clinical and practice management systems. </td> </tr>
 <tr> <td width="40%">Data format, e.g., data structure, data types, and storage form (relational database, Excel, csv, etc.).</td> <td>Microsoft SQL Server relational databases</td> </tr>
 <tr> <td width="40%">How well the data is structured, e.g. free text VS coded text VS pick-list (drop-down list)</td> <td>Extensive use is made of client-configurable controlled lists to ensure that data entry conforms with predetermined values or value ranges.  When industry standards exist they are used. This includes demographic data sets, NZULM, READ and LOINC.  Free text data values are used only where appropriate to the data being captured.  </td> </tr>
 <tr> <td width="40%">How quickly can the data be made available from time of request and how old is the data once it is made available</td> <td>HG: reseasonably quick - Researchers requiring identifiable data will usually need approval from an Ethics Committee.</td> </tr>
 </table>