---
categories: new-zealand administrative
date: '2017-05-08 13:16:22'
description: Information recorded in the process of administering a claim and rehabilitation
  where needed.  This is operational data represented and accessed via the ACC data
  warehouse known as In Fact. Data is available from 1974 although more recent data
  is of better quality and more complete.
id: acc_datasets
layout: post
link: http://www.acc.co.nz/about-acc/research/ABA00043
provider: Accident Compensation Corporation
tags:
- acc
- nzte-report
title: ACC Datasets
---


 <h4> <u>Description:</u> </h4>
Information recorded in the process of administering a claim and rehabilitation where needed.  This is operational data represented and accessed via the ACC data warehouse known as In Fact. Data is available from 1974 although more recent data is of better quality and more complete.
 <h4> <u>Additional information:</u> </h4>
 <table style="border: 1px solid">
 <tr> <td width="40%">Have_(encrypted)_NHI</td> <td>Yes</td> </tr>
 <tr> <td width="40%">Personally identifiable (e.g. linked to NHI numbers) and longitudinal or aggregated (e.g. for planning, clinical research etc.)?</td> <td>ACC claims and claimants can be linked to MOH data (particularly NMDS (National Minimum Data Set). Claimants can be identified via NHI and ACC claim numbers (mostly ACC45 claim form numbers). ACC records full details of claimants (name, address, date of birth, etc.) including demographics.</td> </tr>
 <tr> <td width="40%">Volume of data (e.g. how many records)
Since when?</td> <td>ACC processes about 1.7 million claims per annum at a total cost of about $2.5B for medical, compensation and rehabilitation costs.</td> </tr>
 <tr> <td width="40%">Purpose and governance including ethics committee/patient consent mechanisms. Q: How do you get around ethics/privacy issues with your data sources? Esp. DHBs?</td> <td>Application for privacy level data must be made to the ACC Ethics Committee (details on the ACC website - acc.co.nz in the section "About ACC". If use is beyond bona fide research purposes, ACC will solicit the claimants consent before releasing information.</td> </tr>
 <tr> <td width="40%">Scope</td> <td>National</td> </tr>
 <tr> <td width="40%">Does the data contain diagnoses and clinical outcomes?
Does the data contain procedures, device information and medication for therapy?
Does this data set have cost / price data?</td> <td>1. The data does contain diagnostic information both primary and secondary diagnosis in READ, ICD9 and IC10 coding depending on when and by whom the information was captured. PHOs and DHBs capture the information and is submiotted to ACC.
2. Some procedure/medication information is recorded as part of the treatment and rehabilitation of injured claimants. 
3. ACC pays for services directly in some case but the medical treatment proivided by DHBs is bulk funded and is not recorded in ACC's systems  apart from the fact that it was an ACC related case.</td> </tr>
 <tr> <td width="40%">Presence of Data dictionary? Column headings in Excel or any kind of data model if residing in a relational database (e.g. Access, SQL Server, Oracle etc.) </td> <td>A data dictionary is not available directly as this data is from operational systems. However descriptions of subsets of data can be provided  based on specific requirements. The data is hosted in an Oracle database using OBIEE as a front end tool. In some cases SAS datasets are still being used but are being phased out. </td> </tr>
 <tr> <td width="40%">Linked (or linkable) to other datasets within your organisation or across the Sector</td> <td>Can be linked to levy payers in ACC and external datasets such as CAS (motor vehicle traffic accidents) and NMDS datasets as described.</td> </tr>
 <tr> <td width="40%">How often does this data set get updated? Daily? Weekly? Monthly? Quarterly? Yearly?</td> <td>Updated daily from production systems.</td> </tr>
 <tr> <td width="40%">Indication of data quality (e.g. missing values, duplications, inconsistencies etc.). Q: Audits? How do you ensure the data is valid and correct?</td> <td>Data quality is in line with the main function performed by ACC (paying for claims related costs) including managing long term and rehabilitation. Overall quality is rated to be good. Detailed information about specific data areas can be provided where required.</td> </tr>
 <tr> <td width="40%">Brief info about the systems and processes used to collect/manage data. Q: Where the data is collected, in what form, and accessibility?</td> <td>Medical practitioners/DHBs record injury information and submit this to ACC. In about 90% of cases only medical costs are involved. In more severe cases where compensation for loss of earnings is paid as well as rehabilitation, this area is managed by ACC but provided by external providers. Access to ACC data is by request and if confidential information is required, need toi be applied for via the ACC Ethics Committee for review and approval.</td> </tr>
 <tr> <td width="40%">Data format, e.g., data structure, data types, and storage form (relational database, Excel, csv, etc.).</td> <td>Data can be provided in CSV format extracted files, encrypted if it conatins privavcy information and provided on CD because of the data volumes associated (typically 500MB for 2001-2012 claims data). </td> </tr>
 <tr> <td width="40%">How well the data is structured, e.g. free text VS coded text VS pick-list (drop-down list)</td> <td>Most dat fields are structured with  very few free text fields.</td> </tr>
 </table>