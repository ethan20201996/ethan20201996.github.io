<?php 
	header("Content-type:application/json");
	
	$pgsqlOptions = "host='localhost' dbname='geog5871' user='geog5871student' password='Geibeu9b'";
  $dbconn = pg_connect($pgsqlOptions) or die ('connection failure');
	$query = "SELECT id, latitude, longitude, place, website, details, reopeningtime, type FROM ml19y2j_museums" ;
  $result = pg_query($dbconn, $query) or die ('Query failed: '.pg_last_error());
	$placeData = array();
	
	while ($row = pg_fetch_array($result, null, PGSQL_ASSOC))	{
		$placeData[] = array("id" => $row["id"], "lat" => $row["latitude"], "lng" => $row["longitude"], "place" => $row["place"], "website" => $row["website"], "details" => $row["details"], "reopeningtime" => $row["reopeningtime"], "type" => $row["type"]);
	}
	
	echo json_encode($placeData); 
	pg_close($dbconn);
?>
