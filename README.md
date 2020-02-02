# pyCleanGcal
A few python commands to convert the copy from a gCal guest list into a csv file that can be imported with dataloader into salesforce

The objective:
- get the list of guests from a Gcal appointment, and format so it can be uploaded into an sObject in Salesforce
- the 2 targets sObjects are: Contacts and CampaignMembers

In this scenario the people that attended a session are tracked in Gcal, and ideally you would like to add them to a campaign as campaign members with an status (for example Status = Attended)

The issue is that Gcal put all the guest in a single line separated by commas, like this:

Terence Bruna	<tbruna0@discuz.net>, Batholomew Rault	<brault1@utexas.edu>, Rosalinda Laurenty	<rlaurenty2@1688.com>, Ric O'Rafferty	<rorafferty3@opensource.org>, Yancy Edgson	<yedgson4@biglobe.ne.jp>, Calvin Longworthy	<clongworthy5@bandcamp.com>, Lawrence Brilon	<lbrilon6@163.com>, Mead Doughton	<mdoughton7@java.com>, Christiana Littleproud	<clittleproud8@google.es>, Mikkel McComiskey	<mmccomiskey9@histats.com>, Aluino Kellington	<akellingtona@accuweather.com>, Gallagher Gilham	<ggilhamb@mtv.com>, Allx Liddyard	<aliddyardc@smugmug.com>, Arlyn Wolfit	<awolfitd@etsy.com>, Larina Meddemmen	<lmeddemmene@wikimedia.org>

The desired output should be something like

FirstName,LastName,email,CampaignID,Status
Terence,Bruna,tbruna0@discuz.net,701F0A83FDE68A603A0,Attended
Batholomew,Rault,brault1@utexas.edu,701F0A83FDE68A603A0,Attended
...
...

In a nutshell:
1. transpose the 1 line into one line per guest in the GCal list
2. split into columns with delimiter ","
3. add a first line as a header
4. add more "columns" (to simplify here the columns added have the same information for all the guests: for example de CampaignID value, the same for all the guests, and the campaign member status, again same for all the members)

How to use the python scripts?

- python gcal2csv.py fileName1 fileName2 # split the 1 line file into several lines replacing the ', ' with a '\n'
- python csv2columns.py filename1 filename2 # find any ' ' and replace for a ',' - it has the problem that a name with more than 2 words will add more columns than FirsdtName and LastName. Further manual editing of the file is needed
- python cleanEmail.py fileName1 fileName2 # emails are enclosed in <email>, so the > and the < are replaced with null
- python addCommas.py filename1 fileName2 # if no commas found in a line, it adds str,str,email - str is the first part of the email
- python csvAddStringLine.py fileName1 fileName2 ",701F0A83FDE68A603A0,Attended"
- python csvAddHeader.py fileName1 fileName2 "FirstName, LastName, email, CampaigID, Status"                                     
                                                                                                   
The scripts assume that initial file has a very specific format.
