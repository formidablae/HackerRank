<?php
	$_fp = fopen("php://stdin", "r");
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	$testCases = intval(trim(fgets($_fp)));
	$dictNumbers = [];

	for ($i = 0; $i < $testCases; $i++) {
		list($k, $v) = explode(" ", trim(fgets($_fp)));
		$dictNumbers[$k] = intval($v);
	}

	while (!feof($_fp)) {
		$searchStr = trim(fgets($_fp));
		
		if (isset($dictNumbers[$searchStr])) {
			echo $searchStr . "=" . $dictNumbers[$searchStr]."\n";
		} else {
			echo "Not found\n";
		}
	}
?>

