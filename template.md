$name
=====

**Email** : $email  
**Phone** : $phone  
**Blog**  : $blog  
**Git**   : $git  


#for $point in $summary
 * $point
#end for


Education
---------  
#for $degree in $degrees
 $degree['award']  
 $degree['uni'], $degree['year']  
 GPA: $degree['gpa']  

#end for

Education Highlights
--------------------  
#for $highlight in $highlights
 * $highlight
#end for


Employment History
------------------  
#for $position in $employment
 $position['company']  
 $position['start'] - $position['end']  
 $position['summary']  

#end for

Activities
----------  
#for $activity in $activities
 * $activity
#end for


Awards
------  
#for $award in $awards
 * $award['summary'], $award['year']
#end for


Society Memberships
-------------------  
#for $membership in $memberships
 * $membership
#end for


Skills
------
#for $skill in $skills
 * $skill['name']: $skill['set']
#end for
