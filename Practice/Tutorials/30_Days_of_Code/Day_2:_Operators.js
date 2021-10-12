'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
	inputString += inputStdin;
});

process.stdin.on('end', function() {
	inputString = inputString.split('\n');

	main();
});

function readLine() {
	return inputString[currentLine++];
}

/*
 * Complete the 'solve' function below.
 *
 * The function accepts following parameters:
 *  1. DOUBLE meal_cost
 *  2. INTEGER tip_percent
 *  3. INTEGER tax_percent
 */

function solve(meal_cost, tip_percent, tax_percent) {
	// Write your code here
	let tip = meal_cost * tip_percent / 100;
	let tax = meal_cost * tax_percent / 100;
	let total_cost = meal_cost + tip + tax;
	console.log(total_cost.toFixed(0));
}

function main() {
	const meal_cost = parseFloat(readLine().trim());

	const tip_percent = parseInt(readLine().trim(), 10);

	const tax_percent = parseInt(readLine().trim(), 10);

	solve(meal_cost, tip_percent, tax_percent);
}

