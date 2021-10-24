<?php
	$n = intval(trim(fgets(STDIN)));

	$continueLoop = true;
	$digits = "";
	$consecutiveCount = 0;

	while ($continueLoop)
	{
		$digits = $digits . ($n % 2);
		$n = $n / 2;
		if ($n == 0) {
			$continueLoop = false;
		}
	}

	if (strlen($digits) == 0) {
		print "0";
	} else if (strlen($digits) == 1) {
		print "1";
	} else {
		$onlyOnesArray = explode("0", $digits);

		for ($i = 0; $i < count($onlyOnesArray); $i++)
		{
			if (strlen($onlyOnesArray[$i]) > $consecutiveCount) {
				$consecutiveCount = strlen($onlyOnesArray[$i]);
			}
		}

		print $consecutiveCount;
	}
?>

