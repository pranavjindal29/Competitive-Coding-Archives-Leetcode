<h2><a href="https://leetcode.com/problems/product-sales-analysis-iii">Product Sales Analysis III</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>Table: <code>Sales</code></p>

<pre>
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to <code>Product</code> table.
Each row records a sale of a product in a given year.
A product may have multiple sales entries in the same year.
Note that the per-unit price.

</pre>

<p>Write a solution to find all sales that occurred in the <strong data-end="967" data-start="953">first year</strong> each product was sold.</p>

<ul data-end="1234" data-start="992">
	<li data-end="1078" data-start="992">
	<p data-end="1078" data-start="994">For each <code data-end="1015" data-start="1003">product_id</code>, identify the earliest <code data-end="1045" data-start="1039">year</code> it appears in the <code data-end="1071" data-start="1064">Sales</code> table.</p>
	</li>
	<li data-end="1140" data-start="1079">
	<p data-end="1140" data-start="1081">Return <strong data-end="1095" data-start="1088">all</strong> sales entries for that product in that year.</p>
	</li>
</ul>

<p data-end="1234" data-start="1143">Return a table with the following columns: <strong>product_id</strong>,<strong> first_year</strong>, <strong>quantity, </strong>and<strong> price</strong>.<br />
Return the result in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+

<strong>Output:</strong> 
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+ 
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+
</pre>
