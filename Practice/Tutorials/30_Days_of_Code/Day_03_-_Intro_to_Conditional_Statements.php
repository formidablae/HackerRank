<?php
	$N = intval(trim(fgets(STDIN)));

	if ($N % 2 == 0 && ($N > 20 || $N == 2 || $N == 4)) {
	    print "Not Weird";
	} else {
	    print "Weird";
	}
?>
