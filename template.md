$name
=====

**Email**   : [$email](mailto:$email)  
**Blog**    : [$blog](http://$blog)  
**Twitter** : [@$twitter](http://www.twitter.com/$twitter)  
**Git**     : [$git](http://$git)  


#for $point in $summary
 - $point
#end for

Talks
-----  
#for $talk in $talks
 - $talk['authors'],
   #if 'url' in $talk
     *[$talk['title']]($talk['url'])*,
   #else
     *$talk['title']*,
   #end if
   $talk['conference'], $talk['year']
#end for

Papers
------  
#for $paper in $papers
 - $paper['authors'],
   #if 'url' in $paper
     *[$paper['title']]($paper['url'])*,
   #else
     *$paper['title']*,
   #end if
   $paper['journal'], $paper['year']
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
 - $highlight
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
 - $activity
#end for


Awards
------  
#for $award in $awards
 - $award['summary'], $award['year']
#end for


Keywords
------
#for $category in $keywords
 - $category['name']: $category['set']
#end for
