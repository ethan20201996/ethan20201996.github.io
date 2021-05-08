<?php 
	
		array_filter($_POST, 'trim_value');
		
		$pattern = "/[^A-Za-z0-9\s\.\:\-\+\!\@\,\'\"]/";
		$user		= sanitize('user',FILTER_SANITIZE_SPECIAL_CHARS,$pattern); 
		$password 	= sanitize('password',FILTER_SANITIZE_SPECIAL_CHARS,$pattern); 
		$pattern = "/[^A-Za-z0-9\s\.\:\-\+\.\�\,\'\"]/";
		$lat 		= sanitize('lat',FILTER_SANITIZE_SPECIAL_CHARS,$pattern);
		$lon 		= sanitize('lon',FILTER_SANITIZE_SPECIAL_CHARS,$pattern);
		$place 		= sanitize('place',FILTER_SANITIZE_SPECIAL_CHARS,$pattern);
		$website 	= sanitize('website',FILTER_SANITIZE_URL,$pattern);
		$details 	= sanitize('details',FILTER_SANITIZE_SPECIAL_CHARS,$pattern);
		$reopeningtime = sanitize('reopeningtime',FILTER_SANITIZE_SPECIAL_CHARS,$pattern);
		$type   	= sanitize('type',FILTER_SANITIZE_SPECIAL_CHARS,$pattern);
		
		
		//Connect to db 
		$pgsqlOptions = "host='localhost' dbname='geog5871' user= $user password= $password";
		$dbconn = pg_connect($pgsqlOptions) or die ('connection failure');
		
		//Return current maximum ID
		$getID = pg_query($dbconn, "SELECT MAX(id) FROM ml19y2j_museums") or die ('Query 1 failed: '.pg_last_error());
		$id = pg_fetch_result($getID, 0, 0);
		
		//Increment ID by one to create new row ID
		$id++; 
		
		$dbconn = pg_connect($pgsqlOptions);
		$insertQuery = pg_prepare($dbconn, "my_query", "INSERT INTO ml19y2j_museums(id, latitude, longitude, place, website, details, reopeningtime, type) VALUES($1,$2,$3,$4,$5,$6,$7,$8)");
		$result = pg_execute($dbconn, "my_query", array($id,$lat,$lon,$place,$website,$details,$reopeningtime,$type))  or die ('Insert Query failed: '.pg_last_error()); 

		if (filter_var($website, FILTER_VALIDATE_URL, )) {
			echo("$website is a valid URL");
		} else {
			echo("$website is not a valid URL");
		}
		
		if (is_null($result))	{
			echo 'Data insert failed, please try again';
		} else {
			echo 'Data insert successful';
		}
		
		//Close db connection
		pg_close($dbconn);
		
		
		function trim_value(&$value){
			$value = trim($value);
			$pattern = "/[\(\)\[\]\{\}]/";
			$value = preg_replace($pattern," - ",$value);
		}

		function sanitize($str,$filter,$pattern) {
			$sanStr = preg_replace($pattern,"",$sanStr);
			$sanStr = filter_var($_POST[$str], $filter);
			if (strlen($sanStr) > 255) $sanStr = substr($sanStr,0,255);
		return $sanStr;
		} 
?>
