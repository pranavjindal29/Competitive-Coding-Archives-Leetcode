<h2><a href="https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters">Minimum Number of Food Buckets to Feed the Hamsters</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><p>You are given a <strong>0-indexed</strong> string <code>hamsters</code> where <code>hamsters[i]</code> is either:</p>

<ul>
	<li><code>&#39;H&#39;</code> indicating that there is a hamster at index <code>i</code>, or</li>
	<li><code>&#39;.&#39;</code> indicating that index <code>i</code> is empty.</li>
</ul>

<p>You will add some number of food buckets at the empty indices in order to feed the hamsters. A hamster can be fed if there is at least one food bucket to its left or to its right. More formally, a hamster at index <code>i</code> can be fed if you place a food bucket at index <code>i - 1</code> <strong>and/or</strong> at index <code>i + 1</code>.</p>

<p>Return <em>the minimum number of food buckets you should <strong>place at empty indices</strong> to feed all the hamsters or </em><code>-1</code><em> if it is impossible to feed all of them</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/11/01/example1.png" style="width: 482px; height: 162px;" />
<pre>
<strong>Input:</strong> hamsters = &quot;H..H&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> We place two food buckets at indices 1 and 2.
It can be shown that if we place only one food bucket, one of the hamsters will not be fed.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/11/01/example2.png" style="width: 602px; height: 162px;" />
<pre>
<strong>Input:</strong> hamsters = &quot;.H.H.&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> We place one food bucket at index 2.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/11/01/example3.png" style="width: 602px; height: 162px;" />
<pre>
<strong>Input:</strong> hamsters = &quot;.HHH.&quot;
<strong>Output:</strong> -1
<strong>Explanation:</strong> If we place a food bucket at every empty index as shown, the hamster at index 2 will not be able to eat.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= hamsters.length &lt;= 10<sup>5</sup></code></li>
	<li><code>hamsters[i]</code> is either<code>&#39;H&#39;</code> or <code>&#39;.&#39;</code>.</li>
</ul>
