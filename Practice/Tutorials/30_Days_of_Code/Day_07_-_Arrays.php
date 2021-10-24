<?php
	$n = intval(trim(fgets(STDIN)));

	$arr_temp = rtrim(fgets(STDIN));

	$arr = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));

	for ($i = count($arr) - 1; $i >= 0; $i--) {
		print $arr[$i] . " ";
	}
?>

