---
categories: new-zealand registries-and-screening-database
date: '2017-05-08 13:16:22'
description: Management of the Retinal Screening Service and linked to our Chronic
  Care Management Programme database which holds a large amount of clinical data related
  to long term conditions.
id: chronic_care_management_database_and_retinal_screening_database
layout: post
link: http://www.countiesmanukau.health.nz/
provider: Counties Manukau District Health Board
tags:
- hospital
- nzte-report
title: Chronic Care Management database and Retinal Screening database
---


 <h4> <u>Description:</u> </h4>
Management of the Retinal Screening Service and linked to our Chronic Care Management Programme database which holds a large amount of clinical data related to long term conditions.
 <h4> <u>Additional information:</u> </h4>
 <table style="border: 1px solid">
 <tr> <td width="40%">Have_(encrypted)_NHI</td> <td>Yes</td> </tr>
 <tr> <td width="40%">Personally identifiable (e.g. linked to NHI numbers) and longitudinal or aggregated (e.g. for planning, clinical research etc.)?</td> <td>Linked to NHI and clinical observation data</td> </tr>
 <tr> <td width="40%">Volume of data (e.g. how many records)
Since when?</td> <td>Many Tables ( over 100)
Largest table records at May 2013 Is 30 091 867</td> </tr>
 <tr> <td width="40%">Purpose and governance including ethics committee/patient consent mechanisms. Q: How do you get around ethics/privacy issues with your data sources? Esp. DHBs?</td> <td>Data Access Approval forms need to be applied for access to the data which are reviewed by the Long Term Conditions Clinical Governance Group.  A privacy matrix has been developed which details who has acces to what level of information</td> </tr>
 <tr> <td width="40%">Scope</td> <td>Provider</td> </tr>
 <tr> <td width="40%">Does the data contain diagnoses and clinical outcomes?
Does the data contain procedures, device information and medication for therapy?
Does this data set have cost / price data?</td> <td>data contain diagnoses and clinical outcomes? Yes
data contain procedures, device information and medication for therapy?
 No
It stores the amount of money funded per GP claim</td> </tr>
 <tr> <td width="40%">Presence of Data dictionary? Column headings in Excel or any kind of data model if residing in a relational database (e.g. Access, SQL Server, Oracle etc.) </td> <td>No Data Dictionary. SQL Server 2000/2005</td> </tr>
 <tr> <td width="40%">Linked (or linkable) to other datasets within your organisation or across the Sector</td> <td>Linked to SDM Database and to Enigma
Imports from VIP.Net through Excel for Retinal Screening.</td> </tr>
 <tr> <td width="40%">How often does this data set get updated? Daily? Weekly? Monthly? Quarterly? Yearly?</td> <td>Monthly</td> </tr>
 <tr> <td width="40%">Indication of data quality (e.g. missing values, duplications, inconsistencies etc.). Q: Audits? How do you ensure the data is valid and correct?</td> <td>Authentication at source, when data is entered into the front end
Additional Checks are done when the date is tranformed for local processing.</td> </tr>
 <tr> <td width="40%">Brief info about the systems and processes used to collect/manage data. Q: Where the data is collected, in what form, and accessibility?</td> <td>CCM data is collected from Enigma which is a web based GP Electronic Decision Support Template and stored in SQL Server
Additional data is imported through CSV files from various sources and this process of import is validated for integrity else it is rejected</td> </tr>
 <tr> <td width="40%">Data format, e.g., data structure, data types, and storage form (relational database, Excel, csv, etc.).</td> <td>SQL Server </td> </tr>
 <tr> <td width="40%">How well the data is structured, e.g. free text VS coded text VS pick-list (drop-down list)</td> <td>Structured to drop down lists against 98 percent of the structured data - Comments fields are free form</td> </tr>
 <tr> <td width="40%">How quickly can the data be made available from time of request and how old is the data once it is made available</td> <td>With Data Warehousing the Data is available in raw form and in structured reporting format almost immediately.  Data Requests submitted to the LTC CGG are usually approved within a month.</td> </tr>
 </table>