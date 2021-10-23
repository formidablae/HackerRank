<?php
	$_fp = fopen("php://stdin", "r");
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */

	$testCases = fgets($_fp);

	for ($i = 0; $i < $testCases; $i++) {
		$lineText = trim(fgets($_fp));
		$lineTextArray = str_split($lineText, 1);
		
		for ($j = 0; $j < count($lineTextArray); $j = $j + 2) {
			print $lineTextArray[$j];
		}
		
		print " ";
		
		for ($j = 1; $j < count($lineTextArray); $j = $j + 2) {
			print $lineTextArray[$j];
		}
		
		print "\n";
	}
?>

