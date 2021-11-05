<?php

/*
 * Complete the 'kangaroo' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. INTEGER x1
 *  2. INTEGER v1
 *  3. INTEGER x2
 *  4. INTEGER v2
 */

function kangaroo($x1, $v1, $x2, $v2) {
    // Write your code here
    $previousDistance = abs($x1 - $x2);
    for ($t = 0; ; $t++) {
        $newDistance = abs($x1 + $v1 * $t - $x2 - $v2 * $t);
        if ($newDistance === 0) {
            return "YES";
        } else if ($x1 !== $x2 && $v1 === $v2) {
            return "NO";
        } else if ($newDistance >= $previousDistance && $t > 0) {
            return "NO";
        } else {
            $previousDistance = $newDistance;
        }
    }
}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$first_multiple_input = explode(' ', rtrim(fgets(STDIN)));

$x1 = intval($first_multiple_input[0]);

$v1 = intval($first_multiple_input[1]);

$x2 = intval($first_multiple_input[2]);

$v2 = intval($first_multiple_input[3]);

$result = kangaroo($x1, $v1, $x2, $v2);

fwrite($fptr, $result . "\n");

fclose($fptr);
