include "config.php"; // Database connection using PDO

//$sql="SELECT name,id FROM student"; 

$sql="SELECT area from hospital_details; 

/* You can add order by clause to the sql statement if the names are to be displayed in alphabetical order */

echo "<select name=student value=''>Student Name</option>"; // list box select command

foreach ($dbo->query($sql) as $row){//Array or records stored in $row

echo "<option value=$row[id]>$row[name]</option>"; 

/* Option values are added by looping through the array */ 

}

 echo "</select>";// Closing of list box
