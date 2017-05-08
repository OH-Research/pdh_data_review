---
categories: new-zealand primary-community-care-providers
date: '2017-05-08 13:16:22'
description: There is vast amount of rich clinical and administrative data stored
  in individual practice management systems (PMS) used by GPs. All major vendors have
  implemented the GP2GP interfaces which produces a CDA document used for transferring
  a patient's entire health record to another practice regardless of the PMS used.
  Also there are now open API used for patient portals. In addition there is increasing
  move towards a hosted/cloud based service which can enable access to large scale
  primary care data. This is probably the richest source of clinical data in the country.
id: gp_data_in_pms_individual_or_a_wider_hosted_deployment
layout: post
link: '#'
provider: individual GP Practices
tags:
- primary-care
- gp
- nzte-report
title: GP data in PMS (individual or a wider hosted deployment)
---


 <h4> <u>Description:</u> </h4>
There is vast amount of rich clinical and administrative data stored in individual practice management systems (PMS) used by GPs. All major vendors have implemented the GP2GP interfaces which produces a CDA document used for transferring a patient's entire health record to another practice regardless of the PMS used. Also there are now open API used for patient portals. In addition there is increasing move towards a hosted/cloud based service which can enable access to large scale primary care data. This is probably the richest source of clinical data in the country.
 <h4> <u>Additional information:</u> </h4>
 <table style="border: 1px solid">
 <tr> <td width="40%">Have_(encrypted)_NHI</td> <td>Yes</td> </tr>
 <tr> <td width="40%">Personally identifiable (e.g. linked to NHI numbers) and longitudinal or aggregated (e.g. for planning, clinical research etc.)?</td> <td>Yes - via NHI</td> </tr>
 <tr> <td width="40%">Volume of data (e.g. how many records)
Since when?</td> <td>potentially entire population</td> </tr>
 <tr> <td width="40%">Purpose and governance including ethics committee/patient consent mechanisms. Q: How do you get around ethics/privacy issues with your data sources? Esp. DHBs?</td> <td>Major issue - their main purpose is for supporting care delivery, not secondary use. Individual researchers usually approach a group of practices and obtain data extracts subject to ethics approval. DrInfo and HealthStat reach to a significant proportion of these practices and analyse data for performance and quality reporting. Bottom line is the PMS vendors do not have any ownership of data so getting data would require individual agreements.</td> </tr>
 <tr> <td width="40%">Scope</td> <td>Provider</td> </tr>
 <tr> <td width="40%">Does the data contain diagnoses and clinical outcomes?
Does the data contain procedures, device information and medication for therapy?
Does this data set have cost / price data?</td> <td>Yes - full EHR</td> </tr>
 <tr> <td width="40%">Presence of Data dictionary? Column headings in Excel or any kind of data model if residing in a relational database (e.g. Access, SQL Server, Oracle etc.) </td> <td>Each vendor has propriety data model</td> </tr>
 <tr> <td width="40%">Linked (or linkable) to other datasets within your organisation or across the Sector</td> <td>This is a transactional data - potentially when aggregated they can be linked to any other NHI based dataset</td> </tr>
 <tr> <td width="40%">How often does this data set get updated? Daily? Weekly? Monthly? Quarterly? Yearly?</td> <td>real-time</td> </tr>
 <tr> <td width="40%">Indication of data quality (e.g. missing values, duplications, inconsistencies etc.). Q: Audits? How do you ensure the data is valid and correct?</td> <td>variable</td> </tr>
 <tr> <td width="40%">Brief info about the systems and processes used to collect/manage data. Q: Where the data is collected, in what form, and accessibility?</td> <td>The four major products used in NZ are MedTech, MyPractice, Profile and Houston. These are very sophisticated thick client applications installed locally in practices or hosted service. </td> </tr>
 <tr> <td width="40%">Data format, e.g., data structure, data types, and storage form (relational database, Excel, csv, etc.).</td> <td> All stored in RDBMS and propriety data models</td> </tr>
 <tr> <td width="40%">How well the data is structured, e.g. free text VS coded text VS pick-list (drop-down list)</td> <td>Mix of structured and non-structured data.</td> </tr>
 </table>